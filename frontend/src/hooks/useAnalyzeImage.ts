import { useState } from 'react';
import { AnalysisResult, AnalysisState } from '../types';
import { analyzeImageApi } from '../services/api';

export const useAnalyzeImage = () => {
  const [state, setState] = useState<AnalysisState>({ status: 'idle' });

  const analyze = async (file: File) => {
    setState({ status: 'uploading' });
    try {
      setState({ status: 'processing' });
      const result = await analyzeImageApi(file);
      setState({ status: 'success', result });
    } catch (error: any) {
      setState({ status: 'error', error: error.message || 'Bilinmeyen bir hata oluştu' });
    }
  };

  const reset = () => {
    setState({ status: 'idle' });
  };

  return { state, analyze, reset };
};
