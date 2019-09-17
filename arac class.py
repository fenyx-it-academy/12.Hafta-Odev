class tasit():
    __TasitMiktari = []
    tasitsayisi=0
    tekerlekS=4

    def __init__(self,isim,motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.isim= isim
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili


    def TasitMiktariEkle(self):
        self.__TasitMiktari.append(self.isim)

    def ModelGoster(self):
        print("Aracın modeli {} dir".format(self.modeli))

    def kmGoster(self):
        print("Aracın km'si {} dir".format(self.km_durumu))

    def SatısYılıGoster(self):
        print("Aracın satış yılı {} dir".format(self.satis_yili))

    def MotorGucuGoster(self):
        print("Aracın Motor Gücü {} dir".format(self.motor_gucu))

    def KoltukSayisiniGoster(self):
        print("Aracın koltuk sayısı {} dır".format(self.koltuk_sayisi))


    @classmethod
    def AracListesiGoster(cls):
        for i in range(len(cls.__TasitMiktari)):
            print(i+1,") ",cls.__TasitMiktari[i])

    @classmethod
    def Tasit_guncelle(cls):
        tasitsayisi=len(cls.__TasitMiktari)


class Araba(tasit):
    def __init__(self,isim,motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili,maxhiz):
        super().__init__(isim,motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.maxhiz=maxhiz
    def arabayi_durdur(self):
        print("Araba durdu")

    def gaza_bas(self):
        print("Araba hızlanıyor")

    def araba_yavaslat(self):
        print("Araba yavaşlıyor")

    def maxHızGoster(self):
        print("Aracın max hızı {} dir".format(self.maxhiz))

    @classmethod
    def arabanın_durumu(cls):
        if issubclass(Araba,tasit):
            print("Araba sınıfı tasit sınıfından miras alınmıştır")
        else:
            print("Araba sınıfı tasit sınıfından miras alınmamıştır")

    def tasit_modeli_goster(self):
        super().ModelGoster()
        print("Araba sınıfının modeli ....{}".format(self.modeli))

    def AracTumOzellikGoster(self):
        self.ModelGoster()
        self.SatısYılıGoster()
        self.kmGoster()
        self.SatısYılıGoster()
        self.MotorGucuGoster()
        self.KoltukSayisiniGoster()
        self.maxHızGoster()


# 1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
# 2.modelini goster (tasitin modelini ekrana yazdirmali)
# 3. km_durumunu al (tasitin kilometre durumunu return etmeli)
# 4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.

print("---ARAÇ LİSTESİ ---")
opel=Araba("opel",75,4,12000,2005,2019,180)
toyota=Araba("toyota",90,4,50000,2009,2018,185)
mercedes=Araba("mercedes",120,4,55870,2018,2018,220)
opel.TasitMiktariEkle()
toyota.TasitMiktariEkle()
mercedes.TasitMiktariEkle()


while True:
    Araba.AracListesiGoster()
    secim=input("\nLütfen seçiminizi yapınız\n\n1- Araç Ekle \n2- Araç Göster\n")

    if secim=="1":
        arac_isim=input("Araç isim / marka giriniz..")
        print("Şimdi sırası ile araç gücü, koltuk sayısı, ",
              "km bilgisi, model yılı, satış yılı ve max hızını ",
              "sırası ile enter tuşuna basarak giriniz")
        arac_isim = Araba(arac_isim,int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))
        arac_isim.TasitMiktariEkle()
        continue

    if secim=="2":
        arac_secim=int(input("\nSeçmek istediğiniz aracın numarasını giriniz"))
        if arac_secim==1:
            print("*** OPEL  ***")
            opel.AracTumOzellikGoster()
        if arac_secim == 2:
            print("*** TOYOTA  ***")
            toyota.AracTumOzellikGoster()
        if arac_secim == 3:
            print("*** MERCEDES  ***")
            mercedes.AracTumOzellikGoster()








