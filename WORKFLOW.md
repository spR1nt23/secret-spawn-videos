# Secret Spawn: günlük video üretim yöntemi

Bu belge kanalın her gün nasıl üretildiğini baştan sona anlatır. Temiz bir bulut makinesinde, önceki sohbetleri bilmeyen biri bu belgeyle aynı videoları üretebilmeli.

**Kanal özeti**
- Kanal: **Secret Spawn**, kanal ID'si `UCrBMOIvfjj0z_W7DEE1EqDQ`.
- İçerik: İngilizce Roblox haberleri ve kodları. Hedef kitle ABD.
- Görseller tamamen özgün: düz renkli ikonlar, gradyan arka planlar, büyük başlıklar.
- **Roblox logosu, karakteri veya oyun görüntüsü KULLANILMAZ.**

**Görev ayrımı**
- Üretim (araştırma → senaryo → ses → video → kapak → kontrol) bulut görevinde yapılır.
- **YouTube'a yükleme ayrı bir adımdır.** Kanal sahibi onaylamadan hiçbir şey yüklenmez.
- Bu belgedeki "Studio yükleme ayarları" bölümü, onaydan sonra yapılacak yükleme içindir.

---

## 0. Repo yapısı

```
tools/
  setup.sh          kurulum: ffmpeg, Python paketleri, Kokoro TTS modeli, fontlar
  common.py         yollar ve içerik yükleyici (SS_ASSETS, CONTENT, OUTDIR, FINALDIR)
  palette.py        arka plan ve vurgu renkleri
  icons.py          kendi çizdiğimiz düz ikonlar (python3 tools/icons.py sheet.png ile tümünü görürsün)
  tts.py            Kokoro ile seslendirme + kelime zamanlaması (.wav + .json)
  render.py         PIL kareleri → ffmpeg. Short 1080x1920, uzun video 1920x1080, 30 fps
  mux.py            ses + geçiş whoosh'u + loudnorm (-14 LUFS) → son mp4
  thumbnail.py      kapaklar: uzun video 1280x720, Short 1080x1920
  check_frames.py   kare kontrolü: sahne başına önizleme ve kontak sayfası
  make_day.sh       bir günün tamamını tek komutla üretir
content/
  TEMPLATE.py       senaryo şablonu (yeni gün için kopyala)
  2026-11-08.py ... geçmiş günlerin gerçek senaryoları (örnek olarak)
TOPICS_HISTORY.md   işlenmiş konular ve kodlar (tekrar önleme)
videos/YYYY-MM-DD/  yüklemeye hazır mp4'ler (yükleme adımı buradan raw URL ile çeker)
assets/  work/      .gitignore'da: model, font ve ara çıktılar repoya girmez
```

## 1. Kurulum (temiz makine, tek seferlik)

```bash
git clone https://github.com/spR1nt23/secret-spawn-videos.git && cd secret-spawn-videos
bash tools/setup.sh          # ~1-2 dk; assets/ klasörüne iner
```

`setup.sh` şunları yapar:
- `ffmpeg`, `npm` ve `curl` eksikse apt ile kurar.
- Python paketlerini kurar: `kokoro-onnx soundfile pillow numpy fonttools brotli`. pip "externally managed" hatası verirse otomatik olarak `--break-system-packages` ile yeniden dener.
- Kokoro TTS modelini GitHub release'den indirir:
  - `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx` (~92 MB)
  - `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin` (~28 MB)
  - Hugging Face kullanılmaz, çünkü kısıtlı ağlarda engelli olabiliyor.
- Fontları kurar:
  - Kaynak: npm'deki `@fontsource/bebas-neue` ve `@fontsource/lilita-one` paketleri (latin, 400).
  - woff dosyaları fontTools ile ttf'ye çevrilip `assets/BebasNeue.ttf` ve `assets/LilitaOne.ttf` olarak kaydedilir.

Farklı bir assets klasörü kullanmak için: `SS_ASSETS=/path bash tools/setup.sh`. Sonraki tüm komutlarda da aynı `SS_ASSETS` değerini ver.

