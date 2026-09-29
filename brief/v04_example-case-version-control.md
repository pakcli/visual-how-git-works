# Brief v04: Katalog Skenario & Prompt Visualisasi Version Control Berjenjang (3 Level Intuisi)

Dokumen ini berisi spesifikasi skenario analogi bertingkat (*Tiered Analogies*) yang dirancang untuk membangun pemahaman konsep *Version Control System* (Git) secara bertahap:
1. **Level 1: Awam General** (5 Langkah Sederhana) — Menggunakan metafora fisik sehari-hari.
2. **Level 2: Teknik Non-IT** (6 Langkah Sederhana) — Menggunakan metafora rekayasa mekanik, otomotif, dan ekosistem perangkat keras/firmware.
3. **Level 3: Calon Pengembang Software / Game Dev** (7 Langkah Agak Kompleks) — Menggunakan studi kasus pengembangan 6 game populer (GTA 6, FIFA, UFC, Minecraft, PvZ, Granny).

Setiap skenario disajikan dalam format tabel interaktif dengan 5 kolom standar:
- **No**: Nomor urutan langkah.
- **Nama Step**: Nama tindakan analogi beserta deskripsi konteks skenarionya.
- **Git Example Syntax**: Contoh sintaks perintah Git nyata siap eksekusi di terminal.
- **Git Example Syntax Name**: Nama teknis resmi dari operasi Git tersebut.
- **Visualisasi Prompt**: Panduan detail untuk animator / komponen SVG canvas / generator visual.

---

# LEVEL 1: AWAM GENERAL (5 Step Simple)
*Ditujukan untuk pengguna non-teknis tanpa latar belakang komputer sama sekali.*

---

### Kasus 1.1: Dekorasi & Pengecatan Pagar Rumah
> **Tujuan Mental Model:** Memahami bahwa commit adalah lapisan cat permanen, branch adalah mencoba warna di satu panel terpisah, dan revert/restore adalah menimpa cat baru tanpa merusak pondasi pagar.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Cat Dasar Abu-abu**<br>Pagar besi baru dipasang dan dilapisi cat dasar anti-karat warna abu-abu sebagai fondasi awal yang aman. | `git init`<br>`git commit -m "feat: cat dasar abu-abu anti-karat"` | **Repository Init & Initial Commit** | Ilustrasi 2D flat minimalis: Pagar besi polos berubah menjadi warna abu-abu matte dengan cap stempel hijau bertuliskan *"Versi 1: Cat Dasar"*. Muncul ikon gembok kecil di sudut tiang pagar. |
| **2** | **Cat Utama Hijau Daun**<br>Di atas cat dasar, seluruh pagar dilapisi warna hijau daun segar. Riwayat warna abu-abu kemarin tetap tersimpan di buku riwayat. | `git commit -am "feat: lapis cat utama warna hijau daun"` | **Linear Working Commit** | Kuas besar meluncur dari kiri ke kanan mengubah pagar abu-abu menjadi hijau daun segar. Di bawah pagar muncul diagram lingkaran simpul A terhubung garis ke simpul B (Hijau). |
| **3** | **Coba Motif Garis Kuning di Panel Kanan**<br>Tetangga menyarankan motif garis kuning. Agar tidak merusak pagar hijau, kita hanya mencobanya pada 1 panel ujung terpisah. | `git checkout -b motif-kuning` | **Branch Creation & Switch** | Pagar terbagi dua: sisi kiri tetap hijau utuh (main branch), sisi kanan memiliki panel melayang terpisah dengan pita pembatas sedang dicat garis-garis kuning zig-zag yang cerah. |
| **4** | **Motif Dinilai Jelek & Dibatalkan**<br>Setelah dilihat dari jalan, garis kuning terlalu mencolok. Panel uji coba dibuang dan kita kembali ke pagar hijau asli tanpa noda. | `git checkout main`<br>`git branch -D motif-kuning` | **Branch Discard / Hard Deletion** | Panel uji coba garis kuning memudar dan terlipat menjadi partikel abu-abu lalu hilang (poof effect). Kamera kembali fokus ke pagar hijau utama yang bersih dan kokoh. |
| **5** | **Beri Lapisan Kilap Pelindung Akhir**<br>Warna hijau daun disepakati keluarga. Kita beri pernis anti-gores dan gantungan plat nomor rumah sebagai versi final resmi. | `git tag -a v1.0 -m "release: pagar hijau selesai vernis"` | **Release Tagging** | Efek cahaya berkilau (sparkle animation) menyapu seluruh pagar hijau. Gantungan plat nomor rumah bertuliskan *"No. 10 - FINAL"* terpasang mantap di tiang gerbang. |

---

