# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · **🇳🇱 Nederlands** · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright is een JavaScript-kloon in één bestand van het Flash-puzzelspel *Lightbot*. Programmeer een isometrische robot om over een 3D-tegelraster te lopen en de blauwe doel-tegels te laten oplichten. Sleep instructietegels naar het geheugen van de robot, druk op **Starten** en kijk hoe je programma wordt uitgevoerd.

Het hele spel is één HTML-bestand (`botbright.html`) met inline CSS en JavaScript — geen build-stap, geen externe afhankelijkheden, geen netwerkverzoeken. Open het bestand in elke moderne browser en speel. Sla het op je harde schijf op en het blijft eeuwig offline werken.

Je kunt ook het kleurthema wijzigen en de robot verschillende hoeden opzetten. Er is een ingebouwde levelbewerker, en levels en hoeden kunnen worden geïmporteerd of geëxporteerd als JSON.

## Spelen

Dubbelklik gewoon op het bestand botbright.html of open het in je browser. Het spel werkt offline.

Live-versie: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Hoe het werkt

De robot heeft drie geheugengebieden:

- **Hoofdgeheugen** — 12 instructieslots, draait als je op Starten drukt
- **F1-geheugen** — 8 instructieslots, een aanroepbare functie
- **F2-geheugen** — 8 instructieslots, een tweede aanroepbare functie

Sleep instructietegels vanuit het palet naar het geheugen. Wijzig de volgorde door tussen slots te slepen. Sleep een tegel uit een slot om hem te verwijderen.

| Instructie | Wat het doet |
|-------------|------------|
| Vooruit | Stap op de tegel ervoor, als die op dezelfde hoogte ligt |
| Linksom | Draait 90° tegen de klok in |
| Rechtsom | Draait 90° met de klok mee |
| Springen | Spring één niveau omhoog of een willekeurig aantal omlaag |
| Verlichten | Wisselt de doel-tegel onder de robot |
| F1 / F2 aanroepen | Plaatst die functie op de aanroepstack (recursie toegestaan, met limieten) |

Een level is voltooid als elke doel-tegel geel oplicht.

Programma's die te lang draaien worden gestopt: maximaal 1000 instructies totaal, maximaal 100 frames in de aanroepstack.

## Bediening

**Camera** — WASD of pijltjes om te pannen, Q/E of PageUp/PageDown om 90° te draaien, +/− of het scrollwiel om in/uit te zoomen. Druk op 0 om de weergave te resetten. Sleep over het canvas om te pannen, knijp om te zoomen, draai met twee vingers om te roteren. Houd de camera-knoppen op het scherm ingedrukt voor soepele, continue beweging.

**Breedte zijbalk** — sleep de scheiding tussen canvas en zijbalk.

**Snelheid** — schuif in de zijbalk: langzaam / normaal / snel. Te wijzigen tijdens het draaien.

## Levelbewerker

Het spel komt met een volledige bewerker. Levels toevoegen/dupliceren/verwijderen, raster vergroten/verkleinen (1–32 in elke dimensie), hoogtes 0–9 schilderen, doel-tegels markeren, startpositie en oriëntatie instellen, en testen zonder de bewerker te verlaten.

De volledige levelset wordt als JSON geëxporteerd en op dezelfde manier geïmporteerd, zodat je levels kunt delen of bewerkingen kunt back-uppen.

## Hoeden-editor

De robot kan hoeden dragen. Bevat negentien opties: Geen, Hoge hoed, Tovenaarshoed, Kroon, Muts, Baseballpet, Cowboyhoed, Feestmuts, Bolhoed, Halo, Duivelshoorns, Sombrero, Heksenhoed, Fez, Gewei, Konijnenoren, Kattenoren, Duikhelm en Vikinghelm. Elke hoed is gedefinieerd door vier SVG-sprites — één per schermrichting — zodat de hoed de oriëntatie van de robot volgt bij elke camerarotatie (de klep van de baseballpet, de gesp van de heksenhoed, het patrijspoort van de duikhelm en de binnenkant van de konijnen-/kattenoren bewegen mee). Een live preview draait de robot elke seconde één keer rond zodat je de hoed van alle kanten ziet. Hoeden zijn ook als JSON te exporteren en importeren voor eigen ontwerpen.

## Kleurschema's

Een **Kleuren**-paneel in de zijbalk van het spel toont het palet: tegelkleur, kleur van de tegelranden, doelkleur, opgelichte doelkleur, achtergrond en robotlichaam. Je kunt een ingebouwd thema gebruiken of de kleuren zelf aanpassen.

## Talen

UI-vertalingen in 23 talen: Engels, Spaans, Frans, Duits, Italiaans, Portugees, Russisch, Chinees, Japans, Koreaans, Hindi, Bengali, Vietnamees, Arabisch (met rechts-naar-links-indeling), Thai, Tagalog, Noors, Nederlands, Zweeds, Turks, Swahili, Indonesisch en Pools. De standaardtaal volgt de `navigator.language` van de browser; de taalkiezer op het startscherm overschrijft dit voor de sessie. De namen en beschrijvingen van ingebouwde levels en de namen van ingebouwde hoeden zijn vertaald naar alle ondersteunde talen. De levelbewerker schrijft bij het bewerken van een naam of beschrijving alleen naar het slot van de momenteel geselecteerde taal en laat de andere vertalingen ongemoeid.

## Licht / Donker modus

Volgt de `prefers-color-scheme` van de browser voor het app-omhulsel. Selecteer je het **Standaard**-thema in het Kleuren-paneel, dan wordt het palet toegepast dat past bij de huidige modus van de browser, dus het blijft synchroon als je de modus wisselt. Elk ander ingebouwd thema — of een aangepast palet dat je via het Kleuren-paneel afstelt — overschrijft dit gedrag.

## Credits

Gemaakt door Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Geïnspireerd door *Lightbot* van Daniel Yaroslavski.
