# Git Rescue: Brief Skripsi (v01 - Ide Awal & Fondasi Sistem)

**Judul Kerja:**  
*Perancangan Website Statis Interaktif dengan Skenario Lapangan Tersimulasi untuk Membantu Pemula Mengatasi Masalah Git Lewat Visualisasi Berbasis Masalah dan Analogi Bertingkat*

---

## BAB 1: Overview & Latar Belakang

### 1.1 Latar Belakang
Orang jarang belajar Git secara khusus dan terencana sejak awal. Sebagian besar pemula baru membuka tutorial Git di tengah kepanikan proyek saat terjadi kesalahan (misal: conflict, salah commit ke main, atau branch hilang), sementara fokus dan perhatian mereka tersedot ke tenggat waktu (*deadline*) dan tuntutan klien.

Alat bantu (*tools*) yang ada saat ini (*Learn Git Branching*, *Visualizing Git*, *Oh My Git!*) umumnya mengasumsikan pengguna memiliki waktu luang untuk belajar:
- Sebagian membuka antarmuka dengan modal teks yang panjang dan kurikulum bertingkat.
- Sebagian lain membuka dengan terminal hitam kosong tanpa arahan atau petunjuk aksi awal.

### 1.2 Ide Inti (Pilar Git Rescue)
1. **Rescue-First (< 60 Detik):** Pengguna memilih masalah yang sedang dialami, lalu langsung mendapatkan baris perintah, grafik sebelum/sesudah, dan script siap pakai.
2. **Skenario Lapangan (IRL Simulated):** Setiap kasus bukan sekadar sintaks perintah, melainkan kejadian kerja nyata yang dilengkapi latar cerita, tekanan waktu, pilihan tindakan, dan konsekuensi riil.
3. **Analogi 3 Level:** Menjelaskan konsep Git lewat 3 tangga pemahaman:
   - Level 1: Awam (Skripsi / Cat Pagar Rumah)
   - Level 2: Menengah (Komponen Mobil & Lapisan OS Smartphone)
   - Level 3: Developer (Hash Commit, Pointer HEAD, Branch)
4. **Raw File Lab:** Pengguna melihat isi mentah (*raw bytes* / hex) dari tiap format file, sehingga memahami secara empiris mengapa Git sangat cocok untuk file teks/kode tetapi tidak dirancang untuk file biner (Word, Excel, gambar, video).
5. **Skripsi sebagai Metafora:** Skripsi hanya dipakai sebagai metafora mental model. Praktik di dalam web menggunakan file teks nyata (`bab1.md`, `data.csv`), bukan file `.docx`.

---

### 1.3 Daftar 8 Skenario Lapangan (Rencana Inti)

| No | Situasi Lapangan | Konsep Git Terkait | Dilema / Tekanan Kasus |
| :---: | :--- | :--- | :--- |
| **1** | Klien minta balik ke desain kemarin | `git revert` vs `git reset` | Desain baru dinilai jelek oleh klien; riwayat lama harus aman jika rekan kerja sudah terlanjur pull. |
| **2** | Salah commit ke `main`, padahal harusnya di branch fitur | `git branch` + `git reset` | Pekerjaan belum siap rilis tapi sudah bercampur di cabang produksi. |
| **3** | Menyimpan password / API Key di repo | `git reset` / `amend` + invalidate | File `.env` terunggah; harus dibersihkan dari commit sebelum dipush ke public remote. |
| **4** | Kamu dan rekan mengedit file & baris yang sama | Merge conflict resolution | Dua perubahan valid bertabrakan; menentukan bagian mana yang dipertahankan. |
| **5** | Disuruh bos pindah tugas mendadak saat coding | `git stash` (`push` & `pop`) | Pekerjaan setengah jalan belum layak dicommit, tapi harus segera checkout ke branch urgent. |
| **6** | Butuh satu perbaikan bug spesifik dari branch lain | `git cherry-pick` | Tidak boleh menggabungkan seluruh branch fitur lain yang belum stabil, hanya butuh 1 commit hotfix. |
| **7** | Salah ketik pesan commit / lupa menyertakan 1 file | `git commit --amend` | Memperbaiki commit terakhir tanpa membuat commit sampah tambahan. |
| **8** | Branch penting terhapus tanpa sengaja | `git reflog` + `git checkout -b` | Panik branch hilang dari daftar; memulihkan commit dangling via log pointer HEAD. |

---

### 1.4 Panduan Menjawab Pertanyaan Penguji Sidang

