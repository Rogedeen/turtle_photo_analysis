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

  return response.json();
};
