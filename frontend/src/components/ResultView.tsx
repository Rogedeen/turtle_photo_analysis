import React from 'react';
import { AnalysisResult } from '../types';

interface ResultViewProps {
  result: AnalysisResult;
  onReset: () => void;
}

const ResultView: React.FC<ResultViewProps> = ({ result, onReset }) => {
  // Backend'den gelen yeni yapı: features_used.olasi_turler
  const candidates = result.features_used?.olasi_turler || [];
  
  // Öne çıkan tür verileri
  const mainCandidate = candidates[0] || {
    tur_adi: result.predicted_species || 'Bilinmeyen',
    common_name_tr: result.common_name_tr || 'Bilinmeyen Tür',
    confidence: result.confidence || 0
  };

  const normalizedConfidence = mainCandidate.confidence > 1 
    ? mainCandidate.confidence / 100 
    : mainCandidate.confidence;

  return (
    <div className="mt-8 bg-white border border-emerald-200 rounded-xl overflow-hidden shadow-2xl animate-fade-in">
      {/* Üst Vurgu Alanı: En Yüksek Skorlu Tür */}
      <div className="bg-gradient-to-r from-emerald-600 to-teal-700 text-white p-8 text-center relative overflow-hidden">
        <div className="absolute top-0 right-0 p-4 opacity-10 text-9xl">🐢</div>
        <p className="text-emerald-100 font-bold uppercase tracking-[0.2em] mb-2 text-sm">Tespit Edilen En Yakın Tür</p>
        <h2 className="text-4xl font-black mb-1">{result.common_name_tr}</h2>
        <p className="text-xl text-emerald-100 italic font-medium opacity-90">{mainCandidate.tur_adi}</p>
        
        <div className="mt-6 inline-flex items-center bg-white/10 backdrop-blur-md px-6 py-2 rounded-full border border-white/20">
          <span className="text-emerald-50 mr-2 text-sm font-bold uppercase">Güven Skoru:</span>
          <span className="text-2xl font-black">%{Math.round(normalizedConfidence * 100)}</span>
        </div>
      </div>

      <div className="p-8">
        {/* Karşılaştırmalı Analiz Tablosu */}
        {candidates.length > 0 && (
          <div className="mb-10">
            <h3 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-3">
              <span className="bg-emerald-100 p-2 rounded-lg">📊</span>
              Teorik Bilgi Karşılaştırmalı Analiz
            </h3>
            
            <div className="overflow-x-auto rounded-xl border border-gray-100 shadow-sm">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="bg-gray-50 text-gray-600 text-xs uppercase tracking-wider">
                    <th className="p-4 border-b">Morfolojik / Teorik Özellik</th>
                    {candidates.slice(0, 3).map((candidate, idx) => (
                      <th key={idx} className="p-4 border-b text-center">
                        <div className="font-black text-sm">{candidate.tur_adi}</div>
                        <div className="text-[10px] opacity-70">%{Math.round((candidate.confidence > 1 ? candidate.confidence / 100 : candidate.confidence) * 100)} Uyum</div>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="text-sm">
                  {/* Özellik listesi ilk adaydan alınabilir (hepsinde aynı set gelmeli) */}
                  {candidates[0].teorik_ozellikler.map((feat, fIdx) => (
                    <tr key={fIdx} className="hover:bg-gray-50/50 transition-colors border-b border-gray-50 last:border-0">
                      <td className="p-4 font-bold text-gray-700 bg-gray-50/30">
                        {feat.ozellik_adi}
                      </td>
                      {candidates.slice(0, 3).map((cand, cIdx) => {
                        const feature = cand.teorik_ozellikler.find(f => f.ozellik_adi === feat.ozellik_adi) || feat;
                        return (
                          <td key={cIdx} className="p-4 text-center">
                            <div className="flex flex-col items-center">
                              <span className="mb-1 text-gray-600">{feature.teorik_deger}</span>
                              {feature.gozlemle_uyumlu ? (
                                <span className="text-emerald-500 font-bold flex items-center gap-1">
                                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                                  </svg>
                                </span>
                              ) : (
                                <span className="text-rose-500 font-bold flex items-center gap-1">
                                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                                  </svg>
                                </span>
                              )}
                            </div>
                          </td>
                        );
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* Bilgilendirme ve Reset */}
        <div className="bg-amber-50 rounded-xl p-5 mb-8 border border-amber-100 flex items-start gap-4">
          <span className="text-2xl opacity-80">💡</span>
          <p className="text-amber-900 text-sm leading-relaxed">
            Yukarıdaki tablo, görselden çıkarılan gözlemlerin <strong>herpetolojik literatürdeki teorik verilerle</strong> karşılaştırmasını göstermektedir. 
            İkonlar, gözlemlediğimiz kaplumbağanın özelliğinin o türe ait literatür bilgisiyle örtüşüp örtüşmediğini belirtir.
          </p>
        </div>

        <div className="flex justify-center">
          <button
            onClick={onReset}
            className="group relative px-8 py-4 bg-emerald-600 text-white rounded-2xl hover:bg-emerald-700 transition-all shadow-lg hover:shadow-emerald-200 active:scale-95 overflow-hidden"
          >
            <span className="relative z-10 font-bold text-lg flex items-center gap-2">
              <span>🔄</span> Yeni Analiz Başlat
            </span>
            <div className="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResultView;