| Pertanyaan Penguji | Jawaban Strategis Mahasiswa |
| :--- | :--- |
| *“Google Docs, MS Word, dan Excel kan sudah punya version history otomatis, kenapa masih butuh Git?”* | **Betul, dan itu sudah sangat cukup jika proyek hanya berupa satu file tunggal.** Namun, proyek software dan sistem modern terdiri dari ratusan file teks yang saling terhubung, dikerjakan secara paralel oleh tim dengan alur bercabang (*branching*), serta membutuhkan mekanisme penggabungan (*merge*) yang deterministik. |
| *“Kenapa Git tidak cocok melacak semua jenis file seperti gambar atau dokumen Word?”* | **Git membandingkan perbedaan teks per baris (*line-by-line diff*).** Gambar, audio, video, serta format `.docx`/`.xlsx` pada dasarnya adalah file biner terkompresi (arsip ZIP). Ketika ada 1 huruf diubah di Word, seluruh susunan biner berubah, sehingga Git hanya tahu file tersebut \"berubah secara utuh\", tanpa bisa memperlihatkan baris mana yang berubah dan tidak bisa di-merge secara otomatis. |
| *“Apa perbedaan mendasar antara Git dan GitHub?”* | **Git adalah perangkat lunak lokal (VCS engine)** yang bekerja di mesin pengembang tanpa internet. **GitHub adalah layanan hosting daring berbasis cloud** untuk menyimpan remote repository Git dan memfasilitasi kolaborasi tim. Penelitian ini berfokus penuh pada penguasaan mental model Git lokal. |

---

### 1.5 Tujuan, Manfaat, dan Luaran

* **Tujuan Penelitian:**  
  Membantu pemula keluar dari kepanikan masalah Git dalam waktu **kurang dari 60 detik** serta membangun intuisi logis melalui visualisasi interaktif dan skenario realistis.
* **Manfaat:**
  - *Bagi Pemula:* Meningkatkan rasa percaya diri untuk mencoba Git tanpa takut merusak repositori kerja.
  - *Bagi Pendidik:* Menyediakan media demonstrasi interaktif yang aman untuk praktikum di kelas.
  - *Bagi Akademik:* Memberikan model perancangan *Scenario-Based Learning* (SBL) yang memadukan transfer analogi berjenjang pada topik teknis.
* **Target Luaran (*Outcome*):**
  - Prototipe website interaktif yang dapat diakses publik.
  - 8 skenario lapangan teruji.
  - Hasil evaluasi pengujian pengguna: Skor SUS (*System Usability Scale*), waktu penyelesaian tugas (*time-on-task*), dan tingkat keberhasilan (*task completion rate*).
* **Batasan Masalah:**
  - Ruang lingkup berfokus pada Git lokal (tanpa sistem autentikasi/backend server).
  - Menggunakan engine simulasi visual buatan sendiri (agar ringan, deterministik, dan bebas risiko merusak file asli pengguna).

---

## BAB 2: Technical Brief

### 2.1 Akses & Deployment
- Dapat diakses langsung melalui peramban ponsel (*mobile-first*) maupun laptop.
- Tanpa instalasi perangkat lunak tambahan dan tanpa registrasi akun.
- Dihosting secara statis (GitHub Pages / Netlify / Cloudflare Pages).

### 2.2 Tabel Komponen & Arsitektur Sistem

| Komponen | Pilihan Teknologi | Peran & Fungsi |
| :--- | :--- | :--- |
| **Frontend UI** | HTML5, Modern Vanilla CSS, Vanilla JavaScript (atau Vite) | Antarmuka interaktif yang sangat ringan, mobile-first, dan tanpa overhead runtime besar. |
| **Git Simulator Engine** | Logika State Machine JavaScript murni | Mensimulasikan graph commit, pointer branch, HEAD, dan index staging secara deterministik. |
| **Scenario Engine** | `scenarios.json` | Pusat data tunggal (*single source of truth*) yang memuat cerita, kondisi repo awal, target, pilihan aksi, dan konsekuensi tiap opsi. |
| **Visualizer Graph** | SVG Dinamis (atau D3.js ringan) | Merender diagram Directed Acyclic Graph (DAG) sebelum vs sesudah aksi dieksekusi. |
| **Raw Viewer** | FileReader API + Byte Sampler mini | Menampilkan representasi file dalam 3 mode: Normal, Raw Text, dan Hex Dump, disertai deteksi *magic bytes*. |
| **Shell Exporter** | Blob API + Template Literals | Menghasilkan file skrip siap unduh `.ps1` (PowerShell) dan `.sh` (Bash) dengan komentar instruktif. |
| **State Storage** | `localStorage` Browser | Menyimpan progres skenario dan skor kuis secara lokal tanpa server. |
| **Metodologi** | *Design Thinking* | Tahapan riset: Empathize (wawancara pemula), Define, Ideate, Prototype, Test. |

