## Link Website
HTML : [link](https://tugas2-alip.herokuapp.com/mywatchlist/html)
JSON : [link](https://tugas2-alip.herokuapp.com/mywatchlist/json)
XML  : [link](https://tugas2-alip.herokuapp.com/mywatchlist/xml)

## Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON 
JSON adalah singkatan dari JavaScript Object Notation merupakan suatu format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Walaupun memiliki fungsi yang serupa dengan XML, JSON memiliki perbedaan di beberapa sektor seperti cara menyimpan elemennya, keamanan, dan cara penerapannya. 

Kelebihan
- Dapat menyimpan data dalam bentuk array dan menjadikan transfer data menjadi lebih mudah
- Sintaks yang lebih ringan dan berukuran lebih kecil
- Mendukung beberapa bahasa pemrograman lain

Kekurangan
- Format penulisannya agak sulit untuk dipahami
- Rentan terhadap hacking

XML 
XML sendiri merupakan markup language yang diciptakan oleh World Wide Web Consortium bahasa ini digunakan untuk menyederhanakan pertukaran dan penyimpanan data. XML ini terdiri dari tiga struktur yaitu deklarasi, atribut, dan elemen. 

Kelebihan
- XML merupakan platform dan bahasa yang independen, sehingga dapat digunakan pada berbagai sistem
- Mendukung unicode
- Dapat merubah data kapan saja tanpa mempengaruhi tampilannya

Kekurangan
- Tidak mendukung array
- Ukuran cukup besar, tergantung pada siapa yang menulisnya
- Biaya penyimpanan dan pengiriman data cukup tinggi

HTML
HTML (HyperText Markup Language) adalah suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar. Perbedaannya dengan XML adalah dalam kegunaannya, XML digunakan untuk menyimpan dan menyederhanakan pertukaran data, Sedangkan HTML digunakan untuk menampilkan data.

Kelebihan
- Bahasa pemrograman dijalankan di semua web browser
- Dapat dipelajari dengan mudah oleh pengembang web pemula
- Bahasa pemrograman open source (gratis)
- Mudah diintegrasikan dengan bahasa back-end seperti Node.js dan PHP
- Digunakan untuk pembuatan struktur konten pada website yang dapat ditambahkan dengan CSS atau bahasa pemrograman lain yang dapat dijalankan seperti Javascript

Kekurangan
- Penggunaan HTML murni hanya dapat diimplementasikan untuk halaman web statis. 
- Bahasa pemrograman ini tidak mendukung user untuk menjalankan logic sehingga semua halaman yang dibuat harus dibuat secara terpisah walaupun menggunakan elemen yang sama
- Terdapat beberapa fitur baru yang terkadang tidak dapat digunakan pada browser dengan cepat
- Perilaku browser yang tidak dapat diprediksi membuat proses render tag baru tekendala


## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery digunakan sebagai alat komunikasi antara client dan server. Karena pertukaran data biasanya diperlukan dalam mengimplementasikan sebuah platform, data delivery akan mempermudah dan mempercepat proses pengiriman data. Penyampaian data bisa dalam format JSON, XML, atau format penyampaian data lainnya. Seperti yang kita ketahui, developer frontend dan backend adalah 2 tim yang berbeda dengan adanya Data Delivery ini, tim frontend hanya perlu memanggil suatu url yang dikerjakan oleh tim backend dan membuat frontend yang menggunakan data yang diberikan backend, sedangkan tim backend hanya perlu menyediakan url dan menangani request dari frontend.

## Cara implementasi aplikasi mywatchlist
1. Membuat aplikasi mywatchlist dengan cara `python manage.py startapp mywatchlist` dan menambahkan `mywatchlist` pada `setting.py`.
2. Membuat `views.py` dan `urls.py`
    - `urls.py` memiliki 3 routes, show_html, show_json, show_xml, dan index yang mengembalikan HttpResponse kosong.
3. Membuat show_xml, show_json, dan show_html
    - show_xml dan show_json hanya mengembalikan data pada model MyFilm dalam bentuk JSON dan XML
    - show_html menerima context yang berupa data watchlist di database, dan mengembalikan mywatchlist.html
4. Membuat fixtures yang berisi initial_mywatchlist_data.json
5. Membuat sebuah models baru dengan nama "MyFilm" di `mywatchlist/models.py` sesuai dengan attribute-attribute yang telah disebutkan pada deskripsi tugas dengan fields:
    - watched: models.CharField (max_length = 50)
    - title: models.CharField (max_length = 50) 
    - rating: models.IntegerField() (range = [1 ... 5])
    - release_date: models.CharField (max_length = 50)
    - review: models.TextField()
6. Setelah melakukan semua tahapan di atas, aktifkan virtual environment pada CMD untuk melakukan `makemigrations`, `migrate`, `loaddata`
7. Membuat `mywatchlist.html` pada `mywatchlist/templates`
8. Update `Procfile` dan tambahkan `python manage.py loaddata initial_watchlist_data.json`
9. Mengakses URL dengan menggunakan postman
10. Menambahkan unit test pada tests.py yang ada dalam folder mywatchlist agar bisa mengembalikan respon HTTP 200 OK, 
11. Membuat file `style.css` pada `static\css` membantu agar styling css yang dibuat diterapkan ke mywatchlist.html
11. Terakhir, memastikan bahwa web telah berjalan dengan benar saya melakukan deploy ke Herokuapp. Dengan cara melakukan git add-commit-push.

