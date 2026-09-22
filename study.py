nama = input("masukan nama anda:")
meja = int(input("masukan nomor meja:"))
makanan = input("nama makanan:")
jumlah = int(input("jumlah makanan:"))

print("\n--- data restorant ---")
restorant = "seblak btr"
jenis = "seblak"
buka = True
rating = 4.5
print("nama restorant:",restorant)
print("jenis makanan:",jenis)
print("buka:",buka)
print("rating:",rating)

print("\n--- data pesanan ---")
print("nama pemesan:",nama)
print("nomor meja:",meja)
print("nama makanan:",makanan)
print("jumlah pesanan",jumlah)

print("nama restorant",type(restorant))
print("jenis makanan",type(jenis))
print("buka",type(buka))
print("rating",type(rating))
print("nama pemesan",type(nama))
print("nomor meja",type(meja))
print("nama makanan",type(makanan))
print("jumlah pesanan",type(jumlah))
