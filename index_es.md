# Botbright

[🇬🇧 English](index.md) · **🇪🇸 Español** · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Botbright es un clon de un solo archivo en JavaScript del juego de puzles en Flash *Lightbot*. Programa un robot isométrico para que recorra una cuadrícula 3D de baldosas e ilumine las baldosas azules de meta. Arrastra fichas de instrucción a la memoria del robot, pulsa **Ejecutar** y observa cómo se ejecuta tu programa.

Todo el juego es un único archivo HTML (`botbright.html`) con CSS y JavaScript en línea: sin compilación, sin dependencias externas, sin llamadas de red. Abre el archivo en cualquier navegador moderno y juega. Guárdalo en tu disco duro y seguirá funcionando sin conexión para siempre.

También puedes cambiar el esquema de colores y ponerle distintos sombreros al robot. Incluye un editor de niveles integrado, y los niveles y los sombreros se pueden importar o exportar en formato JSON.

## Jugar

Solo haz doble clic en el archivo botbright.html o ábrelo en tu navegador. El juego funciona sin conexión.

Versión en línea: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Cómo funciona

El robot tiene tres áreas de memoria:

- **Memoria principal** — 12 ranuras de instrucciones, se ejecuta al pulsar Ejecutar
- **Memoria F1** — 8 ranuras de instrucciones, una función reutilizable
- **Memoria F2** — 8 ranuras de instrucciones, una segunda función reutilizable

Arrastra fichas de instrucción desde la paleta a la memoria. Reordénalas arrastrándolas entre ranuras. Arrastra una ficha fuera de cualquier ranura para borrarla.

| Instrucción | Qué hace |
|-------------|------------|
| Avanzar | Pisa la baldosa de delante, si está a la misma altura |
| Girar a la izquierda | Rota 90° en sentido antihorario |
| Girar a la derecha | Rota 90° en sentido horario |
| Saltar | Sube un nivel o baja cualquier número de niveles |
| Iluminar | Alterna la baldosa de meta bajo el robot |
| Llamar F1 / F2 | Apila esa función en la pila de llamadas (se permite recursión, con límites) |

Un nivel se completa cuando todas las baldosas de meta están iluminadas en amarillo.

Los programas que se prolongan demasiado se detienen: máximo 1000 instrucciones totales, máximo 100 marcos en la pila de llamadas.

## Controles

**Cámara** — WASD o flechas para desplazar, Q/E o RePág/AvPág para rotar 90°, +/− o la rueda del ratón para hacer zoom. Pulsa 0 para restablecer la vista. Arrastra el lienzo para desplazarlo, pellizca para hacer zoom, gira con dos dedos para rotar. Mantén pulsados los botones de cámara en pantalla para un movimiento continuo y suave.

**Ancho de la barra lateral** — arrastra el divisor entre el lienzo y la barra lateral.

**Velocidad** — control deslizante en la barra lateral: lento / normal / rápido. Ajustable durante la ejecución.

## Editor de niveles

Un editor completo viene incluido con el juego. Añade/duplica/elimina niveles, cambia el tamaño de la cuadrícula (1–32 en cada dimensión), pinta alturas de 0 a 9, marca baldosas de meta, fija la posición y orientación iniciales, y prueba el nivel sin salir del editor.

El conjunto completo de niveles se exporta como JSON y se importa de la misma forma, para compartir niveles o hacer copias de seguridad.

## Editor de sombreros

El robot puede llevar sombreros. Incluye diecinueve opciones: Ninguno, Sombrero de copa, Sombrero de mago, Corona, Gorro, Gorra, Sombrero de vaquero, Gorro de fiesta, Bombín, Aureola, Cuernos de diablo, Sombrero, Sombrero de bruja, Fez, Cuernos, Orejas de conejo, Orejas de gato, Casco de buzo y Casco vikingo. Cada sombrero se define con cuatro sprites SVG —uno por cada orientación relativa a la pantalla— para que siga la dirección del robot en cualquier rotación de la cámara (la visera de la gorra, la hebilla del sombrero de bruja, el portillo del casco de buzo y las orejas de conejo/gato se desplazan según corresponda). Una vista previa en vivo gira al robot una vez por segundo para que veas el sombrero desde todos los ángulos. Los sombreros también se exportan e importan como JSON para diseños personalizados.

## Esquemas de color

Un panel **Colores** en la barra lateral del juego expone la paleta: color de baldosa, color del borde de la baldosa, color de meta, color de meta iluminada, fondo y cuerpo del robot. Puedes usar un tema integrado o editarlos tú mismo.

## Idiomas

Traducciones de la interfaz a 23 idiomas: inglés, español, francés, alemán, italiano, portugués, ruso, chino, japonés, coreano, hindi, bengalí, vietnamita, árabe (con diseño de derecha a izquierda), tailandés, tagalo, noruego, neerlandés, sueco, turco, suajili, indonesio y polaco. El idioma por defecto sigue al `navigator.language` del navegador; el selector de idioma en la pantalla de inicio lo anula durante la sesión. Los nombres y descripciones de los niveles integrados, así como los nombres de los sombreros integrados, están traducidos a todos los idiomas. El editor de niveles solo escribe en la ranura del idioma seleccionado al editar un nombre o descripción, dejando intactas las demás traducciones.

## Modo claro / oscuro

Sigue el `prefers-color-scheme` del navegador para la interfaz de la app. Al seleccionar el tema **Predeterminado** en el panel de Colores se aplica la paleta correspondiente al modo actual del navegador, de modo que se mantiene sincronizado si cambias de modo. Cualquier otro tema integrado —o una paleta personalizada— anula este comportamiento.

## Créditos

Creado por Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspirado en *Lightbot* de Daniel Yaroslavski.
