# CapstoneProject1
**Rifqi Athala Naufal
JCDSOL - 013**

## Fungsi Utama - pilihanmenu

**pilihanmenu** merupakan fungsi utama yang menjalankan program yang menampilkan menu Apple Store dan meminta input dari pengguna. Program akan memanggil fungsi yang sesuai berdasarkan input dari pengguna. jika pengguna input **5**, maka program akan keluar.

## Fungsi 1 - daftar_produk (Read)

Jika pengguna input **1**, maka program akan menjalankan fungsi **daftar_produk()**. Fungsi daftar_produk() akan menampilkan data mengenai **nama**, **stok** dan **harga** dari semua produk yang tersimpan dalam **list_produk**. Bertujuan untuk memberikan informasi mengenai daftar produk yang tersedia di Apple Store.

## Fungsi 2 - tambah_produk (Create)

Jika pengguna input **2**, maka program akan menjalankan fungsi **tambah_produk()**. Fungsi tambah_produk() akan meminta pengguna untuk input **nama**, **stok** dan **harga** dari produk yang ingin ditambahkan kedalam **list_produk**. jika user telah selesai menginput data maka program akan menampilkan pesan **Data baru sudah berhasil ditambahkan ke dalam daftar produk**.

## Fungsi 3 - hapus_produk (Delete)

Jika pengguna input **3**, maka program akan menjalankan fungsi **hapus_produk()**. Fungsi hapus_produk() akan  meminta pengguna untuk input nomor index dari produk yang ingin dihapus dari **list_produk**. jika user telah selesai menginput nomor index yang ingin dihapus, maka program akan menampilkan pesan **Data baru sudah berhasil dihapus dari daftar produk**.

## Fungsi 4 - beli_produk (Update)

Jika pengguna input **4**, maka program akan menjalankan fungsi **beli_produk()**. Fungsi beli_produk() akan meminta pengguna untuk input index dan jumlah dari produk yang ingin dibeli. jika index dan jumlah produk yang ingin dibeli tersedia, maka seluruh produk yang ingin dibeli akan ditambahkan kedalam variabel **keranjang** yang akan berguna dalam menghitung **total_harga**.

Sebelum melakukan pembayaran, pengguna akan ditanyakan apakah memiliki kode voucher atau tidak. Dalam program ini saya menyediakan kode voucher yaitu **MON100** dan **TUE200**. jika user memasukan kode MON100 akan mendapatkan potongan 100 di total_harga dan apabila user memasukan kode TUE200  akan mendapatkan potongan 200 di total_harga.

selanjutnya untuk proses pembayaran, pengguna diminta input **jumlah_uang** yang akan digunakan dalam proses pembayaran. Jika jumlah uang yang diinput **lebih besar** dari total harga, maka program akan menampilkan pesan "terima kasih" dan juga akan menampilkan jumlah uang kembalian lalu keranjang akan dikosongkan kembali dengan menggunakan metode clear. selanjutnya apabila uang yang diinput **bernilai sama** dengan total harga, maka program akan menampilkan pesan "terima kasih" dan keranjang akan dikosongkan kembali dengan menggunakan metode clear. Apabila jumlah uang yang diinput **lebih kecil** dari total harga, maka program akan menghitung dan mempilkan kekurangan pembayaran lalu program akan *looping* kembali meminta pengguna memasukan jumlah_uang untuk pembayaran.
