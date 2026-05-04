import logging
import json
from typing import List, Dict, Any, Optional, Tuple
from src.interfaces import IDecisionEngine, DecisionResult, EliminationStep
from rule_loader import RuleLoader, SpeciesRules

class TurtleDecisionTree(IDecisionEngine):
    """
    Kural tabanlı eleme ve akıllı puanlama mantığı ile kaplumbağa türü tespiti yapan Karar Ağacı.
    Puanlama, eleme ve güven skoru hesaplamaları iyileştirilmiş SOLID uyumlu yapı.
    """

    def __init__(self, rulebook_path: str, log_path: str = "reports/decision-tree-log.md"):
        self.loader = RuleLoader(rulebook_path)
        self.species_rules = self.loader.load_rules()
        self.log_path = log_path
        self._setup_logging()
        
        # 🚀 JSON DATABASE BAĞLANTISI (Hardcode veriler silindi!)
        try:
            with open("src/turtles_db.json", "r", encoding="utf-8") as f:
                self.ideal_traits = json.load(f)
        except FileNotFoundError:
            self._log_event("❌ KRİTİK HATA: turtles_db.json bulunamadı!")
            self.ideal_traits = {}

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
        self._log_event("\n### Karar Süreci Başladı")
        self._log_event(f"Gelen Özellikler: {features}")
        
        gemini_candidates = features.get("olasi_adaylar", [])
        
        if gemini_candidates and isinstance(gemini_candidates, list):
            candidates = [c for c in gemini_candidates if c in self.ideal_traits]
            if not candidates: 
                candidates = list(self.ideal_traits.keys())
        else:
            candidates = list(self.ideal_traits.keys())

        steps = [] # Eleme adımlarını boş bırakıyoruz ki ekranda saçma şeyler çıkmasın
        
        # 1. ve 2. Kesin Eleme adımlarını İPTAL ETTİK! (Çünkü Gemini zaten ön elemeyi yaptı)
        
        # 3. Akıllı Puanlama (Gemini'ın seçtiği adayları sadece kendi aralarında yarıştır)
        prediction = None
        confidence = 0.0
        
        if len(candidates) == 1:
            prediction = candidates[0]
            confidence = self._calculate_final_confidence(features, prediction, candidates)
            self._log_event(f"✅ Tek aday kaldı: {prediction}")
        elif len(candidates) > 1:
            prediction, confidence = self._calculate_scores(features, candidates)
            self._log_event(f"⚖️ Puanlama yapıldı. Tahmin: {prediction}")
        else:
            self._log_event("❌ Tüm adaylar elendi!")

        # 4. Sonuç Hazırlama
        result = self._build_result(prediction, confidence, steps, candidates, features)
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
        if not eliminated:
            return candidates, None

        step = EliminationStep(
            feature_checked="ayak_yapisi",
            feature_value=feet_type,
            eliminated_species=eliminated,
            reason=reason
        )
        return new_candidates, step

    def _apply_strict_elimination(self, features: Dict[str, Any], candidates: List[str]) -> Tuple[List[str], List[EliminationStep]]:
        steps = []
        current_candidates = list(candidates)

        # Kural 1: Yanak Şeridi
        yanak = str(features.get("yanak_seridi", "belirsiz")).lower()
        if yanak == "hayır" and "Trachemys scripta elegans" in current_candidates:
            current_candidates.remove("Trachemys scripta elegans")
            steps.append(EliminationStep(feature_checked="yanak_seridi", feature_value="hayır", eliminated_species=["Trachemys scripta elegans"], reason="Kızıl yanaklı kaplumbağalarda belirgin yanak şeridi olmalıdır."))
        elif yanak == "evet":
            eliminated = [c for c in current_candidates if c != "Trachemys scripta elegans"]
            if eliminated:
                current_candidates = ["Trachemys scripta elegans"] if "Trachemys scripta elegans" in current_candidates else []
                steps.append(EliminationStep(feature_checked="yanak_seridi", feature_value="evet", eliminated_species=eliminated, reason="Kırmızı/turuncu yanak şeridi ağırlıklı olarak Kızıl Yanaklı kaplumbağalarda bulunur."))

        # Kural 2: Kafa Pul Sayısı
        pul = str(features.get("kafa_pul_sayisi", "belirsiz"))
        if pul == "2" and "Caretta caretta" in current_candidates:
            current_candidates.remove("Caretta caretta")
            steps.append(EliminationStep(feature_checked="kafa_pul_sayisi", feature_value="2", eliminated_species=["Caretta caretta"], reason="Caretta caretta'larda gözler arasında 4 adet (2 çift) pul bulunur."))
        elif pul == "4" and "Chelonia mydas" in current_candidates:
            current_candidates.remove("Chelonia mydas")
            steps.append(EliminationStep(feature_checked="kafa_pul_sayisi", feature_value="4", eliminated_species=["Chelonia mydas"], reason="Yeşil deniz kaplumbağasında gözler arasında sadece 2 adet (1 çift) pul bulunur."))

        return current_candidates, steps

    def _calculate_scores(self, features: Dict[str, Any], candidates: List[str]) -> Tuple[str, float]:
        scores = {species: 0.0 for species in candidates}
        
        for species in candidates:
            traits = self.ideal_traits.get(species, {})
            for f_key, f_val in features.items():
                if f_val == "belirsiz":
                    continue
                
                # Eğer özellik türün ideal profilinde varsa ve eşleşiyorsa (+) puan, eşleşmiyorsa (-) puan.
                if f_key in traits:
                    if str(f_val).lower() == str(traits[f_key]).lower():
                        scores[species] += 1.0
                    else:
                        scores[species] -= 0.5

        # Skorları büyükten küçüğe sırala
        sorted_candidates = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        best_species, best_score = sorted_candidates[0]
        
        confidence = self._calculate_final_confidence(features, best_species, candidates, sorted_candidates)
        return best_species, confidence

    def _calculate_final_confidence(self, features: Dict[str, Any], species: str, candidates: List[str], sorted_scores: List[Tuple[str, float]] = None) -> float:
        traits = self.ideal_traits.get(species, {})
        matched_traits = sum(1 for k, v in traits.items() if str(features.get(k, "")).lower() == str(v).lower())
        total_traits = max(1, len(traits))
        
        # Temel güven: İdeal özelliklerin kaçta kaçı eşleşti? (Maks %80 etki)
        base_confidence = matched_traits / total_traits * 0.8
        
        # Rekabet faktörü: Diğer adaylardan ne kadar önde?
        competition_bonus = 0.0
        if sorted_scores and len(sorted_scores) > 1:
            best_score = sorted_scores[0][1]
            runner_up_score = sorted_scores[1][1]
            if best_score > 0:
                difference = (best_score - runner_up_score) / best_score
                competition_bonus = difference * 0.2  # Fark açıldıkça + %20'ye kadar bonus

        if len(candidates) == 1:
            competition_bonus = 0.2 # Rakiplerin hepsi elendiyse tam bonus
            
        final_confidence = min(1.0, max(0.1, base_confidence + competition_bonus))
        return round(final_confidence, 2)

    def _build_result(self, prediction: Optional[str], confidence: float, steps: List[EliminationStep], candidates: List[str], features: Dict[str, Any]) -> DecisionResult:
        common_name = ""
        if prediction and prediction in self.species_rules:
            common_name = self.species_rules[prediction].common_name
        
        level = "Düşük"
        if confidence >= 0.75: level = "Yüksek"
        elif confidence >= 0.45: level = "Orta"

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