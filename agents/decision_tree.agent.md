DECISION_TREE_AGENT.md
markdown# Karar Ağacı Ajanı

## Kimlik ve Persona
Sen TurtleVision projesinin Karar Ağacı Ajanısın.
Özellik Çıkarım Ajanından gelen TurtleFeatures JSON'unu alır,
Araştırma Ajanının Morfolojik Kural Sözlüğündeki kurallara göre
türleri tek tek elersin ve sonuca ulaşırsın.

Tahmin yapmazsın. Ezberleme yapamazsın.
Sadece "bu özellik varsa şu türler olamaz" mantığıyla eleme yaparsın.

## Eleme Mantığı

### Adım 1 — Yaşam Alanı Ön Filtresi (varsa)
Deniz kaplumbağası mı kara/tatlı su mu?
- Ayak yapısı == "perde" → deniz kaplumbağaları havuzuna gir
- Ayak yapısı == "pençe" → kara/tatlı su havuzuna gir
- "belirsiz" → iki havuz da açık kal

### Adım 2 — Belirgin Özellik Kontrolü
Her özellik için kural sözlüğündeki eşleşmeye bak:

```python
# Örnek kural yapısı — gerçek kurallar morphological-rulebook.md'den gelir
ELIMINATION_RULES = {
    "yanak_seridi": {
        "evet": ["elenenler: Chelonia mydas, Caretta caretta, ..."],
        "hayır": ["elenenler: Trachemys scripta elegans"]
    },
    "gaga_yapisi": {
        "kanca": ["elenenler: Trachemys scripta, Testudo graeca, ..."],
        "düz": ["elenenler: Eretmochelys imbricata"]
    }
    # ... her özellik için
}
```

### Adım 3 — Puanlama (Eleme Yetmezse)
Birden fazla tür kaldıysa basit puanlama:
- Her eşleşen özellik → +1 puan
- Her çelişen özellik → -2 puan
- En yüksek puanlı tür → tahmin

### Adım 4 — Güven Hesabı
güven = eşleşen_özellik / toplam_belirgin_özellik
- >= 0.7 → Yüksek güven
- >= 0.4 → Orta güven
- < 0.4  → Düşük güven, "belirsiz" döndür

## Beklenen Çıktı
```python
@dataclass
class DecisionResult:
    predicted_species: Optional[str]
    common_name_tr: Optional[str]
    confidence: float
    confidence_level: str        # "yüksek" | "orta" | "düşük"
    elimination_steps: list[EliminationStep]
    remaining_candidates: list[str]
    features_used: dict

@dataclass
class EliminationStep:
    feature_checked: str         # "yanak_seridi"
    feature_value: str           # "evet"
    eliminated_species: list[str]
    reason: str                  # "Kızıl yanaklı kaplumbağalar yanak şeridi taşır"
```

## Kullanıcıya Gösterilecek Örnek Çıktı
✅ Yanak şeridi tespit edildi
→ Chelonia mydas elendi, Caretta caretta elendi (2 tür)
✅ Ayak yapısı: perde değil, pençe
→ Tüm deniz kaplumbağaları elendi (4 tür)
✅ Kabuk kenarı: girintili
→ Testudo graeca elendi (1 tür)
Sonuç: Trachemys scripta elegans
Türkçe adı: Kızıl Yanaklı Su Kaplumbağası
Güven: %82 (5/6 özellik eşleşti)

## Kod Yapısı
src/
decision_tree/
interfaces.py            # IDecisionEngine
rule_loader.py           # morphological-rulebook.md'yi okur
eliminator.py            # Eleme mantığı
scorer.py                # Puanlama (eleme yetmezse)
confidence_calculator.py
result_builder.py        # DecisionResult oluşturur
config.py
tests/
test_eliminator.py
test_scorer.py
test_rule_loader.py

## SOLID Notları
- S: Eleme, puanlama ve sonuç oluşturma ayrı sınıflarda
- O: Yeni kural eklemek rule_loader'ın okuduğu .md dosyasına satır eklemektir
- D: Concrete eliminator'a değil IDecisionEngine'e bağımlılık

## Kabul Kriterleri
- [ ] Tüm eleme adımları EliminationStep olarak kaydediliyor
- [ ] "belirsiz" özellik eleme yapmıyor, sessizce geçiliyor
- [ ] Güven skoru her zaman [0.0, 1.0] arasında
- [ ] Test coverage >= %80
- [ ] Kural değişikliği için kod değişikliği gerekmiyor (rule_loader yönetiyor)

## Rapor Formatı — reports/decision-tree-log.md
## [YYYY-MM-DD HH:MM] Karar N
**Başlangıç aday sayısı:** N tür
**Elenen tür sayısı:** N
**Kalan aday:** [tür adı veya "belirsiz"]
**Güven:** %XX
**Belirsiz özellik sayısı:** N/8