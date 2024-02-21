list_produk = [
    {
        'nama': 'Iphone',
        'stok': 200,
        'harga': 1000
    },
    {
        'nama': 'Ipad',
        'stok': 150,
        'harga': 1200
    },
    {
        'nama': 'Airpods',
        'stok': 350,
        'harga': 350
    },
    {
        'nama': 'Macbook',
        'stok': 50,
        'harga': 2500
    }
]

keranjang = []

# Jika user input angka 1, maka akan masuk ke function daftar_produk yang bertujuan untuk menampilkan daftar produk
def daftar_produk() :
    print('''
          -------------------------
          Daftar Produk Apple Store
          -------------------------
          ''')
    print('Index\t| Nama  \t| Stok\t| Harga')
    for i in range(len(list_produk)) :
        print('{}\t| {}  \t| {}\t| {}'.format(i,list_produk[i]['nama'],list_produk[i]['stok'],list_produk[i]['harga']))

# Jika user input angka 2, maka akan masuk ke function tambah_produk
# yang bertujuan untuk menambahkan data produk kedalam daftar produk
def tambah_produk() :
    nama_produk = input('Masukkan Nama Produk : ')
    stok_produk = int(input('Masukkan Stok Produk : '))
    harga_produk = int(input('Masukkan Harga Produk : '))
    list_produk.append({
        'nama': nama_produk,
        'stok': stok_produk,
        'harga': harga_produk
    })
    daftar_produk()
    print('\nData baru sudah berhasil ditambahkan ke dalam daftar produk.\n')

# Jika user input angka 3, maka akan masuk ke function hapus_produk
# yang bertujuan untuk menghapus data produk dari daftar produk
def hapus_produk() :
    daftar_produk()
    index_produk = int(input('Masukkan index produk yang ingin dihapus : '))
    del list_produk[index_produk]
    daftar_produk()
    print('\nData sudah berhasil dihapus dari daftar produk.\n')

# Jika user input angka 4, maka akan masuk ke function tambah_produk
# yang bertujuan untuk melakukan transaksi pembelian di Apple Store
def beli_produk() :
    daftar_produk()
    # proses dibawah ini bertujuan untuk input index dan jumlah produk yang ingin dibeli
    while True :
        index_produk = int(input('Masukkan index produk yang ingin dibeli : '))
        if(index_produk > len(list_produk)):
            print('Index yang dimasukkan salah.')
            continue
        while True:
            qty_produk = int(input('Masukkan jumlah yang ingin dibeli : '))
            if(qty_produk > list_produk[index_produk]['stok']) :
                print('stok tidak cukup, stok {} tinggal {}'.format(list_produk[index_produk]['nama'],list_produk[index_produk]['stok']))
                continue
            else :
                break
        # proses dibawah ini bertujuan untuk menambahkan list item yang ingin kita beli kedalam keranjang
        keranjang.append({
            'nama': list_produk[index_produk]['nama'], 
            'qty': qty_produk, 
            'harga': list_produk[index_produk]['harga'], 
            'index': index_produk
        })
        print('Isi keranjang :')
        print('Nama\t| Qty\t| Harga')
        for item in keranjang :
            print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
        # proses dibawah ini bertujuan untuk menanyakan kembali apakah user ingin membeli barang lain
        checker = input('Mau beli yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break
    # proses dibawah ini bertujuan untuk melakukan perhitungan total harga berdasarkan isi dari keranjang     
    print('Daftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    total_harga = 0
    for item in keranjang :
        print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
        total_harga += item['qty'] * item['harga'] 
    # proses dibawah ini bertujuan untuk menanyakan apakah user memiliki voucher yg berguna untuk mengurangi total harga
    print('Total Yang Harus Dibayar = {}\n'.format(total_harga))
    while True :    
        tanya_voucher = input('Apakah anda memiliki voucher? (ya/tidak) = ')
        if tanya_voucher == 'ya' :
            input_voucher = input('Silahkan masukkan kode voucher = ')
            if (input_voucher == 'MON100'):
                total_harga = total_harga - 100
                print('\nSelamat, Anda mendapatkan potongan sebesar 100.\nTotal harga yang harus dibayar setelah potongan adalah : {}\n'.format(total_harga))
                break
            elif (input_voucher == 'TUE200'):
                total_harga = total_harga - 200
                print('\nSelamat, Anda mendapatkan potongan sebesar 200.\nTotal harga yang harus dibayar setelah potongan adalah : {}\n'.format(total_harga))
                break
            else:
                print('Voucher tidak tersedia.\n')
                continue
        else:
            print('Total Yang Harus Dibayar = {}\n'.format(total_harga))
            break
    # proses dibawah ini bertujuan untuk memasukan jumlah uang untuk pembayaran berdasarkan total harga
    while True :
        jumlah_uang = int(input('Masukkan jumlah uang : '))
        if(jumlah_uang > total_harga) :
            kembali = jumlah_uang - total_harga
            print('Terima kasih \n\nUang kembalian anda : {}'.format(kembali))
            for item in keranjang :
                list_produk[item['index']]['stok'] -= item['qty']
            keranjang.clear()
            break
        elif(jumlah_uang == total_harga) :
            print('Terima kasih')
            for item in keranjang :
                list_produk[item['index']]['stok'] -= item['qty']
            keranjang.clear()
            break
        else :
            kekurangan = total_harga - jumlah_uang
            print('Uang anda kurang sebesar {}'.format(kekurangan))

while True :
    pilihanMenu = input('''
        Selamat Datang di Apple Store

        List Menu :
        1. Menampilkan Daftar Produk
        2. Menambah Produk
        3. Menghapus Produk
        4. Membeli Produk
        5. Exit Program

        Masukkan Angka List Menu yang ingin dipilih : ''') 
    # Jika user input 1/2/3/4/5 maka akan masuk ke function nya masing-masing
    # Jika input selain itu akan masuk ke else dan melakukan looping kembali
    if(pilihanMenu == '1') :
        daftar_produk()
    elif(pilihanMenu == '2') :
        tambah_produk()
    elif(pilihanMenu == '3') :
        hapus_produk()
    elif(pilihanMenu == '4') :
        beli_produk()
    elif(pilihanMenu == '5') :
        break
    else:
        print('\nPilihan salah. Silahkan masukkan kembali angka list menu yang ingin dipilih.')

    
 