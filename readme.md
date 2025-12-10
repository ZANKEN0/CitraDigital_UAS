Pengolahan Citra Biner

Program Python untuk operasi dasar citra biner menggunakan OpenCV

Deskripsi

Proyek ini berisi contoh dasar pengolahan citra biner dan operasi morfologi menggunakan Python dan pustaka OpenCV. Program menampilkan proses mulai dari pembacaan citra grayscale, konversi menjadi citra biner, hingga penerapan operasi erosi, dilasi, opening, closing, dan gradient.
Proyek ini ditujukan sebagai materi pembelajaran pada mata kuliah pengolahan citra.

Kebutuhan Perangkat Lunak

Program tidak memerlukan perangkat keras khusus.
Perangkat lunak yang dibutuhkan:
Python 3
OpenCV
NumPy

Instalasi

Pasang pustaka yang diperlukan dengan perintah:

pip install opencv-python
pip install numpy


Letakkan citra input pada folder bernama img dengan nama file binerPy.jpg.
Pastikan skrip utama berada satu direktori dengan folder tersebut.

Penggunaan

Program akan memuat citra grayscale, mengubahnya menjadi citra biner, kemudian menjalankan beberapa operasi morfologi.
Setiap hasil operasi ditampilkan dalam jendela OpenCV.

Skrip utama menyediakan langkah pemrosesan berikut:

set grayscale
Membaca citra asli dalam format grayscale.

threshold
Mengubah citra grayscale menjadi citra biner.

erode
Melakukan operasi erosi untuk mengecilkan area objek.

dilate
Melakukan operasi dilasi untuk memperbesar area objek.

opening
Melakukan erosi lalu dilasi untuk menghilangkan noise kecil.

closing
Melakukan dilasi lalu erosi untuk menutup celah atau lubang kecil.

gradient
Menghasilkan perbedaan antara dilasi dan erosi untuk menonjolkan tepi objek.

Contoh citra masukan dan alur lengkap pemrosesan terdapat pada kode yang disediakan.

Struktur Folder

proyek
main.py
img
binerPy.jpg
