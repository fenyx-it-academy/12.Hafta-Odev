class Tasit(object):
    tekerlek_sayisi=4
    __tasit_miktari=[]

    def __init__(self,motor_gucu,koltuk_sayisi,km_durumu,model,satis_yil):
        self.mg=motor_gucu
        self.ks=koltuk_sayisi
        self.kmd=km_durumu
        self.m=model
        self.sy=satis_yil
        Tasit.__tasit_miktari.append(self)

    def koltuksayisigoster(self):
        print("Aracin koltuk sayisi:\t",self.ks)

    def modelinigoster(self):
        print("Aracin modeli:\t",self.m)

    def km_durumunual(self):
        print("aracin km_durumu:\t",self.kmd)

    def tasit_miktar_guncelle(self):
        return print(len(self.__tasit_miktari))

    @classmethod
    def tasit_miktari_goruntule(cls):
        return len(cls.__tasit_miktari)




class Araba(Tasit):

    def __init__(self,motor_gucu,koltuk_sayisi,km_durumu,model,satis_yil,max_hiz):
        super().__init__(motor_gucu,koltuk_sayisi,km_durumu,model,satis_yil)
        self.max_hizi=max_hiz

    def araba_durdur(self):
        print("Arac durduruluyor")

    def gaza_bas(self):
        print("Gaza basiliyor")

    def yavaslat(self):
        print("Yavaslatiliyor")

    def arabanin_durumunu_goster(self):
        if issubclass(Araba,Tasit):
            print("Bu arac tasit sinifindan miras alinmistir ")
        else:
            print("Bu arac tasit sinifindan miras alinmamistir")

    def modelini_goster(self):
        super().modelinigoster()
        print("Arabanin modeli:\t",self.modelinigoster)

audi=Tasit(100,4,1000,2010,2011)
skoda=Araba(200,8,2000,2015,2018,280)
print(audi.tekerlek_sayisi)
print(Tasit.tasit_miktari_goruntule())
skoda.arabanin_durumunu_goster()
audi.tasit_miktar_guncelle()
print(skoda.tekerlek_sayisi)