---

## BAB 3: UI/UX Brief & Spesifikasi 8 View

### 3.1 Prinsip Desain
1. **Mobile-First (360px - 412px):** Nyaman dibuka di layar ponsel saat pengguna sedang menatap layar laptop yang bermasalah.
2. **Satu Ide Per Layar:** Menghindari beban kognitif berlebih (*cognitive overload*).
3. **Aksi Dulu, Penjelasan Kemudian:** Tombol solusi dan salin perintah tampil di area utama sebelum penjelasan panjang.
4. **Aturan < 2 Ketukan:** Dari halaman utama ke baris solusi maksimal hanya butuh 2 kali tap.
5. **Zero Blank Screen:** Tidak ada terminal kosong yang membingungkan tanpa petunjuk.

### 3.2 Diagram Alur Navigasi

```text
               ┌───────────────────────┐
               │    View 1: Home       │
               │ (Mode: Rescue/Latihan)│
               └───────────┬───────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
  ┌─────────────────────┐     ┌─────────────────────┐
  │   View 2: Rescue    │     │  View 3: Scenario   │
  │ (Masalah -> Solusi) │     │ (Simulasi Lapangan) │
  └──────────┬──────────┘     └──────────┬──────────┘
             │                           │
             ├─────────────┬─────────────┤
             ▼             ▼             ▼
      ┌────────────┐ ┌───────────┐ ┌───────────┐
      │  View 4:   │ │  View 5:  │ │  Layar    │
      │  Sandbox   │ │  Export   │ │Konsekuensi│
      └────────────┘ └───────────┘ └───────────┘
             │
   (Jalur Eksplorasi Khusus)
   ├─► View 6: Story (3 Analogi)
   ├─► View 7: Raw File Lab
   └─► View 8: Quiz Evaluator
```

---

### 3.3 Wireframe Rinci 8 View Utama

#### View 1: Home (Pilih Masalah Cepat)
```text
┌─ GIT RESCUE ─────────────────────────┐
│ Mode: [● Rescue Cepat ] [ ○ Latihan ]│
├──────────────────────────────────────┤
│ APA YANG BARU SAJA TERJADI?          │
│                                      │
│ [ ⚡ Salah commit ke branch main  → ] │
│ [ ⚡ Batalkan commit terakhir     → ] │
│ [ ⚡ Ada konflik saat merge       → ] │
│ [ ⚡ Mau simpan kerjaan mendadak  → ] │
│ [ ⚡ Password tidak sengaja commit→ ] │
│                                      │
│ ──────────────────────────────────── │
│ 📖 Pelajari Intuisi Dasar (Story)    │
│ 🔬 Raw File Lab (Kenapa Bukan Docs?) │
└──────────────────────────────────────┘
```

#### View 2: Rescue (Solusi Cepat < 60 Detik)
```text
┌─ RESCUE · BATALKAN COMMIT TERAKHIR ──┐
│ Simpan hasil ketikan? [ ● IYA ]      │
├──────────────────────────────────────┤
│ GRAFIK PERUBAHAN:                    │
│ SEBELUM:  A ── B ── C (HEAD)         │
│ SESUDAH:  A ── B (HEAD)              │
│ *Perubahan C tetap aman di Staging ✓ │
├──────────────────────────────────────┤
│ PERINTAH SIAP JALANKAN:              │
│ $ git reset --soft HEAD~1            │
│ [ 📋 Salin ]  [ 🧪 Sandbox ]         │
├──────────────────────────────────────┤
│ [ 📥 Ekspor Script (.ps1 / .sh)    ] │
└──────────────────────────────────────┘
```

#### View 3: Scenario (Simulasi Lapangan / Pembeda Utama)
```text
┌─ SKENARIO 1 · KLIEN MENUNGGU ────────┐
│ Kasus: Klien minta balik ke desain   │
│ kemarin karena desain baru ditolak.  │
│ Waktu: 03:45 | Sisa Nyawa: ❤️❤️❤️     │
├──────────────────────────────────────┤
│ REPO SAAT INI:                       │
│ main: A ── B ── C ── D (HEAD)        │
│ Catatan: D sudah pernah di-push tim  │
├──────────────────────────────────────┤
│ APA TINDAKANMU?                      │
│ ( ) A. git reset --hard B            │
│ ( ) B. git revert D                  │
│ ( ) C. git checkout B                │
├──────────────────────────────────────┤
│ [ 💡 Minta Saran ] [ 🚀 Eksekusi ]   │
└──────────────────────────────────────┘
```

