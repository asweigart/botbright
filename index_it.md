# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · **🇮🇹 Italiano** · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Botbright è un clone in un solo file JavaScript del gioco rompicapo in Flash *Lightbot*. Programma un robot isometrico per camminare su una griglia di tessere 3D e accendere le tessere blu obiettivo. Trascina le tessere istruzione nella memoria del robot, premi **Esegui** e guarda il tuo programma in azione.

L'intero gioco è un singolo file HTML (`botbright.html`) con CSS e JavaScript inline — niente build, niente dipendenze esterne, niente chiamate di rete. Apri il file in un browser moderno e gioca. Salvalo sul disco rigido e continuerà a funzionare offline per sempre.

Puoi anche cambiare lo schema di colori e mettere cappelli diversi al tuo robot. C'è un editor di livelli integrato, e livelli e cappelli si possono importare ed esportare in formato JSON.

## Gioca

Basta fare doppio clic sul file botbright.html o aprirlo nel browser. Il gioco funziona offline.

Versione online: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Come funziona

Il robot ha tre aree di memoria:

- **Memoria principale** — 12 slot di istruzioni, viene eseguita quando premi Esegui
- **Memoria F1** — 8 slot di istruzioni, una funzione richiamabile
- **Memoria F2** — 8 slot di istruzioni, una seconda funzione richiamabile

Trascina le tessere istruzione dalla palette nella memoria. Riordinale trascinandole tra gli slot. Trascina una tessera fuori da uno slot per eliminarla.

| Istruzione | Cosa fa |
|-------------|------------|
| Avanti | Sale sulla tessera davanti, se è alla stessa altezza |
| Gira a sinistra | Ruota di 90° in senso antiorario |
| Gira a destra | Ruota di 90° in senso orario |
| Salta | Salta su di un livello o scende di un numero qualunque di livelli |
| Illumina | Attiva/disattiva la tessera obiettivo sotto il robot |
| Chiama F1 / F2 | Mette quella funzione sullo stack di chiamata (ricorsione permessa, con limiti) |

Un livello è completato quando tutte le tessere obiettivo sono accese in giallo.

I programmi che durano troppo vengono fermati: massimo 1000 istruzioni totali, massimo 100 frame nello stack di chiamata.

## Comandi

**Camera** — WASD o frecce per traslare, Q/E o PagSu/PagGiù per ruotare di 90°, +/− o rotella per lo zoom. Premi 0 per ripristinare la vista. Trascina la tela per traslare, pizzica per zoomare, ruota con due dita per girare. Tieni premuti i pulsanti camera sullo schermo per un movimento continuo e fluido.

**Larghezza della barra laterale** — trascina il divisorio tra la tela e la barra laterale.

**Velocità** — cursore nella barra laterale: lento / normale / veloce. Regolabile durante l'esecuzione.

## Editor di livelli

Un editor completo è incluso nel gioco. Aggiungi/duplica/elimina livelli, ridimensiona la griglia (1–32 in ogni dimensione), dipingi altezze 0–9, segna le tessere obiettivo, imposta posizione e direzione iniziali e prova il livello senza uscire dall'editor.

L'intero set di livelli si esporta come JSON e si importa nello stesso modo, così puoi condividere livelli o fare backup delle modifiche.

## Editor di cappelli

Il robot può indossare cappelli. Sono incluse diciannove opzioni: Nessuno, Cilindro, Cappello da mago, Corona, Berretto, Berretto da baseball, Cappello da cowboy, Cappellino da festa, Bombetta, Aureola, Corna del diavolo, Sombrero, Cappello da strega, Fez, Palchi, Orecchie da coniglio, Orecchie da gatto, Casco da palombaro ed Elmo vichingo. Ogni cappello è definito da quattro sprite SVG — uno per ogni orientamento sullo schermo — così segue la direzione del robot in tutte le rotazioni della camera (la visiera del berretto da baseball, la fibbia del cappello da strega, l'oblò del casco da palombaro e le orecchie di coniglio/gatto si spostano di conseguenza). Un'anteprima dal vivo fa ruotare il robot una volta al secondo per vedere il cappello da ogni angolazione. I cappelli si esportano e si importano anch'essi come JSON per design personalizzati.

## Schemi di colore

Un pannello **Colori** nella barra laterale del gioco espone la palette: colore tessere, colore del bordo delle tessere, colore obiettivo, colore obiettivo acceso, sfondo e corpo del robot. Puoi usare un tema integrato o modificarli da te.

## Lingue

Traduzioni dell'interfaccia in 23 lingue: inglese, spagnolo, francese, tedesco, italiano, portoghese, russo, cinese, giapponese, coreano, hindi, bengali, vietnamita, arabo (con layout da destra a sinistra), thai, tagalog, norvegese, olandese, svedese, turco, swahili, indonesiano e polacco. La lingua predefinita segue `navigator.language` del browser; il selettore di lingua nella schermata iniziale lo sovrascrive per la sessione. I nomi e le descrizioni dei livelli integrati, e i nomi dei cappelli integrati, sono tradotti in tutte le lingue supportate. L'editor di livelli scrive solo nello slot della lingua attualmente selezionata quando modifichi un nome o una descrizione, lasciando intatte le altre traduzioni.

## Modalità chiara / scura

Segue `prefers-color-scheme` del browser per l'interfaccia. Selezionando il tema **Predefinito** nel pannello Colori si applica la palette corrispondente alla modalità corrente del browser, e resta sincronizzata se cambi modalità. Qualunque altro tema integrato — o una palette personalizzata — sovrascrive questo comportamento.

## Crediti

Creato da Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Ispirato a *Lightbot* di Daniel Yaroslavski.
