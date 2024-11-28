import math

def l_persegi (sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f"Luas Persegi {sisi}*{sisi}: {luas}")
    print(f"Keliling persegi adalah: {keliling}")

def persegi_panjang(panjang, lebar):
    luas = panjang*lebar   
    keliling = 2*(panjang + lebar)
    print(f"luas persegi panjang {panjang}*{lebar}: {luas}")
    print (f"keliling persegi panjang: {keliling}")

def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas*tinggi
    keliling = (2*alas)+(2*sisi_miring)
    print(f"luas jajar genjang {alas}*{tinggi}: {luas}")
    print(f"keliling jajar genjang: {keliling}")

def l_lingkaran(jari2):
    phi = 3.14
    luas = phi*jari2*jari2
    keliling = 2*jari2*phi
    print(f"luas lingkaran {phi}*{jari2}*{jari2} : {luas}")
    print (f"keliling lingkaran: {keliling}") 

def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5*diagonal1*diagonal2
    keliling = 4*sisi
    print(f"luas belah ketupat {0.5}*{diagonal1}*{diagonal2} : {luas}")
    print (f"keliling belah ketupat: {keliling}")

 