#### View 4: Layar Hasil & Konsekuensi Tindakan
```text
┌─ EVALUASI KEPUTUSAN ─────────────────┐
│ KEPUTUSAN: git revert D              │
│ STATUS   : ✅ TEPAT & AMAN           │
├──────────────────────────────────────┤
│ DAMPAK TINDAKAN:                     │
│ Riwayat commit tetap utuh. Dibuat    │
│ commit baru E yang membatalkan D.    │
│                                      │
│ ⚠️ MENGAPA BUKAN git reset --hard B? │
│ Karena commit D sudah ditarik rekan  │
│ tim. Jika di-reset hard, riwayat repo│
│ tim akan rusak dan bentrok parah!    │
├──────────────────────────────────────┤
│ [ Coba Kasus di Sandbox ] [ Lanjut ➔]│
└──────────────────────────────────────┘
```

#### View 5: Sandbox (Laboratorium Interaktif Bebas Risiko)
```text
┌─ SANDBOX TERMINAL ───────────────────┐
│ Status: Cabang main | 3 Commits      │
│ Diagram: (A) ── (B) ── (C) [HEAD]    │
├──────────────────────────────────────┤
│ Virtual Terminal:                    │
│ $ git ______________________________ │
│ Saran: [git status] [git log] [reset]│
├──────────────────────────────────────┤
│ [ ↶ Undo ]  [ ↷ Redo ]  [ ⟲ Reset ] │
└──────────────────────────────────────┘
```

#### View 6: Export Studio (Unduh Skrip PowerShell / Bash)
```text
┌─ EXPORT STUDIO ──────────────────────┐
│ Platform: (● PowerShell) (○ Git Bash)│
│ Opsi    : [✓] Komentar Bahasa Indo   │
│           [✓] Cek Status Otomatis    │
├──────────────────────────────────────┤
│ Pratinjau Skrip:                     │
│ # Batalkan commit tanpa hapus teks   │
│ git reset --soft HEAD~1              │
│ git status                           │
├──────────────────────────────────────┤
│ [ 💾 Unduh .ps1 ]  [ 💾 Unduh .sh ]  │
└──────────────────────────────────────┘
```

#### View 7: Story (Tiga Level Analogi)
```text
┌─ STORY ANALOGI ──────────────────────┐
│ Pilih Level: [● Awam] [Menengah] [Dev]│
├──────────────────────────────────────┤
│ ANALOGI: MENGECAT PAGAR RUMAH        │
│ 1. Cat dasar abu-abu   = Commit 1    │
│ 2. Cat warna hijau     = Commit 2    │
│ 3. Coba motif di 1 sisi= Branch      │
│ 4. Jelek? Timpa cat    = Revert      │
├──────────────────────────────────────┤
│ 📄 KENAPA BUKAN GOOGLE DOCS?         │
│ Docs cocok untuk 1 file lurus.       │
│ Git melacak ribuan file, bercabang,  │
│ dan dikerjakan banyak orang sekaligus│
└──────────────────────────────────────┘
```

#### View 8: Raw File Lab (Eksplorasi Format File)
```text
┌─ RAW FILE LAB ───────────────────────┐
│ Format: [● md] [txt] [png] [docx]    │
│ Mode  : [Normal] [● Raw Bytes] [Hex] │
├──────────────────────────────────────┤
│ File: logo.png (2.4 KB)              │
│ Header / Magic Bytes: 89 50 4E 47    │
│ Isi Mentah:                          │
│ ▒PNG ░▒▓ IHDR ▓░▒▒▓░▒░▓▒ ▓▒░▓▒▒░▓▒   │
├──────────────────────────────────────┤
│ RESPON GIT TERHADAP FILE INI:        │
│ ✗ 'Binary files differ'              │
│ Git tidak bisa menampilkan diff teks │
│ karena format ini berupa arsip biner!│
└──────────────────────────────────────┘
```

---

## BAB 4: Metrik Keberhasilan Penelitian Skripsi

1. **Efisiensi Waktu Solusi:** Waktu dari membuka website hingga mendapatkan baris perintah perbaikan di bawah **60 detik**.
2. **System Usability Scale (SUS):** Skor uji kegunaan pengguna di atas **68 (kategori Good/Excellent)**.
3. **Task Completion Rate:** Tingkat keberhasilan pengguna menyelesaikan skenario lapangan di atas **85%**.
4. **Analisis Pola Miskonsepsi:** Mengukur persentase pemilihan opsi salah (blunder) untuk mengidentifikasi kesalahan pemahaman paling umum pada pemula.