### Kasus 1.2: Penulisan Skripsi / Dokumen Karya Ilmiah Mahasiswa
> **Tujuan Mental Model:** Memahami mengapa menamai file `skripsi_final_revisi_fix_bismillah.docx` adalah bencana, dan bagaimana Git menggantikannya dengan satu file tunggal yang memiliki mesin waktu.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Bab 1 Latar Belakang Selesai**<br>Menyelesaikan draf Bab 1 tanpa membuat duplikasi nama file baru; disimpan sebagai titik riwayat pertama. | `git init`<br>`git commit -m "docs: bab 1 latar belakang"` | **Repository Init & Initial Commit** | Tumpukan map binder rapi di atas meja. Dokumen kertas berjudul *"Bab 1: Latar Belakang"* diberi stempel tanggal otomatis dengan tanda centang biru menyala di pojok kanan atas. |
| **2** | **Menambahkan Data Kuesioner Bab 2**<br>Memasukkan tabel data survei 100 responden ke dalam naskah sebagai perkembangan kedua. | `git commit -am "docs: bab 2 data kuesioner responden"` | **Working Commit** | Animasi teks dan grafik batang meluncur masuk ke dalam map binder yang sama. Muncul garis waktu di samping meja memperlihatkan titik simpul 1 terhubung ke titik simpul 2. |
| **3** | **Dosen Minta 2 Teori Berbeda**<br>Dosen meminta versi analisis teori kualitatif, sementara versi kuantitatif lama tidak boleh hilang. Dibuat draf jalur terpisah. | `git checkout -b opsi-teori-kualitatif` | **Feature Branching** | Map binder utama menduplikasi dirinya menjadi bayangan folder transparan berlabel warna oranye *"Cabang Eksperimen Teori B"*, sementara folder asli tetap tersimpan aman di rak. |
| **4** | **Revisi Coretan Merah Dosen**<br>Dosen mencoret 3 paragraf salah. Paragraf dihapus tanpa rasa takut karena teks asli kemarin masih tersimpan utuh di riwayat. | `git diff`<br>`git commit -am "refactor: hapus 3 paragraf teori usang"` | **File Diff Inspection & Commit** | Tampilan dokumen terbelah dua (*split-screen*): sisi kiri memperlihatkan baris teks merah tercoret (*deleted*), sisi kanan memperlihatkan paragraf baru berwarna hijau (*added*). |
| **5** | **Penggabungan Bab & Siap Cetak Sidang**<br>Dosen menyetujui teori baru. Cabang revisi disatukan kembali ke naskah utama dan disegel untuk pendaftaran sidang. | `git checkout main`<br>`git merge opsi-teori-kualitatif`<br>`git tag -a v1.0-sidang -m "naskah siap sidang"` | **Branch Merge & Milestone Tag** | Folder cabang oranye menyatu kembali secara mulus ke dalam binder utama. Muncul pita segel bertuliskan *"SIAP_SIDANG"* dengan stempel resmi universitas berwarna emas. |

---

# LEVEL 2: TEKNIK NON-IT (6 Step Simple)
*Ditujukan untuk praktisi teknik mekanik, elektronika, hardware, atau manufaktur yang memahami komponen fisik tetapi baru mengenal alur kerja Git.*

---

### Kasus 2.1: Servis Mesin, Modifikasi Balap, & Legalitas BPKB Mobil
> **Tujuan Mental Model:** Memahami commit log sebagai buku servis resmi, commit hash sebagai nomor rangka VIN, branch sebagai instalasi kit balap sementara, dan revert sebagai pengembalian ke spek standar pabrik.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Mobil Standar Keluar Pabrik (Spek OEM)**<br>Mobil keluar dari pabrik dengan Buku Manual resmi dan Nomor Rangka (VIN) unik tercatat di lembar pertama. | `git init`<br>`git commit -m "oem: baseline mesin standar pabrik vin-e1a49c"` | **Baseline Initial Commit** | Mesin mobil 4-silinder standar perakitan pabrik. Di sampingnya terdapat buku servis terbuka yang mencatat kode nomor rangka unik `VIN-e1a49c` dengan stempel *"OEM Spec"*. |
| **2** | **Servis Berkala 10.000 KM**<br>Mekanik mengganti oli sintetis dan filter udara. Catatan servis kedua dibubuhkan ke buku servis lengkap dengan kilometer tempuh. | `git commit -am "maint: ganti oli mesin 5w-30 dan filter udara km 10000"` | **Maintenance Commit** | Tangan montir menuangkan oli mesin baru berwarna emas. Di diagram riwayat, simpul rantai bertambah satu blok bertuliskan *"Oli Baru & Busi - KM 10.000"*. |
| **3** | **Pasang Paket Turbo di Bengkel Balap**<br>Pemilik ingin balap akhir pekan; mekanik memasang paket turbocharger plug-and-play di jalur pipa instalasi paralel tanpa membongkar mesin utama. | `git checkout -b modifikasi-stage2-turbo` | **Custom Modification Branch** | Diagram mesin menampilkan pipa intercooler dan keong turbo berwarna biru elektrik menyala yang mencabang keluar dari blok mesin utama dengan label *"Branch: Stage 2 Turbo"*. |
| **4** | **Mesin Mengalami Overheat saat Dyno Test**<br>Saat digas pol di atas mesin dyno, suhu radiator melonjak merah karena rasio kompresi terlalu ekstrem. Sensor ECU mendeteksi anomali. | `git status` | **Status / Anomaly Inspection** | Indikator tachometer bergetar di zona merah (*redline*), jarum suhu mesin melonjak ke tanda bahaya, dan muncul tanda seru kuning berkedip: *"Warning: Cylinder Head Overpressure!"*. |
| **5** | **Copot Turbo, Kembalikan ke Setelan Pabrik**<br>Demi keawetan mesin harian, turbo dilepas kembali. Mobil dikembalikan ke setelan injeksi standar pabrik seperti sebelum masuk dyno. | `git checkout main`<br>`git revert HEAD` | **Branch Switch & Safe Reversion** | Kit turbo terlepas secara mekanis dan kembali ke kotak spare part. Blok mesin kembali ke konfigurasi standar yang tenang dan stabil dengan status *"Kembali ke Spek Aman Pabrik"*. |
| **6** | **Penerbitan Bukti Uji Emisi & BPKB Sah**<br>Mobil dinyatakan lolos uji emisi standar jalan raya. Lembar administrasi BPKB dan STNK diperbarui dengan status mesin bersih dan sah. | `git tag -a v1.0-laik-jalan -m "legalitas bpkb sah lulus uji emisi"` | **Audit Trail Release Tag** | Lembar surat kendaraan BPKB resmi distempel segel hijau bertuliskan *"Lulus Uji Emisi & Laik Jalan"*, menunjuk langsung ke kondisi mesin standar yang reliabel. |

