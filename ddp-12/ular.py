from animals import *

class ular(animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, cara_menyerang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.cara = cara_menyerang

    def cetak_ular(self):
        super ().cetak()
        print(f"hewan ini berwarna {self.warna} dan hewan ini menyerang dengan cara {self.cara}")

print("========Cetak Jenis Burung==========")
print("=====OBJEK PERTAMA=======")
Viper = ular ('Ular viper', 'mamalia Kecil', 'darat', 'bertelur', 'hijau', 'melilit mangsa')
Viper.cetak_ular()

print("=====OBJEK KEDUA=======")
Kobra = ular ('Ular Kobra', 'daging', 'darat', 'bertelur', 'hitam', 'penggunaan bisa')
Kobra.cetak_ular()