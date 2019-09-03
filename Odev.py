
class Tasit():


    __tasit_miktari = []    #Basina koyulan cift altcizgi ile kendisi harici initlerin
                            # goruntulemesine gizledik

    def __init__(self,motorgucu,koltuksayisi,kmdurumu,modeli,satisyili):
        self.TekerlerSayisi=4
        self.motorgucu = motorgucu
        self.koltuksayisi = koltuksayisi
        self.kmdurumu = kmdurumu
        self.modeli = modeli
        self.satisyili = satisyili
        Tasit.__tasit_miktari.append(self)    #HEr Orneklemede initler otomatik calisir..
                                            # bu nedenle her seferinde burdan ana listeye ekler


    def koltuk_sayisini_goster(self):
        print("Aracin Toplam Koltuk Sayisi : ", self.koltuksayisi)


    def modelini_goster(self):
        print("Aracin Modeli : ", self.modeli)


    def km_durumunu_al(self):
        return self.kmdurumu

    @classmethod
    def tasit_miktari_goster(cls):
        return len(cls.__tasit_miktari)







class Araba(Tasit):
    def __init__(self, motorgucu, koltuksayisi, kmdurumu, modeli, satisyili, max_hiz):
        super().__init__(motorgucu, koltuksayisi, kmdurumu, modeli, satisyili)
        self.max_hiz = max_hiz

    def arabayi_durdur(self):
        print("Arac Durduruluyor...")


    def gaza_bas(self):
        print("GAza Basiliyorr...")


    def arabayi_yavaslat(self):
        print("Frene Basiliyor..")


    def arabanin_durumunu_goster(self):

        if 'a' in self.__dir__():

                return print ( 'Bu sinif Tasit sinifindan miras alinmistir ' )
        else:

                return print('Araba sinifi Tasit sinifindan miras alinmamistir.')



    def modelini_goster(self): 
        print("Araba sinifinin methodu….")
        super().modelini_goster()


araba1 = Tasit(1.4,4,34000,2015,2015)

araba2 = Tasit(1.6,4,30.000,2015,2015)

araba3= Araba(1.0,6,54555,2011,2011,280)

araba4 = Araba(1.0,5,54555,2000,2000,300)

print(Tasit.tasit_miktari_goster())
print(araba1.TekerlerSayisi)
print(araba2.koltuk_sayisini_goster())
print(araba4.km_durumunu_al())
araba4.arabanin_durumunu_goster()
