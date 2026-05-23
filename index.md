# Botbright

**🇬🇧 English** · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright is a single-file JavaScript clone of the Flash puzzle game *Lightbot*. Program an isometric robot to walk a 3D-tile grid and light up the blue goal tiles. Drag instruction tiles into the bot's memory, press **Run**, and watch your program execute.

The entire game is one HTML file (`botbright.html`) with inline CSS and JavaScript — no build step, no external dependencies, no network calls. Open the file in any modern browser and play. Save it to your hard drive and it keeps working offline forever.

You can also change the color scheme and give your bot different hats to wear. There is a built-in level editor, and levels and hats can be imported or exported to a JSON format.

## Play

Just double-click the botbright.html file or open it in your web browser. The game works offline.

Live version: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## How it works

The bot has three memory areas:

- **Main Memory** — 12 instruction slots, runs when you press Run
- **F1 Memory** — 8 instruction slots, a callable function
- **F2 Memory** — 8 instruction slots, a second callable function

Drag instruction tiles from the palette into memory. Reorder by dragging between slots. Drag a tile off any slot to delete it.

| Instruction | What it does |
|-------------|------------|
| Forward | Step onto the tile in front, if it's the same height |
| Turn Left | Rotate 90° counter-clockwise |
| Turn Right | Rotate 90° clockwise |
| Jump | Hop up one level, or hop down any number of levels |
| Light | Toggle the goal tile under the bot |
| Call F1 / F2 | Push that function onto the call stack (recursion allowed, with limits) |

A level is complete when every goal tile is lit yellow.

Programs that run too long are halted: max 1000 total instructions, max 100 call-stack frames.

## Controls

**Camera** — WASD or arrow keys to pan, Q/E or PageUp/PageDown to rotate 90°, +/− or scroll wheel to zoom. Press the 0 key to reset the view. Drag the canvas to pan, pinch to zoom, twist with two fingers to rotate. Click-and-hold the on-screen camera buttons for smooth continuous motion.

**Sidebar width** — drag the divider between the canvas and the sidebar.

**Speed** — slider in the sidebar: slow / normal / fast. Adjustable while running.

## Level Editor

A full editor ships with the game. Add/duplicate/delete levels, resize the grid (1–32 in each dimension), paint heights 0–9, mark goal tiles, set the start position and facing, and test-play without leaving the editor.

The complete level set exports as JSON and imports the same way, so you can share levels or back up edits.

## Hats Editor

The bot can wear hats. Ships with nineteen options: None, Top Hat, Wizard Hat, Crown, Beanie, Baseball Cap, Cowboy Hat, Party Hat, Bowler, Halo, Devil Horns, Sombrero, Witch Hat, Fez, Antlers, Bunny Ears, Cat Ears, Diving Helmet, and Viking Helmet. Each hat is defined by four SVG sprites — one per screen-relative facing — so the hat tracks the bot's direction across all camera rotations (the baseball cap's visor, the witch hat's buckle, the diving helmet's porthole, and the bunny/cat ears all shift accordingly). A live preview rotates the bot once per second so you can see how the hat looks from every angle. Hats also export and import as JSON for custom designs.

## Color Schemes

A **Colors** panel in the game sidebar exposes the palette: tile color, tile edge color, goal color, lit goal color, background, and robot body. You can use a built-in color theme or edit them yourself.

## Languages

UI translations for 23 languages: English, Spanish, French, German, Italian, Portuguese, Russian, Chinese, Japanese, Korean, Hindi, Bengali, Vietnamese, Arabic (with right-to-left layout), Thai, Tagalog, Norwegian, Dutch, Swedish, Turkish, Swahili, Indonesian, and Polish. The default language follows the browser's `navigator.language`; the language selector on the start screen overrides it for the session. Built-in level names and descriptions, and built-in hat names, are translated across all supported languages. The level editor writes only to the currently-selected language's slot when you edit a name or description, leaving the other language translations untouched.

## Light / Dark Mode

Follows the browser's `prefers-color-scheme` for the app chrome. Selecting the **Default** theme in the Colors panel applies whichever palette matches the browser's current scheme, so it stays in sync if you toggle modes. Any other built-in theme — or a custom palette you tweak via the Colors panel — overrides this.

## Credit

Generated by Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspired by *Lightbot* by Daniel Yaroslavski.
