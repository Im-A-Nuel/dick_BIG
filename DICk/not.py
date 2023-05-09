daftar={
    'toko' : 'TOKO BUKU AKU',
    'alamat' : 'jl kuburan 34',
    'tanggal' : '9 Mei 2023',
    'pembeli': 'bambang',
    'barang':[
                {'kode_barang':'P001','nama_barang' : 'pensil biasa', 'harga': 1500,'jumlah_beli':2},
                {'kode_barang':'P02B','nama_barang' : 'pensil 2B', 'harga': 3500,'jumlah_beli':1},
                {'kode_barang':'B001','nama_barang' : 'buku', 'harga': 2500,'jumlah_beli':3},
                {'kode_barang':'PG01','nama_barang' : 'penggaris', 'harga': 1500,'jumlah_beli':3},
                {'kode_barang':'PH01','nama_barang' : 'penghapus', 'harga': 750,'jumlah_beli':2},
            ]
                
}
x=0
jumlah=0
data = (len(daftar['barang']))
for i in range(data):
    jumlah=jumlah+((daftar["barang"])[x])["jumlah_beli"]
    x+=1


x=0
jumlah_harga=0
for i in range(len(daftar['barang'])):
    jumlah_harga=jumlah_harga+((daftar["barang"])[x])["harga"]*((daftar["barang"])[x])["jumlah_beli"]
    x+=1
    


print(f'Nama toko : {daftar["toko"]}')
print(f'alamat :  {daftar["alamat"]}')
print(f'tgl :  {daftar["tanggal"]}')
print(f'Nama pembeli :  {daftar["pembeli"]}')
print(f'Jumlah barang yang dibeli : {jumlah}')
jumlah_harganew=jumlah_harga*80/100
print(f'Jumlah harga barang yang dibeli : {jumlah_harga}')
print(f'Jumlah harga barang yang dibayar : {jumlah_harganew}')
# x=0
# for i in range(len(daftar['pembeli'])):
#     print(f'{((daftar["pembeli"])[x])["nama_pembeli"]}, jumlah barang : {((daftar["pembeli"])[x])["jumlah_beli"]}')
#     x+=1
# print('Total ')