---

### Kasus 2.2: Versi Smartphone, Update Firmware, Hardware vs Aplikasi
> **Tujuan Mental Model:** Memahami relasi dependensi, breaking changes, rollback saat OS baru membuat aplikasi crash, dan pentingnya mencatat versi kompatibilitas.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Smartphone Kondisi Pabrik (OS Stabil v14)**<br>HP diproduksi dengan SoC octa-core, RAM 8GB, dan OS v14.0 stabil. Seluruh aplikasi bawaan bekerja tanpa kendala. | `git init`<br>`git commit -m "build: firmware rilis awal os v14.0"` | **Release Baseline Commit** | Diagram lapisan smartphone memanjang ke atas: Lapisan bawah = Hardware (Chipset), Lapisan tengah = Firmware OS 14.0, Lapisan atas = Ikon Aplikasi Chat & Game berjalan lancar. |
| **2** | **Rilis Update Patch Keamanan Bulanan**<br>Pembaruan kecil sebesar 80 MB untuk menutup celah keamanan Bluetooth tanpa mengubah inti sistem. | `git commit -am "sec: patch celah bluetooth rilis v14.1"` | **Security Hotfix Commit** | Kotak perisai hijau kecil meluncur masuk ke lapisan OS dengan animasi checkmark. Riwayat versi melangkah satu tingkat ke depan: `v14.0 -> v14.1`. |
| **3** | **Uji Coba Beta OS v15 Generasi Baru**<br>Tim developer membuka saluran beta untuk menguji arsitektur OS 15 yang merombak manajemen memori, terisolasi dari publik. | `git checkout -b beta-os-15` | **Experimental Channel Branch** | Lapisan OS membelah ke kanan menjadi lintasan baru berwarna neon bertuliskan *"Developer Preview: OS 15-Beta"*, menampilkan animasi pemindaian kernel baru. |
| **4** | **Aplikasi Kamera Utama Crash & Layar Hitam**<br>Aplikasi kamera mogok kerja (*force close*) karena driver lensa lama tidak kompatibel dengan API baru (*breaking change*). | `git log --oneline -n 3` | **Commit History Diagnosis** | Tampilan layar ponsel di lapisan aplikasi menampilkan pesan error *"Camera has stopped working"* disertai segitiga peringatan kuning menyala pada driver sensor kamera. |
| **5** | **Rollback Firmware ke Versi Stabil Sebelumnya**<br>Lewat menu recovery, ponsel di-flash ulang kembali ke titik pemulihan OS 14.1 yang stabil agar kamera berfungsi kembali. | `git reset --hard HEAD~1` | **Hard Reset / Firmware Rollback** | Garis waktu sistem bergerak mundur (*rewind animation*). Lapisan OS 15 beta terhapus, dan ponsel menyala kembali dengan OS 14.1 stabil; ikon kamera kembali berfungsi normal. |
| **6** | **Dokumentasikan Catatan Rilis Kompatibilitas**<br>Vendor menerbitkan catatan resmi: aplikasi kamera wajib diperbarui ke versi 2.0 sebelum diizinkan menginstal OS 15. | `git commit -am "docs: tambah matriks kompatibilitas di changelog"` | **Changelog & Matrix Commit** | File dokumen teks digital berjudul *"Release Notes & Compatibility Matrix"* muncul di layar dengan tanda centang hijau pada kombinasi *"OS 14.1 + Camera v1.8 = Valid"*. |

