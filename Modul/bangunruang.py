import math

def kubus (sisi):
    luas = 6*sisi*sisi
    volume = sisi*sisi*sisi
    print(f"Luas kubus adalah {6}*{sisi}*{sisi} : {luas}")
    print(f"volume kubus adalah: {volume}")
def balok (panjang, lebar, tingi):
    luas = (2*panjang*lebar)+(2*panjang*tingi)+(2*lebar*tingi)
    volume = panjang*lebar*tingi
    print (f"Luas balok ({2}*{panjang}*{lebar})+({2}*{panjang}*{tingi})+{2}*{lebar}*{tingi} : {luas} ")
    print(f"Volume balok adalah: {volume}")
def tabung (jari2, tingi):
    phi = 3.14
    luas = 2*phi*jari2*(jari2+tingi)
    volume = phi * jari2 * jari2 * tingi
    print(f"Luas tabung {2}*{phi}*{jari2}*({jari2}+{tingi}): {luas}")
    print(f"Volume tabung adalah: {volume}")
def kerucut (jari2,tinggi,garispelukis):
    phi = 3.14
    luas= phi*jari2*(jari2+garispelukis)
    volume= 1/3*phi*jari2*jari2*tinggi
    print(f"Luas kerucut {phi}*{jari2}*({jari2}+{garispelukis}): {luas}")
    print(f"Volume kerucut adalah: {volume}")
def bola (jari2):
    phi= 3.14
    luas = 4*phi*jari2*jari2
    volume = 4/3*phi*jari2*jari2*jari2
    print(f"Luas bola {4}*{phi}*{jari2}*{jari2}: {luas} ")
    print(f"Volume bola adalah: {volume}")
    










































