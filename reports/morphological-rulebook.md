# Morfolojik Kural Sözlüğü (Morphological Rulebook)

Bu rapor, Vision AI modellerinin fotoğraflardan kaplumbağa türlerini tespit edebilmesi için gereken fiziksel ayırt edici özellikleri ve sorulması gereken anahtar soruları içerir.

---

**1. Tür:** *Trachemys scripta elegans* / Kızıl Yanaklı Su Kaplumbağası
**Ayırt edici özellikler:**
- **Kırmızı Şerit:** Başın her iki yanında, gözün hemen arkasında belirgin kırmızı/turuncu bir şerit bulunur. → Vision AI sorusu: "Baştaki gözün hemen arkasında kırmızı veya turuncu yatay bir bant var mı?"
- **Karapaks Deseni:** Gençlerde parlak yeşil, yaşlılarda koyu zeytin yeşili üzerine sarı çizgili desenler. → Vision AI sorusu: "Sırt kabuğunun temel rengi nedir ve üzerinde ince sarı çizgiler/halkalar var mı?"
- **Plastron Lekeleri:** Sarı zemin üzerine her plazada birer adet büyük koyu leke. → Vision AI sorusu: "Alt kabuk (plastron) sarı renkte mi ve üzerinde simetrik koyu lekeler var mı?"
**Bu türü kesin eleyecek özellikler:**
- Başın yanındaki kırmızı şerit yoksa (yaşlı melanistik bireyler hariç) bu tür olma ihtimali düşüktür.

---

**2. Tür:** *Chelonia mydas* / Yeşil Deniz Kaplumbağası
**Ayırt edici özellikler:**
- **Prefrontal Pullar:** Gözler arasında sadece 1 çift (2 adet) büyük pul bulunur. → Vision AI sorusu: "Gözlerin arasındaki alanda kaç çift büyük pul (prefrontal scale) görüyorsun? Sadece 1 çift mi?"
- **Lateral Skütler:** Karapaksın merkez hattının yanında 4 çift plaka bulunur. → Vision AI sorusu: "Merkezi sırt plakalarının sağında ve solunda kaçar tane büyük plaka var? (Cevap 4 ise işarettir)."
- **Gaga Yapısı:** Keskin olmayan, daha küt bir gaga yapısı vardır. → Vision AI sorusu: "Üst gaga kuş gagası gibi aşağı kıvrık mı yoksa daha düz ve küt mü?"
**Bu türü kesin eleyecek özellikler:**
- Prefrontal pul sayısı 1 çiftten fazlaysa bu tür değildir.

---

**3. Tür:** *Caretta caretta* / Caretta Caretta (İri Başlı Deniz Kaplumbağası)
**Ayırt edici özellikler:**
- **Büyük Kafa:** Vücut ölçülerine oranla kafa oldukça büyük ve geniştir. → Vision AI sorusu: "Kafa yapısı vücuda oranla çok büyük mü ve prefrontal pul sayısı 2 çift mi?"
- **Lateral Skütler:** 5 veya daha fazla lateral sküt bulunur. → Vision AI sorusu: "Sırt kabuğunun yanlarındaki plaka sayısı (lateral scutes) 5 veya daha fazla mı?"
- **Renk:** Genellikle üniform kırmızımsı-kahverengi tonlar. → Vision AI sorusu: "Kabuk ve deri rengi baskın olarak pas rengi veya kahverengi mi?"
**Bu türü kesin eleyecek özellikler:**
- Yan plaka sayısı (lateral scutes) 4 ise bu tür olamaz.

---

**4. Tür:** *Eretmochelys imbricata* / Şahin Gagalı Deniz Kaplumbağası
**Ayırt edici özellikler:**
- **Kiremit Dizilimi:** Karapaks plakaları birbiri üzerine biner. → Vision AI sorusu: "Sırt kabuğundaki plakalar (scutes) balık pulu gibi birbirinin üstüne gelmiş mi?"
- **Şahin Gagası:** Çok belirgin, sivri ve aşağı kıvrık bir gaga. → Vision AI sorusu: "Gaganın ucu belirgin şekilde aşağı doğru kıvrılmış ve sivri mi?"
- **Prefrontal Pullar:** 2 çift. → Vision AI sorusu: "Gözler arasında 2 çift (toplam 4 adet) pul var mı?"
**Bu türü kesin eleyecek özellikler:**
- Kabuk plakaları birbirinin üzerine binmiyorsa (yüzey düzse) bu tür olamaz.

