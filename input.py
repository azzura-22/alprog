nama = input("masukan nama :")
umur = int(input("masukan umur:"))
ipk = float(input("masukan ipk:"))
asli = bool(input("masukan keaslian:"))
if (umur <= 20):
    print("kolot")

print("nama saya:",nama,type(nama))
print("umur saya:",umur,type(umur))
print("ipk saya:",ipk,type(ipk))
print("keaslian saya:",asli,type(asli))

print(f"nama saya {nama} umur saya {umur} ipk saya {ipk} keaslian saya {asli}")