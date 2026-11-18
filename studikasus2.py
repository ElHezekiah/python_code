saldo = 1000000

print("--- MENU ATM ---")
print("1. Cek Saldo")
print("2. Tarik Tunai")
print("3. Setor Tunai")
print("4. Keluar")

pilihan = input("Pilih menu (1-4): ")

match pilihan:
    case "1":
        print(f"Saldo Anda saat ini: Rp {saldo}")
    
    case "2":
        tarik = int(input("Masukkan jumlah tarik tunai: "))
        if tarik > saldo:
            print("Saldo tidak cukup")
        else:
            saldo -= tarik
            print(f"Tarik tunai berhasil. Sisa saldo: Rp {saldo}")
            
    case "3":
        setor = int(input("Masukkan jumlah setor tunai: "))
        saldo += setor
        print(f"Setor tunai berhasil. Saldo sekarang: Rp {saldo}")
        
    case "4":
        print("Terima kasih telah menggunakan ATM ini.")
        
    case _:
        print("Pilihan tidak valid!")