# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · **🇵🇭 Tagalog** · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Ang Botbright ay isang single-file JavaScript clone ng Flash puzzle na *Lightbot*. I-program ang isometric robot upang maglakad sa 3D-tile grid at paliwanagin ang mga asul na goal tile. I-drag ang mga instruction tile sa memorya ng robot, pindutin ang **Patakbuhin**, at panoorin kung paano isagawa ang iyong programa.

Buo ang laro sa iisang HTML file (`botbright.html`) na may inline na CSS at JavaScript — walang build step, walang external dependencies, walang network calls. Buksan ang file sa kahit anong modernong browser at maglaro. I-save ito sa hard drive mo at patuloy itong gagana offline magpakailanman.

Maaari mo ring baguhin ang color scheme at bigyan ng iba't ibang sumbrero ang robot. May built-in na level editor, at ang mga level at sumbrero ay maaaring i-import o i-export sa JSON format.

## Maglaro

I-double click lang ang botbright.html file o buksan ito sa iyong web browser. Gumagana ito kahit offline.

Live na bersyon: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Paano ito gumagana

May tatlong lugar ng memorya ang robot:

- **Pangunahing Memorya** — 12 slot ng utos, tatakbo kapag pinindot ang Patakbuhin
- **Memorya ng F1** — 8 slot ng utos, isang function na maaaring tawagin
- **Memorya ng F2** — 8 slot ng utos, pangalawang function na maaaring tawagin

I-drag ang mga instruction tile mula sa palette papuntang memorya. Magsaayos sa pamamagitan ng pag-drag sa pagitan ng mga slot. I-drag palabas ng slot ang isang tile para burahin ito.

| Utos | Ano ang ginagawa |
|-------------|------------|
| Sulong | Lumakad sa tile sa harap, kung magkapareho ng taas |
| Liko pakaliwa | Iikot ng 90° pakanan (counter-clockwise) |
| Liko pakanan | Iikot ng 90° pakaliwa (clockwise) |
| Talon | Tumalon pataas ng isang antas, o tumalon pababa kahit ilang antas |
| Pailawan | I-toggle ang goal tile na nasa ilalim ng robot |
| Tawagin ang F1 / F2 | Ilalagay ang function sa call stack (pinapayagan ang recursion, may limitasyon) |

Tapos na ang level kapag bawat goal tile ay nakasinding dilaw.

Ang mga programa na masyadong matagal tumakbo ay hihinto: pinakamarami 1000 utos sa kabuuan, pinakamarami 100 frame sa call stack.

## Mga kontrol

**Camera** — WASD o arrow keys para mag-pan, Q/E o PageUp/PageDown para iikot ng 90°, +/− o scroll wheel para mag-zoom. Pindutin ang 0 para i-reset ang tanaw. I-drag ang canvas para mag-pan, pisilin para mag-zoom, ikutin gamit ang dalawang daliri para iikot. Pindutin at i-hold ang on-screen na camera buttons para sa tuluy-tuloy at malambot na paggalaw.

**Lapad ng sidebar** — i-drag ang divider sa pagitan ng canvas at sidebar.

**Bilis** — slider sa sidebar: mabagal / normal / mabilis. Mababago habang tumatakbo.

## Tagaedit ng Level

May kasamang buong editor ang laro. Magdagdag/magdoble/magtanggal ng level, baguhin ang sukat ng grid (1–32 sa bawat dimensyon), magpinta ng taas 0–9, magmarka ng goal tile, magtakda ng simulang posisyon at direksyon, at sumubok na maglaro nang hindi umaalis sa editor.

Ang buong set ng level ay nai-e-export bilang JSON at nai-i-import sa parehong paraan, kaya pwedeng ibahagi ang mga level o mag-back up ng mga pagbabago.

## Tagaedit ng Sumbrero

Maaaring magsuot ng sumbrero ang robot. May labinsiyam na opsyon na kasama: Wala, Top Hat, Sumbrero ng Mangkukulam (lalaki), Korona, Beanie, Baseball Cap, Sumbrero ng Cowboy, Sumbrero ng Party, Bowler Hat, Halo, Sungay ng Demonyo, Sombrero, Sumbrero ng Bruha, Fez, Sungay ng Usa, Tenga ng Kuneho, Tenga ng Pusa, Helmet ng Maninisid, at Helmet ng Viking. Bawat sumbrero ay binubuo ng apat na SVG sprite — isa para sa bawat direksyon na nakikita sa screen — kaya sumusunod ang sumbrero sa direksyon ng robot kahit umiikot ang camera (ang visor ng baseball cap, hebilya ng sumbrero ng bruha, bintana ng helmet ng maninisid, at loob ng tenga ng kuneho/pusa ay sumasabay). May live preview na umiikot ang robot bawat segundo para makita ang sumbrero mula sa bawat anggulo. Maaari ring i-export at i-import ang mga sumbrero bilang JSON para sa custom na disenyo.

## Mga Kulay na Tema

Isang panel ng **Mga Kulay** sa sidebar ng laro ang naglalantad ng palette: kulay ng tile, kulay ng gilid ng tile, kulay ng goal, kulay ng nailalwang goal, background, at katawan ng robot. Maaari kang gumamit ng built-in na tema o i-edit ang mga ito mismo.

## Mga Wika

Salin sa UI sa 23 wika: Ingles, Espanyol, Pranses, Aleman, Italyano, Portuges, Ruso, Tsino, Hapon, Koreano, Hindi, Bengali, Vietnamese, Arabik (na may right-to-left na layout), Thai, Tagalog, Norwegian, Dutch, Swedish, Turko, Swahili, Indonesyo, at Polish. Sumusunod ang default na wika sa `navigator.language` ng browser; mapapalitan ito ng language selector sa start screen para sa sesyon. Naisalin sa lahat ng sinusuportahang wika ang mga pangalan at paglalarawan ng built-in na mga level, gayundin ang pangalan ng built-in na mga sumbrero. Kapag inedit mo ang pangalan o paglalarawan, isinusulat lamang ng level editor sa slot ng wikang kasalukuyang napili, hindi ginagalaw ang ibang salin.

## Liwanag / Madilim na Mode

Sumusunod ang app chrome sa `prefers-color-scheme` ng browser. Kapag pinili ang **Default** na tema sa Colors panel, ilalapat ang palette na tumutugma sa kasalukuyang mode ng browser, kaya nananatili itong naka-sync kapag inilipat mo ang mode. Ang anumang ibang built-in na tema — o custom na palette na inayos sa Colors panel — ang papalit sa kilos na ito.

## Pasasalamat

Ginawa ni Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspirado mula sa *Lightbot* ni Daniel Yaroslavski.
