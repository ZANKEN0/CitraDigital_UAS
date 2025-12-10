Program ini dibuat untuk melakukan pemrosesan citra biner serta menerapkan berbagai operasi morfologi menggunakan library OpenCV. Citra yang digunakan adalah citra grayscale yang kemudian diubah menjadi citra biner. Setelah proses pembentukan citra biner, beberapa operasi morfologi dasar diterapkan, yaitu erosi, dilasi, opening, closing, dan gradient morfologi.

1. Import Library
   Program ini menggunakan tiga library utama:
   cv2 untuk pengolahan citra
   os untuk pengelolaan file (walau tidak digunakan langsung dalam kode)
   numpy untuk pembuatan kernel operasi morfologi

2. Membaca Citra Grayscale
   Citra dibaca dari folder img dengan mode grayscale yang direduksi ukuran (IMREAD_REDUCED_GRAYSCALE_2).
   image_gray = cv2.imread(path_file, cv2.IMREAD_REDUCED_GRAYSCALE_2)

3. Konversi ke Citra Biner
   Citra grayscale diubah menjadi citra biner dengan threshold 127. Nilai piksel yang lebih tinggi menjadi putih (255), sedangkan yang lebih rendah menjadi hitam (0).
   \_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

4. Pembuatan Kernel
   Kernel berukuran 11x11 dibuat menggunakan array berisi nilai 1.
   kernel2 = np.ones((11,11))

5. Operasi Morfologi
   Berbagai operasi morfologi dilakukan pada citra biner.
   a. Erosi
   Erosi mengecilkan objek dengan mengurangi batas piksel putih.
   erode = cv2.erode(image_binary.copy(), None)
   b. Dilasi
   Dilasi memperbesar objek dengan menambah piksel putih di sekitar kontur.
   dilasi = cv2.dilate(image_binary.copy(), kernel2)
   c. Opening
   Opening merupakan kombinasi erosi diikuti dilasi. Operasi ini berguna untuk menghilangkan noise kecil.
   opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN, None)
   d. Closing
   Closing merupakan kebalikan opening (dilasi diikuti erosi). Digunakan untuk menutup lubang kecil pada objek.
   closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE, kernel2)
   e. Morphological Gradient
   Gradient morfologi diambil dari selisih antara hasil dilasi dan erosi. Operasi ini menonjolkan tepi objek.
   gradient = dilasi - erode

6. Menampilkan Hasil
   Setiap hasil operasi morfologi ditampilkan menggunakan cv2.imshow() dan menunggu input tombol dengan cv2.waitKey(0).
