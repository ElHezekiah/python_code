#lat 7

nilai = int(input("Masukkan nilai: "))
kehadiran = float(input("Masukkan persentase kehadiran (0-100): "))
persentase = kehadiran / 100
 
if nilai >= 70 and persentase >= 0.75:
    print("Anda lulus")
elif nilai >= 70 and persentase < 0.75: # Pakai < biar gak bentrok sama yang di atas
    print("Nilai cukup tetapi kehadiran kurang")
else:
    print("Anda tidak lulus")