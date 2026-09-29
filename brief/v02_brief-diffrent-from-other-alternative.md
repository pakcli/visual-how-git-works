# Git Rescue: Analisis Komparasi Mendalam & Pembeda dari Alternatif Lain (v02)

**Dokumen Pendamping Skripsi:**  
*Analisis Tinjauan Pustaka (*Related Work*), Komparasi Fitur Head-to-Head, Bedah Repositori Git-Study/GitAtlas, dan Posisi Kebaruan Riset (*Research Gap*)*

---

## 1. Posisi Kebaruan Riset (*Research Gap & Value Proposition*)

Kebanyakan alat bantu belajar Git yang ada di dunia saat ini terbagi menjadi dua kutub:
1. **Kutub Referensi / Ensiklopedia Teknis (*Commands-First*):** Menyajikan ratusan sintaks perintah terstruktur (contoh: *GitAtlas*, *Oh Shit, Git!?!*). Pendekatan ini mengasumsikan pengguna sudah tahu nama masalah dan perintah yang dicari.
2. **Kutub Gamifikasi & Visualisasi Abstrak (*Curriculum-First*):** Menyajikan level-level simulasi branch interaktif (contoh: *Learn Git Branching*, *Visualizing Git*, *Oh My Git!*). Pendekatan ini mengasumsikan pengguna memiliki waktu luang untuk belajar dari level 1 secara bertahap.

### Di mana Posisi Kosong yang Diisi oleh *Git Rescue*?
Pemula yang mengalami masalah Git di tengah tenggat waktu kerja mengalami **beban kognitif tinggi (*cognitive overload*) dan kepanikan**. Mereka tidak butuh ensiklopedia 300 perintah dan tidak punya waktu menyelesaikan 20 level game. Mereka butuh:
- Pertolongan darurat dalam **< 60 detik / 2 ketukan**.
- **Skenario Lapangan (IRL)** yang memperhitungkan dampak nyata (misal: "jangan reset hard jika commit sudah dipull rekan kerja").
- **Analogi Bertingkat** yang menjembatani intuisi tanpa jargon teknis langsung.
- **Raw File Lab** yang membuktikan secara visual mengapa Git tidak dirancang untuk file dokumen Word atau file biner.
- **Dual Shell Script Export** (`.ps1` dan `.sh`) siap pakai.

---

## 2. Komparasi Terperinci: Git Rescue vs 6 Tool Populer

Berikut adalah bedah komparasi satu per satu antara Git Rescue dengan masing-masing alat bantu yang ada:

### 2.1 vs Oh Shit, Git!?! (`ohshitgit.com`)
*Situs panduan masalah Git berbasis bahasa kasual populer.*

| Parameter | Oh Shit, Git!?! | Git Rescue (Rancangan Skripsi) |
| :--- | :--- | :--- |
| **Pendekatan** | Berbasis situasi buruk (*problem-first*). | Berbasis masalah (*problem-first*) + simulasi konsekuensi. |
| **Format Sajian** | Halaman artikel teks statis memanjang. | Visual interaktif mobile-first (1 ide per layar). |
| **Visualisasi Graph** | ✗ Tidak ada (hanya teks panduan). | **✓ Ada diagram sebelum vs sesudah.** |
| **Sandbox Pengujian**| ✗ Tidak ada arena coba-coba. | **✓ Ada sandbox virtual deterministik.** |
| **Export Skrip** | ✗ Hanya salin teks manual. | **✓ Unduh `.ps1` (PowerShell) & `.sh` (Bash).** |
| **Gaya Bahasa** | Menggunakan umpatan/bahasa kasar (kurang etis untuk kelas/kampus). | Edukatif, netral, dan ramah lingkungan akademis. |
| **Keunggulan Mereka** | Sangat ringkas, reputasi komunitas global luas. | Kalah di jam terbang dan jumlah artikel rujukan. |

---

### 2.2 vs git-time-machine
*Aplikasi Terminal UI (TUI) interaktif untuk membatalkan kesalahan Git via reflog.*