## 2. Günlük plan ve yayın saatleri

Bir **içerik dosyası** = bir set = 3 Short + 1 uzun video. Dosya adı `content/D.py`, burada D o setin 19:00 Short'unun günüdür.

| Video | Yayın (Europe/Istanbul) | Format | Süre |
|---|---|---|---|
| `short1` | **D 19:00** | 1080x1920 | 20–27 sn |
| `long`   | **D 23:00** | 1920x1080 | ~3:00–3:30 (2:40 kabul edilebilir alt sınır) |
| `short2` | **D+1 01:00** | 1080x1920 | 20–27 sn |
| `short3` | **D+1 03:00** | 1080x1920 | 20–27 sn |

- Üretimi D günü öğleden önce bitir ki onay ve yükleme 19:00'a yetişsin. Bir gün önceden hazırlamak da olur.
- **Tekrar üretme:** Başlamadan önce `videos/` klasörüne, `TOPICS_HISTORY.md` dosyasına ve (erişim varsa) Studio'daki zamanlanmış videolara bak. O günün seti zaten hazırsa yeniden üretme.
- Tipik dağılım:
  - `short1`: günün en büyük haberi (3 madde).
  - `long`: 5 haber, 5 oyunun kodları, hafta/hafta sonu listesi.
  - `short2` ve `short3`: biri haber ya da tarih, biri kod; bazı günler ikisi de kod olur. Kod Short'ları en çok izlenen tür (~1.3–1.4K görüntülenme).

Dosya adları şu kalıptadır:

```
SS_<YYYY-MM-DD>_<HHMM>_<Short|Long>_<Slug>.mp4
örnek: SS_2026-11-13_1900_Short_EngineChanges.mp4
```

## 3. Haber ve kod araştırması (kaynak kuralları)

### Haber kaynakları, öncelik sırasıyla
1. **Resmi:**
   - devforum.roblox.com: Announcements, haftalık "Weekly Recap" başlıkları.
   - create.roblox.com docs.
   - corp.roblox.com, blog.roblox.com.
   - events.roblox.com.
   - Not: DevForum bazen `create.roblox.com/maintenance` adresine yönlendirir. O zaman web aramasının alıntılarını ya da başka resmi sayfaları kullan.
2. **Oyun geliştiricisinin kendi duyurusu:** oyun sayfası, resmi Discord/X duyurusunu aktaran haber siteleri.
3. **Güvenilir oyun basını:** Inven Global, PCGamesN, Pocket Tactics, Destructoid, Pro Game Guides, Beebom, Gaming Route (etkinlik bitiş saatleri için).
4. Wikipedia yalnızca arka plan bilgisi için (çıkış tarihi gibi).

### Kurallar
- Her iddianın bir kaynağı olmalı. Tarih ve saatleri kaynaktan al.
  - Etkinlik saatlerini ekranda **ET** olarak yaz; hedef kitle ABD.
  - Açıklamaya "times are in Eastern Time and can change" notunu ekle.
- **Duyurulmamış bir şeyi olmuş gibi anlatma.**
  - "announced for November" ile "is live" farklı şeylerdir.
  - Beta özellikler için "Studio only / not in live games yet" de.
  - Örnek: DTI 3. yıl dönümü için resmi etkinlik yoktu, bu yüzden videoda sadece çıkış tarihi söylendi.
- **Kodlar:**
  - Son 48 saat içinde güncellenmiş bir kod listesinden al (Destructoid, Pro Game Guides, PCGamesN, Pocket Tactics, Beebom). Mümkünse iki kaynakla doğrula.
  - Kodu **birebir** yaz; büyük/küçük harf ve `!` gibi işaretler dahil. Küçük harfli kodları (`choom`, `candy`) açıklamada küçük harfle ver.
  - Ödülü ve şartı (level 10, grup üyeliği gibi) belirt.
  - Kodlu her açıklamada "Codes may expire at any time, so redeem them fast!" yazmalı.
