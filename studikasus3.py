belanja = int(input("Masukkan total belanja: "))
status = input("Apakah pelanggan member? (y/n): ")

member = True if status.lower() == "y" else False

diskon = 0

if member:
    if belanja >= 1000000:
        diskon = 0.25
    elif belanja >= 500000:
        diskon = 0.15
else:
    if belanja >= 1000000:
        diskon = 0.10

potongan = belanja * diskon
total_bayar = belanja - potongan

print("\n--- HASIL ---")
print("Total Belanja :", belanja)
print("Diskon        :", diskon * 100, "%")
print("Potongan      :", potongan)
print("Total Bayar   :", total_bayar)