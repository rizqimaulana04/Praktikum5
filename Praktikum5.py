print('NAMA \t : MUHAMMAD RIZQI MAULANA')
print('NIM \t : 312210360')
print('PRODI \t : TEKNIK INFORMATIKA')
print(' ')
i=0
nm =[]
ni = []
tgs = []
uts = []
uas = []
akh = []

while True:
    nama = input('Nama\t\t\t: ')
    nm.append(nama)
    nim = input('NIM\t\t\t: ')
    ni.append(nim)
    nilai_tugas = input('Nilai Tugas\t\t: ')
    tgs.append(nilai_tugas)
    nilai_uts = input('Nilai UTS\t\t: ')
    uts.append(nilai_uts)
    nilai_uas = input('Nilai UAS\t\t: ')
    uas.append(nilai_uas)
    akhir =(int(nilai_tugas) *0.3) + (int(nilai_uts) *0.35) + (int(nilai_uas) *0.35)
    akh.append(akhir)

    data = (' ')
    while data!='y' and data!='t':
        data = input('Tambah Data (y/t)?')
    i+=1
    if data =='t':
        break
print("==================================================================")
print("| No |  Nama\t|\tNIM\t| TUGAS\t|  UTS\t|  UAS\t|  Akhir |")
print("==================================================================")
for n in range(i):
    print("|",n+1," |",nm[n],"\t|",ni[n],"\t|", tgs[n],"\t|",uts[n],"\t|", uas[n],"\t|", akh[n]," |")
print("==================================================================") 