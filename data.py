
#menampilkan kontak
def display(daftarK):
	for kontak in daftarK:
		print("========================")
		print(f'nama : {kontak["nama"]}')
		print(f'Gmail : {kontak["email"]}')
		print(f'Telepon : {kontak["tel"]}')
		print("========================")
#tambah kontak
def new():
	nama= input("nama :")
	email = input("Gmail :")
	tel = input("Telepon :")
	kontak = {
	"nama"	: nama,
	"email" : email,
	"tel" : tel
	}

	return kontak
	#hapus kontak
def hapus(daftarK):
  tel =input("data yang di hapus berdasarkan  nomer telpon : ")
  
  index = -1
  for i in range(0, len(daftarK)):
    kontak = daftarK[i]
    if tel == kontak["tel"]:
      index = i
      break
      
  if index == -1:
    print("nothing")
  else:
    del daftarK[index]
    print("di hapus")
    
    
def  cari(daftarK):
	namacari = input("nama yang di cari : ")
	
	for kontak in daftarK:
		nama = kontak["nama"]
		if nama.lower().find(namacari.lower()) != -1:
			print("========================")
			print(f"nama : {kontak['nama']}")
			print(f"Gmail : {kontak['email']}")
			print(f"Telepon : {kontak['tel']}")
			print("========================")