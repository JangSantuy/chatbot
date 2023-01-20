import data
import json

with open('datas.json', 'r') as json_file:
	daftarK = json.load(json_file)
#list
print("""
1.daftar kontak
2.tambah kontak
3.hapus kontak
4.cari kontak
0.keluar
""")

#menu program 
while True:
 menu =int(input("pilih menu : "))
 if menu == 0:
 	break
 elif menu == 1:
 	data.display(daftarK)
 	
 elif menu == 2:
 		kontak = data.new()
 		datas = {}
 		datas.update(kontak)
 		with open('datas.json', 'w') as json_file:
 			json.dump(datas, json_file)
 			
 elif menu == 3:
 	data.hapus(daftarK)
 	
 elif menu == 4:
 	data.cari(daftarK)
 
 else:
 	print("menu gk ada")
 	
print("Program Beres") 