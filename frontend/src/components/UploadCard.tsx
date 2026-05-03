import React, { useCallback } from 'react';

interface UploadCardProps {
  onFileSelect: (file: File) => void;
  disabled?: boolean;
}

export const UploadCard: React.FC<UploadCardProps> = ({ onFileSelect, disabled }) => {
  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    if (disabled) return;
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
      onFileSelect(file);
    }
  }, [disabled, onFileSelect]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (disabled) return;
    const file = e.target.files?.[0];
    if (file) {
      onFileSelect(file);
    }
  };

  return (
    <div 
      className={`border-2 border-dashed border-emerald-400 rounded-xl p-10 flex flex-col items-center justify-center transition-colors duration-200 ${disabled ? 'opacity-50 cursor-not-allowed bg-emerald-50/50' : 'hover:bg-emerald-50 cursor-pointer bg-white'}`}
      onDrop={handleDrop}
      onDragOver={(e) => e.preventDefault()}
    >
      <input 
        type="file" 
        accept="image/*" 
        className="hidden" 
        id="file-upload" 
        onChange={handleChange}
        disabled={disabled}
      />
      <label htmlFor="file-upload" className="flex flex-col items-center cursor-pointer w-full h-full">
        <svg className="w-16 h-16 text-emerald-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path></svg>
        <span className="text-emerald-800 font-semibold text-lg">Fotoğraf Yüklemek İçin Tıklayın veya Sürükleyin</span>
        <span className="text-emerald-600 text-sm mt-2">Sadece JPEG/PNG formatları</span>
      </label>
    </div>
  );
};