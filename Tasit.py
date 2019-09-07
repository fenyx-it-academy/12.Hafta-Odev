
class tasit():
    __tasit_miktari=[]
    def __init__(self,motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili ):
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.modeli=modeli
        self.sais_yili=satis_yili
        self.__tasit_miktari_guncelle()
        self.tekerlek_sayisi=4

    def koltuk_sayisi_goster(self):
        print("bu aracin koltuk sayisi:",self.koltuk_sayisi)
    def model(self):
        print("Bu aracin Modeli",self.modeli)
    def km_al(self):
        return self.km_durumu
    @classmethod
    def __tasit_miktari_guncelle(cls):
        cls.__tasit_miktari.append(1)

class araba(tasit):
    def __init__(self,motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili,max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz=max_hiz
    def arabayi_durdur(self):
        print("Araba Durdu...")
    def gaza_bas(self):
        print("Arabaniz hizlaniyor...")
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




oto=tasit(1,50,100,3,233)
oto1=tasit(1,500,100,3,233)
oto2=araba(1,500,100,3,233,555)
oto2.arabanin_durumunu_goster()
oto2.model()
oto.model()

print(oto.koltuk_sayisi)
print(oto1.koltuk_sayisi, oto1.modeli)
