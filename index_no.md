# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · **🇳🇴 Norsk** · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Botbright er en JavaScript-klone i én enkelt fil av Flash-puslespillet *Lightbot*. Programmer en isometrisk robot til å gå over et 3D-flisrutenett og lyse opp de blå målfliserne. Dra instruksjonsfliser inn i robotens minne, trykk **Kjør**, og se programmet ditt utføres.

Hele spillet ligger i én HTML-fil (`botbright.html`) med innebygd CSS og JavaScript — ingen byggesteg, ingen eksterne avhengigheter, ingen nettverkskall. Åpne filen i en moderne nettleser og spill. Lagre den på harddisken så fungerer den offline for alltid.

Du kan også bytte fargetema og gi roboten din ulike luer å gå med. En nivåredigerer er innebygd, og nivåer og luer kan importeres eller eksporteres som JSON.

## Spille

Bare dobbeltklikk botbright.html-filen eller åpne den i nettleseren. Spillet fungerer offline.

Live-versjon: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Slik fungerer det

Roboten har tre minneområder:

- **Hovedminne** — 12 instruksjonsplasser, kjøres når du trykker Kjør
- **F1-minne** — 8 instruksjonsplasser, en kallbar funksjon
- **F2-minne** — 8 instruksjonsplasser, en andre kallbar funksjon

Dra instruksjonsfliser fra paletten inn i minnet. Endre rekkefølgen ved å dra mellom plasser. Dra en flis ut av en plass for å slette den.

| Instruksjon | Hva den gjør |
|-------------|------------|
| Fremover | Trå inn på flisen foran, hvis den har samme høyde |
| Snu venstre | Roterer 90° mot klokken |
| Snu høyre | Roterer 90° med klokken |
| Hopp | Hopp opp ett nivå, eller ned vilkårlig antall nivåer |
| Lys | Veksler målflisen under roboten |
| Kall F1 / F2 | Legger funksjonen på kallstabelen (rekursjon tillatt, med grenser) |

Et nivå er ferdig når hver målflis lyser gult.

Programmer som kjører for lenge stoppes: maks 1000 instruksjoner totalt, maks 100 rammer i kallstabelen.

## Kontroller

**Kamera** — WASD eller piltastene for å panorere, Q/E eller PageUp/PageDown for å rotere 90°, +/− eller rullehjul for zoom. Trykk 0 for å tilbakestille visningen. Dra lerretet for å panorere, knip for å zoome, vri med to fingre for å rotere. Hold inne kameraknappene på skjermen for jevn kontinuerlig bevegelse.

**Bredde på sidefelt** — dra skilleren mellom lerretet og sidefeltet.

**Hastighet** — glidebryter i sidefeltet: sakte / normal / rask. Kan justeres mens programmet kjører.

## Nivå-editor

En fullverdig editor følger med spillet. Legg til/dupliser/slett nivåer, endre størrelse på rutenettet (1–32 i hver dimensjon), mal høyder 0–9, marker målfliser, sett startposisjon og retning, og prøvespill uten å forlate editoren.

Hele nivåsettet eksporteres som JSON og importeres på samme måte, så du kan dele nivåer eller ta vare på endringer.

## Lue-editor

Roboten kan bruke luer. Det følger med nitten valg: Ingen, Flosshatt, Trollmannshatt, Krone, Topplue, Baseballcaps, Cowboyhatt, Festhatt, Bowlerhatt, Glorie, Djevelhorn, Sombrero, Hekshatt, Fez, Gevir, Kaninører, Katteører, Dykkerhjelm og Vikinghjelm. Hver lue er definert av fire SVG-sprites — én per skjermretning — slik at lua følger robotens retning ved alle kameradreininger (skyggen på baseballcapsen, spennen på hekshatten, vinduet på dykkerhjelmen og innsiden av kanin-/katteørene flyttes tilsvarende). En live forhåndsvisning roterer roboten én gang per sekund så du ser lua fra alle vinkler. Luene kan også eksporteres og importeres som JSON for egne design.

## Fargetemaer

Et **Farger**-panel i spillets sidefelt viser paletten: flisefarge, flisekantfarge, målfarge, opplyst målfarge, bakgrunn og robotkropp. Du kan bruke et innebygd tema eller redigere selv.

## Språk

UI-oversettelser på 23 språk: engelsk, spansk, fransk, tysk, italiensk, portugisisk, russisk, kinesisk, japansk, koreansk, hindi, bengali, vietnamesisk, arabisk (med høyre-til-venstre-oppsett), thai, tagalog, norsk, nederlandsk, svensk, tyrkisk, swahili, indonesisk og polsk. Standardspråket følger nettleserens `navigator.language`; språkvelgeren på startskjermen overstyrer det for økten. Navn og beskrivelser på de innebygde nivåene, og navnene på de innebygde luene, er oversatt til alle støttede språk. Nivåredigereren skriver bare til det språket du har valgt når du endrer et navn eller en beskrivelse, og lar de andre oversettelsene være urørt.

## Lys / Mørk modus

Følger nettleserens `prefers-color-scheme` for app-rammen. Velger du **Standard**-temaet i Farger-panelet, brukes paletten som passer til nettleserens nåværende modus, og den holder seg synkronisert om du bytter modus. Et hvilket som helst annet innebygd tema — eller en egendefinert palett du justerer i Farger-panelet — overstyrer dette.

## Kreditering

Laget av Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspirert av *Lightbot* av Daniel Yaroslavski.
