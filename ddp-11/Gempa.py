class Gempa:
    #kontruktor Insialisasi Atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    #methof Penentu Skala Gempa
    def dampak(self):
        if self.skala < 2:
            print("Maka dampak gempa tidak berasa")
        elif 2 <= self.skala <= 4:
            print("Maka dampak bangunan retak-retak ")
        elif 4 <= self.skala <= 6:
            print("Maka dampak gempa bangunan roboh")
        elif self.skala > 6:
            print("Maka dampak gempa bangunan roboh dan berpotensi tsunami")
            
        print(f"Lokasi gempa: {self.lokasi}")
        print(f"Skala gempa: {self.skala}")

        

