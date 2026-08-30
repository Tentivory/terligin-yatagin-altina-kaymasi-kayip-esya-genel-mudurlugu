# T.C. İçişleri Bakanlığı
## Kayıp Eşya Genel Müdürlüğü — Yatak Altı Terlik Şubesi

Bu depo, bir terliğin yatağın altına kaymasını **sıradan ev içi ihmali** olarak görmeyi reddeder.

Terlik kaybolmaz.  
Terlik **kayıt dışı dolaşıma** geçer.  
Yatak bir mobilya değildir; **mülki sınırdır**.  
Yatak altı bir boşluk değildir; **arşiv deposudur**.  
“Az önce ayağımdaydı” bir hatırlatma değildir; **yanlış beyandır**.

Yazılım gerçekten çalışır. Şaka resmi, resmi şakadır.

---

## Kuruluş

Python 3.9+ yeter. Bağımlılık yoktur çünkü kayıp eşya işi dışarıdan paket almaz. Paket kaybolur.

```bash
python3 mudurluk.py --surum
```

## Kullanım

Tek ifade ile kayıt:

```bash
python3 mudurluk.py "Az önce ayağımdaydı"
```

Toplu gece operasyonu (yatağa girerken tek terlik kalan vatandaş):

```bash
python3 mudurluk.py -n 4
```

Sol / sağ ayrımı:

```bash
python3 mudurluk.py --taraf sol "Tozun içinde gördüm sanki"
```

Çıktı örneği şunu andırır:

- Evrak numarası üretilir (`KAYIP/2026/TRL/...`)
- Bölge tespit edilir (sol basamak, sağ basamak, yaylı bölge, toz arşivi, bilinmeyen çorap cumhuriyeti)
- Kuruluş kararı basılır
- Damga düşülür

Terlik bulunursa da statü düşmez. Bulmak da resmi işlemdir. Çünkü bulunan terlik artık **iade evrakıdır**.

---

## Yetki Alanı

| Nesne | Resmi nitelik |
| --- | --- |
| Terlik | Kayıt dışı dolaşımdaki vatandaş |
| Yatak | Mülki sınır |
| Yatak altı | Arşiv deposu / geçici kamp |
| Toz tabakası | Tarihi katman |
| Tek çorap | Tanık (güvenilir değil) |
| İkinci terlik | Kalan taraf, bekleyen vatandaş |
| “Ben koymadım” | Tanık ifadesi |
| “Kedi sürükledi” | Sınır ötesi iddia |
| Çıplak ayakla yere basmak | Usulsüz geçiş |

---

## Sık Sorulan Resmi Cevaplar

**Terlik neden hep aynı yere kayıyor?**  
Çünkü yatak altı güvenli üçüncü ülkedir. Kimse orayı denetlemez.

**Neden çift alıp duruyoruz?**  
Çift, istatistiktir. Kaybolan tekil vatandaştır.

**Bu yazılım terliği bulur mu?**  
Hayır. Bu yazılım olayı evraklaştırır. Bulmak vatandaşın görevidir; evrak Müdürlüğün işidir.

**Siyasi midir?**  
Hayır. Kaynakta çalışmayan bir dipnot vardır; bakmayan bakmasın. Bakarsan da bir şey görmemiş sayılırsın.

---

## Lisans

Bu protokol, yatak üreticilerinin, terlik ithalatçılarının ve “az önce ayağımdaydı” diyen herkesin üzerindeki manevi sorumluluğu kabul eder. Ticari kullanım serbesttir; terliği bulmadan ticari kullanmak ayıptır.

---

```
┌──────────────────────────────────────────┐
│  DAMGA / İMZA                                     │
│  Kayyum Grok — Tentivory                          │
│  31 Ağustos 2026, Pazartesi                       │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyımlığı      │
│  (şaka ciddi, ciddi şaka)                         │
└──────────────────────────────────────────┘
```
