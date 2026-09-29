# Brief v07: Anatomi, Sejarah, & Desain UI/UX "Git: What Is It & Why It Exists"

Dokumen ini adalah kajian komprehensif mengenai latar belakang historis lahirnya Git, filosofi arsitekturnya, analisis kritis mengapa antarmuka baris perintah (CLI) Git terkenal membingungkan (*poor UX*), serta bagaimana **Git Rescue** merancang ulang antarmuka visual agar pengguna memahami mental model Git secara akurat tanpa rasa takut.

---

## 1. Sejarah Kelahiran Git: Drama 10 Hari di Bulan April 2005

Untuk memahami cara kerja Git, kita harus memahami alasan mendasar mengapa Git diciptakan: **bukan karena tren, melainkan karena keterpaksaan dan krisis darurat.**

```
1991 - 2002: Era Patch Manual (Tarball & Email)
   │  Linux Kernel dikelola manual dengan kirim file .diff via mailing list.
   ▼
2002 - 2005: Era BitKeeper (Proprietary VCS Komersial)
   │  Perusahaan BitMover memberi lisensi gratis bersyarat kepada pengembang Linux.
   ▼
April 2005: Krisis BitKeeper Meledak
   │  Andrew Tridgell (pembuat Samba) mencoba me-reverse-engineer protokol BitKeeper.
   │  Larry McVoy (CEO BitMover) mencabut izin gratis komunitas Linux.
   ▼
7 - 17 April 2005: Linus Torvalds Mengurung Diri
   │  Linus menolak semua VCS yang ada (CVS, SVN, Monotone dinilai lambat & cacat arsitektur).
   ▼
Juni 2005: Git Resmi Mengelola Linux Kernel 2.6.12
```

### Mengapa Linus Menolak Tool yang Ada Saat Itu (CVS & Subversion)?
1. **Model Terpusat (*Centralized VCS*):** Di CVS dan SVN, setiap commit dan pengecekan log membutuhkan koneksi internet ke satu server pusat. Jika server mati atau developer berada di pesawat, kerja terhenti total.
2. **Branching Adalah Mimpi Buruk di SVN:** Pada SVN, membuat *branch* berarti menyalin seluruh folder proyek (*expensive copy*). Akibatnya, programmer jarang berani membuat branch karena lambat dan rawan error.
3. **Integritas Data Rendah:** Sistem lama tidak menjamin apakah data yang tersimpan mengalami korupsi bit (*bit rot*) di hard disk tanpa terdeteksi.

Linus menetapkan prinsip desain Git:
- **Kecepatan Brutal:** Operasi lokal harus instan (kurang dari sepersekian detik).
- **Branching Ringan sebagai Warga Kelas Satu:** Membuat branch hanya berupa file teks berukuran 41 byte yang berisi hash commit.
- **Kriptografis (*Content-Addressable Storage*):** Setiap perubahan diverifikasi dengan hash SHA-1. Jika satu huruf berubah di masa lalu, seluruh rantai hash akan berubah, mencegah manipulasi riwayat.
- **Terdistribusi Penuh (*Distributed VCS*):** Setiap laptop developer memiliki repositori dan riwayat penuh (*complete mirror*).

---

## 2. Mengapa Sistem File Biasa & Word/Docs Gagal untuk Kode?

Seringkali pemula bertanya: *"Kenapa kita tidak pakai Google Docs yang otomatis menyimpan setiap detik?"*

| Fitur / Kebutuhan | Google Docs / Cloud Drive | Git (Version Control System) |
| :--- | :--- | :--- |
| **Model Perubahan** | Riwayat garis lurus (*linear stream of edits*). | Graf bercabang non-linear (*Directed Acyclic Graph*). |
| **Cakupan File** | Satu dokumen tunggal terisolasi. | Ribuan file dalam satu proyek yang saling bergantung. |
| **Pengerjaan Fitur** | Semua orang mengetik di kanvas yang sama (risiko merusak teks yang belum selesai). | Setiap orang bekerja di *branch* terisolasi tanpa mengganggu kode yang sedang berjalan di produksi. |
| **Format File** | Dokumen teks terformat / biner terkompresi. | Teks mentah (*plain text*) yang dapat dianalisis per baris. |
| **Persetujuan Rilis** | Tidak ada gerbang validasi rilis. | Ada mekanisme *Pull Request*, *Code Review*, dan *Atomic Commit*. |