---

# LEVEL 3: CALON PENGEMBANG SOFTWARE & GAME DEV (7 Step Agak Kompleks)
*Ditujukan untuk pemula yang ingin memahami arsitektur industri game dan perangkat lunak modern (studi kasus GTA 6, FIFA, UFC, Minecraft, PvZ, dan Granny).*

---

### Kasus 3.1: Pengembangan Game GTA 6 (Open World City & Vehicle Physics)
> **Skenario:** Mengembangkan sistem fisika mobil di kota Leonida, mengatasi tabrakan kode shader grafis, dan merilis patch darurat.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Base Map Kota Vice City Selesai**<br>Tim arsitek map menyelesaikan layout jalan aspal, gedung pencakar langit, dan pantai di branch `main`. | `git init`<br>`git commit -m "world: base layout jalan dan distrik kota leonida"` | **Initial World Baseline Commit** | Peta 3D low-poly kota tepi pantai modern dengan gedung tinggi dan jalan raya yang membentang rapi, diberi label branch `main (Commit a1b2: World Baseline)`. |
| **2** | **Cabang Fitur: Mekika Fisika Mobil Super**<br>Tim gameplay membuat cabang baru untuk menyetel suspensi mobil sport, ban drift, dan deformasi bodi saat tabrakan. | `git checkout -b feature/supercar-physics` | **Feature Branch Creation** | Dari garis utama `main`, muncul garis cabang biru melengkung ke atas. Mobil sport melaju di lintasan uji coba sambil menabrak rintangan uji pantulan fisik. |
| **3** | **Cabang Paralel: Cuaca Badai Tropis Ekstrem**<br>Tim visual membuat cabang paralel untuk mensimulasikan hujan badai lebat, genangan air jalanan, dan petir volumetrik. | `git checkout -b feature/tropical-storm` | **Parallel Feature Branch** | Garis cabang kedua berwarna ungu mencabang ke bawah. Tampilan layar memperlihatkan efek air hujan membasahi aspal kota dengan pantulan genangan air dinamis. |
| **4** | **Merge Conflict: Shader Jalan Bertabrakan!**<br>Saat digabungkan, terjadi konflik: kode gesekan ban mobil menimpa perhitungan pantulan genangan air aspal. | `git checkout main`<br>`git merge feature/supercar-physics`<br>`git merge feature/tropical-storm` | **Three-Way Merge Conflict** | Dua panah cabang bertemu di satu titik merah yang berdenyut (*Conflict Warning*). Tampilan kode menunjukkan penanda `<<<<<<< HEAD` (ban licin) vs `>>>>>>> feature/storm` (air genangan). |
| **5** | **Menyelesaikan Konflik (Conflict Resolution)**<br>Programmer menggabungkan rumus: ban hanya tergelincir jika melewati genangan air tertentu; konflik diselesaikan secara bersih. | `git add shaders/road_physics.hlsl`<br>`git commit -m "merge: selesaikan konflik shader jalan basah"` | **Merge Conflict Resolution** | Dua blok kode di layar menyatu menjadi warna hijau bersih (*Resolved*). Titik merah berubah menjadi titik biru stabil berlabel *"Merge Commit: Weather & Physics Unified"*. |
| **6** | **Menemukan Memory Leak pada AI Mobil Polisi**<br>AI mobil polisi menghabiskan RAM saat mengejar pemain. Fitur lain yang sedang diketik disimpan sementara ke brankas rahasia untuk perbaikan kilat. | `git stash push -m "wip: tuning rem mobil"`<br>`git stash pop` | **Work-in-Progress Stash & Pop** | Kotak transparan berlogo brankas berlabel `git stash` menyedot potongan kode yang belum selesai dari meja kerja. Meja kembali bersih untuk memperbaiki bug kritis. |
| **7** | **Rilis Milestone 'Pre-Alpha Demo 0.1'**<br>Bug teratasi dan kode brankas dikembalikan; seluruh fitur dikunci sebagai tonggak rilis demo internal studio. | `git tag -a v0.1-prealpha -m "milestone: pre-alpha build studio test"` | **Milestone Release Tag** | Mobil sport melesat menembus genangan air badai kota dengan mulus. Stempel medali emas digital berlabel *"MILESTONE: GTA-VI Pre-Alpha v0.1"* terkunci di ujung diagram Git. |

---

