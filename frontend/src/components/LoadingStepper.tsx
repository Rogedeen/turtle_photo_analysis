import React from 'react';

interface LoadingStepperProps {
  status: 'idle' | 'uploading' | 'processing' | 'success' | 'error';
}

export const LoadingStepper: React.FC<LoadingStepperProps> = ({ status }) => {
  const steps = [
    { key: 'uploading', label: 'Fotoğraf Yükleniyor' },
    { key: 'processing', label: 'Yapay Zeka Analiz Ediyor' },
    { key: 'success', label: 'Sonuçlar Hazırlandı' },
  ];

  const getStepStatus = (stepKey: string, currentStatus: string) => {
    if (currentStatus === 'error') return 'error';
    const currentIndex = steps.findIndex(s => s.key === currentStatus);
    const stepIndex = steps.findIndex(s => s.key === stepKey);
    
    if (currentIndex > stepIndex || currentStatus === 'success') return 'completed';
    if (currentIndex === stepIndex) return 'current';
    return 'pending';
  };

  if (status === 'idle' || status === 'error') return null;

  return (
    <div className="w-full py-4 mt-6">
      <div className="flex justify-between items-center relative">
        {steps.map((step, index) => {
          const stepStatus = getStepStatus(step.key, status);
          return (
            <div key={step.key} className="flex flex-col items-center relative z-10 w-1/3">
              <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm transition-colors duration-300
                ${stepStatus === 'completed' ? 'bg-emerald-500 text-white' : 
                  stepStatus === 'current' ? 'bg-emerald-100 text-emerald-700 border-2 border-emerald-500 animate-pulse' : 
                  'bg-gray-100 text-gray-400'}`}>
                {index + 1}
              </div>
              <div className="mt-2 text-xs font-semibold text-center text-emerald-800">
                {step.label}
              </div>
            </div>
          );
        })}
        {/* Progress Bar Background */}
        <div className="absolute top-5 left-0 w-full h-1 bg-gray-200 -z-10" />
        {/* Progress Bar Fill */}
        <div className="absolute top-5 left-0 h-1 bg-emerald-500 -z-10 transition-all duration-500 rounded" style={{
            width: status === 'uploading' ? '16%' : status === 'processing' ? '50%' : '100%'
        }} />
      </div>
    </div>
  );
};