- Sayıları kontrol et. Başlıktaki kod sayısı videodaki kod sayısıyla aynı olmalı. Girişteki "N games with new codes" ile gerçek oyun sayısı da tutmalı.
  - Bu karıştı ve bir kez videoyu yeniden render etmek gerekti.
- Siyasi, şiddet içeren ya da çocuk güvenliğini zedeleyen konular yok. Platform güvenliği haberleri (ban, yaş derecelendirmesi) tarafsız ve olgusal anlatılır.
- Kaynak URL'lerini sakla. Onay mesajında kanal sahibine kaynak listesi verilir.

### Tekrar önleme
- `TOPICS_HISTORY.md` dosyasını oku. Orada geçen haberi aynı açıdan tekrar işleme; aynı kodu tekrar verme.
- Yeni gelişme varsa `(takip)` olarak işlenebilir.
- Üretim bitince o günün konularını ve kodlarını `TOPICS_HISTORY.md` dosyasına ekle ve commit'le.

## 4. Senaryo kuralları (`content/D.py`)

`content/TEMPLATE.py` dosyasını `content/D.py` olarak kopyala ve doldur. Alanların açıklaması şablonun başında. Gerçek örnek: `content/2026-11-13.py` (UPLOAD bloğu dahil).

### Yapı
- **Short:** intro (kanca) → 3 madde (`n`=1..3) → outro (soru).
  - Her sahnede tek cümle; madde sahneleri en fazla 2 kısa cümle.
- **Uzun video:** intro → haber maddeleri (1–5) → kod maddeleri (6–10) → `list` (hafta / hafta sonu) → outro.
  - Haber maddeleri: 3–4 cümle ve 3–4 madde imi (bullet).
  - Kod maddeleri: 1–2 cümle; bullet olarak `KOD: ÖDÜL`.

### Dil ve yazım
- **Dil:** basit, enerjik, ABD İngilizcesi; 10–16 yaş bir okur anlamalı.
- `vo` içinde vurgulanacak kelimeler `*kelime*` şeklinde işaretlenir. Altyazıda vurgu renginde görünür. Cümle başına 2–4 vurgu yeterli.
- Seslendirmede söylenecek hali yaz:
  - "*three thousand* credz", "*thanks for likes*", "*U P D twelve gold*", "*R N G*".
  - EXP ve RNG otomatik heceletilir.
- Ekrandaki alanlara (`title`, `code`, `bullets`, `badge`) gerçek metni yaz: "3,000 FREE CREDZ", "THX4LIKES".

### Ekran alanları
- `title`: 2–4 kelime, BÜYÜK HARF. En fazla 2 satıra otomatik ve dengeli kırılır.
- `badge`: 1–2 kelime ("NEW", "LIVE", "NOV 14", "FULL RELEASE").
- `game`: oyun veya özellik adı, BÜYÜK HARF.
- `icon`: `icons.py` içindeki ikonlardan biri.
  - Uygun ikon yoksa `icons.py` dosyasına aynı stilde yeni bir düz ikon ekle: kalın koyu kontur, düz renkler, 512 tuvalde çizilip küçültülür.
  - **Roblox ya da oyun logosu/karakteri asla çizilmez.**
- Renkler: aynı videoda ardışık maddelerde farklı `bg`/`acc` kullan.
  - Paletler: `purple`, `navy`, `green`, `maroon`, `red`, `blue`, `violet`.
  - Vurgular: `yellow`, `green`, `blue`, `orange`, `purple`, `pink`.

### Kanca ve outro
- Intro'da sayı ve merak öğesi olsun ("Three Roblox changes just went live, and one could mean less lag").
- Outro bir soruyla biter ve yoruma çağırır. Uzun videoda "subscribe to Secret Spawn" ve "See you tomorrow" de olur.

### UPLOAD bloğu
Dosyanın sonundaki `UPLOAD` bloğunu doldur: dosya adı, yayın saati, başlık, açıklama, etiketler. `make_day.sh` bu bloktan dosya adlarını ve `upload_manifest.json` dosyasını üretir.

## 5. Ses (TTS)

