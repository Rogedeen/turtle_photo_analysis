import logging
from dataclasses import asdict
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from src.api.schemas import DecisionResultSchema
from src.api.dependencies import get_image_preparer, get_feature_extractor, get_decision_tree
from src.image_prep.preparer import ImagePreparer
from src.feature_extraction.gemini_extractor import GeminiFeatureExtractor
from src.decision_tree import TurtleDecisionTree

router = APIRouter()
logger = logging.getLogger("BackendAPI")

@router.post("/analyze", response_model=DecisionResultSchema)
async def analyze_turtle(
    file: UploadFile = File(...),
    preparer: ImagePreparer = Depends(get_image_preparer),
    extractor: GeminiFeatureExtractor = Depends(get_feature_extractor),
    decision_tree: TurtleDecisionTree = Depends(get_decision_tree)
):
    """
    POST /analyze
    Receives an image of a turtle and processes it through the pipeline:
    1. ImagePreparer (Resize, Compress)
    2. FeatureExtractor (Extract features using LLM/AI)
    3. DecisionTreeAgent (Determine species based on rules)
    """
    try:
        content = await file.read()
        if not content:
            raise ValueError("Empty file")
    except Exception as e:
        logger.error(f"File read error: {e}")
        raise HTTPException(status_code=400, detail="Could not read or process the uploaded file.")
        
    try:
        prepared_image = preparer.prepare_image(content, file.filename)
    except Exception as e:
        logger.error(f"Image preparation failed: {e}")
        raise HTTPException(status_code=422, detail=f"Image preparation failed: {str(e)}")
        
    try:
        features = await extractor.extract_features(prepared_image)
    except Exception as e:
        logger.error(f"Feature extraction failed: {e}")
        raise HTTPException(status_code=502, detail=f"Feature extraction failed: {str(e)}")
        
    try:
        features_dict = asdict(features)
        result = decision_tree.decide(features_dict)
        
        # Pydantic-compatible conversion
        response_data = asdict(result)
        
        # Temizleme ve Güvenlik: None içermeyen str listeleri sağlamak
        if response_data.get('remaining_candidates'):
            response_data['remaining_candidates'] = [
                str(c) for c in response_data['remaining_candidates'] if c is not None
            ]
        else:
            response_data['remaining_candidates'] = []

        # Ensure lists are at least empty lists
        if response_data.get('olasi_turler') is None:
            response_data['olasi_turler'] = []
        if response_data.get('top_3_comparison') is None:
            response_data['top_3_comparison'] = []
            
        return response_data
    except Exception as e:
        logger.exception(f"Decision tree failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Decision engine failure: {str(e)}")
