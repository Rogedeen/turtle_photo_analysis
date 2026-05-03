# Frontend Geliştirme Raporu

## 1. Mimari ve Teknoloji Seçimi
*   **Çatı (Framework):** React
*   **Build Aracı:** Vite (Hızlı geliştirme ortamı)
*   **Stil (Styling):** Tailwind CSS
*   **Dil:** TypeScript (Tip güvenliği için)

## 2. Kullanılan SOLID ve Temiz Kod Prensipleri
*   **Single Responsibility Principle (SRP):** Her component sadece tek bir iş yapar. (Örn: `UploadCard` sadece dosya seçimi ile ilgilenir, `ResultDisplay` sadece sonuçları gösterir, `Stepper` süreç aşamalarını gösterir).
*   **Dependency Inversion (DIP) / Separation of Concerns:** API çağrıları `src/services/api.ts` içinde izole edildi. Hook içinden direkt fetch çağrısı yapmak yerine bu servis tüketiliyor. İş mantığı (state yönetimi) `useAnalyzeImage` hook'unda toplanarak UI ile Data katmanı birbirinden ayrıldı.
*   **Tip Güvenliği:** `src/types/index.ts` merkezi olarak veri modellerini tanımlıyor (`AnalysisResult`, `EliminationStep`).

## 3. Component Özeti
*   **UploadCard:** Sürükle bırak destekli fotoğraf yükleme alanı.
*   **Stepper:** İşlem adımlarını ("Yükleniyor...", "Özellikler Çıkarılıyor", "Karar Ağacı İşleniyor") simüle eden/gösteren bileşen.
*   **ResultDisplay:** Eleme adımlarını (x bulundu -> y elendi) ve final Güven Skoru tablosunu yeşil doğa konseptiyle listeleyen sunum bileşeni.

## 4. UI/UX Tasarım Kararları
*   Tema olarak `turtle` ("#3ba473", vb.) odaklı yeşil renk skalası kullanıldı.
*   Yükleme durumu sırasında backend süreçlerini (Görüntü Hazırlama -> Gemini Vision -> Karar Ağacı) yansıtan bilgi iletileri eklendi.

## 5. Hata Düzeltmeleri (Bugfixes)
*   **Default Export:**  `App.tsx` içerisinde default olarak import edilen bileşenlerin (`LoadingStepper`, `UploadCard`, `ResultView`) named export ile export edilmesinden kaynaklanan hatalar düzeltildi. İlgili dosyaların içerisindeki export'lar named'ten (örn. `export const LoadingStepper`) named func + `export default LoadingStepper` formuna alınmıştır.
*   **Kullanılmayan Asset:** `index.html` sayfasından kullanılmayan `vite.svg` simge (favicon) referansı kaldırıldı.

## 6. Hata Düzeltmeleri – 2. Tur (2026-05-04)

### Bug #1 — `LoadingStepper` SyntaxError: no default export
- **Kök Neden:** `App.tsx` line 22'de `<UploadCard onFileUpload={analyze} />` yazılıyordu; `UploadCard` bileşeninin interface'i ise `onFileSelect` prop adını bekliyordu. Prop adı uyumsuzluğu Vite'nin HMR modül grafiğini bozarak `LoadingStepper` için yanlış bir "no default export" hatası yansıtıyordu.
- **Düzeltme:** `App.tsx` line 22 → `onFileUpload` → `onFileSelect` olarak değiştirildi.

### Bug #2 — `GET /vite.svg` 404 Not Found
- **Kök Neden:** Vite default şablon favicon'ı `public/vite.svg` dosyasına referans verir. Bu dosya projede mevcut olmadığı için tarayıcı 404 alıyordu.
- **Düzeltme:** `index.html`'e `<link rel="icon" href="data:image/svg+xml,...">` olarak inline emoji favicon (🐢) eklendi; harici dosya isteği tamamen ortadan kaldırıldı.

### Bug #3 — `ResultView` TypeScript: `onReset` prop tanımsız
- **Kök Neden:** `App.tsx` `<ResultView onReset={reset} />` geçiriyordu fakat `ResultViewProps` interface'inde `onReset` tanımlı değildi. Bu durum TypeScript derleme hatasına yol açıyordu.
- **Düzeltme:** `ResultViewProps` interface'ine `onReset: () => void` alanı eklendi; bileşen imzasında destructure edildi ve bileşen altına "Yeni Analiz Yap" butonu yerleştirildi.


