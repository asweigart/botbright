# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · **🇹🇷 Türkçe** · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright, Flash bulmaca oyunu *Lightbot*'un tek dosyalı JavaScript klonudur. İzometrik bir robotu programlayarak 3B karo ızgarasında yürümesini ve mavi hedef karoları aydınlatmasını sağla. Talimat karolarını robotun belleğine sürükle, **Çalıştır**'a bas ve programının çalışmasını izle.

Tüm oyun tek bir HTML dosyasıdır (`botbright.html`); CSS ve JavaScript satır içinde gömülüdür — derleme adımı yok, dış bağımlılık yok, ağ çağrısı yok. Dosyayı herhangi bir modern tarayıcıda aç ve oyna. Sabit diskine kaydedersen sonsuza dek çevrimdışı çalışmaya devam eder.

Renk şemasını da değiştirebilir ve robotuna farklı şapkalar taktırabilirsin. Yerleşik bir seviye düzenleyici var; seviyeler ve şapkalar JSON biçiminde içe/dışa aktarılabilir.

## Oyna

Sadece botbright.html dosyasına çift tıkla ya da tarayıcında aç. Oyun çevrimdışı çalışır.

Canlı sürüm: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Nasıl çalışır

Robotun üç bellek alanı var:

- **Ana Bellek** — 12 komut yuvası, Çalıştır'a bastığında işletilir
- **F1 Belleği** — 8 komut yuvası, çağrılabilir bir fonksiyon
- **F2 Belleği** — 8 komut yuvası, ikinci çağrılabilir bir fonksiyon

Talimat karolarını paletten belleğe sürükle. Yuvalar arasında sürükleyerek sırala. Bir karoyu yuvanın dışına sürükleyerek sil.

| Komut | Ne yapar |
|-------------|------------|
| İleri | Öndeki karo aynı yükseklikteyse oraya adım at |
| Sola dön | 90° saat yönünün tersine döner |
| Sağa dön | 90° saat yönünde döner |
| Atla | Bir seviye yukarı zıpla ya da istediğin kadar seviye aşağı atla |
| Yak | Robotun altındaki hedef karoyu açar/kapatır |
| F1 / F2 çağır | O fonksiyonu çağrı yığınına ekler (özyineleme limitler dahilinde serbest) |

Her hedef karo sarı yandığında seviye tamamlanır.

Çok uzun süre çalışan programlar durdurulur: en fazla toplam 1000 komut, en fazla 100 çağrı yığını çerçevesi.

## Kontroller

**Kamera** — WASD veya ok tuşları ile kaydır, Q/E veya PageUp/PageDown ile 90° döndür, +/− ya da kaydırma tekerleğiyle yakınlaştır. Görünümü sıfırlamak için 0 tuşuna bas. Tuvali sürükleyerek kaydır, sıkıştırarak yakınlaştır, iki parmakla bükerek döndür. Ekrandaki kamera düğmelerini basılı tut, akıcı ve sürekli hareket elde edersin.

**Kenar çubuğu genişliği** — tuval ile kenar çubuğu arasındaki ayırıcıyı sürükle.

**Hız** — kenar çubuğundaki kaydırıcı: yavaş / normal / hızlı. Çalışırken bile ayarlanabilir.

## Seviye Düzenleyici

Oyunla birlikte tam bir düzenleyici gelir. Seviye ekle/kopyala/sil, ızgarayı yeniden boyutlandır (her boyutta 1–32), 0–9 yükseklik boya, hedef karoları işaretle, başlangıç konumu ve yönünü ayarla, düzenleyiciden çıkmadan test oyna.

Tüm seviye seti JSON olarak dışa aktarılır ve aynı şekilde içe aktarılır; böylece seviyeleri paylaşabilir veya değişiklikleri yedekleyebilirsin.

## Şapka Düzenleyici

Robot şapka takabilir. On dokuz seçenek gelir: Yok, Silindir Şapka, Sihirbaz Şapkası, Taç, Bere, Beyzbol Şapkası, Kovboy Şapkası, Parti Şapkası, Melon Şapka, Hâle, Şeytan Boynuzları, Sombrero, Cadı Şapkası, Fes, Geyik Boynuzu, Tavşan Kulakları, Kedi Kulakları, Dalış Kaskı ve Viking Miğferi. Her şapka dört SVG sprite ile tanımlanır — ekrana göre her yön için bir tane — böylece tüm kamera dönüşlerinde robotun yönüne uyar (beyzbol şapkasının siperliği, cadı şapkasının tokası, dalış kaskının lombozu ve tavşan/kedi kulaklarının içi de buna göre kayar). Canlı önizleme robotu saniyede bir döndürür, şapkayı her açıdan görebilirsin. Özel tasarımlar için şapkalar JSON olarak da dışa/içe aktarılabilir.

## Renk Şemaları

Oyun kenar çubuğundaki **Renkler** paneli paleti açar: karo rengi, karo kenarı rengi, hedef rengi, yanmış hedef rengi, arka plan ve robot gövdesi. Yerleşik bir tema kullanabilir ya da bunları kendin düzenleyebilirsin.

## Diller

23 dil için arayüz çevirileri: İngilizce, İspanyolca, Fransızca, Almanca, İtalyanca, Portekizce, Rusça, Çince, Japonca, Korece, Hintçe, Bengalce, Vietnamca, Arapça (sağdan sola düzenle), Tayca, Tagalog, Norveççe, Felemenkçe, İsveççe, Türkçe, Svahili, Endonezce ve Lehçe. Varsayılan dil tarayıcının `navigator.language` değerini takip eder; başlangıç ekranındaki dil seçici oturum boyunca onu geçersiz kılar. Yerleşik seviye adları ve açıklamaları ile yerleşik şapka adları tüm desteklenen dillerde çevrilmiştir. Bir ad ya da açıklama düzenlediğinde seviye düzenleyici yalnızca o anda seçili dilin yuvasına yazar; diğer dillerin çevirileri olduğu gibi kalır.

## Açık / Koyu Mod

Uygulama çerçevesi tarayıcının `prefers-color-scheme` özelliğini takip eder. Renkler panelinde **Varsayılan** temasını seçtiğinde, tarayıcının mevcut moduna uygun palet uygulanır ve modu değiştirdiğinde de senkronize kalır. Başka bir yerleşik tema — ya da Renkler panelinden özelleştirdiğin bir palet — bu davranışı geçersiz kılar.

## Künye

Hazırlayan Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Daniel Yaroslavski'nin *Lightbot* oyunundan ilham alınmıştır.