### Kasus 3.2: Pengembangan Game FIFA / EA Sports FC (Server Netcode & Transfer Roster)
> **Skenario:** Mengupdate bursa transfer pemain, menyeimbangkan animasi tendangan melengkung (*trivela*), dan memulihkan database server yang corrupt.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Database Pemain & Atribut Standar Musim Baru**<br>Daftar 10.000 pemain dunia, formasi klub, dan atribut stamina tersimpan rapi di commit fondasi server. | `git init`<br>`git commit -m "roster: database awal musim 2026"` | **Initial Database Commit** | Kartu-kartu pemain sepak bola berjejer rapi di atas papan formasi taktik lapangan hijau dengan label simpul awal `HEAD -> main: Season 2026 Kickoff`. |
| **2** | **Update Bursa Transfer Deadline Day**<br>Menjelang penutupan bursa eropa, dibuat cabang cepat untuk memindahkan striker bintang ke klub barunya beserta nomor punggung. | `git checkout -b hotfix/deadline-transfers` | **Hotfix Branch Creation** | Garis cabang cepat berwarna kuning meluncur dari `main`. Animasi jersey klub berganti logo dan kartu striker bergeser ke klub barunya. |
| **3** | **Eksperimen: Animasi Tendangan Trivela Overpowered**<br>Tim desainer memperbarui rumus lengkungan bola luar kaki, namun tendangan ini menjadi terlalu mudah gol dari jarak 40 meter. | `git commit -am "gameplay: naikkan multiplier lengkungan trivela"` | **Experimental Tuning Commit** | Pemain menendang bola dari jarak jauh; bola melengkung tajam membentuk busur laser neon yang menukik otomatis ke pojok atas gawang berkali-kali. |
| **4** | **Komplain Komunitas: Glitch Gol Otomatis!**<br>Pemain daring protes di media sosial. Melalui riwayat log, tim menginvestigasi commit mana yang memasukkan angka kurva 1.85. | `git log --grep="trivela" -p` | **Targeted Commit Audit** | Antarmuka daftar riwayat commit (*git log*) tersorot lampu sorot. Tangan penyelidik menunjuk baris commit `hash c981bf: Tune Trivela Curve Multiplier to 1.85`. |
| **5** | **Revert Commit Glitch Tanpa Matikan Server**<br>Tanpa merestart database global, dieksekusi perintah revert untuk membuat commit kebalikan yang memulihkan kurva bola ke angka aman 1.10. | `git revert c981bf --no-edit` | **Non-Destructive Revert** | Sebuah stempel simpul baru berwarna hijau muda berlabel *"Revert c981bf: Restore Safe Shot Physics"* menimpa efek busur laser bola menjadi lengkungan fisik wajar. |
| **6** | **Menggabungkan Roster Transfer & Nerf Tendangan**<br>Data transfer pemain baru dan formula tendangan yang sudah seimbang disatukan kembali ke cabang server utama. | `git checkout main`<br>`git merge hotfix/deadline-transfers` | **Hotfix Branch Integration** | Dua jalur cabang (Transfer dan Physics Fix) menyatu masuk kembali ke pipa kabel server bercahaya di garis `main`. |
| **7** | **Deploy Patch Server Online v1.04**<br>Pembaruan diunggah ke server global tanpa downtime. Pertandingan daring kembali adil dan kompetitif. | `git tag -a v1.04-fut -m "deploy patch online server v1.04"` | **Production Deployment Tag** | Stadion sepak bola penuh penonton menyala dengan papan skor raksasa menampilkan *"Title Update 1.04 Live - Server Synchronized"*. |

---

### Kasus 3.3: Pengembangan Game UFC (Combat Collision & Fighter Balancing)
> **Skenario:** Mengembangkan sistem benturan pukulan hook, menangani bug animasi ragdoll terlempar keluar oktagon, dan mengamankan kode sebelum tournament esports.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Kerangka Animasi Dasar Petarung di Oktagon**<br>Model 3D petarung di dalam ring memiliki 64 sendi kerangka gerak pukulan jab dan tendangan low kick standar. | `git init`<br>`git commit -m "anim: kerangka rigging dasar petarung 64-bones"` | **Animation Baseline Commit** | Karakter petarung wireframe 3D berdiri di tengah ring oktagon dengan titik-titik sendi (*bones skeleton*) berwarna biru menyala. |
| **2** | **Cabang Khusus: Sistem Bantingan Judo & Gulat**<br>Tim animasi membuat cabang untuk mendesain transisi grapple saat petarung membanting lawan ke matras kanvas. | `git checkout -b feature/takedown-system` | **Feature Branching** | Garis cabang oranye keluar dari poros utama. Dua petarung saling mencengkeram dan melakukan gerakan bantingan bantingan gulat ke lantai kanvas. |
| **3** | **Bug Kritis: Petarung Melayang Keluar Ring!**<br>Saat terkena uppercut di pagar ring, petarung terpental menembus atap. Git Bisect dipakai membedah commit mana pemicunya. | `git bisect start`<br>`git bisect bad`<br>`git bisect good v1.0` | **Binary Bug Hunting (Bisect)** | Petarung meluncur ke udara menembus kawat oktagon seperti roket. Layar simulasi Git membelah riwayat menjadi dua zona: zona hijau (aman) dan zona merah (bug ditemukan). |
| **4** | **Pemisahan Hotfix Darurat dari Fitur Baru**<br>Developer tidak ingin menunggu sistem gulat selesai; dibuat cabang perbaikan kilat langsung dari commit stabil terakhir. | `git checkout -b fix/collision-boundary v1.0` | **Targeted Hotfix Branch** | Jarum penunjuk bercabang membuat jalan pintas kecil langsung dari titik stabil tanpa menyentuh cabang gulat yang belum tuntas. |
| **5** | **Pasang Dinding Collider Tak Kasat Mata**<br>Programmer menambahkan dinding pembatas tak kasat mata agar tubuh petarung tertahan kokoh di jaring kawat oktagon. | `git commit -am "fix: pasang invisible collider boundary jaring oktagon"` | **Bugfix Commit** | Kubus jaring transparan bercahaya merah terpasang mengelilingi oktagon; saat petarung terpukul ke sudut, badannya tertahan kokoh di jaring kawat. |
| **6** | **Ambil Hanya Satu Solusi Perbaikan (Cherry-Pick)**<br>Solusi benturan dinding dari cabang hotfix dipetik dan diterapkan langsung ke cabang turnamen esport tanpa membawa kode lain. | `git checkout tournament-build`<br>`git cherry-pick 7f21a4` | **Selective Cherry-Pick** | Ilustrasi tangan robot mekanis memetik sebuah buah apel bersinar (simbol commit perbaikan `7f21a4`) lalu menancapkannya tepat di cabang turnamen `esports-tournament`. |
| **7** | **Kunci Rilis Turnamen Dunia UFC**<br>Versi game turnamen dikunci resmi; seluruh petarung dan mekanik benturan terverifikasi stabil untuk kompetisi berhadiah miliaran. | `git tag -a v2.1-esports -m "official tournament locked build"` | **Tournament Lock Tag** | Sabuk juara emas UFC diletakkan di tengah ring oktagon dengan stempel hologram bercahaya *"Official Esports Build v2.1 Locked"*. |

