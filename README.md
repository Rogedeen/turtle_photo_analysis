#  TurtleVision - Akıllı Kaplumbağa Tür Tespit ve Analiz Sistemi

TurtleVision, yüklenen bir kaplumbağa fotoğrafını makine öğrenmesi (Vision AI - Gemini 1.5 Flash) ve uzman morfolojik kuralları kullanarak analiz eden, türünü saptayan modern bir **Full-Stack** web uygulamasıdır. 

Sistem basit bir tahmin modelinin ötesine geçerek; tıpkı bir biyolog gibi otonom "Ajanlar" yardımıyla tespit yapar, belirsizlikleri yönetir ve kararlarını eleme mantığıyla şeffaf bir şekilde açıklar.

---

##  Proje Hakkında (Çalışma Mantığı)

Proje mimarisi **SOLID** prensipleri ile birbirine bağlanan modüler bir boru hattı (pipeline) üzerine inşa edilmiştir:

1. **Görüntü Hazırlama (Image Preparer):** 
   Kullanıcıdan gelen fotoğraf (JPEG/PNG/WEBP vb.) ilk olarak bu katmana gelir. Sistemin sağlığı (bandwidth vb.) için resim boyutlandırılır, oranları korunarak 1 MB altına küçültülür ve Vision API'nin anlayacağı `Base64` formatına dönüştürülür.
   
2. **Özellik Çıkarımı (Feature Extractor - Vision AI):**
   Hazırlanan fotoğraf, dinamik bir prompt eşliğinde Google'ın **Gemini 1.5 Flash** modeline gönderilir. Dinamik prompt; sistemdeki güncel "morfolojik kurallar" kitapçığını okuyarak Gemini'a "Kabuk rengi nedir?", "Yanak şeridi var mı?", "Ayak yapısı perde mi pençe mi?" gibi sadece ilgili biyolojik soruları sorar. Geriye yapılandırılmış (JSON) kesin gözlem cevapları döner.

3. **Karar Ağacı (Decision Tree Logic):**
   Modelden alınan parametreler (JSON), *Karar Ağacı Motoru*na aktarılır. Bu adım tahminden uzak, tamamen deterministiktir. Örneğin *"Yanak şeridi bulunamadı -> Trachemys Scripta elendi"* mantığıyla aday listesini tek tek daraltır. Cevabı "belirsiz" olan gözlemler pas geçilirken belirgin çelişkilere de eksi (-) puan verilir.
   
4. **Sonuç Raporlaması (Decision Result):**
   Geriye 1 veya az sayıda aday tür kaldığında; eşleşen belirgin özelliklerin sayısıyla bir **Güven Skoru (Confidence Score)** hesaplanır. Hem nihai tahmin hem de *adım adım eleme gerekçeleri* API vasıtasıyla Frontend'e gönderilir.

---

##  Kullanılan Teknolojiler

**Backend (Arka Yüz)**
- **FastAPI** (Asenkron API uç noktaları)
- **Pydantic** (Veri doğrulama)
- **google-generativeai** (Gemini 1.5 Flash entegrasyonu)
- **PyTest** (Birim testler ve coverage > %86)

**Frontend (Ön Yüz)**
- **React + Vite** (Modüler komponent yapıları)
- **Tailwind CSS** (Doğa temalı emerald/teal tasarım konsepti)
- **Custom Hooks** (API süreç izolasyonları)

---

##  Kurulum Rehberi

Projenin tamamını ayağa kaldırmak için **Backend** ve **Frontend** süreçlerini iki ayrı sekmede başlatmanız gerekir.

### 1. Gereksinimler
- Python 3.10+
- Node.js 18+ ve npm 

### 2. Çevre (Environment) Değişkenleri Ortamı
Dizin içerisinde `.env` veya `key.env` dosyası oluşturun (İkisi de git üzerinden güvenli şekilde ignore edilmiştir). Aşağıdaki içeriği yapıştırın ve kendi API anahtarınızı atayın:

