from animals import *

class Burung(animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung (self):
        super ().cetak()
        print(f"hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}")

print("========Cetak Jenis Burung==========")
print("=====OBJEK PERTAMA=======")
beo = Burung ('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'halo')
beo.cetak_burung()
print("=====OBJEK KEDUA=======")
pipit = Burung ('Burung Pipit', 'biji-bijian', 'udara', 'bertelur', 'coklat', 'Cip-cip-cip')
pipit.cetak_burung()