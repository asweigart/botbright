# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · **🇮🇩 Bahasa Indonesia** · [🇵🇱 Polski](index_pl.md)

---

Botbright adalah klon JavaScript satu berkas dari game teka-teki Flash *Lightbot*. Programkan robot isometrik untuk berjalan di kisi ubin 3D dan menyalakan ubin tujuan biru. Seret ubin instruksi ke memori robot, tekan **Jalankan**, dan saksikan programmu berjalan.

Seluruh game ada di satu berkas HTML (`botbright.html`) dengan CSS dan JavaScript inline — tanpa langkah build, tanpa dependensi eksternal, tanpa panggilan jaringan. Buka berkas di browser modern mana pun dan mainkan. Simpan ke hard drive dan game tetap berjalan offline selamanya.

Kamu juga bisa mengganti skema warna dan memakaikan robotmu berbagai topi. Ada editor level bawaan, dan level serta topi bisa diimpor atau diekspor dalam format JSON.

## Main

Cukup klik dua kali berkas botbright.html atau buka di browser. Game ini berjalan offline.

Versi langsung: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Cara kerjanya

Robot punya tiga area memori:

- **Memori Utama** — 12 slot instruksi, dijalankan saat kamu menekan Jalankan
- **Memori F1** — 8 slot instruksi, sebuah fungsi yang dapat dipanggil
- **Memori F2** — 8 slot instruksi, fungsi kedua yang dapat dipanggil

Seret ubin instruksi dari palet ke memori. Susun ulang dengan menyeret antar slot. Seret ubin keluar dari slot untuk menghapusnya.

| Instruksi | Yang dilakukan |
|-------------|------------|
| Maju | Melangkah ke ubin di depan, jika tingginya sama |
| Belok kiri | Berputar 90° berlawanan arah jarum jam |
| Belok kanan | Berputar 90° searah jarum jam |
| Lompat | Lompat naik satu tingkat, atau lompat turun berapa pun tingkatnya |
| Nyalakan | Mengubah status ubin tujuan di bawah robot |
| Panggil F1 / F2 | Mendorong fungsi tersebut ke tumpukan panggilan (rekursi diizinkan, dengan batas) |

Level selesai ketika setiap ubin tujuan menyala kuning.

Program yang berjalan terlalu lama dihentikan: maksimal 1000 instruksi total, maksimal 100 bingkai tumpukan panggilan.

## Kontrol

**Kamera** — WASD atau tombol panah untuk pan, Q/E atau PageUp/PageDown untuk berputar 90°, +/− atau roda gulir untuk zoom. Tekan 0 untuk mereset tampilan. Seret kanvas untuk pan, cubit untuk zoom, putar dengan dua jari untuk berotasi. Tekan dan tahan tombol kamera di layar untuk gerakan mulus berkelanjutan.

**Lebar bilah sisi** — seret pemisah antara kanvas dan bilah sisi.

**Kecepatan** — penggeser di bilah sisi: lambat / normal / cepat. Bisa disesuaikan saat berjalan.

## Editor Level

Editor lengkap disertakan dalam game. Tambah/duplikasi/hapus level, ubah ukuran grid (1–32 di setiap dimensi), tatah ketinggian 0–9, tandai ubin tujuan, atur posisi dan arah awal, dan uji main tanpa keluar dari editor.

Seluruh set level diekspor sebagai JSON dan diimpor dengan cara yang sama, sehingga kamu bisa berbagi level atau membackup perubahan.

## Editor Topi

Robot bisa memakai topi. Ada sembilan belas opsi bawaan: Tidak ada, Topi Tinggi, Topi Penyihir, Mahkota, Topi Kupluk, Topi Bisbol, Topi Koboi, Topi Pesta, Topi Bowler, Halo, Tanduk Iblis, Sombrero, Topi Penyihir Wanita, Fez, Tanduk Rusa, Telinga Kelinci, Telinga Kucing, Helm Selam, dan Helm Viking. Setiap topi didefinisikan dengan empat sprite SVG — satu per arah relatif layar — sehingga topi mengikuti arah robot di setiap rotasi kamera (visor topi bisbol, gesper topi penyihir wanita, jendela helm selam, dan bagian dalam telinga kelinci/kucing juga ikut bergeser). Pratinjau langsung memutar robot sekali per detik supaya kamu bisa melihat topi dari segala sudut. Topi juga bisa diekspor dan diimpor sebagai JSON untuk desain kustom.

## Skema Warna

Panel **Warna** di bilah sisi game memunculkan palet: warna ubin, warna tepi ubin, warna tujuan, warna tujuan menyala, latar belakang, dan tubuh robot. Kamu bisa menggunakan tema bawaan atau menyuntingnya sendiri.

## Bahasa

Terjemahan antarmuka untuk 23 bahasa: Inggris, Spanyol, Prancis, Jerman, Italia, Portugis, Rusia, Tionghoa, Jepang, Korea, Hindi, Bengali, Vietnam, Arab (dengan tata letak kanan ke kiri), Thai, Tagalog, Norwegia, Belanda, Swedia, Turki, Swahili, Indonesia, dan Polandia. Bahasa default mengikuti `navigator.language` browser; pemilih bahasa di layar awal menggantinya selama sesi. Nama dan deskripsi level bawaan, serta nama topi bawaan, diterjemahkan ke semua bahasa yang didukung. Saat kamu mengubah nama atau deskripsi, editor level hanya menulis ke slot bahasa yang sedang dipilih, sehingga terjemahan bahasa lain tetap utuh.

## Mode Terang / Gelap

Mengikuti `prefers-color-scheme` browser untuk tampilan aplikasi. Memilih tema **Default** di panel Warna akan menerapkan palet yang cocok dengan mode browser saat ini, jadi tetap sinkron ketika kamu mengganti mode. Tema bawaan lain — atau palet kustom yang kamu setel via panel Warna — akan menggantikan perilaku ini.

## Kredit

Dibuat oleh Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Terinspirasi dari *Lightbot* karya Daniel Yaroslavski.
