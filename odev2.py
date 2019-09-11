#hafta 12 odev2#
#ilk olusturulan classtan miras aliyoruz ve yeni fonksiyonlar ekliyoruz

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





class Araba(Tasit):
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz = max_hiz

    def arabayi_durdur(self):
        print("Araba durdu!")

    def gaza_bas(self):
        print("Araba hizlaniyor***")

    def arabayi_yavaslat(self):
        print("Araba yavasliyor--")

    def arabanin_durumu(self):
        if issubclass(self, Tasit):
            print("Bu arac eski nesildir")
        else:
            print("Arac yeni nesildir")

    def modelini_goster(self): 
        print("Tasitin modeli alttadir-->")
        super().modelini_goster()

murat131= Tasit(500, 4, 230000, 1992, 2000)
print(Tasit.tasit_miktari())

opel= Araba(2700, 8, 20000, 2018, 2020, 300)
print(Tasit.tasit_miktari())

murat131.modelini_goster()
print(murat131.km_durumu_al()) 
murat131.koltuk_sayisini_goster()

opel.modelini_goster()
print(opel.km_durumu_al())
opel.koltuk_sayisini_goster() 
