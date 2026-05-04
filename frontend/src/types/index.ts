export interface AnalysisResult {
  confidence_score: number;
  species: string;
  elimination_steps: EliminationStep[];
  status: 'success' | 'error';
  message?: string;
}

export interface EliminationStep {
  feature: string;
  value: string
  eliminated: string[];
  reason: string;
}

export interface AnalysisState {
  status: 'idle' | 'uploading' | 'processing' | 'success' | 'error';
  result?: AnalysisResult;
  error?: string;
}
