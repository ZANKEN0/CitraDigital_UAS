# Implementasi Operasi Morfologi Citra (Python & OpenCV)

Proyek ini merupakan implementasi dasar pengolahan citra biner menggunakan bahasa pemrograman Python dengan pustaka OpenCV. Program ini memuat citra grayscale, mengubahnya menjadi citra biner melalui proses *thresholding*, kemudian menerapkan berbagai operasi morfologi seperti erosi, dilasi, opening, closing, dan morphological gradient.

Proyek ini dibuat sebagai bagian dari pembelajaran mata kuliah **Pengolahan Citra Digital** untuk mendemonstrasikan cara kerja operasi morfologi pada citra biner.

## 📂 Struktur Direktori

Pastikan struktur folder proyek Anda terlihat seperti berikut agar program berjalan tanpa error:

```text
project-folder/
│
├── main.py           # Script utama program
└── img/
    └── binerPy.jpg   # Citra input (wajib ada)

⚙️ Prasyarat & Instalasi
Program ini tidak membutuhkan perangkat keras khusus. Anda hanya memerlukan komputer yang dapat menjalankan Python.

1. Instalasi Dependensi
Jalankan perintah berikut di terminal untuk menginstal pustaka yang diperlukan:

Bash

pip install opencv-python numpy
2. Persiapan File
Pastikan file main.py dan folder img (berisi gambar) ditempatkan dalam satu direktori proyek yang sama.

🚀 Cara Penggunaan (Usage)
Program ini akan memproses citra dan menampilkan hasilnya secara bertahap dalam jendela popup OpenCV. Setiap jendela akan menunggu input tombol dari keyboard sebelum melanjutkan ke proses berikutnya.

Langkah menjalankan program:

Buka terminal atau command prompt.

Arahkan ke direktori proyek.

Jalankan perintah berikut:

Bash

python main.py
Urutan tampilan hasil program:

Citra Grayscale (Asli)

Citra Biner (Hasil Threshold)

Hasil Erosi

Hasil Dilasi

Hasil Opening

Hasil Closing

Hasil Morphological Gradient

🧠 Penjelasan Fungsi Pemrosesan
Berikut adalah detail operasi yang dilakukan oleh program ini:

Memuat Citra Grayscale Membaca citra dari file dan mengubahnya menjadi format skala abu-abu (grayscale).

Thresholding Mengubah citra grayscale menjadi citra biner (hitam putih mutlak) menggunakan nilai ambang batas (threshold) tertentu.

Erosi (Erosion) Mengurangi area objek dengan "mengikis" piksel tepi. Berguna untuk menghilangkan noise kecil di luar objek.

Dilasi (Dilation) Memperbesar area objek dengan menambah piksel di bagian tepi. Berguna untuk mengisi lubang kecil di dalam objek.

Opening Kombinasi operasi Erosi lalu Dilasi. Digunakan untuk menghilangkan noise (bintik-bintik kecil) tanpa mengubah bentuk objek utama secara signifikan.

Closing Kombinasi operasi Dilasi lalu Erosi. Digunakan untuk menutup celah atau lubang kecil di dalam objek (foreground).

Morphological Gradient Menghasilkan citra tepi (outline) objek. Didapatkan dari selisih antara hasil Dilasi dan hasil Erosi.
