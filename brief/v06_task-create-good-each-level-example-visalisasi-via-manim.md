# Brief v06: Rencana Tugas & Spesifikasi Animasi Manim (Model Branching Realistis: Alpha, Beta, & Release)

Dokumen ini berisi spesifikasi skenario dan rancangan adegan Manim yang **tidak lagi sekadar garis lurus (*linear*)**, melainkan mengadopsi model alur kerja industri nyata (*Real-World Git Branching Model*):
- Penggunaan **Semantic Versioning** (`vX.Y.Z-alpha`, `beta`, `rc`, dan `hotfix`).
- Pembagian jalur cabang yang masuk akal: **`main` (Production/Stabil)**, **`develop` (Fitur Berjalan)**, dan **`hotfix` (Perbaikan Darurat)**.
- Tetap mempertahankan metafora bertingkat agar mudah dicerna oleh siapa saja yang ingin memahami Git secara mendalam.

---

## 1. Peta Alur Cabang Realistis untuk 3 Studi Kasus

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. PAGAR RUMAH: Konstruksi -> Draf Warna -> Evaluasi Keluarga -> Rilis      │
│ 2. SMARTPHONE : OS 14 (Prod) -> Beta Channel -> Camera Crash -> Rollback    │
│ 3. MINECRAFT  : v1.15.2 (Main) -> Snapshot Alpha/Beta -> RC -> v1.16 Nether │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. KASUS 1: Pagar Rumah (Level 1 - Alur Proyek Fisik Bertahap)
*Metafora: Membangun pagar rumah bertahap dari uji struktur (Alpha), uji warna (Beta), persetujuan keluarga (RC), hingga pelapisan akhir (v1.0.0).*

| Step | Nama Aksi & Konteks Lapangan | Cabang & Git Command | Semantic Version / Tag | Visualisasi Manim |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Pondasi & Rangka Besi Mentah**<br>Pagar besi dilas dan dicor ke tanah. Belum ada warna, baru struktur dasar. | `git checkout -b develop`<br>`git commit -m "chore: struktur besi rangka"` | `v0.1.0-alpha` | Pagar besi hitam polos tanpa cat. Di diagram Git bawah, muncul commit pertama bertuliskan `v0.1.0-alpha` di cabang `develop`. |
| **2** | **Uji Cat Dasar Anti Karat (Penyebaran Luas)**<br>Seluruh rangka dilapis cat dasar abu-abu tahan hujan untuk uji cuaca 1 minggu. | `git commit -am "test: cat dasar abu-abu anti karat"` | `v0.2.0-beta` | Pagar berubah warna menjadi abu-abu doff. Simpul rantai Git bergerak maju ke titik `v0.2.0-beta`. |
| **3** | **Cabang Eksperimen: Coba Warna Hijau vs Kuning**<br>Keluarga berbeda pendapat: Ayah mau hijau, Ibu mau motif garis kuning. Dibuat 2 panel uji terpisah. | `git checkout -b exp/motif-kuning`<br>`git commit -m "exp: panel garis kuning"` | Branch Terisolasi | Pagar membelah dua tampilan: 1 bilah dicat kuning menyala di cabang atas, bilah lain dicat hijau tua di cabang bawah. |
| **4** | **Musyawarah Keluarga (Code Review): Kuning Ditolak**<br>Keluarga sepakat garis kuning terlalu mencolok. Cabang kuning dibuang, warna hijau tua disetujui. | `git checkout develop`<br>`git branch -D exp/motif-kuning`<br>`git merge exp/warna-hijau` | `v0.9.0-rc.1` *(Candidate)* | Panel kuning terlipat memudar dan hilang. Seluruh pagar dicat hijau tua rapi. Node branch kuning terhapus di graf Git. |
| **5** | **Pernis Anti Gores & Pasang Plat Nomor Rumah**<br>Pagar dilapisi vernis kilap pelindung akhir dan dipasangi plat nomor. Proyek resmi selesai dan dibuka! | `git checkout main`<br>`git merge develop`<br>`git tag -a v1.0.0 -m "release pagar selesai"` | **`v1.0.0 (Release)`** | Efek kilap menyapu pagar hijau. Di diagram bawah, cabang `develop` bergabung (*merge*) ke `main` dan distempel emas `v1.0.0`. |

