Link Herokuapp html : https://tugas2-alip.herokuapp.com/mywatchlist/html
Link Herokuapp json : https://tugas2-alip.herokuapp.com/mywatchlist/json
Link Herokuapp xml : https://tugas2-alip.herokuapp.com/mywatchlist/xml


## Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON 
JSON adalah singkatan dari JavaScript Object Notation merupakan suatu format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna.

Walaupun memiliki fungsi yang serupa dengan XML, akan tetapi JSON ini memiliki perbedaan di beberapa sektor seperti cara menyimpan elemennya, keamanan, dan cara penerapannya. Selain itu, JSON juga memiliki kelebihan yaitu dapat menyimpan data dalam bentuk array sehingga transfer data menjadi lebih mudah dan mendukung beberapa bahasa pemrograman lain. JSON juga memiliki kekurangan yaitu format penulisannya sulit untuk dipahami oleh manusia dan rentan terhadap serangan.

Kelebihan
Dapat menyimpan data dalam bentuk array dan menjadikan transfer data menjadi lebih mudah.
Sintaks yang lebih ringan dan berukuran lebih kecil.
Mendukung beberapa bahasa pemrograman lain.
Lebih cepat dalam parsing data di sisi server.

Kekurangan
Format penulisannya agak sulit untuk dipahami.
Rentan terhadap hacking.

XML 
XML sendiri merupakan markup language yang diciptakan oleh World Wide Web Consortium bahasa ini digunakan untuk menyederhanakan pertukaran dan penyimpanan data. XML ini terdiri dari tiga struktur yaitu deklarasi, atribut, dan elemen. 

Extensible Markup Language memiliki kelebihan seperti, ia dapat digunakan pada berbagai sistem karena ia adalah bahasa pemrograman yang independen. Akan tetapi XML juga memiliki kekurangan seperti kamu tidak dapat menggunakan array pada XML.

Jika kamu penasaran ingin melihat serta mengedit file XML kamu, kamu dapat membuka file tersebut dengan beberapa cara. Ada tiga cara yang biasanya dilakukan untuk membuka file dengan ekstensi XML. Kamu dapat membukanya dengan text editor, dengan browser dan juga dengan XML online editor.

Kelebihan
XML merupakan platform dan bahasa yang independen, sehingga dapat digunakan pada berbagai sistem.
Mendukung unicode.
Dapat merubah data kapan saja tanpa mempengaruhi tampilannya.

Kekurangan
Tidak mendukung array.
Ukuran cukup besar, tergantung pada siapa yang menulisnya.
Biaya penyimpanan dan pengiriman data cukup tinggi.

HTML
HTML (HyperText Markup Language) adalah suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar. Perbedaan kegunaan XML untuk menyimpan dan menyederhanakan pertukaran data, Sedangkan HTML digunakan untuk menampilkan data.

Kelebihan
Memiliki banyak sumber dengan komunitas yang sangat besar dan penggunaan yang sangat luas
Bahasa pemrograman dijalankan di semua web browser
Dapat dipelajari dengan mudah oleh pengembang web pemula
Bahasa pemrograman memiliki struktur yang rapi dan konsisten sehingga mudah untuk dipelajari
Bahasa pemrograman open source (gratis)
Mudah diintegrasikan dengan bahasa back-end seperti Node.js dan PHP
Maintan dilakukan langsung oleh W3C (World Wide Web Consortium)
Digunakan untuk pembuatan struktur konten pada website yang dapat ditambahkan dengan CSS atau bahasa pemrograman lain yang dapat dijalankan seperti Javascript.

Kekurangan
Penggunaan HTML murni hanya dapat diimplementasikan untuk halaman web statis. Untuk fitur yang lebih dinamis, Kanca IT dapat menggunakan Javascript atau bahasa pemrograman back-end lainnya
Bahasa pemrograman ini tidak mendukung user untuk menjalankan logic sehingga semua halaman yang dibuat harus dibuat secara terpisah walaupun menggunakan elemen yang sama
Terdapat beberapa fitur baru yang terkadang tidak dapat digunakan pada browser dengan cepat
Perilaku browser yang tidak dapat diprediksi membuat proses render tag baru tekendala


## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab :
Penyampaian data yang disimpan di database ke frontend
Tentunya data yang disimpan dalam database akan digunakan pada suatu saat, karena itu, data delivery dibutuhkan dalam pembuatan sebuah aplikasi.

Penyampaian data bisa dalam JSON, XML, atau format penyampaian data lainnya.

Karena dalam sebuah tim, developer frontend dan backend adalah 2 tim yang berbeda
Tim Frontend hanya perlu memanggil suatu url yang dikerjakan oleh tim backend dan membuat frontend yang menggunakan data yang diberikan backend

Tim backend hanya perlu menyediakan url dan menangani request dari frontend

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pembuatan fixtures yang berisi initial_watchlist_data.json
Pembuatan constants film-film yang sudah/belum pernah saya tonton, diisi dengan data-data yang sesuai model MyWatchList.
Pembuatan models.py
Buat sebuah Model MyWatchList dengan fields:
watched: Boolean Field (default = False)
title: Character Field (max_length = 100)
rating: Decimal Field (range = [1 ... 5])
release_date: Date Field (menyimpan tanggal/bulan/tahun)
review: Text Field
Pembuatan views.py dan urls.py
Pembuatan show_xml, show_json, dan show_html

show_xml dan show_json hanya mengembalikan data pada model MyWatchList dalam bentuk JSON dan XML

show_html menerima context yang berupa data watchlist di database, dan mengembalikan watchlist.html

Pembuatan urls.py

urls.py memiliki 3 routes, show_html, show_json, show_xml, dan index yang mengembalikan HttpResponse kosong.
Pembuatan watchlist.html
watchlist.html berisi frontend yang akan mengembalikan html yang menyediakan data-data watchlist dalam bentuk tabel.

{% load static %} dan import style.css yang dibuat membantu agar styling css yang dibuat diterapkan ke watchlist.html

![image](<https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/mywatchlist/Postman%209_22_2022%2012_18_39%20AM.png>)
![image](<https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/mywatchlist/Postman%209_22_2022%2012_18_20%20AM.png>)
![image](<https://github.com/ShafanisaAlifia/tugas2PBP/blob/main/mywatchlist/Postman%209_22_2022%2012_16_10%20AM.png>)
