# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · **🇩🇪 Deutsch** · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright ist ein JavaScript-Klon des Flash-Puzzlespiels *Lightbot* in einer einzigen Datei. Programmiere einen isometrischen Roboter, der über ein 3D-Kachelraster läuft und die blauen Zielkacheln zum Leuchten bringt. Ziehe Befehlskacheln in den Speicher des Roboters, drücke **Start** und sieh deinem Programm beim Ausführen zu.

Das gesamte Spiel ist eine HTML-Datei (`botbright.html`) mit eingebettetem CSS und JavaScript — kein Build-Schritt, keine externen Abhängigkeiten, keine Netzwerk-Aufrufe. Öffne die Datei in einem modernen Browser und spiele. Speichere sie auf deiner Festplatte und sie funktioniert für immer offline.

Du kannst auch das Farbschema ändern und deinem Roboter verschiedene Hüte aufsetzen. Ein Level-Editor ist integriert, und Level sowie Hüte lassen sich als JSON importieren und exportieren.

## Spielen

Doppelklicke einfach auf die Datei botbright.html oder öffne sie im Browser. Das Spiel funktioniert offline.

Live-Version: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## So funktioniert es

Der Roboter hat drei Speicherbereiche:

- **Hauptspeicher** — 12 Befehlsplätze, läuft, wenn du Start drückst
- **F1-Speicher** — 8 Befehlsplätze, eine aufrufbare Funktion
- **F2-Speicher** — 8 Befehlsplätze, eine zweite aufrufbare Funktion

Ziehe Befehlskacheln aus der Palette in den Speicher. Sortiere sie um, indem du sie zwischen Plätzen verschiebst. Ziehe eine Kachel aus einem Platz heraus, um sie zu löschen.

| Befehl | Wirkung |
|-------------|------------|
| Vorwärts | Geh auf die Kachel davor, wenn sie auf gleicher Höhe ist |
| Links drehen | Dreht 90° gegen den Uhrzeigersinn |
| Rechts drehen | Dreht 90° im Uhrzeigersinn |
| Springen | Hüpft eine Ebene hoch oder beliebig viele Ebenen herunter |
| Leuchten | Schaltet die Zielkachel unter dem Roboter um |
| F1 / F2 aufrufen | Legt diese Funktion auf den Aufrufstapel (Rekursion erlaubt, mit Grenzen) |

Ein Level ist geschafft, wenn alle Zielkacheln gelb leuchten.

Zu lange laufende Programme werden gestoppt: maximal 1000 Gesamtbefehle, maximal 100 Stapelrahmen.

## Steuerung

**Kamera** — WASD oder Pfeiltasten zum Schwenken, Q/E oder Bild auf/ab für 90°-Drehung, +/− oder Scrollrad zum Zoomen. Drücke 0, um die Ansicht zurückzusetzen. Ziehe die Spielfläche zum Schwenken, kneife zum Zoomen, drehe mit zwei Fingern. Halte die Kamera-Tasten am Bildschirm gedrückt für sanfte, kontinuierliche Bewegung.

**Seitenleistenbreite** — ziehe die Trennlinie zwischen Spielfläche und Seitenleiste.

**Geschwindigkeit** — Schieberegler in der Seitenleiste: langsam / normal / schnell. Auch während der Ausführung anpassbar.

## Level-Editor

Ein vollwertiger Editor ist enthalten. Level hinzufügen/duplizieren/löschen, Rastergröße ändern (1–32 in jeder Dimension), Höhen von 0–9 malen, Zielkacheln markieren, Startposition und Blickrichtung festlegen und Probespiel ohne den Editor zu verlassen.

Das gesamte Level-Set wird als JSON exportiert und genauso importiert, sodass du Level teilen oder Änderungen sichern kannst.

## Hut-Editor

Der Roboter kann Hüte tragen. Es sind neunzehn Optionen enthalten: Keiner, Zylinder, Zaubererhut, Krone, Mütze, Baseballkappe, Cowboyhut, Partyhut, Melone, Heiligenschein, Teufelshörner, Sombrero, Hexenhut, Fez, Geweih, Hasenohren, Katzenohren, Taucherhelm und Wikingerhelm. Jeder Hut ist durch vier SVG-Sprites definiert — eines pro Blickrichtung auf dem Bildschirm — damit er der Roboterausrichtung bei allen Kameradrehungen folgt (der Schirm der Baseballkappe, die Schnalle des Hexenhuts, das Bullauge des Taucherhelms und die Hasen-/Katzenohren wandern entsprechend mit). Eine Live-Vorschau dreht den Roboter einmal pro Sekunde, damit du den Hut aus jedem Winkel siehst. Hüte lassen sich für eigene Designs ebenfalls als JSON exportieren und importieren.

## Farbschemata

Ein **Farben**-Panel in der Spielseitenleiste zeigt die Palette: Kachelfarbe, Kachelkantenfarbe, Zielfarbe, leuchtende Zielfarbe, Hintergrund und Roboterkörper. Du kannst ein eingebautes Theme verwenden oder selbst anpassen.

## Sprachen

UI-Übersetzungen in 23 Sprachen: Englisch, Spanisch, Französisch, Deutsch, Italienisch, Portugiesisch, Russisch, Chinesisch, Japanisch, Koreanisch, Hindi, Bengali, Vietnamesisch, Arabisch (mit rechts-nach-links-Layout), Thailändisch, Tagalog, Norwegisch, Niederländisch, Schwedisch, Türkisch, Swahili, Indonesisch und Polnisch. Die Standardsprache folgt der `navigator.language` des Browsers; die Sprachauswahl auf dem Startbildschirm überschreibt sie für die Sitzung. Die Namen und Beschreibungen der eingebauten Level sowie die Namen der eingebauten Hüte sind in alle unterstützten Sprachen übersetzt. Der Level-Editor schreibt beim Bearbeiten eines Namens oder einer Beschreibung nur in den Slot der aktuell ausgewählten Sprache und lässt die anderen Übersetzungen unverändert.

## Hell- / Dunkelmodus

Folgt dem `prefers-color-scheme` des Browsers für die App-Oberfläche. Wenn du im Farben-Panel das Theme **Standard** wählst, wird die zum aktuellen Browsermodus passende Palette übernommen und bleibt synchron, wenn du den Modus umschaltest. Jedes andere eingebaute Theme — oder eine selbst angepasste Palette — überschreibt dieses Verhalten.

## Credits

Erstellt von Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspiriert von *Lightbot* von Daniel Yaroslavski.
