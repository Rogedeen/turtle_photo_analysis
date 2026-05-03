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
