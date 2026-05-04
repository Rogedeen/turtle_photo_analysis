# Feature Extraction Log

## [2026-05-03 23:25] İlk Kurulum ve Gemini Entegrasyonu

**Kullanılan API:** Gemini 1.5 Flash (Base Implementation)
**Durum:** Başarılı
**Yapılan İşlemler:**
1. `src/feature_extraction` modülü oluşturuldu.
2. `IFeatureExtractor` interface'i SOLID prensiplerine (Interface Segregation, Dependency Inversion) uygun olarak tanımlandı.
3. `PromptBuilder` ile dinamik prompt yapısı kuruldu. `morphological-rulebook.md`'deki sorular temel alındı.
4. `ResponseParser` ile API'den gelen JSON yanıtların `TurtleFeatures` dataclass formatına dönüştürülmesi sağlandı.
5. "belirsiz" durum yönetimi implement edildi; verilmeyen alanlar otomatik olarak `belirsiz` olarak işaretleniyor.
6. `GeminiFeatureExtractor` ile ilk entegrasyon prototipi tamamlandı.

**Clean Code Uyumu:**
- Fonksiyonlar 20 satırın altında tutuldu.
- Anlamlı isimlendirmeler yapıldı (`is_confident` vb. kurallar gözetildi).
- Tip ipuçları ve docstringler eklendi.

**SOLID Uyumu:**
- **S:** `PromptBuilder`, `ResponseParser` ve `GeminiFeatureExtractor` sorumlulukları ayrıldı.
- **O:** Yeni çıkarıcılar (örn: Ollama) `IFeatureExtractor` implement edilerek eklenebilir.
- **D:** High-level modüller interface'e bağımlı kılındı.

**Test Durumu:**
- Mock verilerle ilk testler (`tests/feature_extraction/test_feature_extractor.py`) hazırlandı.

## [2026-05-04 10:45] Confidence Score ve Olası Tür Tahmini Güncellemesi

**Kullanılan API:** Gemini 1.5 Flash
**Durum:** Güncellendi
**Yapılan İşlemler:**
1. src/feature_extraction/models.py: TurtleFeatures modeline olasi_turler (List[Dict[str, float]]) alanı eklendi.
2. src/feature_extraction/prompt_builder.py: Gemini'dan en olası 3 türü ve bunlar için 0-1 arası güven skorunu (confidence) isteyecek şekilde prompt şablonu güncellendi.
3. src/feature_extraction/response_parser.py: API'den gelen olasi_turler verisini model nesnesine aktaracak mantık eklendi.
4. Gereksiz geçici dosyalar temizlendi.

**Gözlemler:**
- Gemini artık sadece fiziksel özellik çıkarmakla kalmayıp, kendi bilgisinden tür tahmini ve güven düzeyi de sağlıyor.
- Karar ağacı ajanı bu skorları son karar aşamasında ağırlıklandırma için kullanabilir.

## [2026-05-04 10:45] Confidence Score ve Olası Tür Tahmini Güncellemesi

**Kullanılan API:** Gemini 1.5 Flash
**Durum:** Güncellendi
**Yapılan İşlemler:**
1. src/feature_extraction/models.py: TurtleFeatures modeline olasi_turler (List[Dict[str, float]]) alanı eklendi.
2. src/feature_extraction/prompt_builder.py: Gemini'dan en olası 3 türü ve bunlar için 0-1 arası güven skorunu (confidence) isteyecek şekilde prompt şablonu güncellendi.
3. src/feature_extraction/response_parser.py: API'den gelen olasi_turler verisini model nesnesine aktaracak mantık eklendi.
4. Gereksiz geçici dosyalar temizlendi.

**Gözlemler:**
- Gemini artık sadece fiziksel özellik çıkarmakla kalmayıp, kendi bilgisinden tür tahmini ve güven düzeyi de sağlıyor.
- Karar ağacı ajanı bu skorları son karar aşamasında ağırlıklandırma için kullanabilir.
## [2026-05-04 12:15] Morfolojik Analiz ve Güven Skoru İyileştirmesi

**Kullanılan API:** Gemini 1.5 Flash
**Durum:** Güncellendi
**Sorun:** Gemini'ın morfolojik detaylara yeterince dikkat etmeden hızlı tür tahmini yapması (Örn: *Terrapene ornata* yerine %98 güvenle *T. carolina* demesi).
**Yapılan İşlemler:**
1. `src/feature_extraction/prompt_builder.py`: Sistem promptu güncellendi.
2. Gemini'a tahmin yapmadan önce morfolojik detayları (kabuk deseni, gaga, ayak pulları vb.) adım adım gözlemlemesi ve bunu `raw_response` içinde açıklaması talimatı eklendi.
3. `confidence` skorunu verirken morfolojik çelişki ihtimalini (8 fiziksel özellik ile türün bilinen özellikleri arasındaki uyumsuzluk) göz önünde bulundurması istendi.

**Sonuç:**
- Gemini artık karar vermeden önce "Think Step-by-Step" mantığıyla morfolojik analiz yapmaya zorlanıyor.
- `raw_response` alanı debug ve doğrulama için daha zengin veri içeriyor.
- Morfolojik çelişkiler güven skoruna yansıtılarak yanlış pozitiflerin önüne geçilmesi hedeflendi.
## [2026-05-04 11:30] Prompt Builder Syntax Hatası Giderildi

**Durum:** Başarılı (Fixed)
**Hata:** `src/feature_extraction/prompt_builder.py` dosyasında 17. satırda multi-line f-string başlangıcındaki hatalı kaçış karakteri (`f\"\"\"`) temizlendi.
**Yapılan İşlemler:**
1. Söz dizimi hatası giderildi.
2. `py_compile` ile dosya doğruluğu kontrol edildi.
## [2026-05-04 14:30] Clean Code Denetimi ve Bilimsel Terminoloji Güncellemesi

