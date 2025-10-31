# tracker/rekap_kelas.py
"""
Modul rekap kelas.
Mengelola kumpulan objek Mahasiswa dan Penilaian.
"""

import csv
from pathlib import Path
from tracker.mahasiswa import Mahasiswa
from tracker.penilaian import Penilaian


class RekapKelas:
    """Menyimpan dan mengelola data mahasiswa beserta penilaiannya."""

    def __init__(self):
        self.data = {}  # {nim: {'mhs': obj, 'nilai': obj}}
        self._init_data_folder()

    def _init_data_folder(self):
        """Membuat folder dan file CSV default jika belum ada."""
        data_path = Path("data")
        data_path.mkdir(exist_ok=True)

        attendance = data_path / "attendance.csv"
        grades = data_path / "grades.csv"

        if not attendance.exists():
            with open(attendance, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["nim", "nama", "hadir_persen"])

        if not grades.exists():
            with open(grades, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["nim", "quiz", "tugas", "uts", "uas"])

    # ===============================
    # === CRUD MAHASISWA & NILAI ===
    # ===============================

    def tambah_mahasiswa(self, nim, nama):
        """Menambahkan mahasiswa baru ke rekap."""
        if nim in self.data:
            raise ValueError("Mahasiswa dengan NIM tersebut sudah ada.")
        self.data[nim] = {"mhs": Mahasiswa(nim, nama), "nilai": Penilaian()}

    def set_hadir(self, nim, persen):
        """Mengubah persentase kehadiran mahasiswa."""
        if nim not in self.data:
            raise ValueError("NIM tidak ditemukan.")
        self.data[nim]["mhs"].hadir_persen = persen

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        """Mengubah data penilaian mahasiswa."""
        if nim not in self.data:
            raise ValueError("NIM tidak ditemukan.")
        self.data[nim]["nilai"] = Penilaian(quiz, tugas, uts, uas)

    # ===============================
    # === LOAD & SAVE TO CSV ===
    # ===============================

    def load_data(self, attendance_path="data/attendance.csv", grades_path="data/grades.csv"):
        """Membaca data dari dua file CSV: presensi dan nilai."""
        self.data.clear()

        # Muat data presensi
        try:
            with open(attendance_path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    nim = row["nim"].strip()
                    nama = row["nama"].strip()
                    hadir = float(row["hadir_persen"])
                    self.tambah_mahasiswa(nim, nama)
                    self.set_hadir(nim, hadir)
        except FileNotFoundError:
            raise FileNotFoundError("File attendance.csv tidak ditemukan.")

        # Muat data nilai
        try:
            with open(grades_path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    nim = row["nim"].strip()
                    if nim in self.data:
                        quiz = float(row["quiz"])
                        tugas = float(row["tugas"])
                        uts = float(row["uts"])
                        uas = float(row["uas"])
                        self.set_penilaian(nim, quiz, tugas, uts, uas)
        except FileNotFoundError:
            raise FileNotFoundError("File grades.csv tidak ditemukan.")

    def simpan_data(self, attendance_path="data/attendance.csv", grades_path="data/grades.csv"):
        """Menyimpan data mahasiswa dan nilai ke file CSV."""
        # Simpan presensi
        with open(attendance_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nim", "nama", "hadir_persen"])
            for nim, item in self.data.items():
                mhs = item["mhs"]
                writer.writerow([mhs.nim, mhs.nama, mhs.hadir_persen])

        # Simpan nilai
        with open(grades_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nim", "quiz", "tugas", "uts", "uas"])
            for nim, item in self.data.items():
                nilai = item["nilai"]
                writer.writerow([
                    nim,
                    nilai.quiz,
                    nilai.tugas,
                    nilai.uts,
                    nilai.uas
                ])

    # ===============================
    # === PENGOLAHAN NILAI ===
    # ===============================

    def predikat(self, nilai):
        """Mengubah nilai akhir menjadi huruf A–E."""
        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 55:
            return "D"
        else:
            return "E"

    def rekap(self):
        """Mengembalikan list berisi rekap nilai mahasiswa."""
        hasil = []
        for nim, item in self.data.items():
            mhs = item["mhs"]
            nilai = item["nilai"]
            total = nilai.nilai_akhir()
            hasil.append({
                "nim": mhs.nim,
                "nama": mhs.nama,
                "hadir": mhs.hadir_persen,
                "nilai_akhir": total,
                "predikat": self.predikat(total)
            })
        return hasil
