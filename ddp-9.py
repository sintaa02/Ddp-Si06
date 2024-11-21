#SOAL 1 
print("\n-------celcius ke fahrenhet-----------")
def celcius_ke_fahrenhet(celcius):
    print(celcius * 9/5 +32 )
celcius_ke_fahrenhet(0)
celcius_ke_fahrenhet(100)
print("==================================")
#SOAL 2
print("\n------------Mencari Bilangan Genap------------")
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)
#SOAL 3
print("---------Keterangan lulus dan tidak lulus----------")
#rata-rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 70:
        print("LULUS")
    else:
        print("GAGAL")
skor(80)
skor(60)

#SOAL 4
print("\n-----------Mencetak bilangan ganjil--------")
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1,2):
        print(i, end="") 
bil_ganjil(20)
