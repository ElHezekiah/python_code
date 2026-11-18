#lat 5

nilai = int(input("NILAI: "))

if nilai <0 or nilai > 100:
    print("TIDAK FALID")
elif nilai >= 85 and nilai <=100 :
    print("Nilai A")
elif nilai >= 75:
    print("Nilai B")
elif nilai >= 65:
    print("Nilai C")
elif nilai >= 50:
    print("Nilai D")
else:
    print("Nilai E")