| Ayar | Değer |
|---|---|
| Motor | Kokoro ONNX (`kokoro-v1.0.int8.onnx`) |
| Ses | **`am_michael`** (en-us erkek) |
| Hız | Short **1.12**, uzun video **1.02** (gerekirse 1.0–1.04) |

`tts.py` nasıl çalışır:
- Cümle cümle seslendirir ve baş/son sessizliği kırpar.
- Cümleler arasına 0.10 sn, sahne sonuna 0.30 sn boşluk koyar.
- Kelime zamanlamasını cümle içinde harf uzunluğuna ve noktalama ağırlığına göre dağıtır. Whisper gerekmez.
- Çıktılar: `OUTDIR/<ad>.wav` ve `<ad>.json` (sahne başlangıç/bitiş zamanları ve kelime zamanları).

Komutlar:

```bash
python3 tools/tts.py am_michael 1.12 --shorts-only
python3 tools/tts.py am_michael 1.02 --long-only
```

Süre hedefin dışına çıkarsa metni kısalt ya da uzat. Hızla oynayarak düzeltme; 1.12'nin üstü anlaşılmaz olur.

## 6. Görsel stil

- **Arka plan:** iki renkli dikey gradyan, yavaş kayan beyaz diyagonal şeritler (%5 opaklık) ve süzülen parçacıklar.
- **Üst bilgi:** kırmızı "● BREAKING" hapı ve yanında "SECRET SPAWN NEWS" (Lilita One).
- **Madde sahnesi:**
  - Short: üstte `#n` daire → oyun adı etiketi → büyük ikon (hafif sallanır) ve eğik rozet → Bebas Neue başlık (ilk satır beyaz, son satır vurgu rengi) → kod kutusu (varsa).
  - Uzun video: ikon solda; sağ sütunda numara, etiket, başlık, kod ve bullet satırları sırayla kayarak gelir.
- **Altyazı:** alt bölümde kelime kelime ilerler, `*vurgu*` kelimeleri vurgu renginde. Uzun videoda altyazı koyu yarı saydam şeridin üstünde durur.
- **İlerleme çubuğu:** en altta, sahnenin vurgu renginde.
- **Ses miksajı:** her sahne geçişinde hafif whoosh (TTS'in %13'ü), `loudnorm I=-14 TP=-1`, AAC 192k / 48 kHz.
- **Kapak (uzun video):** 1280x720; büyük iki satırlık başlık (`LONG['thumb']` veya intro `lines`), ilk 3 haber maddesinin ikonları ve tarih rozeti.
  - Kanalda özel kapak yükleme şu an kapalı (telefon doğrulaması gerekiyor). Studio'da "Upload file" düğmesi devre dışıysa kapağı yükleme; sadece üret ve sakla.

## 7. Render komutları

### Tek komutla bütün gün

```bash
bash tools/make_day.sh content/2026-11-14.py              # short1 short2 short3 long
bash tools/make_day.sh content/2026-11-14.py short1       # sadece belirli hedefler
```

- Çıktılar `work/2026-11-14/final/` altına yazılır: 4 mp4, kapak/cover png'leri ve `upload_manifest.json`.
- Süreler (yaklaşık, 2–4 çekirdekli CPU):
  - Short başına ~1–2 dk.
  - Uzun video TTS'i ~3–5 dk, render'ı ~6–9 dk.
- Araç zaman aşımı varsa uzun işi arka planda çalıştır ve logu takip et:
  `nohup bash tools/make_day.sh ... > /tmp/day.log 2>&1 &`

### Adım adım

```bash
export CONTENT=content/2026-11-14.py OUTDIR=work/2026-11-14/out FINALDIR=work/2026-11-14/final
python3 tools/tts.py am_michael 1.12 --shorts-only
python3 tools/tts.py am_michael 1.02 --long-only
python3 tools/check_frames.py short1 short2 short3 long      # önce kare kontrolü (hızlı)
python3 tools/render.py short1 short2 short3 long            # OUTDIR/<ad>_video.mp4
python3 tools/mux.py short1 SS_2026-11-14_1900_Short_Slug   # FINALDIR/<dosya>.mp4
python3 tools/thumbnail.py long short1                       # kapaklar
```

