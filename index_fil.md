# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · **🇵🇭 Filipino** · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Ang Botbright ay isang single-file na JavaScript clone ng Flash puzzle game na *Lightbot*. I-program ang isang isometric na robot upang maglakad sa 3D-tile grid at paliwanagan ang asul na goal tiles. I-drag ang instruction tiles papunta sa memorya ng robot, pindutin ang **Patakbuhin**, at panoorin ang programa mo na isagawa.

Ang buong laro ay isang HTML file (`botbright.html`) na may inline na CSS at JavaScript — walang build step, walang external dependencies, walang network calls. Buksan ang file sa kahit anong makabagong browser at maglaro. I-save ito sa hard drive mo at patuloy itong gagana offline magpakailanman.

Maaari mo ring baguhin ang color scheme at bigyan ang robot mo ng iba't ibang sumbrero. Mayroong built-in na level editor, at ang mga level at sumbrero ay maaaring i-import o i-export sa JSON format.

## Maglaro

Simpleng i-double click lang ang botbright.html file o buksan ito sa iyong web browser. Gumagana ang laro nang offline.

Live na bersyon: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Paano ito gumagana

May tatlong memorya ang robot:

- **Pangunahing Memorya** — 12 slot ng utos, gumagana kapag pinindot ang Patakbuhin
- **Memorya ng F1** — 8 slot ng utos, isang function na puwedeng tawagin
- **Memorya ng F2** — 8 slot ng utos, pangalawang function na puwedeng tawagin

I-drag ang instruction tiles mula sa palette papunta sa memorya. Ayusin ang pagkakasunud-sunod sa pamamagitan ng pag-drag sa pagitan ng mga slot. I-drag ang isang tile palabas ng slot upang burahin ito.

| Utos | Ano ang ginagawa |
|-------------|------------|
| Sulong | Lumakad sa tile sa harap, kapag pareho ang taas |
| Liko pakaliwa | Pag-ikot ng 90° pakanan (counter-clockwise) |
| Liko pakanan | Pag-ikot ng 90° pakaliwa (clockwise) |
| Talon | Tumalon nang isang antas pataas, o tumalon nang ilang antas pababa |
| Pailawan | I-toggle ang goal tile sa ilalim ng robot |
| Tawagin ang F1 / F2 | Ipo-push ang function na iyon sa call stack (pinapayagan ang recursion, may mga limitasyon) |

Tapos ang level kapag bawat goal tile ay nakasindi ng dilaw.

Ang mga programang masyadong matagal tumakbo ay hihinto: hanggang 1000 utos sa kabuuan, hanggang 100 frame sa call stack.

## Mga kontrol

**Camera** — WASD o arrow keys para mag-pan, Q/E o PageUp/PageDown para iikot ng 90°, +/− o scroll wheel para mag-zoom. Pindutin ang 0 para i-reset ang view. I-drag ang canvas para mag-pan, kurutin para mag-zoom, ikutin gamit ang dalawang daliri para iikot. Pindutin at i-hold ang on-screen camera buttons para sa tuluy-tuloy at malambot na paggalaw.

**Lapad ng sidebar** — i-drag ang divider sa pagitan ng canvas at sidebar.

**Bilis** — slider sa sidebar: mabagal / katamtaman / mabilis. Maaaring i-adjust habang tumatakbo.

## Tagaedit ng Level

May kasamang buong editor ang laro. Magdagdag/duplicate/magtanggal ng level, baguhin ang sukat ng grid (1–32 sa bawat dimensyon), magpinta ng taas 0–9, magmarka ng goal tile, magtakda ng simulang posisyon at direksyon, at subukan ang laro nang hindi umaalis sa editor.

Ang buong set ng level ay nai-e-export bilang JSON at nai-i-import sa parehong paraan, kaya pwedeng ibahagi ang mga level o mag-back up ng mga pagbabago.

## Tagaedit ng Sumbrero

Maaaring magsuot ng sumbrero ang robot. May labinsiyam na opsyon na kasama: Wala, Top Hat, Sumbrero ng Mangkukulam, Korona, Beanie, Baseball Cap, Sumbrero ng Cowboy, Sumbrero ng Party, Bowler Hat, Halo, Sungay ng Demonyo, Sombrero, Sumbrero ng Bruha, Fez, Sungay ng Usa, Tenga ng Kuneho, Tenga ng Pusa, Helmet ng Maninisid, at Helmet ng Viking. Bawat sumbrero ay binubuo ng apat na SVG sprite — isa para sa bawat direksyon na nakikita sa screen — kaya sumusunod ang sumbrero sa direksyon ng robot kahit umiikot ang camera (ang visor ng baseball cap, ang hebilya ng sumbrero ng bruha, ang bintana ng helmet ng maninisid, at ang loob ng tenga ng kuneho/pusa ay sumasabay). May live preview na umiikot ang robot bawat segundo upang makita ang sumbrero mula sa bawat anggulo. Maaari ring i-export at i-import ang mga sumbrero bilang JSON para sa pasadyang disenyo.

## Mga Tema ng Kulay

Ang **Mga Kulay** panel sa sidebar ng laro ay naglalantad ng palette: kulay ng tile, kulay ng gilid ng tile, kulay ng goal, kulay ng nailawang goal, background, at katawan ng robot. Maaari kang gumamit ng built-in na tema o i-edit ang mga ito mismo.

## Mga Wika

Mga salin ng interface sa 23 wika: Ingles, Espanyol, Pranses, Aleman, Italyano, Portuges, Ruso, Tsino, Hapon, Koreano, Hindi, Bengali, Vietnamese, Arabik (na may right-to-left layout), Thai, Tagalog, Norwegian, Dutch, Swedish, Turko, Swahili, Indonesyo, at Polish. Sumusunod ang default na wika sa `navigator.language` ng browser; mapapalitan ito ng language selector sa start screen para sa sesyon. Naisalin sa lahat ng sinusuportahang wika ang mga pangalan at paglalarawan ng built-in na mga level, gayundin ang pangalan ng built-in na mga sumbrero. Kapag inedit mo ang pangalan o paglalarawan, sa slot lamang ng kasalukuyang napiling wika nagsusulat ang level editor, hindi ginagalaw ang ibang salin.

## Liwanag / Madilim na Mode

Sinusunod ang `prefers-color-scheme` ng browser para sa app chrome. Kapag pinili ang **Default** na tema sa Colors panel, ilalapat ang palette na tumutugma sa kasalukuyang mode ng browser, kaya nananatili itong naka-sync kapag inilipat mo ang mode. Ang anumang ibang built-in na tema — o custom na palette na inayos sa Colors panel — ang papalit sa kilos na ito.

## Pasasalamat

Ginawa ni Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspirado mula sa *Lightbot* ni Daniel Yaroslavski.
