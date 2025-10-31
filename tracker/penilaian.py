# tracker/penilaian.py
"""
Kelas Penilaian untuk menyimpan nilai quiz, tugas, UTS, dan UAS.
Berisi validasi nilai serta perhitungan nilai akhir berbobot.
"""

class Penilaian:
    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        """Inisialisasi nilai komponen"""
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    @property
    def quiz(self):
        return self._quiz

    @quiz.setter
    def quiz(self, value):
        self._quiz = self._validate(value, "Quiz")

    @property
    def tugas(self):
        return self._tugas

    @tugas.setter
    def tugas(self, value):
        self._tugas = self._validate(value, "Tugas")

    @property
    def uts(self):
        return self._uts

    @uts.setter
    def uts(self, value):
        self._uts = self._validate(value, "UTS")

    @property
    def uas(self):
        return self._uas

    @uas.setter
    def uas(self, value):
        self._uas = self._validate(value, "UAS")

    def _validate(self, value, nama):
        """Validasi nilai agar berada di rentang 0–100"""
        try:
            value = float(value)
        except ValueError:
            raise ValueError(f"Nilai {nama} harus berupa angka.")
        if not (0 <= value <= 100):
            raise ValueError(f"Nilai {nama} harus antara 0–100.")
        return value

    def nilai_akhir(self):
        """Menghitung nilai akhir berbobot"""
        return (self.quiz * 0.15) + (self.tugas * 0.25) + (self.uts * 0.25) + (self.uas * 0.35)
