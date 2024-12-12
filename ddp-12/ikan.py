from animals import *

class ikan(animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan

    def cetak_ikan(self):
        super ().cetak()
        print(f"hewan ini berwarna {self.warna} dan hewan ini berjenis {self.jenis}")

print("========Cetak Jenis Burung==========")
print("=====OBJEK PERTAMA=======")
badut = ikan ('Ikan Badut', 'plankton', 'air', 'bertelur', 'orange, putih, hitam', 'air laut')
badut.cetak_ikan()

print("=====OBJEK KEDUA=======")
cupang = ikan ('Ikan Cupang', 'pelet', 'air', 'bertelur', 'warna gradasi', 'air tawar ')
cupang.cetak_ikan()