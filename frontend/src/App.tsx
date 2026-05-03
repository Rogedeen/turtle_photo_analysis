import React from 'react';
import UploadCard from './components/UploadCard';
import LoadingStepper from './components/LoadingStepper';
import ResultView from './components/ResultView';
import { useAnalyzeImage } from './hooks/useAnalyzeImage';

function App() {
  const { state, analyze, reset } = useAnalyzeImage();

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <div className="max-w-4xl w-full">
        <header className="text-center mb-10">
          <h1 className="text-4xl font-extrabold text-emerald-700 flex items-center justify-center gap-3">
            🐢 TurtleVision
          </h1>
          <p className="mt-3 text-gray-600 font-medium">Akıllı Kaplumbağa Tür Tespit ve Analiz Sistemi</p>
        </header>

        <main className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
          {state.status === 'idle' && (
            <UploadCard onFileSelect={analyze} />
          )}

          {(state.status === 'uploading' || state.status === 'processing') && (
            <LoadingStepper status={state.status} />
          )}

          {state.status === 'success' && state.result && (
            <ResultView result={state.result} onReset={reset} />
          )}

          {state.status === 'error' && (
            <div className="text-center py-10">
              <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-red-100 text-red-500 mb-4">
                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-2">Analiz Hatası</h3>
              <p className="text-red-600">{state.error}</p>
              <button 
                onClick={reset}
                className="mt-6 px-6 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 transition font-medium"
              >
                Tekrar Dene
              </button>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}

export default App;