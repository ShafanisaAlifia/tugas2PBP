# Tugas 5 PBP - Shafanisa Alifia

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
### Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja. Namun, inline css akan sangat membantu ketika kita hanya ingin menguji dan melihat perubahan pada satu elemen saja, berguna untuk memperbaiki code dengan cepat, dan proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

### Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML.
Pada internal css kita tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file. Namun, internal css memiliki kekurangan yaitu Tidak efisien apabila kita ingin menggunakan CSS yang sama dalam beberapa file.

### Eksternal CSS
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman. Keunggulan penggunaan eksternal css adalah ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi, loading website menjadi lebih cepat, dan file CSS dapat digunakan di beberapa halaman website sekaligus. Namun, bisa terjadi halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.


## Jelaskan tag HTML5 yang kamu ketahui.
- `<!DOCTYPE>` : 	Mendefinisikan jenis document
- `<a>` : Mendefinisikan hyperlink
- `<input>` : Menerima input dari user
- `<body>` : 	Mendefinisikan element body
- `<span>` : 	Mendefinisikan bagian dalam sebuah document
- `<i>` : Mendefinisikan text italic
- `<html>` : Mendefinisikan document html
- `<h1> - <h6>` : Mendefinisikan header
- `<div>` : Mendefinisikan bagian dalam suatu document
- `<button>` : Mendefinisikan document button/tombol
- `<form>` : Mendefinisikan formulir


## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- `*` : Selektor universal (selektor yang digunakan untuk menyeleksi semua elemen pada jangkauan (scope) tertentu)
- `:hover` : Style css pada elemen akan berubah ketika pointer berada di atas elemen HTML
- `:focus` : Style akan diterapkan jika elemen HTML diperhatikan oleh web browser.
- `:nth-child(n)` : Untuk memberikan styling khusus kepada salah satu elemen pada HTML dengan selector yang sama


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya melakukan kostumisasi pada halaman login, register, dan create-task, lalu menambahkan path untuk bootstrap pada base.html agar halaman menjadi responsive serta menghubungkan antara file CSS dengan file HTML kita dengan menggunakan {% load static %} pada setiap halaman HTML. dan melakukan kostumisasi halaman todolist dengan menambahkan cards untuk setiap task.