---

## 3. KASUS 2: Smartphone & Firmware (Level 2 - Siklus Rilis OS Industri)
*Metafora: Siklus rilis sistem operasi mobile dari versi stabil produksi, program beta publik, breaking change driver, hingga hotfix darurat.*

| Step | Nama Aksi & Konteks Lapangan | Cabang & Git Command | Semantic Version / Tag | Visualisasi Manim |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **OS 14.1.0 Stabil di Tangan Konsumen**<br>Versi resmi berjalan di jutaan perangkat pengguna umum tanpa gangguan. | `git checkout main`<br>`git commit -m "release: os 14.1.0 lts"` | `v14.1.0 (Production)` | Tampilan 3 layer ponsel: Hardware aman, OS hijau stabil, semua aplikasi chat & kamera beroperasi normal. Node `main` berwarna hijau. |
| **2** | **Buka Jalur Pembaruan Tahunan: Cabang OS 15**<br>Tim inti membuat cabang pengembangan besar untuk fitur arsitektur AI dan widget baru. | `git checkout -b release/15.0-beta` | `v15.0.0-beta.1` | Muncul jalur cabang baru berwarna oranye neon di atas `main`. Lapisan OS di ponsel menampilkan teks *"Beta Preview Channel"*. |
| **3** | **Breaking Change: Lensa Kamera Layar Hitam**<br>Pengguna beta melaporkan aplikasi kamera bawaan crash saat dibuka karena driver lensa lama tidak cocok dengan kernel baru. | `git status`<br>`git log --grep="camera" -n 2` | *Issue Detected* | Layar HP menampilkan jendela dialog *"Camera has stopped working"* berwarna merah. Di diagram Git, node commit terakhir ditandai peringatan kuning. |
| **4** | **Cabang Perbaikan Kilat: Driver Adapter Patch**<br>Alih-alih menunda rilis OS, tim membuat cabang hotfix untuk menyisipkan adaptor penerjemah driver kamera lama. | `git checkout -b fix/camera-lens-adapter` | *Hotfix Branch* | Jarum branching kecil meluncur dari node bermasalah. Tangan mekanis mengganti sensor kode virtual menjadi kompatibel. |
| **5** | **Rollback Sementara untuk Pengguna Publik**<br>Sementara adapter diuji, pengguna yang komplain dapat menekan tombol rollback ke versi stabil 14.1 tanpa kehilangan data. | `git checkout main`<br>`git reset --hard v14.1.0` | `Rollback Safe Point` | Layar HP kembali menyala normal dengan OS 14.1.0; kamera kembali dapat memotret. Garis waktu mundur ke titik aman. |
| **6** | **Rilis Resmi Akbar OS 15 dengan Kamera Sembuh**<br>Hotfix adaptor digabungkan ke cabang beta, lalu seluruh OS 15 digabungkan ke `main` sebagai rilis global tahunan. | `git checkout main`<br>`git merge release/15.0-beta`<br>`git tag -a v15.0.0 -m "official os 15"` | **`v15.0.0 (Global Release)`** | Seluruh lapisan smartphone menyatu bercahaya biru terang. Node `release/15.0-beta` menyatu ke `main` dengan tag rilis resmi `v15.0.0`. |

---

## 4. KASUS 3: Minecraft Nether Update (Level 3 - Model Mojang Snapshot & Release)
*Mengikuti alur asli Mojang Studios: Rilis LTS ➔ Snapshot Mingguan (Alpha) ➔ Release Candidate (Beta) ➔ Full Release ➔ Hotfix Multiplayer.*