---

### Kasus 3.4: Pengembangan Game Minecraft (World Generation & Nether Update)
> **Skenario:** Mengembangkan generator bioma baru, mempertahankan kompatibilitas blok lama (*backward compatibility*), dan menangani crash modding.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Dunia Blok Klasik (Overworld Survival)**<br>Generator dunia mampu menyusun bukit rumput, pohon kayu ek, goa batu, dan bijih besi dengan seed acak stabil. | `git init`<br>`git commit -m "worldgen: overworld biomes terrain generator"` | **Core Engine Commit** | Pemandangan voxel blok kotak-kotak hijau khas Minecraft lengkap dengan pohon kubus dan matahari berbentuk bujur sangkar dengan tag `v1.0-vanilla`. |
| **2** | **Cabang Eksperimen: Ekosistem Bioma Nether Baru**<br>Tim merancang bioma baru: Hutan Jamur Merah (*Crimson Forest*) dan Lembah Pasir Jiwa (*Soul Sand Valley*) di cabang terpisah. | `git checkout -b feature/nether-expansion` | **Expansion Feature Branch** | Dari garis tanah hijau, muncul cabang bawah tanah berwarna merah membara yang memperlihatkan pohon jamur merah raksasa dan kabut api lava. |
| **3** | **Konflik ID Blok: Blok Emas Nether Menimpa Blok Pasir**<br>Saat menyusun tabel ID, blok emas baru bentrok dengan kode lama blok pasir gurun; game gagal memuat dunia. | `git status`<br>`git diff registry/blocks.json` | **Registry Collision Inspection** | Tampilan dunia Minecraft berkedip ungu-hitam kotak-kotak (*missing texture*). Layar konsol menunjukkan tabrakan angka ID: `ID 154 duplicated between Soul_Soil and Sandstone`. |
| **4** | **Refactor Registry Menggunakan Sistem Penamaan Baru**<br>Programmer memodifikasi kode agar setiap blok memiliki nama unik berseri seperti `minecraft:soul_sand` bukan sekadar angka mentah. | `git commit -am "refactor: migrasi block registry ke NamespacedID"` | **Architecture Refactor Commit** | Kotak-kotak blok di layar mendapatkan label barcode digital yang rapi dan terisolasi, menghilangkan seluruh konflik ID secara permanen. |
| **5** | **Uji Coba Snapshot Mingguan ke Komunitas**<br>Sebelum digabung resmi, versi ini dirilis sebagai 'Snapshot Mingguan' agar jutaan pemain bisa mencoba dan mencari bug gratis. | `git tag -a 24w36a -m "snapshot: nether biome preview"` | **Community Snapshot Tag** | Karakter pemain berpenampilan Steve memegang kaca pembesar memeriksa blok jamur baru sambil mencatat daftar bug di atas buku bulu ayam. |
| **6** | **Menggabungkan Snapshot ke Versi Rilis Resmi**<br>Seluruh umpan balik komunitas diperbaiki; cabang dimensi Nether resmi digabungkan ke cabang utama dengan jejak sejarah rapi. | `git checkout main`<br>`git merge --no-ff feature/nether-expansion` | **Explicit Non-Fast-Forward Merge** | Cabang merah membara menyatu masuk ke dalam portal dimensi obsidian ungu yang kokoh di tengah garis cabang utama `main`. |
| **7** | **Pembaruan Akbar Dunia Minecraft Dirilis**<br>Update akbar diluncurkan ke seluruh dunia di PC, konsol, dan mobile dengan jaminan dunia lama pemain tidak akan rusak. | `git tag -a v1.16.0 -m "release: the nether update official"` | **Major Version Milestone Tag** | Layar utama Minecraft menampilkan judul besar bercahaya *"Minecraft 1.16: The Nether Update"* dengan partikel api dan animasi portal berputar halus. |

