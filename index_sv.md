# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · **🇸🇪 Svenska** · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Botbright är en JavaScript-klon i en enda fil av Flash-pusselspelet *Lightbot*. Programmera en isometrisk robot att gå över ett 3D-rutnät av plattor och tända de blå målplattorna. Dra instruktionsplattor in i robotens minne, tryck **Kör** och se ditt program köras.

Hela spelet är en HTML-fil (`botbright.html`) med inbäddad CSS och JavaScript — inget byggsteg, inga externa beroenden, inga nätverksanrop. Öppna filen i valfri modern webbläsare och spela. Spara den på hårddisken så fortsätter den att fungera offline för alltid.

Du kan också byta färgschema och ge roboten olika hattar att bära. En banredigerare är inbyggd, och banor och hattar kan importeras eller exporteras som JSON.

## Spela

Dubbelklicka bara på botbright.html-filen eller öppna den i webbläsaren. Spelet fungerar offline.

Liveversion: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Så fungerar det

Roboten har tre minnesområden:

- **Huvudminne** — 12 instruktionsplatser, körs när du trycker på Kör
- **F1-minne** — 8 instruktionsplatser, en anropbar funktion
- **F2-minne** — 8 instruktionsplatser, ytterligare en anropbar funktion

Dra instruktionsplattor från paletten in i minnet. Ändra ordningen genom att dra mellan platserna. Dra en platta ut ur en plats för att ta bort den.

| Instruktion | Vad den gör |
|-------------|------------|
| Framåt | Kliv upp på plattan framför om den är på samma höjd |
| Sväng vänster | Roterar 90° moturs |
| Sväng höger | Roterar 90° medurs |
| Hoppa | Hoppa upp en nivå, eller ner hur många nivåer som helst |
| Lys | Växlar målplattan under roboten |
| Anropa F1 / F2 | Lägger funktionen på anropsstacken (rekursion tillåten, med gränser) |

En bana är klar när varje målplatta lyser gult.

Program som körs för länge stoppas: max 1000 instruktioner totalt, max 100 ramar på anropsstacken.

## Kontroller

**Kamera** — WASD eller piltangenter för att panorera, Q/E eller PageUp/PageDown för att rotera 90°, +/− eller scrollhjulet för zoom. Tryck 0 för att återställa vyn. Dra i ytan för att panorera, nyp för att zooma, vrid med två fingrar för att rotera. Håll inne kameraknapparna på skärmen för mjuk, kontinuerlig rörelse.

**Sidopanelens bredd** — dra avdelaren mellan ytan och sidopanelen.

**Hastighet** — skjutreglage i sidopanelen: långsamt / normalt / snabbt. Justerbart under körning.

## Banredigerare

En komplett redigerare följer med spelet. Lägg till/duplicera/ta bort banor, ändra rutnätet (1–32 i varje dimension), måla höjder 0–9, markera målplattor, ställ in startposition och blickriktning och provspela utan att lämna redigeraren.

Hela bansetet exporteras som JSON och importeras på samma sätt, så du kan dela banor eller säkerhetskopiera ändringar.

## Hattredigerare

Roboten kan bära hattar. Det följer med nitton val: Ingen, Hög hatt, Trollkarlshatt, Krona, Mössa, Basebollkeps, Cowboyhatt, Festhatt, Plommonstop, Gloria, Djävulshorn, Sombrero, Häxhatt, Fez, Horn, Kaninöron, Kattöron, Dykarhjälm och Vikingahjälm. Varje hatt definieras av fyra SVG-sprites — en per skärmriktning — så hatten följer robotens riktning vid alla kameravridningar (basebollkepsens skärm, häxhattens spänne, dykarhjälmens fönster och bunny-/kattöronens insida flyttar sig med). En live-förhandsvisning roterar roboten en gång per sekund så att du ser hatten från alla håll. Hattar kan också exporteras och importeras som JSON för egna designer.

## Färgteman

En **Färger**-panel i spelets sidopanel visar paletten: plattfärg, plattkantsfärg, målfärg, tänd målfärg, bakgrund och robotkropp. Du kan använda ett inbyggt tema eller anpassa själv.

## Språk

UI-översättningar till 23 språk: engelska, spanska, franska, tyska, italienska, portugisiska, ryska, kinesiska, japanska, koreanska, hindi, bengali, vietnamesiska, arabiska (med höger-till-vänster-layout), thai, tagalog, norska, nederländska, svenska, turkiska, swahili, indonesiska och polska. Standardspråket följer webbläsarens `navigator.language`; språkväljaren på startskärmen åsidosätter det för sessionen. De inbyggda banornas namn och beskrivningar samt namnen på de inbyggda hattarna är översatta till alla språk som stöds. Banredigeraren skriver bara till det aktuella språkets fält när du ändrar ett namn eller en beskrivning, övriga översättningar lämnas orörda.

## Ljust / Mörkt läge

Följer webbläsarens `prefers-color-scheme` för app-skalet. När du väljer temat **Standard** i Färg-panelen tillämpas den palett som matchar webbläsarens aktuella läge, så det förblir synkroniserat när du växlar läge. Vilket annat inbyggt tema som helst — eller en egen palett du justerar via Färg-panelen — åsidosätter detta beteende.

## Skapare

Skapad av Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspirerad av *Lightbot* av Daniel Yaroslavski.