| Step | Nama Aksi & Konteks Game Dev | Cabang & Git Command | Semantic Version / Tag | Visualisasi Manim |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Minecraft 1.15.2 (Buzzy Bees - Rilis LTS Stabil)**<br>Dunia Overworld klasik dengan bioma lebah. Fondasi awal sebelum proyek pembaruan akbar dimulai. | `git checkout main`<br>`git tag -a v1.15.2 -m "buzzy bees release"` | `v1.15.2 (Stable)` | Blok voxel rumput hijau Minecraft dan sarang lebah kotak. Node Git berstempel `v1.15.2` di garis `main`. |
| **2** | **Cabang Fitur Raksasa: Ekspansi Dimensi Nether**<br>Mojang membuat cabang terpisah untuk mengembangkan bioma Crimson Forest, Piglin, dan Netherite. | `git checkout -b feature/nether-expansion` | *Development Track* | Dari garis hijau Overworld, muncul cabang bawah tanah berwarna merah membara yang memperlihatkan pohon jamur merah raksasa. |
| **3** | **Rilis Snapshot Mingguan Pertama (Komunitas Uji Alpha)**<br>Diberi nama rilis snapshot `20w06a` agar jutaan pemain di forum Reddit bisa mencoba dan mencari glitch. | `git tag -a 20w06a -m "snapshot nether biome preview"` | `Snapshot 20w06a (Alpha)` | Karakter Steve memegang obor menjelajahi lava Nether. Muncul badge tag berwarna ungu `20w06a` di cabang fitur. |
| **4** | **Tabrakan Registry ID Blok & Save Corrupt**<br>Pemain melaporkan saat memuat save game lama, blok pasir gurun berubah menjadi blok tanah jiwa (*missing registry*). | `git checkout -b fix/registry-namespaced-id` | *Emergency Hotfix* | Tampilan dunia voxel berkedip ungu-hitam kotak-kotak (*missing texture*). Layar konsol menunjukkan tabrakan angka ID: `ID 154 duplicated`. |
| **5** | **Rilis Release Candidate: Stabilisasi Terakhir**<br>Registry dimigrasikan ke `minecraft:soul_sand`. Mojang merilis build *Release Candidate 1* untuk memastikan tidak ada crash lagi. | `git merge fix/registry-namespaced-id`<br>`git tag -a 1.16-rc1 -m "release candidate 1"` | `1.16-rc1 (Release Candidate)` | Blok voxel kembali memiliki tekstur tajam tanpa glitch. Stempel oranye bertuliskan `1.16-rc1` terpasang di ujung cabang. |
| **6** | **Peluncuran Akbar: The Nether Update Resmi Digabung**<br>Fitur Nether digabungkan secara resmi ke cabang utama `main` dengan metode penggabungan eksplisit non-fast-forward. | `git checkout main`<br>`git merge --no-ff feature/nether-expansion` | `Merge Commit (Integration)` | Cabang merah membara menyatu ke garis hijau utama `main` melalui portal obsidian ungu yang menyala megah. |
| **7** | **Tag Milestone Global & Hotfix Patch 1.16.1**<br>Game dirilis serentak di PC, konsol, dan mobile dengan tag `v1.16.0`. Lalu ditambahkan patch kilat `v1.16.1` untuk memperbaiki lag server server online. | `git tag -a v1.16.0 -m "the nether update"`<br>`git commit -am "hotfix: server network tick lag"`<br>`git tag -a v1.16.1` | **`v1.16.0` & `v1.16.1 (Hotfix)`** | Layar menyala menampilkan banner emas *"Minecraft 1.16.0 Live"*, diikuti simpul kecil bertuliskan *"v1.16.1 Hotfix (Server Sync)"*. |

---

## 5. Rencana Tugas Implementasi Render Manim

- [ ] **Task 1:** Konfigurasi layout split-screen Manim dengan rasio 55% metafora atas dan 45% DAG Git bawah.
- [ ] **Task 2:** Buat generator badge Semantic Versioning (`alpha`, `beta`, `rc`, `release`, `hotfix`) agar otomatis menempel pada simpul commit.
- [ ] **Task 3:** Implementasikan adegan `PagarGitScene` (Siklus draf warna pagar keluarga).
- [ ] **Task 4:** Implementasikan adegan `SmartphoneGitScene` (Siklus rilis OS & rollback kamera).
- [ ] **Task 5:** Implementasikan adegan `MinecraftGitScene` (Siklus Mojang Snapshot ➔ RC ➔ Nether Release ➔ Hotfix).
- [ ] **Task 6:** Ekspor klip MP4 resolusi 1080p dan WebM transparan untuk dipasang di folder `assets/videos/` pada website Git Rescue.
