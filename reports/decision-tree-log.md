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
