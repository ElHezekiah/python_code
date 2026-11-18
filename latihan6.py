#lat 6

umur = int(input("usia: "))

if umur <= 5:
    print("Balita")
elif umur <= 12:
    print("Anak-anak")
elif umur <= 17:
    print("Remaja")
elif umur <= 59:
    print("Dewasa")
else:
    print("Lansia")