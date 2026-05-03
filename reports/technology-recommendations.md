# Teknoloji Önerileri (Technology Recommendations)

TurtleVision projesi için yapılan Vision AI karşılaştırması aşağıdadır:

| Model | Ücretsiz Tier | Görüntü Analizi Kapasitesi | JSON Yanıt | Basitlik | Öneri |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Google Gemini 1.5 Flash** | **Mevcut (Geniş)** | Çok Yüksek (Hızlı ve Detaylı) | Evet | Yüksek | **Birinci Tercih** |
| **OpenAI GPT-4o mini** | Hayır (Düşük Maliyet) | Çok Yüksek | Evet | Yüksek | **Yedek Tercih** |
| **Anthropic Claude Haiku** | Hayır | Orta-Yüksek | Evet | Orta | - |
| **Ollama (LLaVA)** | Tamamen Ücretsiz | Orta (Donanıma Bağlı) | Zor | Düşük | Sadece Gizlilik Öncelikli Durumlarda |

## Karar: Google Gemini 1.5 Flash

### Gerekçe:
1.  **Maliyet:** Günlük 1500 isteğe kadar (model bazlı değişebilir ancak genellikle en yüksek ücretsiz kota) sunduğu ücretsiz kullanım hakkı, geliştirme aşaması için en idealidir.
2.  **Hız ve Kalite:** "Flash" serisi, özellikle fotoğraflardan morfolojik özellik (pullanma, desen, renk) çıkarma konusunda oldukça optimize edilmiştir.
3.  **JSON Formatı:** Gemini API'si, yapılandırılmış çıktıları (System Instructions veya Schema ile) doğrudan destekler, bu da uygulama tarafında işlemeyi kolaylaştırır.
4.  **Ulaşılabilirlik:** Fotoğrafın URL'si veya Base64 verisi ile saniyeler içinde analiz yapabilmektedir.

### Uygulama Stratejisi:
Vision AI'ya doğrudan "Bu hangi kaplumbağa?" diye sormak yerine, hazırlanan **Morfolojik Kural Sözlüğü**'ndeki spesifik soruların (Örn: "Prefrontal pul sayısını belirle") sorulması ve gelen yanıtların bir mantık süzgecinden geçirilmesi önerilir.

---

## Web Mimarisi Teknolojileri (Web Architecture Technologies)

TurtleVision projesinin web ortamına taşınması için gereken Backend ve Frontend teknolojileri incelenmiş ve aşağıdaki kararlar alınmıştır.

### 1. Backend Framework Seçimi

Python tabanlı makine öğrenmesi ve AI projelerinde kullanılacak API altyapısı için alternatifler değerlendirilmiştir:

*   **Django:** Kapsamlı (batteries-included) ancak bizim gibi hafif bir API ve AI iş yükü odaklı projeler için fazlasıyla büyük (monolithic).
*   **Flask:** Basit ve hafif. Ancak asenkron (async/await) desteği doğuştan değildir ve veri doğrulaması için harici kütüphaneler (Marshmallow vb.) gerektirir.
*   **FastAPI:** Modern, çok hızlı, doğuştan I/O tabanlı asenkron desteği (Gemini API çağrıları için kritik) sunar. Pydantic ile veri doğrulamayı otomatikleştirir ve projedeki SOLID prensiplerine uygun mimariyle (`models.py`) kusursuz çalışır.

**Araştırmacı Ajanı Kararı:** **FastAPI**
**Gerekçe:** API isteklerinin ve AI yanıtlarının asenkron yönetilmesi projenin kritik noktasıdır. FastAPI, Pydantic ile sıfır eforla veri doğrulama (validation) ve dökümantasyon (Swagger UI) sağlayacaktır.

### 2. Frontend Stack Seçimi

Kaplumbağa analizi süreçlerini şık ve kullanıcı dostu bir şekilde gösterecek modern bir önyüz arayışı yapılmıştır:

*   **Vanilla JS + HTML:** Kurulumu kolaydır ancak adım adım analiz süreçlerindeki UI durumu (loading, AI extracting, applying rules vb.) DOM manipülasyonunu hızlıca karmaşıklaştırıp spagetti koda sebep olabilir.
*   **Vue 3 + Vite:** Çok hafif ve reaktif bir yapı sunar. Öğrenme ve geliştirme eğrisi çok tatmin edicidir.
*   **React + Vite + Tailwind CSS:** Endüstri standardı ve devasa bir ekosisteme sahip. Analiz adımlarının her birini izole UI komponentlerine dönüştürmek, projenin büyümesi açısından avantajlı olacaktır. Tailwind, prototipleme hızımızı çok artırır.

**Araştırmacı Ajanı Kararı:** **React (Vite tabanlı) + Tailwind CSS**
**Gerekçe:** Arayüzdeki adımları (fotoğraf yükleme, ekstraksiyon adımı, analiz onayı) React'ın state yönetimiyle kolayca ayrıştırıp takip edebiliriz. Tailwind ile doğa/kaplumbağa uyumlu estetik bir tasarım çok hızlı çıkartılır. 

### 3. Backend ve Frontend İletişimi (REST & CORS)

Sistem **RESTful Architecture** kullanılarak "Client-Server" modelinde ayrıştırılacaktır.
*   **CORS (Cross-Origin Resource Sharing):** Geliştirme sürecinde Frontend (örn: `localhost:5173`) ve Backend (örn: `localhost:8000`) farklı domain/port ikilisinde çalışacaktır. FastAPI tarafında CORS Middleware eklenerek Frontend origin değerlerine (veya `*`) izin verilmesi zaruridir.
*   **Veri Akışı:**
    1. İstemci (React), resmi Multipart Form-Data (veya Base64) formatında Backend'in `/api/analyze` endpoint'ine yollar.
    2. Backend (FastAPI), resmi `ImagePreparer` ile işler, `GeminiExtractor`'a gönderir (asynchronous).
    3. Analiz boyunca Frontend tarafında Skeleton Loader veya "Kaplumbağa İnceleniyor..." animasyonları gösterilebilir.
    4. Backend işlemi bitirdiğinde; ayıklanan özellikleri, alınan kararı ve test sürecinin günlüğünü (log) `application/json` formatında döndürür.
    5. Frontend, JSON'ı yakaladığında kullanıcıya analiz sonuçlarını "Card" veya "Stepper/Timeline" mantığında estetik şekilde sunar.

### 4. Geliştirici Ajanlara Bildirim

*   **@Backend_Ajanı (%s):** Lütfen hızlıca bir `FastAPI` iskeleti kur. CORS politikalarını geliştirme ortamına göre ayarla. Mevcut `main.py` akışını refactor ederek uygun REST endpoint'lerine (`/upload`, `/analyze`) dönüştür. Pydantic `models.py` entegrasyonu senin sorumluluğunda.
*   **@Frontend_Ajanı (%s):** UI geliştirmesi için `npm create vite@latest` ile React projesi ayağa kaldır. `Tailwind CSS` kurulumunu sağla. Uygulamamızın teması doğa (green/emerald/teal) renk tonlarında olmalı. API servisleri ile konuşmak için `axios` veya `fetch` kullanabilirsin.

