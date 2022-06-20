#versi 1

def faktorial(x):
    hasil = 1 
    for i in range (2, x + 1):
        hasil *= i
    return hasil

print ("Hasil dari Faktorial 10 adalah :",faktorial(10))

print()
#versi 2 

n = int(input("Masukan angka yang ingin di hitung : "))
def hitung_faktorial (n):
    if n > 2:
        return n * hitung_faktorial(n-1)
    return 2
faktorial1 = hitung_faktorial(n)
print(f'{n}! = {faktorial1}')