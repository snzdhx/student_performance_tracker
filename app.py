# app.py
"""
Aplikasi utama Student Performance Tracker.
Mengelola data mahasiswa, nilai, dan laporan dalam format Markdown.
"""

from tracker import RekapKelas, build_markdown_report, save_text

def main():
    rekap = RekapKelas()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Muat data dari CSV")
        print("2) Tambah mahasiswa")
        print("3) Ubah presensi")
        print("4) Ubah nilai")
        print("5) Lihat rekap")
        print("6) Simpan laporan Markdown")
        print("7) Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            rekap.load_data()
            print("✅ Data berhasil dimuat dari CSV.")

        elif pilihan == "2":
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan nama: ")
            try:
                rekap.tambah_mahasiswa(nim, nama)
                rekap.simpan_data()
                print("✅ Mahasiswa berhasil ditambahkan dan disimpan.")
            except ValueError as e:
                print("❌", e)

        elif pilihan == "3":
            nim = input("Masukkan NIM: ")
            try:
                persen = float(input("Masukkan persentase kehadiran (0–100): "))
                rekap.set_hadir(nim, persen)
                rekap.simpan_data()
                print("✅ Data presensi berhasil diperbarui dan disimpan.")
            except ValueError as e:
                print("❌", e)

        elif pilihan == "4":
            nim = input("Masukkan NIM: ")
            try:
                quiz = float(input("Masukkan nilai quiz: "))
                tugas = float(input("Masukkan nilai tugas: "))
                uts = float(input("Masukkan nilai UTS: "))
                uas = float(input("Masukkan nilai UAS: "))
                rekap.set_penilaian(nim, quiz, tugas, uts, uas)
                rekap.simpan_data()
                print("✅ Data nilai berhasil diperbarui dan disimpan.")
            except ValueError as e:
                print("❌", e)

        elif pilihan == "5":
            data = rekap.rekap()
            if not data:
                print("⚠️ Belum ada data.")
            else:
                print("\n# Rekap Nilai Mahasiswa")
                print("| NIM | Nama | Hadir (%) | Nilai Akhir | Predikat |")
                print("|---|---|---:|---:|:---:|")
                for r in data:
                    print(f"| {r['nim']} | {r['nama']} | {r['hadir']:.1f} | {r['nilai_akhir']:.2f} | {r['predikat']} |")

        elif pilihan == "6":
            data = rekap.rekap()
            if not data:
                print("⚠️ Tidak ada data untuk disimpan.")
            else:
                content = build_markdown_report(data)
                save_text("out/report.md", content)
                print("✅ Laporan berhasil disimpan di out/report.md")

        elif pilihan == "7":
            print("Keluar dari program.")
            break

        else:
            print("❌ Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
