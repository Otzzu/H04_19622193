# NIM/Nama : 19622193//Mesach Harmasendro
# Tanggal : 2 November 2022
# Deskripsi : Program untuk mengoperasikan sebuah array of integer sehingga semua isi dari array itu menjadi 0 semua
#             Terdapat 2 fungsi di sini yaitu fungsi mencari nilai minimum di array tapi tidak 0 dan fungsi untuk mengecek apakah array sudah berisi 0 semua atau belum
#             Menerima masukan berupa banyak nilai dan data dari nilai tersebut
#             Mengeluarkan pada layar isi array pada setiap prosesnya
#             Dipastikan semua nilai pada array merupakan integer tak negatif

# KAMUS
# N, i, min: integer
# arr, arr2: array of integer

# ALGORITMA
def minArray(arr):
    # Fungsi untuk mencari nilai minimum di dalam sebuah array tapi bukan 0
    # Mengembalikan nilai minimum pada array
    
    # KAMUS LOKAL
    # min, i: integer
    # arr: array of integer
    
    # ALGORITMA
    min = -1
    for i in arr:
        if min == -1 and i != 0:
            min = i
        elif i < min and i != 0:
            min = i
    return min

def checkArray(arr):
    # Fungsi untuk mengecek apakah isi sebuah array sudah 0 semua atau belum
    # jika sudah 0 semua maka akan mengembalikan True, jika belum maka akan mengembalikan False
    
    # KAMUS LOKAL
    # i: integer
    # arr: array of integer
    
    # ALGORITMA
    for i in arr:
        if i != 0:
            return False
    return True

def printArray(arr):
    # Sebuah fungsi prosedur yang digunakan untuk memgeluarkan isi pada array ke layar sesuai dengan format yang ditentukan
    
    # KAMUS LOKAL
    # i: integer
    # arr: array of integer
    
    # ALGORITMA
    for i in arr:
        print(i, end=" ")
    print("")
    
N = int(input("Masukkan banyak nilai: "))

arr = [0 for i in range(N)]

for i in range(N):
    arr[i] = int(input(f"Masukkan nilai ke-{i+1}: "))

printArray(arr)
while not checkArray(arr):
    min = minArray(arr)
    
    arr2 = [(arr[i]-min) for i in range(N)]
    
    for i in range(N):
        if arr2[i] < 0:
            arr2[i] = 0
    
    arr = arr2
    printArray(arr)