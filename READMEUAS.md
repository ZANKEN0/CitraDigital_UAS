Morphology Operations with OpenCV (Python)

Repository ini berisi contoh implementasi operasi morfologi pada citra biner menggunakan OpenCV. Program menampilkan hasil setiap tahapan proses mulai dari pembacaan citra grayscale, thresholding, hingga berbagai operasi morfologi.

Fitur Utama

Program melakukan beberapa operasi dasar morfologi antara lain:

Thresholding untuk mengubah citra grayscale menjadi biner

Erosi

Dilasi

Opening

Closing

Morphological Gradient

Setiap hasil operasi ditampilkan dalam jendela terpisah agar mudah diamati perbedaannya.

Struktur Folder
morphology-opencv/
│
├── img/
│ └── binerPy.jpg
│
├── src/
│ └── main.py
│
└── README.md

Persiapan Lingkungan

Pastikan Python sudah terpasang di sistem. Instal dependensi berikut:

pip install opencv-python numpy

Cara Menjalankan Program

Masukkan gambar yang akan diproses ke dalam folder img dengan nama binerPy.jpg.

Kemudian jalankan perintah:

python src/main.py

Setiap tahapan proses akan ditampilkan melalui jendela OpenCV. Tekan tombol apa pun untuk melanjutkan ke tampilan berikutnya.

Penjelasan Singkat Operasi Morfologi

Erosi
Mengikis bagian putih pada citra biner sehingga objek mengecil.

Dilasi
Menambah area putih sehingga objek tampak lebih besar.

Opening
Menggabungkan erosi lalu dilasi. Berguna untuk menghilangkan noise kecil.

Closing
Menggabungkan dilasi lalu erosi. Berguna untuk menutup celah kecil pada objek.

Morphological Gradient
Menghasilkan tepi objek melalui selisih antara hasil dilasi dan erosi.

Anggota Kelompok

Abdul Aziez A. S
Dwi Nurcahyo
Rayhan Maullana B.
Ryan Hidayat
