#hafta 12 odev1#
#class olusturup uygun ornek ekleme#

class Tasit:
    __tasit_miktari = []      # degiskeni gizliyoruz
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4
        Tasit.__tasit_miktari.append(self)

    def koltuk_sayisini_goster(self):
        print("Koltuk sayisi:", self.koltuk_sayisi)

    def modelini_goster(self):
        print("Arac modeli:", self.modeli)

    def km_durumu_al(self):
        return self.km_durumu

    @classmethod
    def tasit_miktari(cls):
        return len(cls.__tasit_miktari) # olusturulan ornek miktari sayi cinsinden 

BMW= Tasit(1400, 5, 9000, 2016, 2010)
Audi= Tasit(1600, 2, 5000, 2020, 2011)
Mercedes= Tasit(1700, 5, 10000, 2019, 2019)
print(Tasit.tasit_miktari())