Uzun videonun bölüm zamanları (description chapters) için:

```bash
python3 -c "import json;d=json.load(open('work/2026-11-14/out/long.json'));print('\n'.join('%d:%02d'%(int(s['start'])//60,int(s['start'])%60) for s in d))"
```

- Satırlar sahne sırasındadır (intro, 1, 2, … list, outro).
- İlk bölüm 0:00 olmalı ve bölümler en az 10 sn arayla olmalı. Bu kural sağlanmıyorsa kısa sahneleri tek bölümde birleştir.

## 8. Kare kontrolü (zorunlu)

1. `python3 tools/check_frames.py <hedefler>` komutu `OUTDIR/sheet_<ad>.jpg` kontak sayfalarını üretir. Her sahne için 2 kare alınır.
2. Görüntüyü aç ve şunlara bak:
   - Hiçbir yazı ekran kenarından taşmıyor. Intro ve outro başlıkları `fit_lines` ile otomatik küçülür, yine de kontrol et.
   - Başlık 1–2 satır ve dengeli; tek kelime ikinci satırda kalmamış.
   - Kod kutusundaki kod doğru. Rozet kısa ve ikonla çakışmıyor.
   - Altyazıda vurgulu kelimeler renkli görünüyor.
   - Roblox logosu, karakteri ya da oyun görüntüsü yok.
3. Son mp4'ten de birkaç kare al ve süreyi kontrol et:

   ```bash
   ffmpeg -v error -ss 5 -i FILE.mp4 -frames:v 1 check.jpg
   ffprobe -v error -show_entries format=duration -of csv=p=0 FILE.mp4
   ```

4. Ses: dosyanın başını ve bir kod sahnesini dinle (ya da en azından süreye bak). Kodların okunuşu anlaşılır olmalı.
5. Senaryodaki sayılar (oyun sayısı, kod sayısı, tarihler) başlık ve açıklamayla tutarlı olmalı.

## 9. Başlık, açıklama ve etiket kalıpları

### Başlıklar (emoji + #roblox; Short'larda + #shorts; 100 karakterden kısa)
- Short haber: `Roblox Wants 18+ Games Now! 🎮 #roblox #shorts`, `Roblox Ban Lists Are Coming! 🚫 #roblox #shorts`
- Short liste: `3 BIG Wins for Roblox Creators This Month! 🛠️ #roblox #shorts`
- Short kod: `3 FREE Roblox Codes You Need Today! 🎁 #roblox #shorts`
  - Her gün farklı bir kalıp kullan: "Just Dropped 💎", "You Probably Missed 👀", "Weekend … You Need 🎁"…
- Uzun video: `Roblox News Today: <Konu A>, <Konu B> & <N> New Codes 🚨 #roblox`
  - N, videodaki toplam kod sayısıdır ve birebir doğru olmalı.

### Açıklama, Short
```
<2-3 cümlelik özet, ya da kod listesi: "Game: CODE (reward)" satırları>

[kodluysa] Codes may expire at any time, so redeem them fast!

Subscribe to Secret Spawn for daily Roblox news!

#roblox #robloxnews #shorts        (kodluysa #robloxcodes; Studio haberi varsa #robloxstudio)
```

### Açıklama, uzun video
```
Today's Roblox news: <tek paragraf özet>.

Chapters:
0:00 Intro
0:13 <Bölüm 1>
...
2:32 Outro

Codes in this video:
<Game>: CODE1 (reward), CODE2 (reward)
...

Codes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.

Subscribe to Secret Spawn for daily Roblox news!

#roblox #robloxnews #robloxcodes #robloxupdate
```

### Etiketler (yalnızca uzun video, ~15–17 adet, toplam 500 karakterden az)
- Sabitler: `roblox, roblox news, roblox update, roblox codes, roblox studio, secret spawn, roblox news today`
- Ek olarak: haber konuları ve `<game> codes` etiketleri.