```env
# Ana dizindeki key.env ya da .env dosyası
GEMINI_API_KEY=kendi_gemini_api_anahtarinizi_buraya_yazin
MODEL_NAME=gemini-1.5-flash

# Backend ve Frontend İletişimi
PORT=8080
DEBUG=True
VITE_API_BASE_URL=http://localhost:8080/api/v1
```

### 3. Backend (FastAPI) Sunucusunu Çalıştırma
Projenin kök (ana) dizininde bir terminal açın ve aşağıdaki adımları sırasıyla yürütün:

```bash
# Sadece İlk Kurulumda: Sanal Ortam (venv) oluşturun
python -m venv venv

# Sanal ortamı aktifleştirin
# Windows CMD / PowerShell için:
venv\Scripts\activate
# Mac / Linux için:
# source venv/bin/activate

# Gerekli bağımlılıkları indirin
pip install -r requirements.txt

# Uvicorn ile FastAPI'yi ayağa kaldırın
uvicorn src.api.main:app --reload --port 8080
```
*API Sunucunuz `http://localhost:8080` adresinde başlayacaktır.* 
*(API endpoint özelliklerini `http://localhost:8080/docs` swagger sayfasından inceleyebilirsiniz.)*

### 4. Frontend (UI) Sunucusunu Çalıştırma
Yeni bir terminal sekmesi açın, proje ana dizininden `frontend` klasörüne girin:

```bash
cd frontend

# Paketleri yükleme (Sadece ilk kullanımda)
npm install

# Arayüzü derleme ve çalıştırma
npm run dev
```
*Web Arayüzünüz `http://localhost:5173` adresinde görülebilir olacaktır.*

---

##  Testlerin Çalıştırılması
İlgili tüm parçaların (Eleme mantığı, Modüller, API istekleri) düzgün çalışıp çalışmadığını test etmek isterseniz ana dizinde (venv aktif iken) şu komutu çalıştırabilirsiniz:

```bash
pytest --cov=src --cov-report=term-missing
```

---

## 🛡️ Kalite Güvencesi ve Kurallara Uyum (Audit Report)

Proje, geliştirme sürecinin sonunda tüm alt ajanlar tarafından (Image, Feature Extraction, Decision Tree, Backend, Frontend) kurallara uyum açısından denetlenmiştir.

### 📋 Denetlenen Kurallar
- **CLEAN_CODE_RULES.md:** İsimlendirme standartları, fonksiyon boyutu ve modülerlik.
- **SOLID_PRINCIPLES.md:** SRP, OCP, LSP, ISP ve DIP prensiplerine tam uyum.
- **REPORT_FORMAT.md:** Şeffaf ve izlenebilir raporlama.

### 🧩 Ajan Rapor Özetleri
- **Görüntü İşleme:** Görüntü standardizasyonu ve Base64 optimizasyonu SOLID prensiplerine uygun olarak `IImagePreparer` arayüzü üzerinden soyutlanmıştır.
- **Özellik Çıkarımı:** Gemini 1.5 Flash entegrasyonu, `PromptBuilder` ve `ResponseParser` sınıfları ile sorumluluklarına bölünmüş (SRP), hata toleransı (JSON Sanitization) maksimize edilmiştir.
- **Karar Motoru:** Hibrit (Vision AI + Morfoloji) puanlama sistemi, `rule_loader` üzerinden dinamik olarak beslenmekte ve %100 deterministik sonuçlar üretmektedir.
- **API (Backend):** FastAPI mimarisi asenkron yapıda kurulmuş, Pydantic modelleri ile tip güvenliği (Type Safety) garanti altına alınmıştır.
- **Arayüz (Frontend):** React bileşenleri `useAnalyzeImage` hook'u ile mantıksal katmandan izole edilmiş, Tailwind CSS ile doğa temalı UX/UI standartları yakalanmıştır.

---
*TurtleVision; test güvenceli yapısı, şeffaf karar alma algoritması ve modern UI bileşenleriyle yapay zekayı doğa bilimlerine taşıyan örnek bir proje çatısıdır.*
 
