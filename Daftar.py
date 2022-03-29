data = []
while True:
    print("program daftar siswa".center(20+10,'='))
    nama = input("masukkan nama siswa \t: ")
    nilai = float(input("masukkan nilai siswa \t: "))
    data_sementara = [nama,nilai]
    data.append(data_sementara)
    for index,da in enumerate(data):
        print(f"{index+1} <> {da[0]} <> {da[1]}")
    
    penjumlahan = 0
    print("="*10)
    #penjumlahan total nilai
    for i in data:
        penjumlahan += i[1]

    total_murid = len(data)
    rata2 = penjumlahan/total_murid
    print(f"rata - rata nilai kelas : {rata2}" )
    print(f"nilai total {penjumlahan}")

    cek = input("apakah mau lanjut (y/n) : ")

    if cek == 'n':
        break


