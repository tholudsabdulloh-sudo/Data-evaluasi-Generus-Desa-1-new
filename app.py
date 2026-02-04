import pandas as pd
from datetime import datetime

# Data dari TARGET_MASTER
TARGET_MASTER = {
    "Kelas A": {
        "Tahun Pertama": {
            "Juli": {"quran": "Al Angkabut 45 - Arrum 24", "hadist": "Kitabussholah 1-18", "surat": "An-Nas s/d Al-Kafirun", "doa": "Doa kumpulan nabi muhammad", "dalil": "Mengaji (2 dalil)"},
            # ... data lengkap dari kode sebelumnya
        }
    }
}

# Konversi TARGET_MASTER ke DataFrame
target_data = []
for kelas, tahun_data in TARGET_MASTER.items():
    for tahun, bulan_data in tahun_data.items():
        for bulan, target in bulan_data.items():
            target_data.append({
                "Kelas": kelas,
                "Tahun": tahun,
                "Bulan": bulan,
                "Target Quran": target["quran"],
                "Target Hadist": target["hadist"],
                "Target Surat": target["surat"],
                "Target Doa": target["doa"],
                "Target Dalil": target["dalil"]
            })

df_target = pd.DataFrame(target_data)

# Data kriteria nilai
kriteria_nilai = [
    {"Persentase": "95-100%", "Huruf": "A", "Predikat": "Sangat Baik", "Keterangan": "Menguasai materi dengan sempurna"},
    {"Persentase": "85-94%", "Huruf": "A-", "Predikat": "Baik", "Keterangan": "Menguasai materi dengan baik"},
    {"Persentase": "75-84%", "Huruf": "B+", "Predikat": "Cukup Baik", "Keterangan": "Memahami materi cukup baik"},
    {"Persentase": "65-74%", "Huruf": "B", "Predikat": "Cukup", "Keterangan": "Memahami materi dasar"},
    {"Persentase": "55-64%", "Huruf": "C", "Predikat": "Kurang", "Keterangan": "Perlu bimbingan lebih"},
    {"Persentase": "0-54%", "Huruf": "D", "Predikat": "Sangat Kurang", "Keterangan": "Perlu pengulangan materi"}
]

df_kriteria = pd.DataFrame(kriteria_nilai)

# Data template santri
data_santri = [
    {
        "ID": "GEN001",
        "Nama Lengkap": "Ahmad Fauzi",
        "Tempat Lahir": "Jakarta",
        "Tanggal Lahir": "15-08-2010",
        "Alamat": "Jl. Merdeka No. 10",
        "No HP Orang Tua": "081234567890",
        "Tanggal Masuk": "01-07-2023",
        "Kelas Sekarang": "Kelas A",
        "Kelompok": "LA 1"
    },
    {
        "ID": "GEN002",
        "Nama Lengkap": "Siti Nurhaliza",
        "Tempat Lahir": "Bandung",
        "Tanggal Lahir": "22-03-2011",
        "Alamat": "Jl. Asia Afrika No. 5",
        "No HP Orang Tua": "081298765432",
        "Tanggal Masuk": "01-07-2023",
        "Kelas Sekarang": "Kelas B",
        "Kelompok": "C 2"
    }
]

df_santri = pd.DataFrame(data_santri)

# Template data evaluasi
template_evaluasi = pd.DataFrame(columns=[
    "No", "Tanggal", "Nama Santri", "Kelompok", "Kelas", "Tahun", 
    "Bulan", "Minggu", "Quran (%)", "Hadist (%)", "Surat (%)", 
    "Doa (%)", "Dalil (%)", "Rata-rata (%)", "Keterangan", 
    "Penguji", "Target Quran", "Target Hadist"
])

# Template rekap bulanan
template_rekap = pd.DataFrame(columns=[
    "Bulan", "Nama Santri", "Kelas", "Minggu 1", "Minggu 2", 
    "Minggu 3", "Minggu 4", "Rata-rata", "Quran", "Hadist", 
    "Surat", "Doa", "Dalil", "Total", "Keterangan", "Peringkat"
])

# Data statistik contoh
statistik_data = {
    "METRIK": ["Jumlah Santri", "Total Evaluasi", "Rata-rata Umum", "Santri Terbaik", "Bulan Terbaik"],
    "NILAI": ["50", "1200", "86.4%", "Siti Nurhaliza (94%)", "November (88.5%)"]
}

df_statistik = pd.DataFrame(statistik_data)

# Buat file Excel dengan multiple sheets
with pd.ExcelWriter("Template_Evaluasi_Generus.xlsx", engine='openpyxl') as writer:
    # Sheet 1: Template Evaluasi
    template_evaluasi.to_excel(writer, sheet_name='DATA_EVALUASI', index=False)
    
    # Sheet 2: Target Kurikulum
    df_target.to_excel(writer, sheet_name='TARGET_KURIKULUM', index=False)
    
    # Sheet 3: Template Rekap
    template_rekap.to_excel(writer, sheet_name='REKAP_BULANAN', index=False)
    
    # Sheet 4: Statistik
    df_statistik.to_excel(writer, sheet_name='STATISTIK', index=False)
    
    # Sheet 5: Kriteria Nilai
    df_kriteria.to_excel(writer, sheet_name='KRITERIA_NILAI', index=False)
    
    # Sheet 6: Data Santri
    df_santri.to_excel(writer, sheet_name='DATA_SANTRI', index=False)
    
    # Sheet 7: Instruksi
    instruksi = pd.DataFrame({
        "KOLOM": ["DATA_EVALUASI", "TARGET_KURIKULUM", "REKAP_BULANAN", "STATISTIK"],
        "KETERANGAN": [
            "Untuk input data evaluasi harian/mingguan per santri",
            "Database target pembelajaran (JANGAN DIUBAH)",
            "Template untuk rekap nilai bulanan (isi manual)",
            "Dashboard statistik (isi manual atau otomatis)"
        ]
    })
    instruksi.to_excel(writer, sheet_name='INSTRUKSI', index=False)

print("File Excel 'Template_Evaluasi_Generus.xlsx' berhasil dibuat!")

# File Excel sederhana untuk input cepat
data_input = pd.DataFrame(columns=[
    "Tanggal", "Nama", "Kelompok", "Kelas", "Bulan",
    "Quran_Materi", "Quran_Makna", "Quran_Ket", 
    "Hadist_Materi", "Hadist_Makna", "Hadist_Ket",
    "Surat_Hafalan", "Doa_Hafalan", "Dalil_Hafalan",
    "Total_Quran", "Total_Hadist", "Catatan"
])

data_input.to_excel("Input_Evaluasi_Generus.xlsx", index=False)
print("File 'Input_Evaluasi_Generus.xlsx' untuk input cepat juga dibuat!")
