# Masukan nilai dan kehadiran
nilai = float(input("Nilai akhir (0-100): "))
kehadiran = float(input("Persentase kehadiran (0-100): "))

# 1. Periksa syarat kehadiran minimal 80 persen
if kehadiran < 80:
    predikat = "-"
    status = "Tidak Lulus (Kehadiran kurang dari 80%)"
else:
    # 2. Tentukan predikat dengan rantai elif menurun
    if nilai >= 85:
        predikat = "A"
    elif nilai >= 70:
        predikat = "B"
    elif nilai >= 60:
        predikat = "C"
    elif nilai >= 50:
        predikat = "D"
    else:
        predikat = "E"
    
    # 3. Tentukan status lulus atau belum lulus dari predikat
    if predikat in ["A", "B", "C"]:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

# 4. Tampilkan predikat dan status
print(f"Predikat: {predikat}")
print(f"Status: {status}")