**Kullanılan API:** Gemini 1.5 Flash
**Durum:** Güncellendi & Denetlendi

**Yapılan İşlemler:**
1. **PromptBuilder Denetimi:** src/feature_extraction/prompt_builder.py dosyası Clean Code ve SOLID açısından incelendi. 
   - Sorumluluk tek bir sınıfta (PromptBuilder) ve tek bir amaçta toplandığı için Single Responsibility (SRP) prensibine uyumlu olduğu görüldü.
   - Fonksiyon boyutları 20 satırın altında tutularak okunabilirlik korundu.
2. **Kafa Pul Sayısı Güncellemesi:** kafa_pul_sayisi sorusu, herpetolojik terminoloji ve veritabanıyla uyumlu olması için "2 çift (veya 4 adet)" veya "4 çift (veya 8 adet)" seçeneklerini içerecek şekilde detaylandırıldı.
3. **Bilimsel Ad Vurgusu:** olasi_turler listesinde türlerin bilimsel adlarının (örn: *Caretta caretta*) tam olarak yazılması gerektiği prompt içinde açıkça belirtildi.
4. **Güven Hesabı:** confidence hesaplanırken morfolojik uyumsuzlukların (syntax vs. biyoloji) skorları düşürmesi gerektiği vurgusu korundu.

**Clean Code Notları:**
- İsimlendirmeler (questions, rules, build_prompt) açık ve eylem odaklı.
- Tip ipuçları (-> str) kullanılarak kodun kendini belgelemesi sağlandı.

## [2026-05-04 15:45] Confidence Normalizasyonu ve Eleme Mantığı Güncellemesi

**Kullanılan API:** Gemini 1.5 Flash
**Durum:** Başarılı
**Yapılan İşlemler:**
1. [src/feature_extraction/prompt_builder.py](src/feature_extraction/prompt_builder.py) güncellendi.
2. Gemini'a `olasi_turler` listesindeki güven skorlarının toplamının her zaman 1.0 (100%) olması zorunluluğu eklendi.
3. Gemini'a, en yüksek olasılıklı tür dışındaki türlerin neden elendiğini veya daha düşük skor aldığını `raw_response` içinde açıklaması talimatı verildi.
4. JSON şablonu ve örnek değerler 1.0 toplamına uygun hale getirildi.

**Gözlemler:**
- Bu güncelleme, karar ağacı aşamasında olasılık tabanlı karşılaştırmaları daha tutarlı hale getirecektir.
- `raw_response` içeriği, modelin karar verme sürecinin izlenebilirliğini artıracaktır.

## [2026-05-04 17:15] JSON Parser Robustness ve Sanitize Güncellemesi

**Hata:** `Feature extraction failed: API call failed: Failed to parse API response: Invalid control character at: line 2 column 1782`
**Durum:** Fixlendi
**Yapılan İşlemler:**
1. [src/feature_extraction/response_parser.py](src/feature_extraction/response_parser.py) üzerinde kritik bir güncelleme yapıldı.
2. **Sanitization:** _sanitize_json metodu eklenerek JSON yüklenmeden önce kontrol karakterleri (\x00-\x1F\x7F) regex ile temizlendi.
3. **Markdown Handling:** Gemini'dan gelen yanıtların içindeki JSON bloklarını ( `json ... ` ) ayıklamak için e.DOTALL destekli bir regex parser eklendi.
4. **Tolerance:** json.loads fonksiyonuna strict=False parametresi eklenerek string içindeki bazı kontrol karakterlerine (satır sonu vb.) karşı tolerans artırıldı.
5. aw_json parametre ismi standardizasyon için aw_response olarak güncellendi.

**Sonuç:**
- API'den dönen açıklama (explanation) veya ham veri bölümlerindeki teknik karakterler artık parser'ı bozmayacak.
- Markdown içindeki kod blokları daha güvenilir şekilde ayıklanacak.

## [2026-05-04 12:03] Teorik Bilgi Odaklı Yapıya Geçiş
**Kullanılan API:** Gemini Flash
**Değişiklik:** Gözlem odaklı yapıdan teorik kaynak karşılaştırmalı yapıya geçildi.
**Yeni Model Yapısı:** 3 tür x (5-8 teorik özellik) + Gözlem uyumu (True/False).
**Prompt Güncellemesi:** Herpetolojik literatür verisi talep eden yeni şablon aktif edildi.
**Not:** Decision Tree adımının bu yeni karmaşık yapıya uyum sağlaması gerekecektir.


## [2026-05-04 12:03] Teorik Bilgi Odaklı Yapıya Geçiş
**Kullanılan API:** Gemini Flash
**Değişiklik:** Gözlem odaklı yapıdan teorik kaynak karşılaştırmalı yapına geçildi.
**Yeni Model Yapısı:** 3 tür x (5-8 teorik özellik) + Gözlem uyumu (True/False).
**Prompt Güncellemesi:** Herpetolojik literatür verisi talep eden yeni şablon aktif edildi.
**Not:** Decision Tree adımının bu yeni karmaşık yapıya uyum sağlaması gerekecektir.

## [2026-05-04] Teorik Bilgi Odaklı Yapıya Geçiş
**Kullanılan API:** Gemini Flash
**Değişiklik:** Gözlem odaklı yapıdan teorik kaynak karşılaştırmalı yapıya geçildi.
**Yeni Model Yapısı:** 3 tür x (5-8 teorik özellik) + Gözlem uyumu (True/False).
**Prompt Güncellemesi:** Herpetolojik literatür verisi talep eden yeni şablon aktif edildi.
