class Tasit ():
    __tasit__miktari = []

    def __init__(self,motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.model = model
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4

    def koltuk_sayisini_goster (self):
        print(self.koltuk_sayisi)

    def km_durumunu_goster(self):
        print(self.km_durumu)

    def modelini_goster (self):
        print(self.model)

    def tasit_miktarini_guncelle(self):
        self.__tasit__miktari.append (1)


    @classmethod

    def __tasit_miktarini_goster(cls):
        return len(cls.__tasit__miktari)


class Araba(Tasit):
    def __init__(self, motorgucu,koltuksayisi,kmdurumu,modeli,satisyili,max_hiz):
        super().__init__(motorgucu,koltuksayisi,kmdurumu,modeli,satisyili)
        self.max_hiz = max_hiz

    def arabayi_durdur(self):
        print('Arac durduruluyor...')

    def gaza_bas(self):
        print('Gaza basiliyor...')

    def arabayi_yavaslat(self):
        print('Frene basiliyor...')

    def arabanin_durumunu_goster (self):

        if 'a' in  self.__dir__():

            return print('Bu sinif Tasit sinifindan miras alinmistir.')

        else:
            return print('Araba sinifi Tasit sinifinden miras alinmamistir.')


    def modelini_goster(self):
        print('Araba sinifinin methodu...')
        super().modelini_goster()


araba1 = Tasit(1.4,4,34000,2017,2017)

araba2 = Tasit(1.6,4,30.000,2017,2017)

araba3= Araba(1.0,6,54555,2012,2012,280)

araba4 = Araba(1.0,5,54555,2000,2000,300)

print(araba1.tekerlek_sayisi)
araba2.koltuk_sayisini_goster()
araba4.km_durumunu_goster()
araba4.arabanin_durumunu_goster()