---

**5. Tür:** *Testudo graeca* / Tosbağa (Kara Kaplumbağası)
**Ayırt edici özellikler:**
- **Uyluk Mahmuzu:** Arka bacakların kalçaya yakın kısımlarında kemiksi birer mahmuz/çıkıntı bulunur. → Vision AI sorusu: "Arka bacakların iç-üst kısmında küçük, konik bir mahmuz veya sert bir tüberkül var mı?"
- **Kuyruk Mahmuzu YOK:** Kuyruk ucunda sert bir iğne bulunmaz. → Vision AI sorusu: "Kuyruğun en ucunda sert bir mahmuz/iğne var mı yoksa kuyruk yumuşak bir dokuyla mı bitiyor?"
- **Supracaudal Sküt:** Kuyruk üstündeki plaka genellikle tektir (bölünmemiştir). → Vision AI sorusu: "Kuyruğun hemen üzerindeki plaka (supracaudal) tek parça mı yoksa ortadan ikiye bölünmüş mü?"
**Bu türü kesin eleyecek özellikler:**
- Kuyruk ucunda sert bir mahmuz varsa veya uyluk mahmuzları yoksa bu tür değildir.

---

**6. Tür:** *Testudo hermanni* / Hermann Kaplumbağası
**Ayırt edici özellikler:**
- **Kuyruk Mahmuzu:** Kuyruk ucunda çok belirgin, boynuzsu bir iğne (spur) bulunur. → Vision AI sorusu: "Kuyruk ucunda sert ve ucu sivri bir mahmuz/spike görünüyor mu?"
- **Plastron Bantları:** Alt kabukta boyuna uzanan iki kesintisiz siyah bant. → Vision AI sorusu: "Alt kabuğun (plastron) üzerinde merkez hattına paralel uzanan iki adet koyu siyah şerit var mı?"
- **Bacak Mahmuzu YOK:** Bacaklarda uyluk mahmuzu bulunmaz. → Vision AI sorusu: "Arka bacaklarda Testudo graeca'daki gibi mahmuz var mı?"
**Bu türü kesin eleyecek özellikler:**
- Plastronun altındaki iki siyah bant yoksa veya uylukta mahmuz varsa bu tür olamaz.

---

**7. Tür:** *Dermochelys coriacea* / Deri Sırtlı Deniz Kaplumbağası
**Ayırt edici özellikler:**
- **Deri Yapısı:** Sert, pullu bir kabuk yerine pürüzsüz, deri benzeri bir doku. → Vision AI sorusu: "Kabukta sert plakalar mı var yoksa pürüzsüz, deri gibi bir doku mu görünüyor?"
- **Sırt Hatları:** Boyuna uzanan 7 adet belirgin sırt hattı (ridge). → Vision AI sorusu: "Sırt kabuğu üzerinde baştan kuyruğa uzanan 7 adet paralel çıkıntı sırtı var mı?"
- **Boyut ve Renk:** Siyah-gri zemin üzerinde beyaz benekler. → Vision AI sorusu: "Canlı genel olarak siyah renkte ve üzeri beyaz küçük lekelerle mi kaplı?"
**Bu türü kesin eleyecek özellikler:**
- Kabuk üzerinde sert, ayrık plakalar (scutes) varsa bu kesinlikle bu tür değildir.

---

**8. Tür:** *Mauremys rivulata* / Çizgili Boyunlu Kaplumbağa
**Ayırt edici özellikler:**
- **Çizgili Boyun:** Boyun boyunca açık renkli, ince ve uzunlamasına çizgiler. → Vision AI sorusu: "Boyun bölgesinde baştan gövdeye doğru uzanan ince paralel çizgiler var mı?"
- **Plastron Rengi:** Tamamen siyah veya ağırlıklı olarak siyah. → Vision AI sorusu: "Alt kabuk (plastron) tamamen siyah veya çok koyu renkte mi?"
- **Kabuk Şekli:** Genellikle daha basık ve oval. → Vision AI sorusu: "Sırt kabuğu kara kaplumbağaları gibi kubbeli mi yoksa daha basık (suya uyumlu) mıdır?"
**Bu türü kesin eleyecek özellikler:**
- Boyunda çizgi desenleri yoksa veya kabuk çok yüksek kubbeliyse bu tür olamaz.
