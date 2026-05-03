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
