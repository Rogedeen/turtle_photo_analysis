import React from 'react';
import { AnalysisResult } from '../types';

interface ResultViewProps {
  result: AnalysisResult;
}

export const ResultView: React.FC<ResultViewProps> = ({ result }) => {
  return (
    <div className="mt-8 bg-white border border-emerald-200 rounded-xl overflow-hidden shadow-lg">
      <div className="bg-emerald-600 text-white p-4 text-center">
        <h2 className="text-2xl font-bold">Analiz Sonucu</h2>
      </div>
      
      <div className="p-6">
        <div className="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-emerald-100 pb-6">
          <div className="mb-4 md:mb-0 text-center md:text-left">
            <p className="text-sm text-emerald-600 font-semibold uppercase tracking-wider">Tespit Edilen Tür</p>
            <p className="text-3xl font-bold text-emerald-900">{result.species}</p>
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
                  strokeDasharray={`${result.confidence_score * 100}, 100`}
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
              <div className="absolute inset-0 flex items-center justify-center">
                <span className="text-xl font-bold text-emerald-800">
                  {Math.round(result.confidence_score * 100)}%
                </span>
              </div>
            </div>
          </div>
        </div>

        <div>
          <h3 className="text-lg font-bold text-emerald-800 mb-4">Eleme Adımları</h3>
          <div className="space-y-4">
            {result.elimination_steps?.map((step, index) => (
              <div key={index} className="bg-emerald-50/50 p-4 rounded-lg border border-emerald-100">
                <div className="flex justify-between items-center mb-2">
                  <span className="font-semibold text-emerald-700">{step.feature}</span>
                  <span className={`px-3 py-1 rounded-full text-xs font-bold ${step.found ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-700'}`}>
                    {step.found ? 'Bulundu' : 'Bulunamadı'}
                  </span>
                </div>
                <p className="text-sm text-gray-700 mb-2">{step.reason}</p>
                {step.eliminated.length > 0 && (
                  <div className="pt-2 border-t border-emerald-100">
                    <p className="text-xs font-semibold text-gray-500 mb-1">Elenenler:</p>
                    <div className="flex flex-wrap gap-2">
                      {step.eliminated.map(el => (
                        <span key={el} className="text-xs bg-white border border-gray-200 px-2 py-1 rounded text-gray-600">
                          {el}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};