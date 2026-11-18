pembayaran = input("Status pembayaran UKT (lunas/belum): ").lower()
nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran (0-100): "))

if pembayaran == "lunas":
    if nilai >= 70 and kehadiran >= 75:
        hasil = "LULUS"
    elif nilai >= 70 and kehadiran < 75:
        hasil = "Tidak lulus (kehadiran kurang)"
    else:
        hasil = "Tidak lulus (nilai kurang)"
else:
    hasil = "Tidak bisa ikut ujian karena UKT belum lunas"

status_akhir = "Selamat!" if hasil == "LULUS" else "Tetap semangat!"

print("--- HASIL EVALUASI ---")
print("Status: {}".format(hasil))
print(f"Pesan: {status_akhir}")