# =====================================================================
# PROGRAM MANAJEMEN OBAT APOTEK & PASIEN OPNAME RUMAH SAKIT
# Penerapan Operator Pembanding (==, !=, <, >, <=, >=) & Kondisional
# =====================================================================

# 1. DATA 10 JENIS OBAT DI APOTEK (Nama, Stok, Harga per Strip/Botol)
daftar_obat = [
    {"nama": "Paracetamol 500mg", "stok": 5, "harga": 10000},
    {"nama": "Amoxicillin 500mg", "stok": 25, "harga": 15000},
    {"nama": "OBH Combi Batuk", "stok": 8, "harga": 22000},
    {"nama": "Antasida Doen", "stok": 40, "harga": 8000},
    {"nama": "Vitamin C 1000mg", "stok": 12, "harga": 35000},
    {"nama": "Cetirizine 10mg", "stok": 3, "harga": 12000},
    {"nama": "Omeprazole 20mg", "stok": 18, "harga": 25000},
    {"nama": "Asam Mefenamat", "stok": 10, "harga": 14000},
    {"nama": "Betadine Cair 30ml", "stok": 30, "harga": 28000},
    {"nama": "Salep Kulit Hydrocortisone", "stok": 0, "harga": 18000},
]

# 2. DATA 10 JENIS PASIEN OPNAME RUMAH SAKIT
daftar_pasien = [
    {
        "nama": "Budi Santoso",
        "jenis_opname": "Demam Berdarah (DBD)",
        "lama_inap": 5,
        "tarif_kamar": 300000,
        "penjamin": "BPJS",
    },
    {
        "nama": "Siti Aminah",
        "jenis_opname": "Persalinan Caesar",
        "lama_inap": 4,
        "tarif_kamar": 500000,
        "penjamin": "Umum",
    },
    {
        "nama": "Andi Wijaya",
        "jenis_opname": "Tifus (Tipes)",
        "lama_inap": 6,
        "tarif_kamar": 300000,
        "penjamin": "BPJS",
    },
    {
        "nama": "Rina Marlina",
        "jenis_opname": "Pasca Operasi Usus Buntu",
        "lama_inap": 3,
        "tarif_kamar": 450000,
        "penjamin": "Asuransi",
    },
    {
        "nama": "Dedi Kurniawan",
        "jenis_opname": "Pneumonia / Paru-paru",
        "lama_inap": 8,
        "tarif_kamar": 600000,
        "penjamin": "Umum",
    },
    {
        "nama": "Maya Sari",
        "jenis_opname": "Observasi Jantung (ICU)",
        "lama_inap": 2,
        "tarif_kamar": 1200000,
        "penjamin": "BPJS",
    },
    {
        "nama": "Hendra Gunawan",
        "jenis_opname": "Patah Tulang (Ortopedi)",
        "lama_inap": 7,
        "tarif_kamar": 500000,
        "penjamin": "Umum",
    },
    {
        "nama": "Lestari Putri",
        "jenis_opname": "Gastritis Akut / Maag",
        "lama_inap": 2,
        "tarif_kamar": 250000,
        "penjamin": "BPJS",
    },
    {
        "nama": "Agus Salim",
        "jenis_opname": "Pemulihan Stroke",
        "lama_inap": 10,
        "tarif_kamar": 600000,
        "penjamin": "Asuransi",
    },
    {
        "nama": "Nurul Hidayah",
        "jenis_opname": "Infeksi Saluran Kemih",
        "lama_inap": 3,
        "tarif_kamar": 300000,
        "penjamin": "Umum",
    },
]

print("=" * 65)
print("LAPORAN PENGECEKAN STOK OBAT APOTEK")
print("=" * 65)

for i, obat in enumerate(daftar_obat, start=1):
    # Operator Pembanding (==, <=) dan Operator Kondisional (Ternary)
    if obat["stok"] == 0:
        status_stok = "HABIS (Segera Order!)"
    elif obat["stok"] <= 10:
        status_stok = "MENIPIS (Perlu Restock)"
    else:
        status_stok = "AMAN"

    # Contoh Operator Kondisional 1 Baris (Ternary Operator)
    kategori_harga = "Obat Mahal" if obat["harga"] > 20000 else "Obat Standar"

    print(
        f"{i}. {obat['nama']:<26} | Stok: {obat['stok']:<2} | {status_stok:<23} | {kategori_harga}"
    )

print("\n" + "=" * 65)
print("LAPORAN ADMINISTRASI PASIEN OPNAME RUMAH SAKIT")
print("=" * 65)

for j, pasien in enumerate(daftar_pasien, start=1):
    total_awal = pasien["lama_inap"] * pasien["tarif_kamar"]

    # Operator Pembanding (!=, >=) untuk menentukan tanggungan biaya
    if pasien["penjamin"] == "BPJS":
        diskon = total_awal  # Ditanggung 100%
        keterangan = "Ditanggung Penuh BPJS"
    elif pasien["penjamin"] != "BPJS" and pasien["lama_inap"] >= 7:
        diskon = total_awal * 0.15  # Diskon 15% jika rawat inap >= 7 hari
        keterangan = "Diskon Rawat Lama 15%"
    else:
        diskon = 0
        keterangan = "Tarif Normal"

    total_bayar = total_awal - diskon

    print(
        f"{j}. {pasien['nama']:<15} | {pasien['jenis_opname']:<24} | {pasien['lama_inap']} Hari"
    )
    print(
        f"   Penjamin: {pasien['penjamin']:<8} | Status: {keterangan:<21} | Bayar: Rp {int(total_bayar):,}\n"
    )
