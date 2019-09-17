class tasit():
    __tasit_miktari=[]
    def __init__(self,motor_gucu, koltuk_sayisi, km_göster, modeli, satis_yili ):
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_göster=km_göster
        self.modeli=modeli
        self.satis_yili=satis_yili
        self.__tasit_miktari_guncelle()
        tekerlek_sayisi=4

    def koltuk_sayisi_goster(self):
        print("aracın koltuk sayısı:",self.koltuk_sayisi)
    def model(self):
        print("aracın modeli",self.modeli)
    def km_göster(self):
        return self.km_göster
    @classmethod
    def __tasit_miktari_guncelle(cls):
        cls.__tasit_miktari.append(1)

class araba(tasit):
    def __init__(self,motor_gucu, koltuk_sayisi, km_göster, modeli, satis_yili,max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_göster, modeli, satis_yili)
        self.max_hiz=max_hiz
    def arabayi_durdur(self):
        print("Araba Durduruluyor...")
    def gaza_bas(self):
        print("Araba hizlaniyor...")
    def araba_yavaslat(self):
        print("Araba yavasliyor....")
    def arabanin_durumunu_goster(self):
        if issubclass(araba,tasit)==True:
            print("Bu sinif Tasit sinifindan miras alinmistir.")
        else:
            print("Araba sinifi Tasit sinifindan miras alinmamistir.")
    def model(self):
        print("Araba sinifinin metodudur.")
        super().model()




oto=tasit(1600,5,90000,3,2015)
oto1=tasit(1600,5,90000,3,2015)
oto2=araba(1800,7,75000,5,2018,360)
oto2.arabanin_durumunu_goster()
oto2.model()
oto.model()

print(oto.koltuk_sayisi)
print(oto1.koltuk_sayisi, oto1.modeli)
print(oto2.arabanin_durumunu_goster())
