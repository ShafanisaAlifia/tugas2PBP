# Tugas 6 PBP - Shafanisa Alifia

## Asynchronous programming VS Synchronous programming.
**Asynchronous programming** adalah proses jalannya program yang dapat terus berinteraksi dengan halaman saat data dimuat. Sedangkan **Synchronous programming** merupakan bagian dari Asynchronous (1 antrian) dimana user harus menunggu pada saat halaman baru di muat (click, wait,refresh).
 
## Event-Driven Programming
Event-driven programming adalah suatu paradigma di mana alur yang dijalankan suatu program didasarkan atas event atau perilaku yang dilakukan antar user dan client (Berkomunikasi dengan satu sama lain secara tidak langsung)

Dalam tugas ini, contoh penggunaan event adalah dengan onReady document untuk inisialisasi, onClick untuk button form baru, serta onSuccess yang dipanggil setelah pemanggilan AJAX berhasil.

## Penerapan Asynchronous programming pada AJAX
AJAX atau Asynchronous JavaScript and XML adalah teknik yang digunakan untuk membuat website yang dinamis. Artinya website mampu mengupdate dan menampilkan data baru dari server tanpa perlu melakukan reload. Fungsi AJAX adalah untuk mempersingkat atau mempermudah user experience. pengguna kini tak perlu lagi menunggu lama hanya untuk mengakses konten di situs yang kita buat.

## Implementasikan checklist 
1. Menambahkan views untuk AJAX
2. Routing di `urls.py`, dan melakukan mapping sesuai function
3. Rendering dirubah dari templating menjadi AJAX GET 
4. Membuat modal lalu menaruh form di dalam modal tersebut
5. Untuk tombol buat, di-hook dengan event onClick untuk melakukan AJAX POST
6. Setelah berhasil, tutup modal
7. Lakukan Reset container todo dengan menggunakan .empty(), lalu render kembali
