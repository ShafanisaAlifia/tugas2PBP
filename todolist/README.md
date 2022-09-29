# Tugas 4 PBP - Shafanisa Alifia

link HerokuApp : [link](https://tugas2-alip.herokuapp.com/todolist/login/)

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF (Cross-Site Request Forgery) adalah jenis serangan yang dilakukan oleh malicious sites atau users commit. User mungkin saja mengunjungi malicious sites tersebut dan situs tersebut akan mengirimkan formulir tersembunyi yang memungkinkan mereka mendapatkan kredensial dari pengguna. Dan bisa saja mereka dapat menggunakan kredensial dari client untuk mengakses rekening bank, forum, dan masih banyak lagi.

Itu sebabnya Django menyediakan cara sederhana untuk mencegahnya, yaitu dengan menggunakan {% csrf_token %} yang unik untuk situs tertentu itu. {% csrf_token %} pada dasarnya adalah token yang dikirimkan server kepada client, dan client harus mengirimkan kembali token tersebut sebagai bagian dari request. Apabila token tidak sesuai, server tidak akan menerimanya maka request tersebut akan di-reject.


## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya kita dapat membuat form secara manual tanpa menggunakan {{ form.as_table }}. Yaitu dengan membuat elemen <form>, dan membuat tag <input> dengan atribute widget sesuai dengan yang kita butuhkan. 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Saat user mengklik tombol untuk submit form melalui HTML form, data-data yang dimasukkan ke form akan diperiksa, data tersebut dapat dilihat dalam variabel request.POST. Dalam `views.py` dilakukan `save()` dan data tersebut akan tersimpan. Selanjutnya, server akan memproses input yang diberikan melalui `views.py` yang ada. 
 
Data tersebut diproses oleh server, untuk memeriksa apakah sesuai dengan batasan yang diberikan oleh form. Jika data yang dimasukkan tidak valid, user akan diarahkan untuk mengisi kembali form tersebut. Jika sudah valid, data tersebut akan diproses, server akan mengambil data tersebut, dan membuat atau menyimpannya ke database. Ketika dibutuhkan, Model pada database dapat diambil dan ditampilkan pada template HTML.

## Implementasi dari checklist di atas
1. Karena menggunakan project Django yang sudah ada, kita bisa langsung membuat new app `todolist` dengan cara `python manage.py startapp todolist`. Dan jangan lupa untuk mendaftarkan new app `todolist` pada `project_django/settings.py`.
2. Create new models dengan nama Task pada `todolist/models.py` sesuai dengan attribute yang disebutkan pada deskripsi tugas.
![Image](<https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/todolist/models.jpg>)
3. Membuat fungsi `login_user`, `logout_user`, dan `register` pada `views.py` dan membuat 2 buah template HTML, `login.html` dan `register.html` untuk menampilkannya kepada user. 
4. Membuat 2 new HTML file di dalam `todolist/templates` yaitu `create_task.html` yang berfungsi untuk pembuatan `Task` baru dan `todolist.html` untuk menampilkan data yang sesuai berdasarkan user login.
5. Pada `views.py` tambahkan fungsi `show_todolist` 
![Image](<https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/todolist/show_todolist.jpg>)

user harus melakukan login terlebih dahulu lalu membawa `request.user` dan `todo_list` yang merupakan task yang sudah dibuat oleh user dan akan dikirimkan ke `todolist.html`.

6. Lalu pada `views.py` kita tambahkan lagi fungsi `create_task` yang berfungsi untuk membuat `Task` baru.
![Image](<https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/todolist/create_task.jpg>)

`request.method` == `POST` artinya sudah membuat new task, mengambil `title` dan `description` yang di input oleh user dan waktu saat user menginput semua data tersebut langsung direct ke `show_todolist`. 

7. Pada `todolist/urls.py` kita perlu untuk mendaftarkan fungsi `login_user`, `logout_user`, `register`, `show_todolist`, dan `create_task` yang baru kita buat tadi. Setelah itu, kita perlu melakukan routing pada `project_django/urls.py` dengan membuat path `path('todolist/', include('todolist.urls'))` agar semua path dalam `todolist.urls` dapat dilaksanakan dengan baik.

8. Setelah semua selesai dibuat kita perlu untuk melakukan `makemigration`, `migrate` dan melakukan `runserver` untuk mengecek apakah new app yang kita buat sudah berjalan dengan baik.

9. Terakhir kita lakukan `add` `commit` `push` dan deployment pada HerokuApp akan berjalan secara otomatis.
 
## Akun Dummy
Username : Alip
Password : hihuhihu
 
Username : Alifia
Password : hahahihi


