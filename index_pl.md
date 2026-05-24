# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · **🇵🇱 Polski** · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Botbright to klon w jednym pliku JavaScript flashowej gry logicznej *Lightbot*. Zaprogramuj izometrycznego robota tak, by przemieszczał się po siatce kafelków 3D i zapalał niebieskie kafelki celu. Przeciągaj kafelki instrukcji do pamięci robota, naciśnij **Uruchom** i obserwuj, jak Twój program się wykonuje.

Cała gra to jeden plik HTML (`botbright.html`) z osadzonymi CSS i JavaScriptem — bez kroku budowania, bez zewnętrznych zależności, bez wywołań sieciowych. Otwórz plik w dowolnej nowoczesnej przeglądarce i graj. Zapisz go na dysku twardym, a będzie działać offline na zawsze.

Możesz też zmieniać paletę kolorów i zakładać robotowi różne czapki. Wbudowany jest edytor poziomów, a poziomy i czapki można importować i eksportować w formacie JSON.

## Grać

Wystarczy kliknąć dwukrotnie plik botbright.html lub otworzyć go w przeglądarce. Gra działa offline.

Wersja online: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Jak to działa

Robot ma trzy obszary pamięci:

- **Pamięć główna** — 12 slotów na polecenia, uruchamia się po naciśnięciu Uruchom
- **Pamięć F1** — 8 slotów na polecenia, wywoływalna funkcja
- **Pamięć F2** — 8 slotów na polecenia, druga wywoływalna funkcja

Przeciągaj kafelki poleceń z palety do pamięci. Zmieniaj kolejność, przeciągając między slotami. Wyciągnij kafelek poza slot, aby go usunąć.

| Polecenie | Co robi |
|-------------|------------|
| Naprzód | Wejdź na kafelek z przodu, jeśli jest na tej samej wysokości |
| Skręć w lewo | Obrót o 90° w lewo (przeciwnie do ruchu wskazówek) |
| Skręć w prawo | Obrót o 90° w prawo (zgodnie z ruchem wskazówek) |
| Skocz | Wskocz jeden poziom wyżej lub zeskocz dowolną liczbę poziomów niżej |
| Zaświeć | Przełącza kafelek celu pod robotem |
| Wywołaj F1 / F2 | Odkłada tę funkcję na stos wywołań (rekurencja dozwolona, w ramach limitów) |

Poziom kończy się, gdy każdy kafelek celu zaświeci się na żółto.

Programy działające zbyt długo są zatrzymywane: maks. 1000 instrukcji łącznie, maks. 100 ramek na stosie wywołań.

## Sterowanie

**Kamera** — WASD lub strzałki do przesuwania, Q/E lub PageUp/PageDown do obrotu o 90°, +/− lub kółko myszy do powiększania. Naciśnij 0, aby zresetować widok. Przeciągaj kanwę, by przesuwać, ściskaj dwoma palcami, by przybliżać, obracaj dwoma palcami, by obrócić. Przytrzymaj ekranowe przyciski kamery, aby uzyskać płynny ciągły ruch.

**Szerokość paska bocznego** — przeciągnij separator między kanwą a paskiem bocznym.

**Prędkość** — suwak w pasku bocznym: wolno / normalnie / szybko. Można zmieniać podczas wykonywania.

## Edytor poziomów

Z grą dostarczany jest pełny edytor. Dodawaj/duplikuj/usuwaj poziomy, zmieniaj rozmiar siatki (1–32 w każdym wymiarze), maluj wysokości 0–9, oznaczaj kafelki celu, ustalaj pozycję i kierunek startu i testuj rozgrywkę bez wychodzenia z edytora.

Cały zestaw poziomów eksportuje się jako JSON i tak samo importuje, dzięki czemu możesz dzielić się poziomami albo zachowywać kopie zapasowe edycji.

## Edytor czapek

Robot może nosić czapki. W zestawie znajduje się dziewiętnaście opcji: Brak, Cylinder, Kapelusz czarodzieja, Korona, Czapka, Czapka z daszkiem, Kapelusz kowbojski, Czapka imprezowa, Melonik, Aureola, Diabelskie rogi, Sombrero, Kapelusz wiedźmy, Fez, Poroże, Króliczy uszy, Kocie uszy, Hełm nurka i Hełm wikinga. Każda czapka jest opisana czterema spritami SVG — po jednym na każdy kierunek względem ekranu — dzięki czemu czapka podąża za kierunkiem robota przy wszystkich obrotach kamery (daszek czapki bejsbolowej, sprzączka kapelusza wiedźmy, okienko hełmu nurka oraz wnętrze króliczych/kocich uszu odpowiednio się przesuwają). Podgląd na żywo obraca robota raz na sekundę, dzięki czemu widzisz czapkę pod każdym kątem. Czapki też można eksportować i importować jako JSON, na potrzeby własnych projektów.

## Schematy kolorów

Panel **Kolory** w pasku bocznym gry udostępnia paletę: kolor kafelka, kolor krawędzi kafelka, kolor celu, kolor zaświeconego celu, tło i ciało robota. Możesz wybrać wbudowany motyw albo edytować kolory samodzielnie.

## Języki

Tłumaczenia interfejsu na 23 języki: angielski, hiszpański, francuski, niemiecki, włoski, portugalski, rosyjski, chiński, japoński, koreański, hindi, bengalski, wietnamski, arabski (z układem od prawej do lewej), tajski, tagalog, norweski, niderlandzki, szwedzki, turecki, suahili, indonezyjski i polski. Domyślny język wynika z `navigator.language` przeglądarki; selektor języka na ekranie startowym nadpisuje go na czas sesji. Nazwy i opisy wbudowanych poziomów oraz nazwy wbudowanych czapek są przetłumaczone na wszystkie obsługiwane języki. Edytor poziomów przy zmianie nazwy lub opisu zapisuje wyłącznie do slotu bieżącego języka, pozostawiając tłumaczenia w innych językach nietknięte.

## Tryb jasny / ciemny

Otoczka aplikacji podąża za ustawieniem `prefers-color-scheme` przeglądarki. Wybór motywu **Domyślny** w panelu Kolory zastosuje paletę pasującą do bieżącego trybu przeglądarki, dzięki czemu pozostaje zsynchronizowany przy przełączaniu trybu. Każdy inny wbudowany motyw — lub własna paleta dostosowana w panelu Kolory — nadpisuje to zachowanie.

## Autorzy

Utworzone przez Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Zainspirowane *Lightbot* autorstwa Daniela Yaroslavskiego.
