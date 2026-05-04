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
2026-05-04 03:16:36,574 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:16:36,574 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Glyptemys muhlenbergii",\n    "Clemmys guttata",\n    "Terrapene carolina"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:16:36.573911'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'düz', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'hayır', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": [\n    "Glyptemys muhlenbergii",\n    "Clemmys guttata",\n    "Terrapene carolina"\n  ],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "düz",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "hayır",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:16:36.573911'}
2026-05-04 03:16:36,575 - ⚖️ Puanlama yapıldı. Tahmin: Testudo hermanni
⚖️ Puanlama yapıldı. Tahmin: Testudo hermanni
2026-05-04 03:17:29,176 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:17:29,177 - Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'evet', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": ["Terrapene carolina", "Terrapene ornata", "Cuora flavomarginata"],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:17:29.176239'}
Gelen Özellikler: {'yanak_seridi': 'hayır', 'gaga_yapisi': 'hafif_kıvrık', 'kabuk_rengi': 'karışık', 'kabuk_sari_benek': 'evet', 'boyun_deseni': 'evet', 'ayak_yapisi': 'pençe', 'kabuk_kenari': 'düz', 'kafa_pul_sayisi': 'belirsiz', 'api_model': 'gemini-2.5-flash', 'raw_response': '{\n  "olasi_adaylar": ["Terrapene carolina", "Terrapene ornata", "Cuora flavomarginata"],\n  "yanak_seridi": "hayır",\n  "gaga_yapisi": "hafif_kıvrık",\n  "kabuk_rengi": "karışık",\n  "kabuk_sari_benek": "evet",\n  "boyun_deseni": "evet",\n  "ayak_yapisi": "pençe",\n  "kabuk_kenari": "düz",\n  "kafa_pul_sayisi": "belirsiz"\n}', 'extraction_timestamp': '2026-05-04T03:17:29.176239'}
2026-05-04 03:17:29,178 - ⚖️ Puanlama yapıldı. Tahmin: Testudo hermanni
⚖️ Puanlama yapıldı. Tahmin: Testudo hermanni
2026-05-04 03:27:02,790 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:27:02,791 - ⚖️ Puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 03:28:09,828 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:28:09,829 - ⚖️ Puanlama yapıldı. Tahmin: Testudo hermanni
⚖️ Puanlama yapıldı. Tahmin: Testudo hermanni
2026-05-04 03:30:01,573 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 03:30:01,573 - ⚖️ Puanlama yapıldı. Tahmin: Chelonia mydas
⚖️ Puanlama yapıldı. Tahmin: Chelonia mydas
2026-05-04 10:55:03,146 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 10:55:03,147 - ⚖️ Puanlama yapıldı. Tahmin: Stigmochelys pardalis
⚖️ Puanlama yapıldı. Tahmin: Stigmochelys pardalis

## [2026-05-04 14:35] Karar Mantığı İyileştirmesi (Hibrit Yaklaşım)
**Yapılan Değişiklikler:**
- **Gemini Önceliği:** src/decision_tree.py içindeki decide metodu, Gemini'dan gelen olasi_turler listesindeki güven skorlarını kontrol edecek şekilde güncellendi.
- **Yüksek Güven Eşiği:** Eğer Gemini bir tür için %85 veya daha fazla güven duyuyorsa, bu tür veritabanında (15 tür) olmasa bile doğrudan sonuç olarak döndürülüyor.
- **Fallback Mekanizması:** Veritabanı ile yapılan morfolojik eşleşme skoru çok düşükse (< 0.4), sistem otomatik olarak Gemini'ın en olası gördüğü türe güveniyor.
- **Dinamik İsimlendirme:** Veritabanı dışı türler için "Veritabanı Dışı / Küresel Tür" etiketi eklendi.

