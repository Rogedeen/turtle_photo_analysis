# Decision Tree Agent Log — TurtleVision

## Otonom Karar Ağacı Süreci [2026-05-03]

### 1. Hazırlık ve Analiz
- `agents/decision_tree.agent.md` okundu. Kimlik benimsendi: Tahmin yapmayan, sadece elemeye dayalı mantık kuran, kural tabanlı uzman sistem ajanı.
- `rules/CLEAN_CODE_RULES.md` ve `rules/SOLID_PRINCIPLES.md` okundu.
- `reports/morphological-rulebook.md` analiz edildi. Dinamik parsing için regex desenleri belirlendi.

### 2. RuleLoader Yeniden Yapılandırma (SOLID & Clean Code) — TAMAMLANDI
- `RuleLoader` sınıfı `rule_loader.py` içinde güncellendi.
- Regex tabanlı parsing geliştirildi. `**Tür:**` ve `Bu türü kesin eleyecek özellikler:**` bölümleri başarıyla ayrıştırılıyor.
- `SpeciesRules` ve `MorphologicalRule` dataclass'ları ile veri yapısı normalize edildi.

### 3. Karar Mekanizması (Elimination & Scoring) — TAMAMLANDI
- `src/interfaces.py` oluşturuldu. `IDecisionEngine` soyutu tanımlandı.
- `src/decision_tree.py` agent persona'sına uygun olarak baştan yazıldı.
- Ayak yapısına göre habitat ön filtresi eklendi (Deniz vs Kara/Tatlı su).
- Morfolojik kural sözlüğünden gelen "Kesin Eleme" kuralları için semantik kontrol yapısı kuruldu.
- Güven hesabı ve sonuç oluşturma mantığı SOLID prensiplerine uygun hale getirildi.

### 4. Test Stratejisi — TAMAMLANDI
- `tests/test_decision_tree.py` yazıldı. 
- Habitat filtresi, özellik bazlı eleme ve güven seviyeleri test edilerek DOE 5/5 başarı sağlandı.

