#list of dictionaries
daftar_harga=[{'nama':'apel', 'harga': 10000},
              {'nama':'jeruk', 'harga': 120000},
              {'nama':'durian', 'harga': 120000},
              {'nama':'kiwi', 'harga': 60000},
              {'nama':'melon', 'harga': 300000},

]

#tampilkan semua nama buah dan harga

for buah in daftar_harga:
    print(f'{buah["nama"]} - {buah["harga"]}')

x=[]
#tampilkan nama buah paling mahal
harga_termahal=0
nama_buah_termahal=""
for buah in daftar_harga:
    if buah["harga"]>harga_termahal:
        harga_termahal=buah["harga"]
        nama_buah_termahal=buah["nama"]
print(f'Nama buah termahal adalah {nama_buah_termahal} dengan harga {harga_termahal}')

#hapus buah dengan harga kurang dari 100000
batas=100000

#ambil dulu jumlah dalam list
count=len(daftar_harga)
index=0
while index<count:
    if daftar_harga[index]['harga']<batas:
        #harus dihapus
        del daftar_harga[index]
    else :
        index+=1
    count=len(daftar_harga)
    
'''for index in range (len(daftar_harga)):
    if daftar_harga[index]['harga'] <batas:
        del daftar_harga[index]
'''
#tampilkan semua nama buah dan harga
print('Setelah  semua buah dibawah daftar harga dihapus')
for buah in daftar_harga:
    print(f'{buah["nama"]} - {buah["harga"]}')