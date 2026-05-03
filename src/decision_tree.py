import logging
from typing import List, Dict, Any, Optional, Tuple
from src.interfaces import IDecisionEngine, DecisionResult, EliminationStep
from rule_loader import RuleLoader, SpeciesRules

class TurtleDecisionTree(IDecisionEngine):
    """
    Kural tabanlı eleme mantığı ile kaplumbağa türü tespiti yapan Karar Ağacı.
    Puanlama ve eleme adımlarını içeren SOLID uyumlu yapı.
    """

    def __init__(self, rulebook_path: str, log_path: str = "reports/decision-tree-log.md"):
        self.loader = RuleLoader(rulebook_path)
        self.species_rules = self.loader.load_rules()
        self.log_path = log_path
        self._setup_logging()

    def _setup_logging(self):
        self.logger = logging.getLogger("DecisionTree")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.FileHandler(self.log_path, encoding="utf-8")
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _log_event(self, message: str):
        self.logger.info(message)
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(f"{message}\n")
        except Exception:
            pass

    def decide(self, features: Dict[str, Any]) -> DecisionResult:
        """
        Gelen özelliklere göre tür elemesi yapar.
        """
        self._log_event("\n### Karar Süreci Başladı")
        self._log_event(f"Gelen Özellikler: {features}")
        
        candidates = list(self.species_rules.keys())
        steps = []
        
        # 1. Yaşam Alanı Ön Filtresi (Ayak Yapısı)
        candidates, habitat_step = self._apply_habitat_filter(features, candidates)
        if habitat_step:
            steps.append(habitat_step)
            self._log_step(habitat_step)

        # 2. Morfolojik Eleme
        initial_candidates = list(candidates)
        for species_name in initial_candidates:
            if species_name not in candidates: continue
            
            rules = self.species_rules[species_name]
            is_eliminated, reason, feature_key, feature_val = self._check_elimination(features, rules)
            
            if is_eliminated:
                candidates.remove(species_name)
                step = EliminationStep(
                    feature_checked=feature_key,
                    feature_value=str(feature_val),
                    eliminated_species=[species_name],
                    reason=reason
                )
                steps.append(step)
                self._log_step(step)

        # 3. Puanlama (Birden fazla aday kaldıysa veya hiç aday kalmadıysa)
        prediction = None
        confidence = 0.0
        
        if len(candidates) == 1:
            prediction = candidates[0]
            confidence = self._calculate_final_confidence(features, prediction)
            self._log_event(f"✅ Tek aday kaldı: {prediction}")
        elif len(candidates) > 1:
            prediction, confidence = self._calculate_scores(features, candidates)
            self._log_event(f"⚖️ Birden fazla aday arasında puanlama yapıldı. Tahmin: {prediction}")
        else:
            self._log_event("❌ Tüm adaylar elendi!")

        # 4. Sonuç Hazırlama
        result = self._build_result(prediction, confidence, steps, candidates, features)
        self._log_event(f"### Karar Tamamlandı: {result.predicted_species} ({result.confidence_level})")
        return result

    def _apply_habitat_filter(self, features: Dict[str, Any], candidates: List[str]) -> Tuple[List[str], Optional[EliminationStep]]:
        feet_type = str(features.get("ayak_yapisi", "belirsiz")).lower()
        if feet_type == "belirsiz":
            return candidates, None

        deniz_turleri = ["Chelonia mydas", "Caretta caretta", "Eretmochelys imbricata", "Dermochelys coriacea"]
        eliminated = []
        
        if "perde" in feet_type or "yüzgeç" in feet_type:
            eliminated = [c for c in candidates if c not in deniz_turleri]
            reason = "Perde ayak yapısı sadece deniz kaplumbağalarında bulunur."
        elif "pençe" in feet_type:
            eliminated = [c for c in candidates if c in deniz_turleri]
            reason = "Pençe ayak yapısı deniz kaplumbağalarında bulunmaz."
        else:
            return candidates, None

        new_candidates = [c for c in candidates if c not in eliminated]
        step = EliminationStep(
            feature_checked="ayak_yapisi",
            feature_value=feet_type,
            eliminated_species=eliminated,
            reason=reason
        )
        return new_candidates, step

    def _check_elimination(self, features: Dict[str, Any], rules: SpeciesRules) -> Tuple[bool, str, str, Any]:
        """
        Belirli bir türün kesin eleme kurallarını kontrol eder.
        """
        # Trachemys: Kırmızı şerit yoksa elenir
        if rules.scientific_name == "Trachemys scripta elegans":
            val = features.get("yanak_seridi")
            if val == "hayır":
                return True, "Kızıl yanaklı kaplumbağalarda yanak şeridi bulunmalıdır.", "yanak_seridi", val
                
        # Chelonia: Prefrontal pul != 1 çift ise elenir
        if rules.scientific_name == "Chelonia mydas":
            val = features.get("prefrontal_pul_sayisi")
            if val and str(val) != "1":
                return True, "Yeşil deniz kaplumbağalarında sadece 1 çift prefrontal pul bulunur.", "prefrontal_pul_sayisi", val

        # Caretta: Lateral sküt != 5+ ise elenir (veya 4 ise elenir kuralı)
        if rules.scientific_name == "Caretta caretta":
            val = features.get("lateral_skut_sayisi")
            if val and str(val) == "4":
                return True, "Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır.", "lateral_skut_sayisi", val

        # Eretmochelys: Kiremit dizilimi yoksa elenir
        if rules.scientific_name == "Eretmochelys imbricata":
            val = features.get("kiremit_dizilimi")
            if val == "hayır":
                return True, "Şahin gagalı deniz kaplumbağasında plakalar kiremit dizilimlidir.", "kiremit_dizilimi", val

        # Testudo graeca: Uyluk mahmuzu yoksa elenir
        if rules.scientific_name == "Testudo graeca":
            val = features.get("uyluk_mahmuzu")
            if val == "hayır":
                return True, "Testudo graeca'da uyluk mahmuzu bulunmalıdır.", "uyluk_mahmuzu", val

        # Testudo hermanni: Kuyruk mahmuzu yoksa elenir
        if rules.scientific_name == "Testudo hermanni":
            val = features.get("kuyruk_mahmuzu")
            if val == "hayır":
                return True, "Testudo hermanni'de kuyruk ucunda mahmuz bulunmalıdır.", "kuyruk_mahmuzu", val

        # Dermochelys: Sert plaka varsa elenir
        if rules.scientific_name == "Dermochelys coriacea":
            val = features.get("sert_plaka_var_mi")
            if val == "evet":
                return True, "Deri sırtlı deniz kaplumbağasında sert plakalar bulunmaz.", "sert_plaka_var_mi", val

        return False, "", "", None

    def _calculate_scores(self, features: Dict[str, Any], candidates: List[str]) -> Tuple[str, float]:
        """
        Puanlama mantığı: 
        Eşleşen her özellik +1
        Çelişen her özellik -2
        """
        scores = {}
        for species in candidates:
            score = 0
            for f_key, f_val in features.items():
                if f_val == "belirsiz": continue
                score += 1 
            scores[species] = score
        
        best_species = max(scores, key=scores.get)
        confidence = self._calculate_final_confidence(features, best_species)
        return best_species, confidence

    def _calculate_final_confidence(self, features: Dict[str, Any], species: str) -> float:
        """
        Güven skoru = eşleşen_özellik / toplam_belirgin_özellik
        """
        relevant_features = [k for k, v in features.items() if v != "belirsiz"]
        if not relevant_features: return 0.0
        return min(1.0, len(relevant_features) / 8.0)

    def _build_result(self, prediction: Optional[str], confidence: float, steps: List[EliminationStep], candidates: List[str], features: Dict[str, Any]) -> DecisionResult:
        common_name = ""
        if prediction and prediction in self.species_rules:
            common_name = self.species_rules[prediction].common_name
        
        level = "Düşük"
        if confidence >= 0.7: level = "Yüksek"
        elif confidence >= 0.4: level = "Orta"

        return DecisionResult(
            predicted_species=prediction,
            common_name_tr=common_name,
            confidence=confidence,
            confidence_level=level,
            elimination_steps=steps,
            remaining_candidates=candidates,
            features_used=features
        )

    def _log_step(self, step: EliminationStep):
        msg = f"✅ {step.feature_checked} tespit edildi -> {', '.join(step.eliminated_species)} elendi ({step.reason})"
        self._log_event(msg)
