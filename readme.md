Program ini memproses citra grayscale menjadi citra biner lalu menerapkan operasi morfologi seperti erosi, dilasi, opening, closing, dan gradient menggunakan OpenCV. Seluruh proses ditampilkan secara interaktif melalui jendela tampilan.

Persiapan Lingkungan

Pasang dependensi berikut:

pip install opencv-python
pip install numpy

Siapkan folder kerja seperti berikut:

proyek/
main.py
img/
binerPy.jpg

Cara Menjalankan Program

Jalankan dengan:

python main.py

Program akan membuka beberapa jendela hasil proses secara bergantian. Setiap tampilan menunggu penekanan tombol sebelum lanjut ke proses berikutnya.

Penjelasan Alur Program dalam Format prom py
Membaca Citra Grayscale
image_gray = cv2.imread(path_file, cv2.IMREAD_REDUCED_GRAYSCALE_2)

Konversi Menjadi Citra Biner
\_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

Membuat Kernel
kernel2 = np.ones((11, 11))

Operasi Erosi
erode = cv2.erode(image_binary.copy(), None)

Operasi Dilasi
dilasi = cv2.dilate(image_binary.copy(), kernel2)

Operasi Opening
opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN, None)

Operasi Closing
closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE, kernel2)

Operasi Gradient
gradient = dilasi - erode

Penjelasan Hasil

Erosi mengurangi ukuran objek.
Dilasi menambah luas objek.
Opening menghilangkan noise kecil.
Closing menutup celah dan lubang kecil.
Gradient menunjukkan garis tepi objek.

Pengembangan

Bagian kode tambahan seperti operasi top hat, black hat, dan iterasi morfologi tersedia dalam komentar dan dapat diaktifkan sesuai kebutuhan eksplorasi.

Anggota Kelompok

Abdul Aziez A. S

Dwi Nurcahyo

Rayhan Maullana B.

Ryan Hidayat
