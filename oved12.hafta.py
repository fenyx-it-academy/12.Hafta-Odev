class tasit():
    tasit_miktari = []
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4
    def modeli_goster(self):
        print("arabanin modeli", self.modeli)
    def koltuk_sayisigoster(self):
        print("arabanin toplam koltuk sayisi:", self.koltuk_sayisi)
    def km_durumugoster(self):
        return print("arabanin km durumu:", self.km_durumu)
    @classmethod
    def tasit_miktarini_goster(cls):
        return len(cls.tasit_miktati)
class araba(tasit):
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz = max_hiz
    def arabayi_durdur(self):
        print("araba durdu..")
    def gaza_bas(self):
        print("arabanin max hizi:")
        print("arabanin hizlaniyor..")
    def arabayi_yavaslat(self):
        print("araba yavasliyor..")
    def durum(self):
        if isinstance(araba, tasit):
            print("Bu sinif Tasit sinifindan miras alinmistir")
        else:
            print("Araba sinifi Tasit sinifindan miras alinmamistir.")
    def modeli_goster(self):
        print("araba sinifinin methodu..")
        super().modeli_goster()
toyoto=araba(2,5,150.000,"aygo",2018,300)
mercedes=tasit(2.2,7,200.000," S-Klasse",2015)
bwm=araba(6,5,0," Gran Turismo",2019,600)
ferrari=araba(800,5,4.670,"812 Superfast 6.5",2018,250)
print(toyoto.tekerlek_sayisi)
mercedes.koltuk_sayisigoster()
bwm.km_durumugoster()
ferrari.durum()
toyoto.modeli_goster()
