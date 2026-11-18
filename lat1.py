#startwith
print("aku ganteng".startswith('aku'))
print("aku ganteng".startswith('kau'))

#endswith
print("aku ganteng".endswith("aku"))
print("aku ganteng".endswith("ganteng"))

#mengabung string
print("".join(["Mikael", "Ganteng"]))

#menggabung elemen string di tengah
print("123".join(["Mikael", "Ganteng"]))

#mengubah string menjadi array
print("Mikael Ganteng".split())

#Mengganti elemen string
string="CE ADALAH KATA YANG BAGUS"
print(string.replace("KATA", "KELAS"))

#menghitung panjang data
con_list = [1,1,3,3,5,5,7,7,9,9]
print(con_list)
print(len(con_list))

#menghitung panjang data set
cont_list = set([1,1,3,3,5,5,7,7,9,9])
print(cont_list)
print(len(cont_list))

#minimal maximal
angka = [1,6,77,854,78,4,34]
print(min(angka))
print(max(angka))

#Menghitung banyak angka count
genap=[1,2,2,3,4,6,6,6,7]
print(genap.count(6))

#Menghitung banyak huruf
string="Nama saya Mikael Jordan Simanjuntak yang paling ganteng"
print(string.count("t"))

#in dan not in
kalimat = 'Mikael Jordan Simanjuntak adalah orang paling ganteng sedunia'
print("Mikael" in kalimat)
print("orang" not in kalimat)
print("Mikael" not in kalimat)
print("orang" in kalimat)

#sort
kendaraan =["mobil",'pesawat','kereta','kapal']
kendaraan.sort()
print(kendaraan)