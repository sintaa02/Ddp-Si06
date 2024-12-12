class animals:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self. makanan = makanan
        self. hidup = hidup
        self. berkembang_biak = berkembang_biak

    def cetak(self):
        print(f"Hewan {self.nama} dia memakan {self.makanan}, dia juga hidup di {self.hidup}, dan berkembang biak dengan cara {self.berkembang_biak}")

# C1 = animals('buaya', 'daging', 'Amphibi', 'Bertelur')
# C1.cetak()
# C2 = animals('ikan','Pelet', 'Air', 'bertelur')
# C2.cetak()