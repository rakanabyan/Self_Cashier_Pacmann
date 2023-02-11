# Self_Cashier_Pacmann
Project Self Cashier Service Pacmann dari Rakan Abyan di kelas Python 

## Latar Belakang Permasalahan

Mesin kasir mandiri alias _self-service cashier_ adalah sebuah mesin yang berfungsi untuk menyelesaikan transaksi customer sendiri tanpa memerlukan kasir tradisional. Saat menggunakan mesin kasir mandiri, _customer_ dapat memasukan nama barang satu per satu sebelum membayar belanjaannya tanpa memerlukan bantuan staf. Mesin tersebut umunya digunakan di supermarket, toserba, bahkan di Jerman, beberapa toko bangunan sudah menggunakan _self-service cashier_. Mesin tersebut biasanya diawasi oleh satu atau dua staf yang berfungsi untuk membantu pelanggan dalam proses transaksi, koreksi harga dan jumlah barang, bahkan hingga mengecek kembali barang-barang yang belum direkap oleh customer itu sendiri.

Kali ini, penulis akan mendeskripsikan program mesin kasir mandiri sederhana dengan menggunakan bahasa pemrograman Python.  

## Tujuan Project Self Cashier
1. Membuat Program Cashier sederhana dalam bahasa pemograman Python yang mempunyai fitur berikut: 
  - Memasukkan nama Barang, beserta jumlah dan harga barang secara manual
  - Mengubah nama sebuah barang yang akan dibeli
  - Mengubah jumlah sebuah barang yang akan dibeli 
  - Mengubah harga sebuah barang yang akan dibeli
  - Menghapus sebuah barang yang akan dibeli
  - Me-_reset_ sebuah transaksi
  - Mengecek sebuah transaksi
  - Melakukan pembayaran
  
