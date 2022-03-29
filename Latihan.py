import datetime as waktu

time = waktu.date.today()
data = []
while True:
    print(f"program ini di buka pada {time}")

    print("===================================")


    print("program daftar peserta".center(22+10,'='))
    print("identitas data")
    print(f"nama data : data\njumlah data : {len(data)}")
    print(f"isi : {data}")
    print('1.menambahkan data')
    print('2.merubah data')
    print('3.melihat data')
    print('4.menghapus data')
    print('5.keluar dari program')
    a = int(input(": "))
    if a == 1:
        kondisi = True
        while kondisi:
            print("menambahkan data".center(16+10,'='))
            nama = input("masukkan nama : ")
            data.append(nama)
            data.sort()
            cek = int(input("apakah anda mau menambahkan lagi (1) dan (2) untuk berhenti : "))
            if cek == 2:
                kondisi = False
            else: 
                continue

    elif a == 5:
        print("keluar dari program".center(20+10,'='))
        print("terima kasih telah menggunakan program kami (:")
        break

    elif a == 4:
        print("menghapus data".center(14+10,'='))
        print(f"data anda : \n {data}")
        hapus = input("masukkan nama yang akan di hapus ")
        data.remove(hapus)
        print(f"data sekarang : \n {data}")

    elif a == 2:
        print("mengubah data".center(13+10,'='))
        print(f"data anda\n {data}")
        ubah = int(input("masukkan data yang akan diubah menurut angka : "))
        baru = input("masukkan nama yang baru : ")
        data[ubah] = baru
        print(f"data sekarang  \n{data}")
    
    elif a == 3:
        print("melihat data".center(12+10,'='))
        print(f"data anda : \n{data}")
        print(f"jumlah data {len(data)}")
        print(f"urut dari depan {data.sort()}")
        print(f"urut dari belakang {data.reverse()}")
        

