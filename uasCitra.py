import cv2
import os
import numpy as np

# Kelompok
#Abdul Aziez A.S
#Dwi Nurcahyo
#Rayhan Maullana B.
#Ryan Hidayat 

path_file = 'img/binerPy.jpg'
image_gray = cv2.imread(path_file, cv2.IMREAD_REDUCED_GRAYSCALE_2)
_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("1. Asli Grayscale", image_gray)
cv2.imshow("2. Setelah Threshold (Biner)", image_binary)
waitKey = cv2.waitKey(0)
#buat Arr

kernel2 = np.ones((11,11))
#EROSI
# for i in range(0,3) :
#     dilasi = cv2.dilate(image_binary.copy(),kernel2, iterations=i + 1)
#     cv2.imshow(f"Dilasi ke {i+1} ",dilasi)
#     waitKey = cv2.waitKey(0)
erode = cv2.erode(image_binary.copy(),None)
cv2.imshow("EROSI",erode)
waitKey = cv2.waitKey(0)
#DILASI
dilasi = cv2.dilate(image_binary.copy(),kernel2)
cv2.imshow("DILASI",dilasi)
waitKey = cv2.waitKey(0)

#Opening
opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN,None)
cv2.imshow("OPENING",opening)
waitKey = cv2.waitKey(0)
#closing
closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE,kernel2)
cv2.imshow("CLOSING",closing)
waitKey = cv2.waitKey(0)

# for i in range(0,3) :
#     open2 = cv2.morphologyEx(image_binary,cv2.MORPH_OPEN,kernel2, iterations=i + 1)
#     cv2.imshow(f"OPENING KE {i+1} ",open2)
#     waitKey = cv2.waitKey(0)

gradient = dilasi - erode
cv2.imshow("gradient", gradient)
waitKey = cv2.waitKey(0)

# tophat = image_binary - opening
# cv2.imshow("TOPHAT", tophat)
# blackHat = image_binary - closing
# cv2.imshow("BlackHat", blackHat)
# gradient
# waitKey = cv2.waitKey(0)
# #OPENING
# daftar_kernel_size = [(3,3), (5,5), (7,7)]
# for k_size in daftar_kernel_size:
#     # PENTING: Lakukan morphology pada gambar BINARY
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k_size) 
#     opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN,kernel )
#     judul = f"Opening Biner : ({k_size[0]},{k_size[1]})"
#     cv2.imshow(judul, opening)
#     print(f"Menampilkan {judul}. Tekan tombol untuk lanjut...")
#     cv2.waitKey(0)
#     cv2.destroyWindow(judul)


# #CLOSING
# for k_size in daftar_kernel_size:
#     # PENTING: Lakukan morphology pada gambar BINARY
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k_size) 
#     closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE,kernel )
#     judul = f"Opening Biner : ({k_size[0]},{k_size[1]})"
#     cv2.imshow(judul, closing )
#     print(f"Menampilkan {judul}. Tekan tombol untuk lanjut...")
#     cv2.waitKey(0)
#     cv2.destroyWindow(judul)
    
    
# for i in range(0,3) :
#     dilasi = cv2.dilate(image_binary.copy(),None, iterations=i + 1)
#     cv2.imshow(f"Dilasi{i+1}kali ",dilasi)
#     waitKey = cv2.waitKey(0)