---

### Kasus 3.5: Pengembangan Game Plants vs. Zombies (Tanaman Baru & Rebalance Tingkat Sulit)
> **Skenario:** Menambahkan tanaman es penembak semangka, menyeimbangkan serangan zombie penari tiang, dan memperbaiki aset suara tumpang-tindih.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Halaman Rumput 5 Lajur & Peashooter Standar**<br>Gameplay dasar: Peashooter menembak zombie biasa di halaman rumput 5 baris dengan siklus produksi matahari dari Sunflower. | `git init`<br>`git commit -m "gameplay: 5-lane lawn grid dan peashooter basic"` | **Gameplay Baseline Commit** | Papan catur rumput hijau 5 baris. Tanaman Sunflower tersenyum menghasilkan matahari kecil kuning, dan Peashooter menembakkan kacang polong hijau. |
| **2** | **Cabang Tanaman Baru: Winter Melon (Semangka Es)**<br>Tim membuat tanaman pelontar semangka es yang memberikan efek slow-motion area kepada segerombolan zombie kerucut. | `git checkout -b feature/winter-melon` | **Unit Feature Branch** | Cabang berwarna biru es keluar dari alur utama. Tanaman ketapel semangka es melontarkan semangka beku yang meledakkan es saat menghantam kerumunan zombie. |
| **3** | **Zombi Terlalu Cepat Menang di Gelombang 10**<br>Penguji mengeluh gelombang akhir zombie terlalu cepat memakan tanaman karena harga matahari Winter Melon terlalu mahal (500 matahari). | `git log -n 1 --stat` | **Balance Verification Inspection** | Meteran tingkat kesulitan melompat ke angka 99% (*Tingkat Kematian Ekstrem*). Kumpulan zombie berkostum ember besi menembus barisan pertahanan dengan mudah. |
| **4** | **Rebalance Harga & Radius Beku**<br>Di cabang fitur, harga diturunkan ke 400 matahari dan radius perlambatan diperluas agar permainan adil dan seimbang. | `git commit -am "balance: turunkan cost semangka es ke 400 sun"` | **Game Balancing Commit** | Kartu tanaman Winter Melon berubah harga dari angka merah `500` menjadi angka hijau `400`, dan lingkaran aura beku di rumput membesar menutupi 3 lajur. |
| **5** | **Pengerjaan Paralel Zombi Baru: Bungee Zombie**<br>Rekan setim sedang mengerjakan zombie penerjun tali karet dari langit tanpa mengganggu pengerjaan tanaman semangka es. | `git checkout -b feature/bungee-zombie` | **Concurrent Feature Branch** | Garis cabang terpisah memperlihatkan zombie bergelantungan dengan tali elastis dari awan dan mencuri satu pot tanaman labu dari kebun. |
| **6** | **Menggabungkan Keseimbangan Tanaman & Zombi Baru**<br>Kedua cabang disatukan ke cabang utama; logika tanaman es otomatis memperlambat ayunan tali zombie tanpa bentrok kode. | `git checkout main`<br>`git merge feature/winter-melon`<br>`git merge feature/bungee-zombie` | **Multi-Branch Integration** | Dua elemen (Semangka Es dan Zombie Tali) mendarat bersamaan di halaman rumput tanpa tabrakan kode; logika tanaman es otomatis memperlambat ayunan tali zombie. |
| **7** | **Final Golden Master: Game Siap Rilis Toko**<br>Seluruh level petualangan 50 lantai dinyatakan seimbang dan bebas bug; master build dikunci untuk didistribusikan ke jutaan pemain. | `git tag -a v1.0-gold -m "gold master: release version siap distribusi"` | **Gold Master Release Tag** | Ikon trofi piala emas dengan tanaman bunga matahari bergoyang gembira di samping buku almanak tanaman berstempel *"Version 1.0 Gold Master"*. |

---

### Kasus 3.6: Pengembangan Game Horor Mirip Granny (AI Monster Pathfinding & Door Triggers)
> **Skenario:** Mengembangkan kecerdasan buatan Nenek pemburu yang mendengar suara barang jatuh, memperbaiki pintu terkunci yang tembus pandang, dan merilis versi mobile ringan.

