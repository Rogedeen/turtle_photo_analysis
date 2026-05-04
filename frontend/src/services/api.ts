import { AnalysisResult } from '../types';

const API_BASE_URL = 'http://localhost:8080/api/v1';

export const analyzeImageApi = async (file: File): Promise<AnalysisResult> => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Görüntü analizi sırasında bir hata oluştu');
  }

  // Backend'den gelen ham veriyi alıyoruz
  const rawData = await response.json();

  // DTO (Data Transfer Object) Mapping:
  // Gelen veriyi Frontend'in AnalysisResult tipine tam olarak uyarlıyoruz.
  const mappedResult: AnalysisResult = {
    predicted_species: rawData.predicted_species,
    common_name_tr: rawData.common_name_tr,
    confidence: rawData.confidence || 0,
    confidence_level: rawData.confidence_level || "Bilinmiyor",
    elimination_steps: rawData.elimination_steps || [],
    remaining_candidates: rawData.remaining_candidates || [],
    features_used: rawData.features_used || {},
    olasi_turler: rawData.olasi_turler || []
  };

  return mappedResult;
};