## 10. Studio yükleme ayarları (onaydan SONRA, ayrı adım)

### Genel ayarlar
- **Kitle:** her videoda "No, it's not made for kids" (`VIDEO_MADE_FOR_KIDS_NOT_MFK`).
- **Uzun video:** Show more açılır; Tags girilir, Video language **English**, Category **Gaming**. Studio API'sinde Gaming kategorisi `CREATOR_VIDEO_CATEGORY_GADGETS` olarak görünür; bu normal.
- **Görünürlük:** Schedule seçilir; tarih ve saat yukarıdaki tabloya göre. Studio saat dilimi İstanbul (GMT+3).
- **Başlık ve açıklama:** `upload_manifest.json` dosyasından.

### Dosyanın Studio'ya aktarılması (yerel dosya seçmeden)
1. mp4'ler `videos/YYYY-MM-DD/` klasörüne push'lanır.
2. Studio'da doğru kanalda (URL'de `UCrBMOIvfjj0z_W7DEE1EqDQ`) `.../videos/upload?d=ud` açılır.
3. Dosya JS ile `raw.githubusercontent.com/spR1nt23/secret-spawn-videos/<COMMIT_SHA>/videos/...` adresinden çekilir ve `ytcp-uploads-file-picker input[type=file]` alanına DataTransfer ile verilir.
   - URL'de `main` yerine **commit SHA** kullan; raw CDN eski dosyayı birkaç dakika önbellekte tutabiliyor.
   - Çekilen blob'un boyutu yerel dosyayla aynı mı kontrol et.

### Dikkat edilecekler
- Upload sayfası 403 veriyorsa tarayıcı başka bir Google hesabındadır. Avatar → Switch account → Secret Spawn ile geç.
  - Aynı tarayıcıyı başka kanalların sohbetleri de kullanıyor. Hesap değiştirmeden önce açık bir yükleme olmadığından emin ol.
  - İki sohbet aynı anda yükleme yapmamalı.
- Açıklama yanlışlıkla başlık kutusuna yazılabiliyor. Açıklamaya önce tek bir karakter yaz, doğru kutuya gittiğini doğrula, sonra devam et.
- Etiketleri virgüllerle yazdıktan sonra **Enter**'a bas; yoksa chip'e dönüşmezler.
- Tarih kutusuna `Nov 14, 2026` yaz ve Enter'a bas. Saat listesindeki metinlerde dar boşluk (U+202F) var; karşılaştırmadan önce normalize et.
- Tarayıcı paneli gizliyken "Video scheduled" penceresi geç gelebilir. Studio'nun `video_manager/metadata_update` yanıtındaki `scheduledTimeSeconds` alanını kontrol et ve UTC'den İstanbul saatine çevir.
- Videoları **tek tek** yükle. "Uploaded"/"Checks complete" görünmeden sayfadan ayrılma.
- Yanlış yüklenen bir video gizli taslak olarak kalabilir. Silmek kalıcıdır; kanal sahibine sormadan silme.

## 11. Günlük kontrol listesi (özet)

1. `git pull`. Bugünün setinin zaten hazır olup olmadığına bak (`videos/`, `TOPICS_HISTORY.md`).
2. Araştırma yap (bölüm 3). Kaynak URL'lerini not al.
3. `content/D.py` dosyasını yaz (senaryo ve UPLOAD bloğu).
4. `bash tools/make_day.sh content/D.py`
5. Kare kontrolünü yap (bölüm 8). Gerekirse senaryoyu düzeltip yeniden üret.
6. Bölüm zamanlarını uzun videonun açıklamasına yaz; `UPLOAD` bloğunu ve manifesti güncelle.
7. mp4'leri `videos/D/` klasörüne kopyala. `TOPICS_HISTORY.md` dosyasına günü ekle.
8. Commit ve push yap (main). Commit mesajı örneği: `Add Nov 14 set`
9. Kanal sahibine onay için şunları gönder: 4 başlık, yayın saatleri, süreler, kısa konu özeti, kaynaklar.
10. Onay gelince bölüm 10'a göre yükle ve zamanla.
