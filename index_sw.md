# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · **🇰🇪 Kiswahili** · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright ni nakala ya JavaScript ya faili moja ya mchezo wa Flash wa mafumbo *Lightbot*. Programu roboti ya mtazamo wa isometriki itembee kwenye gridi ya vigae vya 3D na kuwasha vigae vya buluu vya lengo. Buruta vigae vya maagizo ndani ya kumbukumbu ya roboti, bonyeza **Endesha**, na utazame programu yako ikitekeleza.

Mchezo wote ni faili moja ya HTML (`botbright.html`) yenye CSS na JavaScript zilizopachikwa — hakuna hatua ya kujenga, hakuna utegemezi wa nje, hakuna miito ya mtandao. Fungua faili katika kivinjari chochote cha kisasa na ucheze. Ihifadhi kwenye diski yako kuu na itaendelea kufanya kazi nje ya mtandao milele.

Unaweza pia kubadilisha mpangilio wa rangi na kumvalisha roboti yako kofia tofauti. Kuna kihariri cha ngazi kilichojengwa ndani, na ngazi pamoja na kofia zinaweza kuingizwa au kutolewa katika muundo wa JSON.

## Cheza

Bofya mara mbili faili ya botbright.html au ifungue kwenye kivinjari chako. Mchezo unafanya kazi nje ya mtandao.

Toleo la moja kwa moja: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Jinsi inavyofanya kazi

Roboti ina maeneo matatu ya kumbukumbu:

- **Kumbukumbu Kuu** — nafasi 12 za maagizo, hutekelezwa unapobonyeza Endesha
- **Kumbukumbu ya F1** — nafasi 8 za maagizo, kifaa kinachoweza kuitwa
- **Kumbukumbu ya F2** — nafasi 8 za maagizo, kifaa cha pili kinachoweza kuitwa

Buruta vigae vya maagizo kutoka kwenye paleti hadi kwenye kumbukumbu. Panga upya kwa kuvuta kati ya nafasi. Buruta kigae nje ya nafasi ili kukifuta.

| Agizo | Linafanya nini |
|-------------|------------|
| Mbele | Pita kwenye kigae cha mbele, ikiwa kiko kwenye urefu uleule |
| Geuka kushoto | Hugeuka 90° kinyume cha saa |
| Geuka kulia | Hugeuka 90° kufuata saa |
| Ruka | Ruka juu ngazi moja, au ushuke ngazi nyingi kadiri unavyotaka |
| Washa | Hubadilisha kigae cha lengo chini ya roboti |
| Ita F1 / F2 | Huingiza kifaa hicho kwenye rundo la miito (urejeshi unaruhusiwa, kwa mipaka) |

Ngazi imekamilika wakati kila kigae cha lengo kinawaka rangi ya manjano.

Programu zinazokimbia kwa muda mrefu zinazuiliwa: kiwango cha juu cha maagizo 1000 jumla, kiwango cha juu cha fremu 100 kwenye rundo la miito.

## Vidhibiti

**Kamera** — WASD au funguo za mishale kwa kuhamia, Q/E au PageUp/PageDown kwa kuzungusha 90°, +/− au gurudumu la kusongesha kwa kuvuta karibu/mbali. Bonyeza 0 kurudisha mwonekano. Buruta turubai kuhamisha, banana ili kuvuta karibu, zungusha kwa vidole viwili ili kuzungusha. Bonyeza na ushikilie vifungo vya kamera vya skrini kwa mwendo laini wa kuendelea.

**Upana wa upau wa kando** — buruta kigawanyiko kati ya turubai na upau wa kando.

**Kasi** — kitelezi kwenye upau wa kando: polepole / kawaida / haraka. Kinaweza kubadilishwa wakati wa kukimbia.

## Mhariri wa Ngazi

Mchezo unakuja na mhariri kamili. Ongeza/nakili/futa ngazi, badilisha ukubwa wa gridi (1–32 kila upande), paka urefu 0–9, weka alama vigae vya lengo, weka nafasi ya kuanzia na mwelekeo, na ujaribu kucheza bila kuondoka kwenye mhariri.

Seti nzima ya ngazi inatolewa kama JSON na kuingizwa kwa njia ile ile, ili uweze kushiriki ngazi au kuhifadhi nakala za mabadiliko.

## Mhariri wa Kofia

Roboti inaweza kuvaa kofia. Inakuja na chaguo kumi na tisa: Hakuna, Kofia ya juu, Kofia ya Mchawi, Taji, Kofia ya kuvuta, Kofia ya Besiboli, Kofia ya Mfugaji, Kofia ya Sherehe, Kofia ya Bowler, Halo, Pembe za Shetani, Sombrero, Kofia ya Mchawi mke, Fez, Pembe za Kulungu, Masikio ya Sungura, Masikio ya Paka, Kofia ya Mzamiaji, na Kofia ya Viking. Kila kofia inafafanuliwa na sprite nne za SVG — moja kwa kila mwelekeo unaohusiana na skrini — ili kofia ifuate mwelekeo wa roboti katika mizunguko yote ya kamera (kingo ya kofia ya besiboli, kifungo cha kofia ya mchawi mke, dirisha la kofia ya mzamiaji, na sehemu za ndani za masikio ya sungura/paka pia huhama ipasavyo). Onyesho la moja kwa moja huizungusha roboti mara moja kila sekunde ili uone kofia kutoka kila pembe. Kofia pia zinaweza kutolewa na kuingizwa kama JSON kwa miundo ya kibinafsi.

## Mipangilio ya Rangi

Paneli ya **Rangi** kwenye upau wa kando wa mchezo inafichua paleti: rangi ya kigae, rangi ya ukingo wa kigae, rangi ya lengo, rangi ya lengo iliyowashwa, mandharinyuma, na mwili wa roboti. Unaweza kutumia mandhari iliyojengwa ndani au kuihariri mwenyewe.

## Lugha

Tafsiri za UI katika lugha 23: Kiingereza, Kihispania, Kifaransa, Kijerumani, Kiitaliano, Kireno, Kirusi, Kichina, Kijapani, Kikorea, Kihindi, Kibengali, Kivietinamu, Kiarabu (mpangilio wa kulia kwenda kushoto), Kithai, Kitagalogi, Kinorwe, Kiholanzi, Kiswidi, Kituruki, Kiswahili, Kiindonesia, na Kipolandi. Lugha chaguo-msingi hufuata `navigator.language` ya kivinjari; kichaguzi cha lugha kwenye skrini ya kuanzia kinaibadilisha katika kipindi cha matumizi. Majina na maelezo ya ngazi zilizojengwa ndani, pamoja na majina ya kofia zilizojengwa ndani, yametafsiriwa katika lugha zote zinazoungwa mkono. Mhariri wa ngazi anaandika tu kwenye nafasi ya lugha iliyochaguliwa sasa unapohariri jina au maelezo, akiacha tafsiri za lugha nyingine bila kuguswa.

## Hali ya Mwangaza / Giza

Hufuata `prefers-color-scheme` ya kivinjari kwa muundo wa programu. Kuchagua mandhari ya **Chaguo-msingi** kwenye paneli ya Rangi hutekeleza paleti inayolingana na hali ya sasa ya kivinjari, hivyo inabaki ikilingana ukibadilisha hali. Mandhari nyingine yoyote iliyojengwa ndani — au paleti ya kibinafsi unayoirekebisha kupitia paneli ya Rangi — hubadilisha tabia hii.

## Sifa

Imetengenezwa na Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Imechochewa na *Lightbot* ya Daniel Yaroslavski.
