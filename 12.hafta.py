"""Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari
 isimli bir bos liste tanimlayiniz. Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli,
 satis_yili gibi obje ozellikleri(instance attributes) olsun. Ve her orneklenme durumunda bu ozellikler
 parametre olarak verilsin. Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek
 niteligi tanimlayin ve degeri 4 olsun. Ayrica bu objenin su methodlari olmalidir:

1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
2.modelini goster (tasitin modelini ekrana yazdirmali)
3. km_durumunu al (tasitin kilometre durumunu return etmeli)
4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.

- bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
- class method olarak tasit_miktarini gosterecek bir method tanimlayiniz."""

class Tasit:
    __tasit_miktari = []      # degisken gizlendi
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
        print("Tasit modeli:", self.modeli)

    def km_durumu_al(self):
        return self.km_durumu

    @classmethod
    def tasit_miktari(cls):
        return len(cls.__tasit_miktari) # listedeki eleman sayisini yani tasit miktarini return ediyor

# araba = Tasit(1700, 5, 10000, 2019, 2019)
# print(Tasit.tasit_miktari())

"""Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. 
Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir 
ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin. 
Bu sinifta su methodlari tanimlayiniz;

1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
“Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
miras alinmamistir.’ seklinde yazsin)
Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz 
ve ‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz."""

class Araba(Tasit):
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz = max_hiz

    def arabayi_durdur(self):
        print("Araba durdu.")

    def gaza_bas(self):
        print("Araba hizlaniyor.")

    def arabayi_yavaslat(self):
        print("Araba yavasliyor.")

    def arabanin_durumu(self):
        if issubclass(self, Tasit):
            print("Bu sinif Tasit sinifindan miras alinmistir.")
        else:
            print("Araba sinifi Tasit sinifindan miras alinmamistir.")

    def modelini_goster(self): # super in methodu override edildi
        print("Araba sinifinin methodu….")
        super().modelini_goster()

at_arabasi = Tasit(1, 2, 100, 1900, 1945)
print(Tasit.tasit_miktari())

volvo = Araba(2400, 5, 1000, 2019, 2020, 400)
print(Tasit.tasit_miktari())

at_arabasi.modelini_goster()
print(at_arabasi.km_durumu_al()) # sadece return ettigi icin print e alindi
at_arabasi.koltuk_sayisini_goster()

volvo.modelini_goster()
print(volvo.km_durumu_al())
volvo.koltuk_sayisini_goster()