# tracker/mahasiswa.py
"""
Kelas Mahasiswa untuk menyimpan data dasar mahasiswa.
Berisi validasi kehadiran menggunakan property.
"""

class Mahasiswa:
    def __init__(self, nim, nama, hadir_persen=0):
        """Inisialisasi data mahasiswa"""
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0     # atribut privat (enkapsulasi)
        self.hadir_persen = hadir_persen  # lewat setter agar tervalidasi

    @property
    def hadir_persen(self):
        """Mengambil nilai kehadiran"""
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        """Menetapkan nilai kehadiran dengan validasi"""
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Nilai kehadiran harus berupa angka.")

        if not (0 <= value <= 100):
            raise ValueError("Nilai kehadiran harus antara 0–100.")

        self._hadir_persen = value

    def info(self):
        """Mengembalikan informasi mahasiswa sebagai dict"""
        return {
            "nim": self.nim,
            "nama": self.nama,
            "hadir_persen": self.hadir_persen
        }
