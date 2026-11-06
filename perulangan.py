jumlah = int(input("Jumlah mahasiswa : "))

if jumlah > 0:
    total = 0
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan Nilai Mahasiswa {i} : "))
        total += nilai

    rata_rata = total / jumlah
    print("rata rata :", rata_rata)
else:
    print("Jumlah mahasiswa harus lebih dari 0")