| Parameter | git-time-machine | Git Rescue (Rancangan Skripsi) |
| :--- | :--- | :--- |
| **Format** | TUI (Terminal User Interface berbasis ncurses). | Website statis responsif (*browser-based*). |
| **Aksesibilitas** | Wajib diinstal via package manager / terminal. | **Zero-install, cukup buka URL di HP/laptop.** |
| **Target Pengguna** | Developer yang sudah fasih navigasi terminal. | **Pemula yang belum percaya diri di terminal.** |
| **Eksekusi Asli** | ✓ Bekerja langsung pada repo Git lokal pengguna. | ✗ Simulasi aman tanpa risiko merusak data nyata. |
| **Cakupan Materi**| Sangat terfokus pada eksplorasi log reflog. | Multikasus (revert, reset, stash, merge conflict, dll). |

---

### 2.3 vs Coddy Git Playground (`coddy.tech`)
*Playground interaktif berbasis browser dengan commit-graph reaktif.*

| Parameter | Coddy Git Playground | Git Rescue (Rancangan Skripsi) |
| :--- | :--- | :--- |
| **Engine** | Git asli di Linux container / WebAssembly (akurat). | Simulator JavaScript deterministik (ringan). |
| **Visual Undo** | Commit yang di-undo tampil pudar (*ghost commit*). | Diagram SVG sebelum vs sesudah yang jelas. |
| **Titik Mulai** | Pengguna harus mengetik perintah sendiri (*commands-first*). | **Mulai dari memilih masalah nyata (*rescue-first*).** |
| **Konteks Masalah**| Playground kosong tanpa cerita/dilema. | **Skenario kerja nyata (klien, tim, deadline).** |
| **Fitur Edukasi** | ✗ Tanpa analogi & tanpa inspeksi file biner. | **✓ 3 Level Analogi + Raw File Lab.** |

---

### 2.4 vs Learn Git Branching (`learngitbranching.js.org`)
*Aplikasi visualisasi branching paling populer di dunia saat ini.*

| Parameter | Learn Git Branching | Git Rescue (Rancangan Skripsi) |
| :--- | :--- | :--- |
| **Model Belajar** | Kurikulum tutorial terstruktur level demi level. | **Rescue Cepat (< 60 dtk) + Skenario Kasus Lapangan.** |
| **Pengalaman Awal** | Membuka dengan dialog modal teks instruksi panjang. | **Langsung memilih masalah dalam 1-2 ketukan.** |
| **Gamifikasi** | Menghitung jumlah perintah (*Git Golf*). | Evaluasi keputusan & analisis blunder konsekuensi. |
| **Kedalaman Materi**| Sangat luas (mencakup remote, rebase interaktif). | Terfokus pada 8 masalah kritis harian pemula. |
| **Dukungan HP** | Terlalu padat jika dibuka di layar smartphone. | **Mobile-First (dioptimasi untuk layar 360–412px).** |

---

### 2.5 vs Visualizing Git
*Aplikasi sandbox visualisasi DAG berbasis web.*

| Parameter | Visualizing Git | Git Rescue (Rancangan Skripsi) |
| :--- | :--- | :--- |
| **Tampilan Awal** | Layar hitam terminal kosong tanpa petunjuk aksi. | **Pilihan kartu masalah siap klik.** |
| **Alur Edukasi** | Pengguna harus mandiri mencoba perintah. | Terpandu langkah demi langkah menuju perbaikan. |
| **Konteks Nyata** | Netral tanpa skenario kerja tim. | Berbasis dilema nyata (rekan kerja, bos, klien). |
| **Fitur Ekspor** | ✗ Tidak ada fitur unduh skrip otomatis. | **✓ Dual Script Generator (.ps1 dan .sh).** |

---

### 2.6 vs Oh My Git!
*Game pembelajaran Git berbasis engine Godot.*

| Parameter | Oh My Git! | Git Rescue (Rancangan Skripsi) |
| :--- | :--- | :--- |
| **Format** | Game desktop yang harus diunduh (Linux/macOS/Windows). | Website statis instan via web browser. |
| **Antarmuka** | Berbasis kartu aksi dan terminal grafis game. | UI profesional web-native yang realistis. |
| **Pemakaian di HP**| ✗ Tidak dapat dijalankan di HP. | **✓ Dirancang khusus untuk kenyamanan di HP.** |
| **Fokus Sasaran** | Belajar konsep Git secara menyenangkan saat santai. | **Pertolongan pertama saat panik di tengah proyek.** |

