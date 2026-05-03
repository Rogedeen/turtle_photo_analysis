# 🐢 TurtleVision: Deniz Kaplumbağası Tür Tespiti Platformu
## Final Proje Sunumu ve Teslim Raporu

**Hazırlayan:** Proje Orkestratörü  
**Sürüm:** Üretime Hazır (Production-Ready) Web Platformu

---

## 1. Vizyon: Makine Öğrenmesi Pipeline'ından Full-Stack Modern Web Ürününe Geçiş
Projemiz, ilk fazlarında salt bir "Makine Öğrenmesi Özellik Çıkarımı (Feature Extraction)" ve kural tabanlı bir karar ağacı olarak doğdu. Ancak vizyonumuz, bunu laboratuvar ortamından çıkarıp, bilim insanları ve doğa gözlemcileri tarafından kolayca kullanılabilecek modern bir web ürününe yerleştirmekti.

Bu vizyon doğrultusunda sistem; terminal üzerinden çalışan bir Python script'inden, uçtan uca haberleşen **React (Vite+Tailwind) - FastAPI - Gemini AI** destekli modern, tam teşekküllü (full-stack) bir web uygulamasına evrilmiştir.

---

## 2. Ajan (Agent) Rolleri ve SOLID Entegrasyonu
Projenin geliştirilmesinde Çoklu-Ajan (Multi-Agent) mimarisi kullanılmış ve görevler birbirinden kesin çizgilerle izole edilmiştir:

- 👑 **Orkestratör (Orchestrator):** Proje mimarisinin bütünlüğünü, ajanlar arası iletişimi ve büyük resmi yönetti.
- 🔬 **Araştırmacı Ajan (Researcher):** Kaplumbağa türlerinin morfolojik analizlerini toplayıp dinamik kural motoru için `morphological-rulebook.md` dosyasını oluşturdu.
- 🖼️ **Görüntü ve Karar Ajanları:** Özellik çıkarımı (Feature Extractor) ve Görüntü Ön İşleme (Image Prep) modüllerini inşa etti.
- ⚙️ **Backend Ajanı:** Mock mantığıyla çalışan ağacı, gerçeğe dönüştürerek FastAPI ile dış dünya iletişimine açtı.
- 💻 **Frontend Ajanı:** Kullanıcı dostu, bileşen (component) tabanlı React UX/UI tasarımlarını inşa etti.
- ✅ **Doğrulayıcı (Validator):** Yazılan her kod bloğunu denetledi.

**SOLID Kuralları ile Uyum:**
Bu iş bölümü, doğrudan Single Responsibility Principle (Tek Sorumluluk Prensibi) temel alınarak kuruldu. Her bir ajan, Dependency Inversion (Bağımlılığı Tersine Çevirme) prensibini uygulayarak "Interface" ve "Soyut" sınıflar üzerinden birbirini çağıran sistemler yazdı.

---

## 3. Backend Dönüşümü: Mock API'lerden Gerçek FastAPI Mimarisine Geçiş
Geliştirmenin ilk aşamalarında, sistemin doğru karar verip vermediğini test etmek adına Mock (Sahte) veri dizilimleri kullanılıyordu.  *(Örn: MockDecisionEngine)*

**Geçiş Hikayesi:**
1. **Model & Schema İnşası:** Pydantic ile girdi (request) ve çıktı (response) modelleri standardize edildi (`PredictionResponse`, `ImageUpload`).
2. **Controller/Router Ayrımı:** API uç noktaları `main.py` içerisindeki `routers` modülü ile parçalara bölündü.
3. **Bağımlılık Enjeksiyonu (Dependency Injection):** `get_feature_extractor` ve `get_decision_tree` gibi bağımlılık enjeksiyonları kurularak, sistemin Mock'lanabilme yeteneği korunurken gerçek sınıf bağlantıları yapıldı.
4. **Gerçek Karar Anı:** Sadece mock logları basan yapı terk edildi; sistem gerçek zamanlı olarak yüklenen bir görseli AI modeline (Gemini) gönderip, dönen JSON yapılarını Parse ederek gerçek karar ağacı algoritmalarından (Rule Engine) geçirmeye başladı.

---

## 4. React Frontend: Mimari Yapı ve Esneklik
Kullanıcıların karmaşık AI sürecini pratik bir formattan deneyimleyebilmesi için **SPA (Single Page Application)** vizyonuyla bir React frontend uygulaması ayağa kaldırıldı.

- **Teknolojiler:** React + Vite, Typescript mimarisi ve Tailwind CSS.
- **Bileşen Tabanlı (Component-Based) Mimari:**
  - `UploadCard.tsx`: Drag-and-Drop (Sürükle-bırak) deneyimi ve görsel yükleme yönetimi (Görsel ve UX geri bildirimleri).
  - `LoadingStepper.tsx`: Makine öğrenmesi pipeline'ının aşamalarını (Ön İşleme -> Gemini Analizi -> Kural Ağacı Kararı) kullanıcıya animasyonlu şekilde gösteren şeffaf geri bildirim ekranı.
  - `ResultView.tsx`: Tespit edilen kaplumbağa türü, güven skoru (Confidence) ve "Elenme Nedenleri (Elimination Logic)" detaylarını sunan estetik sonuç raporu.
- **Hook Yapısı (Hooks):** İş mantığı ile görsel katman `useAnalyzeImage.ts` isimli custom hook ile birbirinden ayrıştırılarak, bileşenlerin yalnızca arayüzden (UI) sorumlu olması (SRP) sağlandı.
- **Esneklik:** Arayüz, Axios entegrasyonuyla gelecekteki backend eklemelerine ve model güncellemelerine hızlı yanıt verebilecek modüler donanıma sahip kılındı.

---

## 5. Sonuç
**TurtleVision**, sadece algoritmik bir tespit motoru olmanın ötesine geçmiş, SOLID mimarisi ile donatılmış, ölçeklenebilir, modüler (Frontend, Backend, AI Pipeline) bir sistem bütünü haline formüle edilmiştir. Proje Orkestratörü ve alt ajanlarının başarılı koordinasyonu ile teslim edilmiştir.