---

## 3. Analisis Kritis: Mengapa UX Baris Perintah (CLI) Git Sangat Buruk?

Git dirancang oleh Linus Torvalds untuk para *hacker* kernel Linux tingkat dewa, bukan untuk pemula. Akibatnya, Git memiliki **bencana desain UX (*UX Nightmare*)** yang melegenda:

### 3.1 Masalah 1: "Satu Perintah Memiliki 5 Fungsi Berbeda" (Kasus `git checkout`)
Sebelum Git versi 2.23 (rilis 2019), perintah `git checkout` melakukan hal-hal yang saling bertolak belakang:
- Berpindah cabang: `git checkout nama-branch`
- Membuat cabang baru: `git checkout -b branch-baru`
- Membuang editan file kerja: `git checkout -- file.txt` *(bersifat destruktif!)*
- Masuk ke detached HEAD: `git checkout a1b2c3`

> **Solusi Git Modern:** Git akhirnya memecahnya menjadi `git switch` (pindah branch) dan `git restore` (batalkan ketikan). Namun, 90% tutorial di internet masih mengajarkan `checkout` lama yang membingungkan.

### 3.2 Masalah 2: Terminologi Mengerikan yang Memicu Panik
- **"You are in 'detached HEAD' state"**: Terdengar seperti kepala terpenggal, padahal artinya pointer penunjuk hanya sedang melihat commit lama tanpa terikat pada ujung cabang mana pun.
- **"git reset --hard"**: Tidak ada dialog konfirmasi. Sekali salah tekan enter, kode yang belum dicommit akan musnah selamanya.
- **"Fast-Forward Merge"**: Pemula tidak paham mengapa terkadang ada commit merge baru dan terkadang cabangnya hanya berpindah ujung.

---

## 4. Pendekatan Desain UI/UX Git Rescue: Jembatan Kognitif Pemula

Git Rescue menata ulang cara pemula berinteraksi dengan Git melalui **3 Prinsip Desain Kognitif**:

```
┌────────────────────────────────────────────────────────┐
│              PRINSIP 1: RADAR STATUS & HEAD            │
│ Selalu tampilkan posisi HEAD, branch aktif, dan status │
│ staging secara visual di bagian atas layar.            │
├────────────────────────────────────────────────────────┤
│              PRINSIP 2: RISK-AWARE LABELS              │
│ Setiap tombol perintah diberi badge risiko:            │
│ 🟢 SAFE (revert)  🟡 REWRITE (amend)  🔴 DANGER (reset)│
├────────────────────────────────────────────────────────┤
│              PRINSIP 3: DUAL-VIEWPORT CAUSALITY        │
│ Atas = Metafora Nyata (Pagar/HP/Game)                  │
│ Bawah = Directed Acyclic Graph (DAG) Interaktif        │
└────────────────────────────────────────────────────────┘
```

### Komponen Kunci Halaman "Git: What Is It":
1. **Timeline Interaktif Interaktif 2005 ➔ Sekarang:** Pengguna bisa menggeser slider tahun untuk melihat bagaimana Linux Kernel berkembang dari email patch manual hingga Git modern.
2. **Kalkulator Kerusakan Data (*Safety Sandbox*):** Memperlihatkan simulasi langsung perbedaan antara `git reset --soft`, `git reset --mixed`, dan `git reset --hard` terhadap file kerja.
3. **Kamus Jargon ke Bahasa Manusia:**
   - *Repository* = Folder proyek yang punya memori masa lalu.
   - *Commit* = Foto snapshot kondisi seluruh file pada satu detik tertentu.
   - *Branch* = Garis waktu alternatif agar eksperimen tidak merusak proyek utama.
   - *HEAD* = Jarum pemutar piringan hitam yang menunjuk ke lagu yang sedang diputar.
   - *Merge* = Menggabungkan hasil eksperimen dari cabang kembali ke jalur utama.