2. Mengimplementasikan beberapa materi dalam kelas Python, diantaranya:
  - Operasi aritmatika dalam Python
  - Penggunaan Dictionary dalam Python
  - _Function_
  - _Branching_
  - _Object-Oriented Programming_
  - Clean Code berdasarkan PEP 8
  
 ## Alur Program
 
 1. Eksekusi file ``cashier.py`` untuk menjalankan basis program
 2. Eksekusi ``main.py`` untuk menjalankan program self-service-cashier
 3. Masukan angka 1-8 untuk menjalankan fitur berikut
    1. ``1: Insert your Article`` <br>
    Fitur tersebut memanggil fungsi ``add_item`` pada class ``transaction`` pada ``cashier.py``, dimana fungsi tersebut berguna untuk memasukan nama barang yang dibeli, beserta jumlah harga dan barang
    2. ``2: Update Article Name``<br>
    Fitur tersebut memanggil fungsi ``update_item_name`` pada class ``transaction`` pada file ``cashier.py``, dimana fungsi tersebut berguna untuk berfungsi mengubah nama sebuah barang yang akan dibeli
    3. ``3: Update Article Quantity``<br> 
    Fitur tersebut memanggil fungsi ``update_item_quantity`` pada class ``transaction`` pada file ``cashier.py``, dimana fungsi tersebut berguna mengubah jumlah sebuah barang yang akan dibeli
    4. ``4: Update Article Price`` <br> Fitur tersebut memanggil fungsi ``update_item_price`` pada class ``transaction`` pada file ``cashier.py``, dimana fungsi tersebut akan mengubah harga sebuah barang yang dibeli
    5. ``5: Remove Article``<br> Fitur tersebut memanggil fungsi ``delete_item`` pada class ``transaction`` pada file ``cashier.py``, dimana fungsi tersebut berguna menghapus barang yang tidak jadi dibeli
    6. ``6: Restart Transaction``<br> Fitur tersebut memanggil fungsi ``reset_transaction`` pada class ``transaction`` pada file ``cashier.py``, dimana fungsi tersebut mempunyai kegunaan me-_reset_ transaksi dari awal
    7. ``7: Check your order``<br> Fitur tersebut memanggil fungsi ``check_order`` pada class ``transaction`` pada file ``cashier.py``, dimana fungsi tersebut mempunyai kegunaan mengecek sebuah transaksi
    8. ``8: Pay Now!`` <br> Fitur tersebut memanggil fungsi ``total_price`` pada class ``transaction`` pada file ``cashier.py``, dimana metode tersebut mempunyai kegunaan yaitu membayar barang belanjaan. Setelah membayar, program ini berakhir.
  4. Apabila pengguna tidak memasukkan nomor 1-8, maka menu akan kembali muncul.

 ## Penjelasan Fungsi dalam Program Self Cashier
 
 1. ``add_item`` berfungsi memasukan nama barang yang dibeli, beserta jumlah harga dan barang 
 2. `update_item_name` berguna mengubah nama artikel, apabila customer salah memasukkan nama barang
 3. `update_item_quantity` berguna mengubah jumlah suatu item yang dibeli oleh customer, apabila customer salah memasukkan jumlah barang
 4. `update_item_price` mempunyai kegunaan mengubah harga suatu item yang dibeli oleh customer, apabila customer salah memasukkan harga barang
 5. `delete_item` berguna menghapus salah satu item 
 6. `reset_transaction` berguna menghapus semua barang belanjaan dan customer akan kembali menginput barang belanjaannya dari awal.
 7. `check_order` berfungsi kembali mengecek barang belanjaan yang sudah diinput oleh customer
 8. 'total_price' berguna menghitung harga total dari barang belanjaan customer
 9. `exit` berguna mengakhiri program
 
 ## Test Case
 **1. Memasukan barang dengan menggunakan `add_item`**
 
 ![Add Article](https://user-images.githubusercontent.com/92530633/218282106-0633ac53-5b4e-4459-be90-74f9bb10660a.png)
 
 **2. Memperbaharui nama artikel dengan menggunakan fungsi `update_item_name`**
 
 ![Update Article Name](https://user-images.githubusercontent.com/92530633/218282134-944df3a3-74dc-4081-9a23-22b2a09e10cf.png)
 
 **3. Memperbaharui jumlah item suatu barang dengan menggunakan fungsi `update_item_quantity`**
 
 ![Update Quantity](https://user-images.githubusercontent.com/92530633/218282203-6c1bef25-a25b-4f7d-b092-ae0ed86b4eec.png)
 
 **4. Memperbaharui harga barang dengan menggunakan fungsi `update_item_price`**
 
 ![Update Price](https://user-images.githubusercontent.com/92530633/218282315-f57c91ec-11d3-404a-93a9-8317f158e6e4.png)

 **5. Menghapus sebuah barang dengan fungsi `delete_item`**
 
 ![Remove Article](https://user-images.githubusercontent.com/92530633/218282318-1ed01bdb-9d22-4147-9529-a784176b9b08.png)

 **6. Mengulang kembali transaksi dengan fungsi `reset_transaction`**
 
 ![Reset Transaction](https://user-images.githubusercontent.com/92530633/218282323-3557cef0-3715-4dd1-b35b-094bc3aa0f84.png)

 **7. Mengecek barang-barang belanjaan _customer_ dengan fungsi `check_order`**
 
 ![Cek Order](https://user-images.githubusercontent.com/92530633/218282326-cab86456-4a17-4999-b36c-8c0c3fec998a.png)

 **8. Membayar barang belanjaan dengan fungsi `total_price`**
 
 ![Pay it](https://user-images.githubusercontent.com/92530633/218282327-e9eae38c-38ba-46a0-9da9-26fc361fac5f.png)

## Saran dan Perbaikan

1. Membutuhkan fitur exit untuk mengakhiri secara langsung transaksi di mesin kasir mandiri dengan syarat program harus bisa menolak permintaan customer, apabila program menemukan paling sedikit satu barang dalam sebuah transaksi. 
2. Dapat menyesuaikan nama barang dengan satuan massa barang atau volume, misal ada pilihan suatu barang bisa dibayar berdasarkan per item, per liter atau per gram. 
3. Perlu menyesuaikan nama barang dengan nomor barcode barang, agar program ini bisa dikembangkan di masa mendatang.

Rakan Abyan

Marburg, 2023 


 
