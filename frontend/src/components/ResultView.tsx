import React from 'react';
import { AnalysisResult } from '../types';

interface ResultViewProps {
  result: AnalysisResult;
  onReset: () => void;
}

const ResultView: React.FC<ResultViewProps> = ({ result, onReset }) => {
  // Backend'den gelen özellikleri filtrele (Sistem loglarını ve 'belirsiz' olanları gizle)
  const displayFeatures = Object.entries(result.features_used || {}).filter(
    ([key, value]) => 
      !['api_model', 'raw_response', 'extraction_timestamp', 'olasi_adaylar'].includes(key) && 
      value !== 'belirsiz'
  );

  return (
    <div className="mt-8 bg-white border border-emerald-200 rounded-xl overflow-hidden shadow-lg">
      <div className="bg-emerald-600 text-white p-4 text-center">
        <h2 className="text-2xl font-bold">Analiz Sonucu</h2>
      </div>
      
      <div className="p-6">
        {/* Üst Kısım: Tür ve Güven Skoru */}
        <div className="flex flex-col md:flex-row justify-between items-center mb-6">
          <div className="mb-4 md:mb-0 text-center md:text-left">
            <p className="text-sm text-emerald-600 font-semibold uppercase tracking-wider">Tespit Edilen Tür</p>
            <p className="text-3xl font-bold text-emerald-900">{result.species || "Bilinmeyen Tür"}</p>
          </div>
          
          <div className="flex flex-col items-center bg-emerald-50 px-6 py-4 rounded-xl border border-emerald-100">
            <p className="text-sm font-semibold text-emerald-600 mb-1">Güven Skoru</p>
            <div className="relative w-20 h-20">
              <svg className="w-full h-full" viewBox="0 0 36 36">
                <path
                  className="text-emerald-200"
                  strokeWidth="3"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  className="text-emerald-600"
                  strokeWidth="3"
                  strokeDasharray={`${(result.confidence_score || 0) * 100}, 100`}
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
              <div className="absolute inset-0 flex items-center justify-center">
                <span className="text-xl font-bold text-emerald-800">
                  {Math.round((result.confidence_score || 0) * 100)}%
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Alt Kısım: Tespit Edilen Özellikler (Açıklanabilir Yapay Zeka - XAI) */}
        {displayFeatures.length > 0 && (
          <div className="mt-2 mb-6 border-t border-emerald-100 pt-6">
            <h3 className="text-lg font-bold text-emerald-800 mb-4">Tespit Edilen Fiziksel Özellikler</h3>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              {displayFeatures.map(([key, value]) => (
                <div key={key} className="bg-emerald-50/50 p-3 rounded-lg border border-emerald-100 hover:bg-emerald-100 transition duration-200">
                  <p className="text-xs text-emerald-600 font-bold uppercase mb-1">
                    {key.replace(/_/g, ' ')} {/* Alt çizgileri boşluğa çevirir: ayak_yapisi -> ayak yapisi */}
                  </p>
                  <p className="text-sm font-semibold text-gray-800 capitalize">
                    {String(value)}
                  </p>
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="px-6 pb-2 text-center">
          <button
            onClick={onReset}
            className="px-6 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 transition font-medium"
          >
            Yeni Analiz Yap
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResultView;