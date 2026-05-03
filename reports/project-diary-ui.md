# TurtleVision Proje Gelişim Günlüğü (UI Entegrasyonu)

## [2026-05-03] Döngü 5: Mimari Araştırma ve Profilleme
Arka yüz (Backend) ve Ön yüz (Frontend) geliştiricileri için sırasıyla `agents/Backend.agent.md` ve `agents/Frontend.agent.md` profilleri oluşturuldu.
Araştırma Ajanı teknolojileri analiz ederek Backend için **FastAPI**, Frontend için **React(Vite) + Tailwind CSS** yığınını seçti. Mimarilerin nasıl güvenle haberleşeceği kurgulandı.
Rapor: `reports/technology-recommendations.md`

## [2026-05-03] Döngü 6: Backend API Geliştirme
Backend Ajanı FastAPI kullanarak projeyi dışa açan endpoint olan `api/v1/analyze` yapısını oluşturdu. CORS origin izinleri `localhost:5173` için ayarlandı. 422, 502 ve 500 nolu HTTPxception'lar Handle edildi. Pydantic validasyonları uygulandı. Test coverage %86 ile Doğrulayıcı Ajan tarafından onaylandı.
Rapor: `reports/backend-log.md`

## [2026-05-03] Döngü 7: Frontend Entegrasyonu
Frontend Ajanı React ile SRP kurallarına (Single Responsibility Principle) uyarak UI bileşenlerini (`UploadCard`, `LoadingStepper`, `ResultView`) izole etti. Tailwind ile proje konseptine uygun şekilde zümrüt ve doğa yeşili ekolojik tema uygulandı. FastAPI ile API bağlantısının sağlanması amacıyla `useAnalyzeImage` şeklinde bir custom hook tasarlandı. (API kısıtlarına takılmaması için Orkestratör tarafından manuel kod yapısı iskele olarak kuruldu.)
Rapor: `reports/frontend-log.md`