**Sonuç:** Sistem artık hem kural tabanlı (yerel türler için kesinlik) hem de model tabanlı (küresel türler için esneklik) hibrit bir yapıda çalışıyor.
2026-05-04 11:08:34,485 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:08:34,485 - 🌟 Gemini Yüksek Güven (%98.0): Terrapene carolina
🌟 Gemini Yüksek Güven (%98.0): Terrapene carolina
2026-05-04 11:11:38,719 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:38,719 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:11:38,721 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:38,721 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:11:38,722 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:38,723 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
2026-05-04 11:11:38,724 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:38,724 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:11:38,725 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:38,725 - ⚖️ Puanlama tamamlandı. Tahmin: Graptemys geographica (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Graptemys geographica (Puan: 3.0)
2026-05-04 11:11:46,765 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:46,766 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:11:46,769 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:46,770 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:11:46,772 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:46,773 - ⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
2026-05-04 11:11:46,776 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:46,777 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:11:46,779 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:11:46,780 - ⚖️ Puanlama tamamlandı. Tahmin: Terrapene carolina (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Terrapene carolina (Puan: 3.0)
2026-05-04 11:12:03,151 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:03,152 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:03,154 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:03,154 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:03,156 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:03,156 - ⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
2026-05-04 11:12:03,157 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:03,157 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:03,168 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:03,169 - ⚖️ Puanlama tamamlandı. Tahmin: Chelydra serpentina (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelydra serpentina (Puan: 3.0)
2026-05-04 11:12:10,196 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:10,197 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:10,199 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:10,199 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:10,201 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:10,201 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo graeca (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo graeca (Puan: 1.0)
2026-05-04 11:12:10,202 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:10,203 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:10,205 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:10,205 - ⚖️ Puanlama tamamlandı. Tahmin: Macrochelys temminckii (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Macrochelys temminckii (Puan: 3.0)
2026-05-04 11:12:21,391 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,391 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
2026-05-04 11:12:21,393 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,393 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:12:21,394 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,395 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:21,395 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,396 - ⚖️ Puanlama tamamlandı. Tahmin: Chrysemys picta (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chrysemys picta (Puan: 3.0)
2026-05-04 11:12:21,397 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,397 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
2026-05-04 11:12:21,398 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,399 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:12:21,400 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:21,400 - ⚖️ Puanlama tamamlandı. Tahmin: Chrysemys picta (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chrysemys picta (Puan: 3.0)
2026-05-04 11:12:28,294 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,294 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
2026-05-04 11:12:28,298 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,299 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:12:28,299 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,300 - ⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
2026-05-04 11:12:28,300 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,301 - ⚖️ Puanlama tamamlandı. Tahmin: Geochelone elegans (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Geochelone elegans (Puan: 3.0)
2026-05-04 11:12:28,301 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,302 - ⚖️ Puanlama tamamlandı. Tahmin: Geochelone elegans (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Geochelone elegans (Puan: 3.0)
2026-05-04 11:12:28,302 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,303 - ⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
2026-05-04 11:12:28,305 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,306 - ⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
2026-05-04 11:12:28,308 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,308 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:12:28,311 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:28,311 - ⚖️ Puanlama tamamlandı. Tahmin: Geochelone elegans (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Geochelone elegans (Puan: 3.0)
2026-05-04 11:12:34,126 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,126 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
2026-05-04 11:12:34,128 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,128 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:12:34,129 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,129 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:34,129 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,129 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonoidis carbonarius (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonoidis carbonarius (Puan: 3.0)
2026-05-04 11:12:34,130 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,130 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonoidis carbonarius (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonoidis carbonarius (Puan: 3.0)
2026-05-04 11:12:34,130 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,130 - ⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Eretmochelys imbricata (Puan: 3.0)
2026-05-04 11:12:34,132 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,133 - ⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Mauremys rivulata (Puan: 1.0)
2026-05-04 11:12:34,134 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,134 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:12:34,135 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:34,136 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonoidis carbonarius (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonoidis carbonarius (Puan: 3.0)
2026-05-04 11:12:41,744 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,745 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
2026-05-04 11:12:41,747 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,747 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:41,747 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,748 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:41,748 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,748 - ⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
2026-05-04 11:12:41,749 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,749 - ⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
2026-05-04 11:12:41,750 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,750 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 3.0)
2026-05-04 11:12:41,752 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,752 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
2026-05-04 11:12:41,753 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,754 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:12:41,755 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:41,756 - ⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
2026-05-04 11:12:48,236 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,237 - ⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
⚖️ Puanlama tamamlandı. Tahmin: Chelonia mydas (Puan: 4.0)
2026-05-04 11:12:48,240 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,240 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:12:48,241 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,241 - ⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
2026-05-04 11:12:48,242 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,242 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 3.0)
2026-05-04 11:12:48,243 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,243 - ⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Centrochelys sulcata (Puan: 3.0)
2026-05-04 11:12:48,244 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,244 - ⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 3.0)
2026-05-04 11:12:48,245 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,246 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 1.0)
2026-05-04 11:12:48,247 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,247 - ⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Dermochelys coriacea (Puan: 3.0)
2026-05-04 11:12:48,248 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:12:48,249 - ⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 3.0)
⚖️ Puanlama tamamlandı. Tahmin: Testudo hermanni (Puan: 3.0)
2026-05-04 11:16:41,869 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:16:41,869 - 🌟 Gemini Yüksek Güven (%95.0): Caretta caretta
🌟 Gemini Yüksek Güven (%95.0): Caretta caretta
2026-05-04 11:16:41,870 - ⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 6.5)
⚖️ Puanlama tamamlandı. Tahmin: Caretta caretta (Puan: 6.5)

## [2026-05-04 15:30] Self-Elimination Hatası Giderildi
**Sorun:** Gemini'ın %85+ güvenle bildiği türler, küçük morfolojik uyuşmazlıklar nedeniyle eleniyor ve sistem "Bilinmeyen" döndürüyordu.
**Çözüm:** src/decision_tree.py güncellendi. Eğer tüm adaylar elenirse ve Gemini güveni yüksekse, en yüksek skorlu aday "Görsel Güven" notuyla sürece geri dahil ediliyor.
**Sonuç:** Sistem artık daha esnek ve kullanıcı dostu. Morfoloji çelişse bile görsel kanıt güçlüyse sonuç gösteriliyor.
2026-05-04 11:23:47,079 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:23:47,080 - 🌟 Gemini Yüksek Güven (%98.0): Caretta caretta
🌟 Gemini Yüksek Güven (%98.0): Caretta caretta
2026-05-04 11:23:47,080 - ### Karar Tamamlandı: Caretta caretta (yüksek)
### Karar Tamamlandı: Caretta caretta (yüksek)
## [2026-05-04 14:30] Karar Ağacı Güvenilirlik Güncellemesi

**HATA ANALİZİ VE DÜZELTME:**
- **Problem:** Caretta caretta vakalarında prefrontal pul sayısının '4' veya '2 çift' olarak tespit edilmesine rağmen, sistemin sadece tek bir değere odaklanıp türü elemesi.
- **Düzeltme:** src/decision_tree.py içinde morfolojik tolerans mantığı eklendi. Artık '4', '2 çift', 'dört' gibi ifadeler Caretta caretta için geçerli kabul ediliyor.

**SOLID VE CLEAN CODE DENETİMİ:**
- src/decision_tree.py dosyası TurtleVision standartlarına göre optimize edildi.
- Sert eleme (Strict Elimination) yerine Puanlama (Scoring) ağırlıklı sisteme geçildi.
- "Geri Çağırma" (Recall) mekanizması ile Gemini güveni %90+ olan türlerin tek bir morfolojik uyuşmazlıkla elenmesi engellendi.

**VERİTABANI GÜNCELLEMELERİ:**
- src/turtles_db.json içinde common_name_tr alanları eksik olan türler için standardizasyon yapıldı.
- kafa_pul_sayisi verileri prefrontal pul tanımlarıyla uyumlu hale getirildi.

**SONUÇ:**
- Caretta caretta için Gemini %98 güven verdiğinde, tek bir özellik uyuşmazlığı olsa bile sonuç artık "Bilinmeyen" dönmeyecek. Adaylar listesinde korunacak.
2026-05-04 11:31:45,698 - 
### Karar Süreci Başladı

### Karar Süreci Başladı
2026-05-04 11:31:45,698 - 🌟 Gemini Yüksek Güven (%98.0): Terrapene carolina carolina
🌟 Gemini Yüksek Güven (%98.0): Terrapene carolina carolina
2026-05-04 11:37:13,280 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,282 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,282 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,282 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,283 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,283 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,284 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,285 - Seçilen aday: Trachemys scripta elegans, Güven: %68.6
Seçilen aday: Trachemys scripta elegans, Güven: %68.6
2026-05-04 11:37:13,287 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:37:13,287 - Seçilen aday: Chelonia mydas, Güven: %90.0
Seçilen aday: Chelonia mydas, Güven: %90.0
2026-05-04 11:39:28,274 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:39:28,275 - Seçilen aday: Trachemys scripta elegans, Güven: %68.6
Seçilen aday: Trachemys scripta elegans, Güven: %68.6
2026-05-04 11:39:28,276 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:39:28,276 - Seçilen aday: Chelonia mydas, Güven: %90.0
Seçilen aday: Chelonia mydas, Güven: %90.0
2026-05-04 11:39:30,375 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:39:30,375 - Seçilen aday: Trachemys scripta elegans, Güven: %68.6
Seçilen aday: Trachemys scripta elegans, Güven: %68.6
2026-05-04 11:39:30,376 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:39:30,377 - Seçilen aday: Chelonia mydas, Güven: %90.0
Seçilen aday: Chelonia mydas, Güven: %90.0
2026-05-04 11:47:58,557 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:47:58,557 - Seçilen aday: Terrapene carolina carolina, Güven: %90.0
Seçilen aday: Terrapene carolina carolina, Güven: %90.0
2026-05-04 11:48:59,262 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:48:59,263 - Seçilen aday: Caretta caretta, Güven: %73.0
Seçilen aday: Caretta caretta, Güven: %73.0
2026-05-04 11:52:30,350 - 
## Karar Süreci Başladı

## Karar Süreci Başladı
2026-05-04 11:52:30,350 - Seçilen aday: Caretta caretta, Güven: %73.0
Seçilen aday: Caretta caretta, Güven: %73.0
2026-05-04 11:58:08,784 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,849 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,849 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,849 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,850 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,850 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,853 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,853 - Seçilen aday: Trachemys scripta elegans, Gemini Güveni: %98.0, Nihai Güven: %93.1
Seçilen aday: Trachemys scripta elegans, Gemini Güveni: %98.0, Nihai Güven: %93.1
2026-05-04 11:58:08,864 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,864 - Seçilen aday: Chelonia mydas, Gemini Güveni: %90.0, Nihai Güven: %90.5
Seçilen aday: Chelonia mydas, Gemini Güveni: %90.0, Nihai Güven: %90.5
2026-05-04 11:58:08,870 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,871 - Seçilen aday: Trachemys scripta elegans, Gemini Güveni: %98.0, Nihai Güven: %93.1
Seçilen aday: Trachemys scripta elegans, Gemini Güveni: %98.0, Nihai Güven: %93.1
2026-05-04 11:58:08,874 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:08,874 - Seçilen aday: Chelonia mydas, Gemini Güveni: %90.0, Nihai Güven: %90.5
Seçilen aday: Chelonia mydas, Gemini Güveni: %90.0, Nihai Güven: %90.5
2026-05-04 11:58:25,539 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:25,540 - Seçilen aday: Trachemys scripta elegans, Gemini Güveni: %90.0, Nihai Güven: %85.5
Seçilen aday: Trachemys scripta elegans, Gemini Güveni: %90.0, Nihai Güven: %85.5
2026-05-04 11:58:25,542 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:25,543 - Seçilen aday: Chelonia mydas, Gemini Güveni: %70.0, Nihai Güven: %66.5
Seçilen aday: Chelonia mydas, Gemini Güveni: %70.0, Nihai Güven: %66.5
2026-05-04 11:58:25,545 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 11:58:25,545 - Seçilen aday: Chelonia mydas, Gemini Güveni: %90.0, Nihai Güven: %90.5
Seçilen aday: Chelonia mydas, Gemini Güveni: %90.0, Nihai Güven: %90.5
## [2026-05-04 15:30] Karar Sistemi Güncellendi
**Sistem Mimarisi:** Gemini Tahmin Odaklı
**Ağırlıklar:** %95 Gemini, %5 Morfolojik Doğrulama
**Eleme Mantığı:** Bilgilendirme Seviyesine Çekildi (Tür Eleme Artık Yapılmıyor)
**Yeni Veri Yapısı:** 	op_3_comparison eklendi (İlk 3 türün ideal özellikleri)
## [2026-05-04 15:30] Karar Sistemi Güncellendi
**Sistem Mimarisi:** Gemini Tahmin Odaklı
**Ağırlıklar:** %95 Gemini, %5 Morfolojik Doğrulama
**Eleme Mantığı:** Bilgilendirme Seviyesine Çekildi (Tür Eleme Artık Yapılmıyor)
**Yeni Veri Yapısı:** 	op_3_comparison eklendi (İlk 3 türün ideal özellikleri)
2026-05-04 12:07:55,250 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:07:55,250 - Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
2026-05-04 12:11:02,531 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:11:02,532 - Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
2026-05-04 12:12:51,946 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:12:51,946 - Seçilen aday: None, Gemini Güveni: %90.0, Nihai Güven: %90.5
Seçilen aday: None, Gemini Güveni: %90.0, Nihai Güven: %90.5
2026-05-04 12:16:18,113 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:16:18,113 - Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
2026-05-04 12:17:00,659 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:17:00,659 - Seçilen aday: None, Gemini Güveni: %90.0, Nihai Güven: %90.5
Seçilen aday: None, Gemini Güveni: %90.0, Nihai Güven: %90.5
2026-05-04 12:22:06,361 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:22:06,362 - Seçilen aday: None, Gemini Güveni: %90.0, Nihai Güven: %90.5
Seçilen aday: None, Gemini Güveni: %90.0, Nihai Güven: %90.5
2026-05-04 12:33:08,701 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:33:08,702 - Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
Seçilen aday: None, Gemini Güveni: %95.0, Nihai Güven: %95.2
2026-05-04 12:34:03,538 - 
## Karar Süreci Başladı (Gemini Tahmin Odaklı)

## Karar Süreci Başladı (Gemini Tahmin Odaklı)
2026-05-04 12:34:03,539 - Seçilen aday: None, Gemini Güveni: %98.0, Nihai Güven: %98.1
Seçilen aday: None, Gemini Güveni: %98.0, Nihai Güven: %98.1
