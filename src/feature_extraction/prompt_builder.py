class PromptBuilder:
    def __init__(self):
        self.rules = [
            "Gözün arkasında veya yanağında kırmızı/turuncu renkli belirgin bir şerit var mı? (evet/hayır/belirsiz)",
            "Gaga yapısı: düz mi, hafif kıvrık mı, belirgin kanca şeklinde kıvrık mı? (düz/hafif_kıvrık/kanca/belirsiz)",
            "Kabuğun genel rengi nedir? (yeşil/kahverengi/siyah/gri/turuncu/karışık/belirsiz)",
            "Kabuğun yüzeyinde belirgin sarı veya turuncu benekler var mı? (evet/hayır/belirsiz)",
            "Boyun bölgesinde çizgi veya desen var mı? (evet/hayır/belirsiz)",
            "Ön ayaklarda perde (yüzgeç) var mı, yoksa pençe mi? (perde/pençe/belirsiz)",
            "Kabuğun kenarları düz mı yoksa testere dişi gibi girintili mi? (düz/girintili/belirsiz)",
            "Kafanın üzerinde ve gözler arasında kaç adet büyük pul grubu görülüyor? (2/4/belirsiz)"
        ]

    def build_prompt(self) -> str:
        questions = "\n".join(f"{i+1}. {rule}" for i, rule in enumerate(self.rules))
        
        return f"""Sen bir kaplumbağa biyologusun. Bu fotoğraftaki kaplumbağayı inceleyerek aşağıdaki fiziksel özellikleri tespit et.
Her özellik için yalnızca belirtilen formatta yanıt ver. Göremediğin özellik için "belirsiz" yaz.

Sorular:
{questions}

Yanıtını SADECE JSON formatında ver, başka hiçbir şey yazma:
{{
  "yanak_seridi": "...",
  "gaga_yapisi": "...",
  "kabuk_rengi": "...",
  "kabuk_sari_benek": "...",
  "boyun_deseni": "...",
  "ayak_yapisi": "...",
  "kabuk_kenari": "...",
  "kafa_pul_sayisi": "..."
}}
"""
