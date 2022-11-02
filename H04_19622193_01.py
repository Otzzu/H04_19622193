# NIM/Nama : 19622193//Mesach Harmasendro
# Tanggal : 2 November 2022
# Deskripsi : Program untuk memeriksa tumpukan apakah sudah sesuai dengan perintah Tuan Leo atau tidak
#             Menerima input banyak tumpukan, tinggi tumpukan, dan data berat benda yang akan ditumpuk
#             Mengeluarkan pada layar apakah tumpukkan memenuhi perintah Tuan Leo atau tidak

# KAMUS
# M, N, i, j, max: integer
# str_memenuhi: string
# tumpukan: matrix of integer (NxM)
# k: array of integer

# ALGORTIMA
M = int(input("Masukkan tinggi tumpukan: "))
N = int(input("Masukkan banyak tumpukan: "))

tumpukan = [[0 for i in range(M)] for i in range(N)]

for i in range(M):
    for j in range(N):
        tumpukan[j][i] = int(input(f"Masukkan berat benda pada baris ke-{i+1} kolom ke-{j+1}: "))

str_memenuhi = "memenuhi"

for k in tumpukan:
    max = k[M-1]
    for j in range(M-1):
        if k[j] > max:
            str_memenuhi = "tidak memenuhi"
            
print(f"Susunan tersebut {str_memenuhi} perintah Tuan Leo.")
            