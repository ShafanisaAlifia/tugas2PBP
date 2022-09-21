## Link HerokuApp: https://tugas2-alip.herokuapp.com/katalog/ 

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html; 
![Bagan](https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/katalog/BaganDjango.png "Bagan Django")

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual Environment merupakan sebuah ruang lingkup virtual yang terisolasi dari dependencies utama.

Virtual environment sangat berguna ketika kita membutuhkan dependensi yang berbeda antara proyek yang berjalan pada sistem operasi yang sama. Virtual environment biasanya digunakan untuk proyek berbasis Python. Karena project memiliki kebutuhan/dependensi yang berbeda, maka diperlukan virtual environment untuk menjalankannya, tanpa mengubah konfigurasi sistem operasi yang kita gunakan.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun Python merekomendasikan penggunaan venv setiap kita akan membuat proyek baru. Ini untuk memastikan bahwa versi library yang digunakan dalam satu proyek tidak akan berubah jika kita memperbarui library yang sama di proyek lain.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Adapun beberapa cara yang saya lakukan untuk mengimplementasikan poin 1 - 4  adalah :
1. Pertama saya membuat new repository yang memuat isi source code yang telah diberikan dan melalukan clone repository ke dalam folder local.
2. Setelah berhasil meng-clone folder tersebut, kemudian saya mulai mengerjakannya pada VsCode. Mulai dari views.py saya menambahkan list_item yang berisikan objek dari katalog kemudian menambahkan context 'list item', 'nama', dan 'NPM' yang berfungsi sebagai variabel untuk mapping ke katalog.html.
3. Lalu saya melakukan rooting terhadap views.py pada fungsi urls.py pada folder template dengan cara mengimport show_katalog untuk menghubungkan antara HTML dan web browser.
4. Setelah melakukan mapping pada katalog.html yang ada pada folder templates seluruh data-data yang tadi sudah kita render di views.py untuk menampilkan Item name, Item price, Item stock, Rating, Description, dan Item URL pada halaman HTML, saya mengiterasi variable list_item untuk menampilkan data tersebut dan dilanjutkan dengan memanggil setiap variabel dari objek-objek pada list item.
5. Setelah melakukan semua tahapan di atas saya mengaktifkan virtual environment pada CMD untuk melakukan migration, loaddata, dan menjalankan proyek. 
6. Setelah melakukan run server, saya mengecek apakah web sudah dapat berjalan dengan baik dan benar pada local host.
7. Lalu tahapan yang terakhir adalah setelah saya sudah memastikan bahwa web telah berjalan dengan benar saya melakukan deploy ke Herokuapp. Dengan cara melakukan git add-commit-push, lalu meng-copy API key dari akun herokuapp dan memasukkannya ke dalam menu secret di Github pada HEROKU_API_KEY dan memberikan nama aplikasi pada HEROKU_APP_NAME. 
8. Update workflow sampai berhasil, lalu setelah itu kita sudah bisa mengakses aplikasi yang sudah kita buat pada browser dengan url pada poin pertama yaitu https://tugas2-alip.herokuapp.com/katalog/

Pada poin 2 terdapat bagan yang berisi tahapan request client ke web aplikasi berbasis Django. Seperti yang kita ketahui bahwa Django merupakan framework yang mengikuti struktur MVT (Model-View-Template). MVT adalah salah satu turunan dari struktur MVC (Model-View-Controller), yang model-nya lebih difokuskan sebagai objek yang mendefinisikan entitas pada database beserta konfigurasinya, lalu ada views yang berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk, dan template berperan sebagai tampilan yang akan dikembalikan kepada user.
