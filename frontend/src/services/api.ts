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
  // Gelen veriyi Frontend'in AnalysisResult tipine uyarlıyoruz.
  const mappedResult: AnalysisResult = {
    species: rawData.predicted_species || "Tür Belirlenemedi",
    confidence_score: rawData.confidence || 0,
    elimination_steps: rawData.elimination_steps?.map((step: any) => ({
      feature: step.feature_checked,
      value: step.feature_value, // Artık "evet/hayır" kontrolü yok, doğrudan gelen veriyi alıyoruz
      reason: step.reason,
      eliminated: step.eliminated_species || []
    })) || []
  };

  return mappedResult;
};