#lat 8

belanja = int(input("Masukkan harga belanja: "))
member = input("Apakah member (ya/tidak): ")

if member.lower() == "ya":
    if belanja >= 500000:
        total = belanja - (belanja * 0.2)
    elif belanja >= 300000:
        total = belanja - (belanja * 0.1)
    else:
        total = belanja - (belanja * 0.05)
else:
    total = belanja

print(f"Total bayar: {total}")