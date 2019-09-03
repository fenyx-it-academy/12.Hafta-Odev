"""(1)Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari isimli bir bos liste tanimlayiniz.
Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili gibi obje ozellikleri(instance attributes) olsun. Ve her orneklenme
durumunda bu ozellikler parametre olarak verilsin. Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek niteligi tanimlayin ve degeri 4 olsun.
Ayrica bu objenin  su methodlari olmalidir:

    1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
    2.modelini goster (tasitin modelini ekrana yazdirmali)
    3. km_durumunu al (tasitin kilometre durumunu return etmeli)
    4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.

    - bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
    - class method olarak tasit_miktarini gosterecek bir method tanimlayiniz."""

"""(2)Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz 
ve max_hiz isimli bir ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin.
Bu sinifta su methodlari tanimlayiniz;

    1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
    2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
    3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
    4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
    “Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
    miras alinmamistir.’ seklinde yazsin)
Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve ‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.
"""


class Tasit():
    __tasit_miktari = []
    #tasit miktarini gizledik
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.model = model
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4

    def koltuk_sayisini_goster(self):
        print(self.koltuk_sayisi)

    def modelini_goster(self):
        print(self.model)

    def km_durumu_goster(self):
        return float(self.km_durumu)

    def tasit_miktari_guncel(self):
        self.__tasit_miktari += [1]#her orneklemede tasit +1 artiyor
        print(len(self.__tasit_miktari))

    @classmethod
    def tasit_miktarigoster(cls):
        print(len(cls.__tasit_miktari))


class Araba(Tasit):
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili,max_hiz):#mirastan aldigimiza bir tane ozellik daha ekledik
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili)

        self.max_hiz = max_hiz

    def arabayi_durdur(self):
        print("araba durdu")

    def gaza_bas(self):
        print("araba hizlaniyor")

    def arabayi_yavaslat(self):
        print("araba yavasliyor")

    def araba_durumunu_goster(self):
        if issubclass(Araba,Tasit):#miras durumunu sorguluyoruz
            print("Bu sinif Tasit sinifindan miras alinmistir")
        else:
            print("Araba sinifi Tasit sinifindan miras alimamistir")
    def modelini_goster(self):
        print(self.model)
        print("araba sinifinn methodu")

ford = Araba(1.6,12,120,"transit",2005,180)
toyota = Araba(1.5,6,60,"corolla",2010,150)
mercedes = Araba(1.9,6,10,"benz",2003,180)

ford.araba_durumunu_goster()
toyota.modelini_goster()
mercedes.arabayi_durdur()
mercedes.tasit_miktarigoster()