---
**Durum:** Karar Ağacı Ajanı görevini başarıyla tamamladı. Sistem artık dinamik kural sözlüğünden beslenerek otonom eleme yapabiliyor.
2026-05-03 23:20:18,451 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:18,452 - Gelen Özellikler: {'yanak_seridi': 'hayır'}
Gelen Özellikler: {'yanak_seridi': 'hayır'}
2026-05-03 23:20:18,452 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-03 23:20:18,453 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:18,453 - ### Karar Tamamlandı: Chelonia mydas (Düşük)
### Karar Tamamlandı: Chelonia mydas (Düşük)
2026-05-03 23:20:18,456 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:18,456 - Gelen Özellikler: {'ayak_yapisi': 'perde', 'prefrontal_pul_sayisi': '1', 'lateral_skut_sayisi': '4', 'kiremit_dizilimi': 'hayır'}
Gelen Özellikler: {'ayak_yapisi': 'perde', 'prefrontal_pul_sayisi': '1', 'lateral_skut_sayisi': '4', 'kiremit_dizilimi': 'hayır'}
2026-05-03 23:20:18,457 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-03 23:20:18,457 - ✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
2026-05-03 23:20:18,457 - ✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
2026-05-03 23:20:18,458 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:18,458 - ### Karar Tamamlandı: Chelonia mydas (Orta)
### Karar Tamamlandı: Chelonia mydas (Orta)
2026-05-03 23:20:18,460 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:18,461 - Gelen Özellikler: {'ayak_yapisi': 'pençe'}
Gelen Özellikler: {'ayak_yapisi': 'pençe'}
2026-05-03 23:20:18,461 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-03 23:20:18,461 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-03 23:20:18,461 - ### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
2026-05-03 23:20:18,468 - 
### Karar Süreci Başladı
2026-05-03 23:20:18,469 - Gelen Özellikler: {'ayak_yapisi': 'pençe'}
2026-05-03 23:20:18,469 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-03 23:20:18,469 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-03 23:20:18,470 - ### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
2026-05-03 23:20:27,414 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,415 - Gelen Özellikler: {'ayak_yapisi': 'perde', 'sert_plaka_var_mi': 'evet', 'yanak_seridi': 'hayır', 'lateral_skut_sayisi': '4', 'kiremit_dizilimi': 'hayır', 'prefrontal_pul_sayisi': '2'}
Gelen Özellikler: {'ayak_yapisi': 'perde', 'sert_plaka_var_mi': 'evet', 'yanak_seridi': 'hayır', 'lateral_skut_sayisi': '4', 'kiremit_dizilimi': 'hayır', 'prefrontal_pul_sayisi': '2'}
2026-05-03 23:20:27,416 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-03 23:20:27,416 - ✅ prefrontal_pul_sayisi tespit edildi -> Chelonia mydas elendi (Yeşil deniz kaplumbağalarında sadece 1 çift prefrontal pul bulunur.)
✅ prefrontal_pul_sayisi tespit edildi -> Chelonia mydas elendi (Yeşil deniz kaplumbağalarında sadece 1 çift prefrontal pul bulunur.)
2026-05-03 23:20:27,416 - ✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
2026-05-03 23:20:27,417 - ✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
2026-05-03 23:20:27,417 - ✅ sert_plaka_var_mi tespit edildi -> Dermochelys coriacea elendi (Deri sırtlı deniz kaplumbağasında sert plakalar bulunmaz.)
✅ sert_plaka_var_mi tespit edildi -> Dermochelys coriacea elendi (Deri sırtlı deniz kaplumbağasında sert plakalar bulunmaz.)
2026-05-03 23:20:27,417 - ❌ Tüm adaylar elendi!
❌ Tüm adaylar elendi!
2026-05-03 23:20:27,417 - ### Karar Tamamlandı: None (Düşük)
### Karar Tamamlandı: None (Düşük)
2026-05-03 23:20:27,418 - 
### Karar Süreci Başladı
2026-05-03 23:20:27,419 - Gelen Özellikler: {'ayak_yapisi': 'pençe'}
2026-05-03 23:20:27,419 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-03 23:20:27,419 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-03 23:20:27,420 - ### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
2026-05-03 23:20:27,423 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,424 - Gelen Özellikler: {'lateral_skut_sayisi': '4', 'ayak_yapisi': 'perde'}
Gelen Özellikler: {'lateral_skut_sayisi': '4', 'ayak_yapisi': 'perde'}
2026-05-03 23:20:27,424 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-03 23:20:27,424 - ✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
2026-05-03 23:20:27,425 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:27,425 - ### Karar Tamamlandı: Chelonia mydas (Düşük)
### Karar Tamamlandı: Chelonia mydas (Düşük)
2026-05-03 23:20:27,425 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,426 - Gelen Özellikler: {'kiremit_dizilimi': 'hayır', 'ayak_yapisi': 'perde'}
Gelen Özellikler: {'kiremit_dizilimi': 'hayır', 'ayak_yapisi': 'perde'}
2026-05-03 23:20:27,426 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-03 23:20:27,426 - ✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
2026-05-03 23:20:27,426 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:27,427 - ### Karar Tamamlandı: Chelonia mydas (Düşük)
### Karar Tamamlandı: Chelonia mydas (Düşük)
2026-05-03 23:20:27,427 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,427 - Gelen Özellikler: {'uyluk_mahmuzu': 'hayır', 'ayak_yapisi': 'pençe'}
Gelen Özellikler: {'uyluk_mahmuzu': 'hayır', 'ayak_yapisi': 'pençe'}
2026-05-03 23:20:27,427 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-03 23:20:27,427 - ✅ uyluk_mahmuzu tespit edildi -> Testudo graeca elendi (Testudo graeca'da uyluk mahmuzu bulunmalıdır.)
✅ uyluk_mahmuzu tespit edildi -> Testudo graeca elendi (Testudo graeca'da uyluk mahmuzu bulunmalıdır.)
2026-05-03 23:20:27,428 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-03 23:20:27,428 - ### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
2026-05-03 23:20:27,428 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,429 - Gelen Özellikler: {'kuyruk_mahmuzu': 'hayır', 'ayak_yapisi': 'pençe'}
Gelen Özellikler: {'kuyruk_mahmuzu': 'hayır', 'ayak_yapisi': 'pençe'}
2026-05-03 23:20:27,429 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-03 23:20:27,429 - ✅ kuyruk_mahmuzu tespit edildi -> Testudo hermanni elendi (Testudo hermanni'de kuyruk ucunda mahmuz bulunmalıdır.)
✅ kuyruk_mahmuzu tespit edildi -> Testudo hermanni elendi (Testudo hermanni'de kuyruk ucunda mahmuz bulunmalıdır.)
2026-05-03 23:20:27,430 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-03 23:20:27,430 - ### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
2026-05-03 23:20:27,430 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,431 - Gelen Özellikler: {'sert_plaka_var_mi': 'evet', 'ayak_yapisi': 'perde'}
Gelen Özellikler: {'sert_plaka_var_mi': 'evet', 'ayak_yapisi': 'perde'}
2026-05-03 23:20:27,431 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-03 23:20:27,431 - ✅ sert_plaka_var_mi tespit edildi -> Dermochelys coriacea elendi (Deri sırtlı deniz kaplumbağasında sert plakalar bulunmaz.)
✅ sert_plaka_var_mi tespit edildi -> Dermochelys coriacea elendi (Deri sırtlı deniz kaplumbağasında sert plakalar bulunmaz.)
2026-05-03 23:20:27,431 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:27,431 - ### Karar Tamamlandı: Chelonia mydas (Düşük)
### Karar Tamamlandı: Chelonia mydas (Düşük)
2026-05-03 23:20:27,434 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,434 - Gelen Özellikler: {'yanak_seridi': 'hayır'}
Gelen Özellikler: {'yanak_seridi': 'hayır'}
2026-05-03 23:20:27,434 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-03 23:20:27,435 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:27,435 - ### Karar Tamamlandı: Chelonia mydas (Düşük)
### Karar Tamamlandı: Chelonia mydas (Düşük)
2026-05-03 23:20:27,438 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,438 - Gelen Özellikler: {'ayak_yapisi': 'perde', 'prefrontal_pul_sayisi': '1', 'lateral_skut_sayisi': '4', 'kiremit_dizilimi': 'hayır'}
Gelen Özellikler: {'ayak_yapisi': 'perde', 'prefrontal_pul_sayisi': '1', 'lateral_skut_sayisi': '4', 'kiremit_dizilimi': 'hayır'}
2026-05-03 23:20:27,438 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-03 23:20:27,439 - ✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
✅ lateral_skut_sayisi tespit edildi -> Caretta caretta elendi (Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.)
2026-05-03 23:20:27,439 - ✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
✅ kiremit_dizilimi tespit edildi -> Eretmochelys imbricata elendi (Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.)
2026-05-03 23:20:27,439 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-03 23:20:27,439 - ### Karar Tamamlandı: Chelonia mydas (Orta)
### Karar Tamamlandı: Chelonia mydas (Orta)
2026-05-03 23:20:27,442 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-03 23:20:27,442 - Gelen Özellikler: {'ayak_yapisi': 'pençe'}
Gelen Özellikler: {'ayak_yapisi': 'pençe'}
2026-05-03 23:20:27,442 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-03 23:20:27,443 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-03 23:20:27,443 - ### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
### Karar Tamamlandı: Trachemys scripta elegans (Düşük)
2026-05-04 00:24:32,929 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 00:24:32,930 - Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'kahverengi', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "kahverengi",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T00:24:32.929037'}
Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'kahverengi', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "kahverengi",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T00:24:32.929037'}
2026-05-04 00:24:32,931 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-04 00:24:32,932 - ### Karar Tamamlandı: Trachemys scripta elegans (Yüksek)
### Karar Tamamlandı: Trachemys scripta elegans (Yüksek)
2026-05-04 01:12:33,955 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:12:33,956 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:12:33.955004'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:12:33.955004'}
2026-05-04 01:12:33,957 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-04 01:12:33,957 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:12:33,958 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:24:38,557 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:24:38,557 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:24:38.557280'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:24:38.557280'}
2026-05-04 01:24:38,558 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-04 01:24:38,558 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:24:38,558 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:30:48,257 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:30:48,257 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'belirsiz', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "belirsiz",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:30:48.257220'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'belirsiz', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "belirsiz",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:30:48.257220'}
2026-05-04 01:30:48,257 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:30:48,258 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:30:48,258 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:33:42,142 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:33:42,142 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': '4', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "4"\n}', 'extraction_timestamp': '2026-05-04T01:33:42.142188'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': '4', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "4"\n}', 'extraction_timestamp': '2026-05-04T01:33:42.142188'}
2026-05-04 01:33:42,142 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:33:42,143 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:33:42,143 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:34:09,908 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:34:09,908 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'siyah', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "siyah",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:34:09.908215'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'siyah', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "siyah",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:34:09.908215'}
2026-05-04 01:34:09,908 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-04 01:34:09,908 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:34:09,909 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 01:34:09,909 - ### Karar Tamamlandı: Testudo graeca (Yüksek)
### Karar Tamamlandı: Testudo graeca (Yüksek)
2026-05-04 01:35:27,980 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:35:27,980 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:35:27.980550'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:35:27.980550'}
2026-05-04 01:35:27,981 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-04 01:35:27,982 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:35:27,982 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 01:35:27,983 - ### Karar Tamamlandı: Testudo graeca (Yüksek)
### Karar Tamamlandı: Testudo graeca (Yüksek)
2026-05-04 01:37:28,162 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:37:28,163 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:37:28.162712'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:37:28.162712'}
2026-05-04 01:37:28,163 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-04 01:37:28,163 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:37:28,163 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 01:37:28,164 - ### Karar Tamamlandı: Testudo graeca (Yüksek)
### Karar Tamamlandı: Testudo graeca (Yüksek)
2026-05-04 01:37:47,334 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:37:47,334 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:37:47.334176'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:37:47.334176'}
2026-05-04 01:37:47,335 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-04 01:37:47,335 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:37:47,336 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 01:37:47,336 - ### Karar Tamamlandı: Testudo graeca (Yüksek)
### Karar Tamamlandı: Testudo graeca (Yüksek)
2026-05-04 01:38:29,052 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:38:29,053 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:38:29.052778'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:38:29.052778'}
2026-05-04 01:38:29,053 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:38:29,053 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:38:29,054 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:38:57,223 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:38:57,223 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:38:57.222969'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T01:38:57.222969'}
2026-05-04 01:38:57,223 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-04 01:38:57,224 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:38:57,224 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:39:18,732 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:39:18,733 - Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:39:18.732501'}
Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:39:18.732501'}
2026-05-04 01:39:18,733 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-04 01:39:18,734 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 01:39:18,734 - ### Karar Tamamlandı: Chelonia mydas (Yüksek)
### Karar Tamamlandı: Chelonia mydas (Yüksek)
2026-05-04 01:48:46,602 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:48:46,603 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'siyah', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "analiz_notlari": "Bu kaplumbağa yavrusu, ön ayaklarında belirgin pençelere sahip olup, deniz kaplumbağalarında görülen yüzgeç yapısını göstermemektedir. Kabuğu ağırlıklı olarak siyah renkte ve üzerinde çok sayıda küçük, açık renkli benekler bulunmaktadır. Uzun ve sivri kuyruk yapısı dikkat çekicidir. Kafasındaki pullar küçük ve granüler yapıda olup, deniz kaplumbağalarında kritik olan belirgin büyük prefrontal pul gruplarını ayırt etmek mümkün değildir.",\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "siyah",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:48:46.602730'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'siyah', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'belirsiz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "analiz_notlari": "Bu kaplumbağa yavrusu, ön ayaklarında belirgin pençelere sahip olup, deniz kaplumbağalarında görülen yüzgeç yapısını göstermemektedir. Kabuğu ağırlıklı olarak siyah renkte ve üzerinde çok sayıda küçük, açık renkli benekler bulunmaktadır. Uzun ve sivri kuyruk yapısı dikkat çekicidir. Kafasındaki pullar küçük ve granüler yapıda olup, deniz kaplumbağalarında kritik olan belirgin büyük prefrontal pul gruplarını ayırt etmek mümkün değildir.",\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "siyah",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "belirsiz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:48:46.602730'}
2026-05-04 01:48:46,603 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-04 01:48:46,604 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:48:46,604 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 01:48:46,604 - ### Karar Tamamlandı: Testudo graeca (Yüksek)
### Karar Tamamlandı: Testudo graeca (Yüksek)
2026-05-04 01:49:22,435 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:49:22,435 - Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "analiz_notlari": "Fotoğraftaki kaplumbağanın belirgin kırmızı-turuncu yanak şeridi, boynundaki sarı çizgiler ve kabuğundaki benzer renkteki desenler, bir tatlı su kaplumbağası olduğunu düşündürmektedir. Gaga yapısı hafif kıvrık olup, ön ayak yapısı ve kafa pulları net görülemediğinden belirsizdir. Kabuk kenarları gözlemlenen kısımda düz görünmektedir.",\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:49:22.435056'}
Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'evet', 'ayak_yapisi': 'belirsiz', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "analiz_notlari": "Fotoğraftaki kaplumbağanın belirgin kırmızı-turuncu yanak şeridi, boynundaki sarı çizgiler ve kabuğundaki benzer renkteki desenler, bir tatlı su kaplumbağası olduğunu düşündürmektedir. Gaga yapısı hafif kıvrık olup, ön ayak yapısı ve kafa pulları net görülemediğinden belirsizdir. Kabuk kenarları gözlemlenen kısımda düz görünmektedir.",\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "belirsiz",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:49:22.435056'}
2026-05-04 01:49:22,435 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Trachemys scripta elegans
2026-05-04 01:49:22,435 - ### Karar Tamamlandı: Trachemys scripta elegans (Yüksek)
### Karar Tamamlandı: Trachemys scripta elegans (Yüksek)
2026-05-04 01:49:44,551 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 01:49:44,551 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "analiz_notlari": "Gözlemlenen kaplumbağa, güçlü pençelere sahip karasal ayak yapısı ile bir kara veya tatlı su kaplumbağası olduğunu düşündürmektedir. Kabuğu yüksek kemerli olup, koyu kahverengi/siyah zemin üzerinde belirgin sarı/turuncu radyasyonlu desenlere sahiptir. Kafa üzerindeki pullar küçük ve granüler olduğundan, deniz kaplumbağalarına özgü büyük prefrontal pul gruplarını saymak mümkün değildir.",\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:49:44.551075'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "analiz_notlari": "Gözlemlenen kaplumbağa, güçlü pençelere sahip karasal ayak yapısı ile bir kara veya tatlı su kaplumbağası olduğunu düşündürmektedir. Kabuğu yüksek kemerli olup, koyu kahverengi/siyah zemin üzerinde belirgin sarı/turuncu radyasyonlu desenlere sahiptir. Kafa üzerindeki pullar küçük ve granüler olduğundan, deniz kaplumbağalarına özgü büyük prefrontal pul gruplarını saymak mümkün değildir.",\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T01:49:44.551075'}
2026-05-04 01:49:44,551 - ✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
✅ ayak_yapisi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Pençe ayak yapısı deniz kaplumbağalarında bulunmaz.)
2026-05-04 01:49:44,551 - ✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
✅ yanak_seridi tespit edildi -> Trachemys scripta elegans elendi (Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.)
2026-05-04 01:49:44,552 - ⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 01:49:44,552 - ### Karar Tamamlandı: Testudo graeca (Yüksek)
### Karar Tamamlandı: Testudo graeca (Yüksek)
2026-05-04 02:59:46,301 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 02:59:46,302 - Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": ["Trachemys scripta elegans", "Trachemys scripta scripta", "Trachemys scripta troostii"],\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T02:59:46.301445'}
Gelen Özellikler: {'yanak_seridi': 'evet', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": ["Trachemys scripta elegans", "Trachemys scripta scripta", "Trachemys scripta troostii"],\n  "yanak_seridi": "evet",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T02:59:46.301445'}
2026-05-04 02:59:46,302 - Gemini'ın Ön Elediği ve Karar Ağacına Giren Adaylar: ['Chelonia mydas', 'Caretta caretta', 'Eretmochelys imbricata', 'Dermochelys coriacea', 'Trachemys scripta elegans', 'Testudo graeca', 'Testudo hermanni', 'Mauremys rivulata']
Gemini'ın Ön Elediği ve Karar Ağacına Giren Adaylar: ['Chelonia mydas', 'Caretta caretta', 'Eretmochelys imbricata', 'Dermochelys coriacea', 'Trachemys scripta elegans', 'Testudo graeca', 'Testudo hermanni', 'Mauremys rivulata']
2026-05-04 02:59:46,303 - ✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
✅ ayak_yapisi tespit edildi -> Trachemys scripta elegans, Testudo graeca, Testudo hermanni, Mauremys rivulata elendi (Perde ayak yapısı sadece deniz kaplumbağalarında bulunur.)
2026-05-04 02:59:46,303 - ✅ yanak_seridi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Kırmızı/turuncu yanak şeridi ağırlıklı olarak Kızıl Yanaklı kaplumbağalarda bulunur.)
✅ yanak_seridi tespit edildi -> Chelonia mydas, Caretta caretta, Eretmochelys imbricata, Dermochelys coriacea elendi (Kırmızı/turuncu yanak şeridi ağırlıklı olarak Kızıl Yanaklı kaplumbağalarda bulunur.)
2026-05-04 02:59:46,304 - ❌ Tüm adaylar elendi!
❌ Tüm adaylar elendi!
2026-05-04 02:59:46,304 - ### Karar Tamamlandı: None (Düşük)
### Karar Tamamlandı: None (Düşük)
2026-05-04 03:04:12,287 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:04:12,287 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Macrochelys temminckii",\n    "Macrochelys suwanniensis",\n    "Macrochelys apalachicolae"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:04:12.287439'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Macrochelys temminckii",\n    "Macrochelys suwanniensis",\n    "Macrochelys apalachicolae"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:04:12.287439'}
2026-05-04 03:04:12,288 - ⚖️ Puanlama yapıldı. Tahmin: Eretmochelys imbricata
⚖️ Puanlama yapıldı. Tahmin: Eretmochelys imbricata
2026-05-04 03:05:36,227 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:05:36,228 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Terrapene carolina",\n    "Terrapene carolina carolina",\n    "Terrapene ornata"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:05:36.227057'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'evet', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Terrapene carolina",\n    "Terrapene carolina carolina",\n    "Terrapene ornata"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:05:36.227057'}
2026-05-04 03:05:36,228 - ⚖️ Puanlama yapıldı. Tahmin: Testudo graeca
⚖️ Puanlama yapıldı. Tahmin: Testudo graeca
2026-05-04 03:10:50,079 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:10:50,080 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Macrochelys suwanniensis",\n    "Macrochelys apalachicolae",\n    "Macrochelys temminckii"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:10:50.079818'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'kanca', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'girintili', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Macrochelys suwanniensis",\n    "Macrochelys apalachicolae",\n    "Macrochelys temminckii"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "kanca",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "girintili",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:10:50.079818'}
2026-05-04 03:10:50,080 - ⚖️ Puanlama yapıldı. Tahmin: Eretmochelys imbricata
⚖️ Puanlama yapıldı. Tahmin: Eretmochelys imbricata
2026-05-04 03:12:35,537 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:12:35,537 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": ["Chelonia mydas", "Natator depressus", "Caretta caretta"],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T03:12:35.537138'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'hayır', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'perde', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': '2', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": ["Chelonia mydas", "Natator depressus", "Caretta caretta"],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "hayır",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "perde",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "2"\n}', 'extraction_timestamp': '2026-05-04T03:12:35.537138'}
2026-05-04 03:12:35,538 - ⚖️ Puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Puanlama yapıldı. Tahmin: Chelonia mydas
