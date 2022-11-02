# NIM/Nama : 19622193//Mesach Harmasendro
# Tanggal : 2 November 2022
# Deskripsi : Program untuk mencari total tinggi bangunan yang bisa di foto oleh Tuan Kil, foto terbaik adalah foto dengan total tinggi bangunan tertimggi
#             Menerima masukan besar kota Kompeng dan data tinggi bangunan di kota Kopeng
#             Mengeluarkan pada layar total tinggi untuk foto terbaik            

# KAMUS
# N, i, j, tinggi, sum, k, max: integer
# tinggi_bangunan: matrix of integer (NxN)
# total_tinggi: array of integer

# ALGORITMA
N = int(input("Masukkan besar Kota Kompeng: "))

tinggi_bangunan = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        tinggi_bangunan[j][i] = int(input(f"Masukkan tinggi bangunan bari {i + 1} kolom {j + 1}: "))

total_tinggi = [0 for i in range(N*2)]

for i in range(N):
    tinggi = tinggi_bangunan[i][0]
    sum = tinggi_bangunan[i][0]
    for j in range(1, N):
        if tinggi_bangunan[i][j] > tinggi:
            sum += tinggi_bangunan[i][j]
            tinggi = tinggi_bangunan[i][j]
    total_tinggi[i] = sum
    
for i in range(N):
    tinggi = tinggi_bangunan[i][N-1]
    sum = tinggi_bangunan[i][N-1]
    for j in range(N-2, -1,-1):
        if tinggi_bangunan[i][j] > tinggi:
            sum += tinggi_bangunan[i][j]
            tinggi = tinggi_bangunan[i][j]
    total_tinggi[i + N] = sum
    
max = total_tinggi[0]
for k in total_tinggi:
    if k > max:
        max = k
        
print(f"Foto terbaik memiliki total tinggi: {max}")