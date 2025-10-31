# tracker/report.py
"""
Modul untuk membangun laporan dalam format Markdown.
"""

from pathlib import Path

def build_markdown_report(data):
    """Membangun string Markdown dari data rekap."""
    lines = []
    lines.append("# Rekap Nilai Mahasiswa\n")
    lines.append("| NIM | Nama | Hadir (%) | Nilai Akhir | Predikat |")
    lines.append("|---|---|---:|---:|:---:|")
    for row in data:
        lines.append(f"| {row['nim']} | {row['nama']} | {row['hadir']:.1f} | {row['nilai_akhir']:.2f} | {row['predikat']} |")
    return "\n".join(lines)

def save_text(path, content):
    """Menyimpan teks ke file Markdown di folder out/"""
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    path.write_text(content, encoding="utf-8")