| No | Nama Step | Git Example Syntax | Git Example Syntax Name | Visualisasi Prompt |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Rumah Kayu Tua 2 Lantai & Jebakan Lantai Berderit**<br>Denah rumah kayu gelap dengan lantai berderit; jika pemain berjalan di atas papan longgar, sistem mengirim sinyal koordinat suara. | `git init`<br>`git commit -m "env: denah rumah kayu tua dan sistem sound trigger"` | **Environment Baseline Commit** | Rumah kayu suram tampak transparan (*isometric blueprint*). Gelombang lingkaran suara oranye memancar dari langkah kaki pemain di lantai 2. |
| **2** | **Cabang AI: Logika Nenek Mendengar Suara**<br>Saat sinyal suara terdeteksi, AI monster Nenek akan mengubah arah patroli dan berlari menuju titik koordinat suara tersebut. | `git checkout -b feature/granny-hearing-ai` | **AI Feature Branching** | Cabang ungu gelap keluar dari jalur utama. Sosok siluet Nenek membawa pemukul bisbol berbalik cepat saat gelombang suara oranye menyentuh telinganya. |
| **3** | **Bug Fatal: Nenek Menyerang Tembus Pintu Tertutup**<br>Saat pemain menutup dan mengunci pintu, tongkat Nenek tetap bisa memukul menembus daun pintu dan membunuh pemain seketika (*clip-through glitch*). | `git status`<br>`git diff scripts/door_collision.cs` | **Glitch & Collision Inspection** | Pemain bersembunyi di balik pintu kayu tertutup, namun tangan Nenek menembus kayu pintu secara ganjil (*glitch clip-through*) disertai tulisan merah *"Player Died - Game Over"*. |
| **4** | **Memperbaiki Raycast & Lapisan Fisika Pintu**<br>Programmer membuat cabang kilat untuk memastikan daun pintu memblokir jangkauan tongkat Nenek sampai pintu benar-benar didobrak terbuka. | `git checkout -b fix/door-raycast-occlusion` | **Hotfix Occlusion Branch** | Garis laser deteksi (*raycast*) berwarna biru dari tongkat Nenek terbentur daun pintu dan memantul aman; pemain di dalam kamar selamat terlindungi. |
| **5** | **Menemukan Masalah Frame Rate Anjlok di HP Murah**<br>Efek bayangan senter berlebihan membuat game patah-patah di HP RAM 2GB; shader bayangan dinamis di-revert ke bayangan statis ringan. | `git revert HEAD~1` | **Performance Hotfix Revert** | Indikator FPS melonjak dari `14 FPS` (merah patah-patah) menjadi `60 FPS` (hijau mulus). Bayangan rumit disederhanakan menjadi lingkaran bayangan gelap lembut di bawah kaki. |
| **6** | **Menggabungkan AI Cerdas & Fisika Pintu yang Rapi**<br>Perbaikan pintu dimasukkan kembali ke alur utama; kini Nenek harus mendobrak pintu sebelum bisa melukai pemain. | `git checkout main`<br>`git merge fix/door-raycast-occlusion` | **Bugfix Branch Merge** | Pintu kayu bergetar saat Nenek memukulnya dari luar, papan pintu terlepas satu per satu secara realistis memberi waktu pemain kabur lewat ventilasi. |
| **7** | **Peluncuran Update Horor Halloween**<br>Mode malam ekstra gelap dengan teka-teki gembok baru selesai dikunci; file APK dan versi iOS siap diunduh jutaan pemain pencinta game horor. | `git tag -a v1.2-halloween -m "release: halloween nightmare update"` | **Seasonal Event Release Tag** | Layar menu utama game berubah menjadi malam berkabut dengan kilatan petir; Nenek tersenyum menyeramkan di depan gerbang berstempel *"Update 1.2: Halloween Nightmare Live"*. |

---

## 4. Panduan Implementasi Teknis ke Prototype Web Git Rescue

1. **Format Data Penyimpanan (`data/analogies.json`):**  
   Seluruh tabel di atas dapat langsung diekspor menjadi skema JSON dengan struktur:
   ```json
   {
     "level": 1,
     "category": "awam",
     "cases": [
       {
         "id": "cat-pagar",
         "title": "Dekorasi & Pengecatan Pagar Rumah",
         "steps": [
           {
             "step": 1,
             "name": "Cat Dasar Abu-abu",
             "gitSyntax": "git init && git commit -m 'feat: cat dasar abu-abu anti-karat'",
             "gitSyntaxName": "Repository Init & Initial Commit",
             "visualPrompt": "Ilustrasi 2D flat minimalis: Pagar besi polos berubah menjadi warna abu-abu matte..."
           }
         ]
       }
     ]
   }
   ```
2. **Koneksi ke View 6 (Story) & View 7 (Raw Lab):**
   - Saat pengguna menekan tab *"Awam"*, panggil Kasus 1.1 atau 1.2.
   - Saat pengguna menekan tab *"Menengah / Teknik"*, panggil Kasus 2.1 atau 2.2.
   - Saat pengguna menekan tab *"Developer / Game Dev"*, sajikan menu kartu 6 game populer (GTA 6, FIFA, UFC, Minecraft, PvZ, Granny) yang langsung menghubungkan intuisi game favorit mereka ke cara kerja Git sesungguhnya.
