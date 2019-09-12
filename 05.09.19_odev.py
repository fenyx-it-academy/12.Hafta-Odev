class Tasit():

    tasit_sayisi = 0
    __tasitlarim = []

    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, tekerlek_sayisi = 4):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = tekerlek_sayisi
        Tasit.__tasitlarim.append(self)

    @classmethod
    def tasit_miktari_goruntule(cls):
        return len(cls.__tasitlarim)

    def koltuksayisi(self):
        print("Aracin koltuk sayisi : ", tasit1.koltuk_sayisi)

    def model_goster(self):
        print("Aracin modeli : ", tasit1.modeli)

    def kmdurumu(self):
        print("Aracin km'si : ", tasit1.km_durumu)

    def tasit_miktari_guncelle(self):
        Tasit.tasit_sayisi += 1
        print("Mevcut arac sayisi : ", Tasit.tasit_sayisi)


class Araba(Tasit):

    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz=max_hiz

    def arabayi_durdur(self):
        print("Araba durdu")

    def gaza_bas(self):
        print("Araba hizlaniyor")

    def arabayi_yavaslat(self):
        print("Araba yavasliyor")

    def arabanin_durumunu_goster(self):
        if issubclass(Araba,Tasit):
            print("Bu sinif 'Tasit' sinifindan miras alinmistir")
        else:
            print("Araba sinifi 'Tasit' sinifindan miras alinMAmistir")

    def model_goster(self):
        print("Araba sinifinin methodu…")
        super().model_goster()

tasit1 = Tasit(1600, 6, 76825, 2016, 2018)
araba1 = Araba(1600, 6, 76825, 2016, 2018, 340)




print("""Lutfen yapmak istediginiz islemi seciniz\n
    Koltuk sayisini gorme       1
    Tasitin modelini gorme      2
    Tasitin km'sini gorme       3
    Tasit miktarini guncelle    4
    Arabayi durdur              5
    Arabayi hizlandir           6
    Arabayi yavaslat            7
    Arabanin modelini goster    8
    Arabanin durumunu goster    9
""")

while True:

    islem = input("\nLutfen yapmak istediginiz islemi seciniz : ")

    if islem == "1":
        koltuk = tasit1.koltuk_sayisi
        tasit1.koltuksayisi()

    elif islem == "2":
        model = tasit1.modeli
        tasit1.model_goster()

    elif islem == "3":
        km = tasit1.km_durumu
        tasit1.kmdurumu()

    elif islem == "4":
        tasit1.tasit_miktari_guncelle()

    elif islem == "5":
        araba1.arabayi_durdur()

    elif islem == "6":
        araba1.gaza_bas()

    elif islem == "7":
        araba1.arabayi_yavaslat()

    elif islem == "8":
        araba1.model_goster()

    elif islem == "9":
        araba1.arabanin_durumunu_goster()