---

### 2.7 Matriks Ringkasan 6 Tool Klasik

| Fitur Kunci | Git Rescue | Oh Shit, Git!?! | git-time-machine | Coddy | Learn Git Branching | Visualizing Git | Oh My Git! |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Rescue-First (<60s)** | **✓** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Skenario Lapangan (IRL)**| **✓** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Analogi Bertingkat** | **✓** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Raw File Lab** | **✓** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Dual Script Export** | **✓** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Zero-Install (Web HP)** | **✓** | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |

---

## 3. Bedah Khusus: Proyek Modern GitAtlas / Git-Study (`Thushar070/Git-Study`)

Repositori GitHub: [Thushar070/Git-Study](https://github.com/Thushar070/Git-Study)  
Demo Publik: [git-study.netlify.app](https://git-study.netlify.app)

### 3.1 Bedah Arsitektur & Jeroan Repositori
- **Stack Teknologi:** React 19, TypeScript, Vite, Tailwind CSS, Lucide React.
- **Struktur Halaman Utama:**
  - `/git`: Ensiklopedia lengkap 60+ perintah Git lokal.
  - `/github`: Panduan perintah resmi GitHub CLI (`gh`).
  - `/visual-lab`: Visualisasi diagram SVG branching, rebase, dan merge.
  - `/situations`: Daftar skenario pencarian solusi masalah (`situations.ts`).
  - `/troubleshooting`: Pencarian solusi berdasarkan pesan error terminal (`troubleshooting.ts`).
  - `/terminal`: Simulator terminal interaktif berbasis React state.

### 3.2 Keunggulan Utama GitAtlas (Pros Mereka)
1. **Cakupan Informasi Ensiklopedis:** Mendokumentasikan ratusan perintah dan flag lengkap dengan tautan dokumentasi resmi `git-scm`.
2. **Metadata Risiko (*Danger Level*):** Memiliki penanda warna tingkat risiko (`safe`, `caution`, `danger`).
3. **Pencarian Pesan Error:** Fitur `/troubleshooting` sangat berguna bagi mereka yang menyalin langsung teks eror terminal (contoh: `detached HEAD`).

### 3.3 Kelemahan GitAtlas untuk Pemula Panik (Cons & Celah Riset Skripsimu)
Meskipun fiturnya sangat lengkap, analisis terhadap *source code* Git-Study membuktikan celah penelitian yang nyata:
1. **Fitur Situations Ternyata Hanya \"FAQ Statis\":**  
   Pada file `src/data/situations.ts`, data kasus hanya berupa array objek statis:
   ```typescript
   {
     id: 'undo-last-commit',
     question: 'I want to undo my last commit but keep the changes',
     recommendedCommands: [{ commandId: 'reset', example: 'git reset --soft HEAD~1' }]
   }
   ```
   Pengguna hanya membaca teks solusi dan menyalinnya. **Tidak ada simulasi kejadian lapangan, tidak ada pilihan berganda, dan tidak ada visualisasi konsekuensi blunder jika salah langkah.**
2. **Beban Kognitif Sangat Padat (*Cognitive Overload*):**  
   Antarmukanya dirancang seperti kamus teknis padat di layar desktop. Jika pemula yang sedang panik membuka situs ini di ponsel, mereka akan kewalahan memilih di antara ratusan tab menu dan parameter.
3. **Modul Visual Terpisah dari Masalah:**  
   Halaman `/situations` terpisah dari `/visual-lab`. Saat pemula membaca solusi, mereka tidak melihat diagram perubahan commit graph secara terpadu.
4. **Tanpa Jembatan Mental Model (Analogi):**  
   Langsung menggunakan istilah teknis murni tanpa jembatan konsep (tidak ada analogi bertingkat).
5. **Tidak Menjawab Alasan Teknis Format File:**  
   Tidak ada pembuktian mengapa Git menolak file biner seperti Word atau gambar.

### 3.4 Tabel Head-to-Head: Git-Study vs Git Rescue

| Parameter Evaluasi | Git-Study (`Thushar070/Git-Study`) | Git Rescue (Rancangan Skripsimu) |
| :--- | :--- | :--- |
| **Model Pembelajaran** | *Reference & Encyclopedia* terpisah | **Scenario-Based Learning (SBL) Terpadu** |
| **Karakter Kasus** | Statis FAQ (hanya teks solusi & copy) | **Dilematis & Kontekstual** (cerita kerja nyata, rekan tim, deadline) |
| **Umpan Balik Keputusan** | Pasif (hanya label `caution` / `safe`) | **Aktif (*Blunder Feedback*)**: Menjelaskan dampak buruk ke repo tim jika salah pilih |
| **Integrasi Visual & Kasus**| Terpisah (halaman `/situations` beda dengan `/visual-lab`) | **Menyatu**: Setiap skenario langsung menampilkan grafik sebelum vs sesudah |
| **Integrasi Terminal** | Terpisah di `/terminal` (mulai dari kondisi kosong) | **Terkoneksi**: Tombol *Sandbox* langsung membuka state commit dari kasus terkait |
| **Mental Model / Analogi** | ✗ Menggunakan istilah teknis langsung | **✓ 3 Level Analogi** (Awam, Menengah, Dev) + Jembatan \"Kenapa bukan Docs\" |
| **Investigasi Format File** | ✗ Tidak ada pembahasan biner | **✓ Raw File Lab** (demo byte mentah `.png`, `.docx` vs diff teks `.md`) |
| **Format Ekspor** | ✗ Hanya copy baris tunggal | **✓ Script `.ps1` & `.sh`** dengan proteksi error dan komentar |
| **Desain Antarmuka** | Desktop-first (padat tab & tabel) | **Mobile-first (< 60 detik / 2 ketukan)** |

### 3.5 Ide dari Git-Study yang Diadopsi ke Git Rescue
1. **Penerapan Badge `dangerLevel`:**  
   Mengadopsi penanda bahaya:
   - 🟢 `SAFE` (Operasi aman, tidak menghapus pekerjaan).
   - 🟡 `REWRITE HISTORY` (Mengubah riwayat lampau, bahaya untuk repo bersama).
   - 🔴 `DESTRUCTIVE` (Menghapus perubahan yang belum dicommit secara permanen).
2. **State Tracking Pointer HEAD:**  
   Logika pelacakan commit graph ringan diadaptasi agar simulator visual deterministik dan tidak membutuhkan server eksternal.

---

## 4. Strategi Menghadapi Penguji Sidang Skripsi

Jika dosen penguji menanyakan:  
> *\"Sudah ada puluhan tool belajar Git seperti Learn Git Branching dan GitAtlas yang fiturnya jauh lebih banyak dari website Anda. Apa nilai kebaruan ilmiah skripsi Anda?\"*

### Jawaban Terstruktur yang Terbukti Kuat:
> *\"Alat bantu seperti GitAtlas dan Learn Git Branching adalah ensiklopedia dan simulator kurikulum yang dirancang untuk pengguna yang memiliki waktu belajar terencana. Namun, survei kebutuhan menunjukkan bahwa mayoritas pemula baru membuka tutorial saat mengalami kegagalan Git darurat di tengah deadline proyek, di mana beban kognitif mereka sangat tinggi.*
>
> *Kebaruan Git Rescue terletak pada **tiga pilar yang belum pernah disatukan sebelumnya**:*
> 1. *Pendekatan **Scenario-Based Learning (SBL)** berbasis kejadian lapangan nyata lengkap dengan evaluasi konsekuensi blunder terhadap repositori tim.*
> 2. *Jembatan intuisi melalui **Analogi Bertingkat 3-Level** dan **Raw File Lab** yang membuktikan secara empiris mengapa Git tidak dirancang untuk file biner seperti Word.*
> 3. *Prinsip antarmuka **Mobile-First Rescue-First** yang menjamin solusi perbaikan dapat diperoleh dalam waktu kurang dari 60 detik tanpa beban membaca dokumentasi teknis yang panjang.*
>
> *Dengan demikian, Git Rescue melengkapi celah mendasar yang ditinggalkan oleh tool ensiklopedis konvensional.\"*
