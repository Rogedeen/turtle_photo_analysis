export interface AnalysisResult {
  confidence_score: number;
  species: string;
  elimination_steps: EliminationStep[];
  status: 'success' | 'error';
  message?: string;
}

export interface EliminationStep {
  feature: string;
  found: boolean;
  eliminated: string[];
  reason: string;
}

export interface AnalysisState {
  status: 'idle' | 'uploading' | 'processing' | 'success' | 'error';
  result?: AnalysisResult;
  error?: string;
}
