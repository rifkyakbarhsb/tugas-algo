tugas = float(input("Masukkan nilai Tugas :90"))
uts = float(input("Masukkan nilai UTS :90"))
uas = float(input("Masukkan nilai UAS :90"))
kehadiran = float(input("Masukkan kehadiran (%) :95"))

nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)
nilai_akhir = round(nilai_akhir, 2) 

if nilai_akhir >= 75 and kehadiran >= 80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
        status = "LULUS DENGAN PREDIKAT"
    else:
        status = "LULUS"
else:
    status = "BELUM LULUS"

print("\n=== HASIL EVALUASI ===")
print("Nilai Akhir :", nilai_akhir)
print("Kehadiran   :", kehadiran, "%")
print("Status      :", status)
