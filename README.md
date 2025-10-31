# Student Performance Tracker

A Python-based application for managing **student data**, **attendance**, and **grades**, while automatically generating a **Markdown report (`report.md`)**.

---

## 🇮🇩 Deskripsi (Bahasa Indonesia)

**Student Performance Tracker** adalah aplikasi sederhana berbasis Python untuk mengelola data mahasiswa, presensi, dan nilai ujian.  
Program ini dapat membuat laporan otomatis dalam format Markdown dan menyimpan hasilnya di folder `out/`.

---

## 🇬🇧 Description (English)

**Student Performance Tracker** is a simple Python program designed to manage student data, attendance, and exam grades.  
It automatically generates a Markdown report and saves it inside the `out/` folder.

---

## Struktur Proyek / Project Structure

student_performance_tracker/
│
├── tracker/
│ ├── **init**.py
│ ├── mahasiswa.py
│ ├── penilaian.py
│ ├── rekap_kelas.py
│ └── report.py
│
├── app.py
├── data/
│ ├── attendance.csv
│ └── grades.csv
│
├── out/
│ └── report.md
│
└── README.md

---

## Cara Menjalankan / How to Run

### 🇮🇩 Bahasa Indonesia

1. Pastikan sudah menginstal **Python 3.8+**
2. Buka terminal di folder proyek ini
3. Jalankan perintah berikut:
   python app.py

### 🇬🇧 English

1. Make sure **Python 3.8+** is installed
2. Open your terminal inside this project folder
3. Run the following command:
   python app.py

---

## Fitur / Features

| 🇮🇩 Fitur                | 🇬🇧 Feature Description                                                   |
| ----------------------- | ------------------------------------------------------------------------ |
| Tambah Mahasiswa        | Add new student by NIM and name                                          |
| Tambah Presensi         | Set student's attendance percentage                                      |
| Tambah Nilai            | Input `quiz`, `tugas`, `uts`, `uas` scores                               |
| Lihat Rekap Nilai       | Display student grade summary                                            |
| Muat Data dari CSV      | Load data automatically from `data/attendance.csv` and `data/grades.csv` |
| Simpan Laporan Markdown | Generate report file (`out/report.md`) automatically                     |

---

## Format CSV / CSV Format

### attendance.csv

nim,nama,hadir_persen
23001,Prima,90
23002,Sandhika,85

### grades.csv

nim,quiz,tugas,uts,uas
23001,80,85,90,88
23002,70,75,78,80

---

## Nilai Akhir & Predikat / Final Grade & Letter Score

| Nilai / Score | Predikat / Grade |
| ------------- | ---------------- |
| ≥ 85          | A                |
| ≥ 75          | B                |
| ≥ 65          | C                |
| ≥ 55          | D                |
| < 55          | E                |

---

## Contoh Output / Example Output (`out/report.md`)

# Rekap Nilai Mahasiswa / Student Grade Summary

| NIM   | Nama     | Hadir (%) | Nilai Akhir | Predikat |
| ----- | -------- | --------: | ----------: | :------: |
| 23001 | Prima    |      90.0 |       86.55 |    A     |
| 23002 | Sandhika |      85.0 |       76.75 |    B     |

---

## Catatan / Notes

- Folder `data/` dan `out/` akan dibuat otomatis jika belum ada.
- Semua file menggunakan encoding **UTF-8**.
- File `report.md` akan menimpa versi lama secara otomatis.
- Dirancang agar mudah dikembangkan untuk sistem akademik yang lebih besar.

---

📌 **Dibuat dengan Python oleh [Prima Sandhika]**
Made in Python by [Prima Sandhika]
