export interface TheoreticalFeature {
  ozellik_adi: string;
  teorik_deger: string;
  gozlemle_uyumlu: boolean;
}

export interface SpeciesDetail {
  tur_adi: string;
  confidence: number;
  teorik_ozellikler: TheoreticalFeature[];
}

export interface AnalysisResult {
  predicted_species: string | null;
  common_name_tr: string | null;
  confidence: number;
  confidence_level: string;
  elimination_steps: EliminationStep[];
  remaining_candidates: string[];
  features_used: {
    olasi_turler: SpeciesDetail[];
    api_model: string;
    extraction_timestamp: string;
    [key: string]: any;
  };
  olasi_turler?: any[];
  top_3_comparison?: any[];
}

export interface PredictionFeatures {
  common_name_tr?: string;
  [key: string]: any;
}

export interface EliminationStep {
  feature_checked: string;
  feature_value: string;
  eliminated_species: string[];
  reason: string;
}

export interface AnalysisState {
  status: 'idle' | 'uploading' | 'processing' | 'success' | 'error';
  result?: AnalysisResult;
  error?: string;
}
