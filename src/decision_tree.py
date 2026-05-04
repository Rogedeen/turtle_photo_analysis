import logging
import json
from typing import List, Dict, Any, Optional, Tuple
from src.interfaces import IDecisionEngine, DecisionResult, EliminationStep
from rule_loader import RuleLoader

class TurtleDecisionTree(IDecisionEngine):
    def __init__(self, rulebook_path: str, log_path: str = 'reports/decision-tree-log.md'):
        self.loader = RuleLoader(rulebook_path)
        self.species_rules = self.loader.load_rules()
        self.log_path = log_path
        self._setup_logging()
        try:
            with open('src/turtles_db.json', 'r', encoding='utf-8') as f:
                self.turtles_db = json.load(f)
        except FileNotFoundError:
            self._log_event('❌ KRİTİK HATA: turtles_db.json bulunamadı!')
            self.turtles_db = {}

    def _setup_logging(self):
        self.logger = logging.getLogger('DecisionTree')
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.FileHandler(self.log_path, encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _log_event(self, message: str):
        self.logger.info(message)
        try:
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(f'{message}\n')
        except Exception:
            pass

    def decide(self, features: Dict[str, Any]) -> DecisionResult:
        self._log_event('\n## Karar Süreci Başladı (Gemini Tahmin Odaklı)')
        olasi_turler = features.get('olasi_turler', [])
        if not olasi_turler:
            return self._empty_result(features)
        
        # En yüksek güvene sahip adayları sırala
        sorted_candidates = sorted(olasi_turler, key=lambda x: x.get('confidence', 0), reverse=True)
        top_candidate = sorted_candidates[0]
        predicted_species = top_candidate.get('tur')
        visual_confidence = top_candidate.get('confidence', 0)
        
        morphological_score = 0
        total_checks = 0
        steps = []
        
        # Seçilen türün DB verisini al
        db_entry = self.turtles_db.get(predicted_species, {})
        common_name_tr = db_entry.get('common_name_tr', db_entry.get('common_name', predicted_species))
        
        check_fields = ['ayak_yapisi', 'kafa_pul_sayisi', 'gaga_yapisi', 'kabuk_kenari', 'habitat', 'yanak_seridi', 'boyun_deseni']
        for field in check_fields:
            user_val = str(features.get(field, 'belirsiz')).lower()
            ideal_val = str(db_entry.get(field, 'unknown')).lower()
            
            if user_val != 'belirsiz' and ideal_val != 'unknown':
                total_checks += 1
                if user_val == ideal_val:
                    morphological_score += 1
                    steps.append(EliminationStep(field, user_val, [], f'Bilgi: {predicted_species} özellikleri ile uyumlu ({ideal_val}).'))
                else:
                    # Artık eleme yok, sadece puanı çok az etkileyen bir uyarı
                    morphological_score -= 0.1 
                    msg = f'Bilgi: Görselde {user_val} görüldü, ancak tipik {predicted_species} {ideal_val} özelliğine sahiptir.'
                    steps.append(EliminationStep(field, user_val, [], msg))

        # Yeni Güven Hesabı: %95 Gemini, %5 Morfolojik doğrulama
        match_ratio = (morphological_score / total_checks) if total_checks > 0 else 1.0
        # match_ratio [-0.1*N, 1.0] arasında olabilir, 0 ile 1 arasına sıkıştıralım
        normalized_match = max(0, min(1.0, match_ratio))
        
        final_confidence = (visual_confidence * 0.95) + (normalized_match * 0.05)
        conf_level = 'Yüksek' if final_confidence >= 0.8 else 'Orta' if final_confidence >= 0.5 else 'Düşük'
        
        self._log_event(f'Seçilen aday: {predicted_species}, Gemini Güveni: %{visual_confidence*100:.1f}, Nihai Güven: %{final_confidence*100:.1f}')
        
        # Filtreleme: None olan adayları temizle ve boşsa default değer ata
        raw_candidates = [cand.get('tur') for cand in sorted_candidates if cand.get('tur') is not None]
        remaining_candidates = raw_candidates if raw_candidates else ["Bilinmeyen"]

        # Geriye dönük uyumluluk için predicted_features ekleyelim
        features_with_db = features.copy()
        if db_entry:
            features_with_db['predicted_features'] = db_entry

        # top_3_comparison yapısını hazırla (İlk 3 aday için DB'deki gerçek özellikleri döndür)
        top_3_comparison = []
        for cand in sorted_candidates[:3]:
            cand_species = cand.get('tur')
            if not cand_species:
                continue
            cand_db = self.turtles_db.get(cand_species, {}).copy()
            
            # Pydantic ve Frontend ile uyumlu alan adları (Snake Case)
            cand_db['confidence'] = cand.get('confidence', 0)
            cand_db['scientific_name'] = cand_species
            cand_db['common_name'] = cand_db.get('common_name', cand_species)
            cand_db['common_name_tr'] = cand_db.get('common_name_tr', cand_db['common_name'])
            
            # Özellikleri derle
            features_summary = {
                'habitat': cand_db.get('habitat', 'Bilinmiyor'),
                'ayak_yapisi': cand_db.get('ayak_yapisi', 'Bilinmiyor'),
                'gaga_yapisi': cand_db.get('gaga_yapisi', 'Bilinmiyor')
            }
            cand_db['features'] = features_summary
            
            top_3_comparison.append(cand_db)

        return DecisionResult(
            predicted_species=predicted_species,
            common_name_tr=common_name_tr,
            confidence=final_confidence,
            confidence_level=conf_level,
            elimination_steps=steps,
            remaining_candidates=remaining_candidates,
            features_used=features_with_db, # DB özelliklerini içeren kopya
            olasi_turler=olasi_turler,
            top_3_comparison=top_3_comparison
        )

    def _empty_result(self, features: Dict[str, Any]) -> DecisionResult:
        return DecisionResult('Bilinmeyen', 'Tespit Edilemedi', 0.0, 'Düşük', [], [], features, [])
