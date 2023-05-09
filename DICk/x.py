data={
    'Genap':[],
    'Ganjil':[]
}
while True:
    angka=int(input('Masukkan angka [negatif untuk berhenti] : '))
    if angka <0:
        break
    elif angka%2==0:
        data['Genap'].append(angka)
    else :
        data['Ganjil'].append(angka)
print(data)

