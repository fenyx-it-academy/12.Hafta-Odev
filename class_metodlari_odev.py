#
#
# 12.Hafta-Odev
# Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi
# (class method) olarak tasit_miktari isimli bir bos liste tanimlayiniz.
# Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili gibi obje ozellikleri
# (instance attributes) olsun. Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin.
# Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek niteligi tanimlayin
# ve degeri 4 olsun. Ayrica bu objenin su methodlari olmalidir:
#
# 1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
# 2.modelini goster (tasitin modelini ekrana yazdirmali)
# 3. km_durumunu al (tasitin kilometre durumunu return etmeli)
# 4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.
#
# - bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
# - class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.
#

class Tasit():
    tasit_miktari=[]

    def __init__(self,marka, model,motor_gucu, koltuk_sayisi, km_durumu, satis_yili):
        self.marka=marka
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.model=model
        self.satis_yili=satis_yili
        self.tekerlek_sayisi=4
        self. __tasit_miktarini_guncelle()

    def __tasit_miktarini_guncelle(self):
        self.tasit_miktari.append(self)
    def koltuk_sayisini_goster(self):
        print(self.marka,'marka',self.model,"model aracin koltuk sayisi",self.koltuk_sayisi)

    def modelini_goster(self):
        print ( 'ARACIN MODELI',self.model )


    def km_durumu_goster(self):
        return print(self.marka,'marka',self.model,"model aracin km`si",self.km_durumu)

    @classmethod
    def __tasit_miktarini_goster(cls):
        print(len(cls.tasit_miktari),'adet tasit bulunmaktadir')
    @classmethod
    def goster(cls):
        return cls._Tasit__tasit_miktarini_goster()
    @classmethod
    def __str__(self) :
        return """ Lutfen marka, model,motor_gucu, koltuk_sayisi, km_durumu, satis_yili  seklinde giris yapiniz"""
#*****************************************************************************************************************8


class Araba(Tasit):                    #cvp-Araba sinifi tanimlandi ve Tasit tan miras alindi

    # Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir
    # ornek niteligi tanimlayiniz bu nitelik her orneklenme durumunda parametre olarak verilsin.
    def __init__(self,marka, model,motor_gucu, koltuk_sayisi, km_durumu, satis_yili,max_hiz):

        super().__init__(marka, model,motor_gucu, koltuk_sayisi, km_durumu, satis_yili)
        self.max_hiz=max_hiz

    def arabayi_durdur (self):    #1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
        print('Araba durdu....')

    def gaza_bas(self):           # 2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
        print("arabanin max hizi=",self.max_hiz)
        print('Araba hizlaniyor.....')

    def arabayi_yavaslat(self):      # 3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
        print('Araba yavaslayiyor.....')

    # Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve
    # ‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.

    def modelini_goster(self):
        print ('Araba sinifindaki model', self.model )

    # 4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise
    # “Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan
    # miras alinmamistir.’ seklinde yazsin)

    def arabanin_durumunu_goster(self):
        if 'goster' in self.__dir__():

            return print ( 'Bu sinif Tasit sinifindan miras alinmistir ' )
        else:

            return print('Araba sinifi Tasit sinifindan miras alinmamistir.')


#

while True:
    print()
    print ( 'TASIT CLASS ICIN GIRIS YAPINIZ' )
    print ( Tasit.__str__ () )
    Tasit.goster ()
    MARKA=input('MARKA :')
    MODEL=input('MODEL :')
    MOTOR_GUCU=input('MOTOR_GUCU :')
    KOLTUK_SAYISI=input('KOLTUK_SAYISI :')
    KM=input('KM :')
    SATIS_YILI=input('SATIS_YILI :')
    mercedes=Tasit(MARKA,MODEL,MOTOR_GUCU,KOLTUK_SAYISI,KM,SATIS_YILI)
    mercedes.goster()
    mercedes.modelini_goster ()
    mercedes.koltuk_sayisini_goster()
    mercedes.km_durumu_goster()
    print()
    print('ARABA CLASS ICIN GIRIS YAPINIZ')
    MARKA_A = input ( 'MARKA :' )
    MODEL_A = input ( 'MODEL :' )
    MOTOR_GUCU_A = input ( 'MOTOR_GUCU :' )
    KOLTUK_SAYISI_A = input ( 'KOLTUK_SAYISI :' )
    KM_A = input ( 'KM :' )
    SATIS_YILI_A = input ( 'SATIS_YILI :' )
    MAX_HIZ=input('MAX HIZ :')

    araba=Araba(MARKA_A,MODEL_A,MOTOR_GUCU_A,KOLTUK_SAYISI_A,KM,SATIS_YILI_A,MAX_HIZ)

    araba.goster ()
    araba.modelini_goster ()
    araba.koltuk_sayisini_goster ()

    araba.km_durumu_goster ()

    araba.arabanin_durumunu_goster()
    araba.gaza_bas ()
    araba.arabayi_yavaslat()
    araba.arabayi_durdur()


