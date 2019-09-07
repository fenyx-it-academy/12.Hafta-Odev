class Tasit():

    tasit_sayisi = 0

    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, tekerlek_sayisi = 4):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = tekerlek_sayisi

    @classmethod
    def tasit_miktari(cls):
        cls.tasit_sayisi += 1
        print("Mevcut arac sayisi : ", cls.tasit_sayisi)

    def koltuksayisi(self):
        print("Aracin koltuk sayisi : ", tasit1.koltuk_sayisi)

    def model_goster(self):
        print("Aracin modeli : ", tasit1.modeli)

    def kmdurumu(self):
        print("Aracin km'si : ", tasit1.km_durumu)


tasit1 = Tasit(1600, 6, 76825, 2016, 2018)


print("""Lutfen yapmak istediginiz islemi seciniz\n
    Koltuk sayisini gorme       1
    Tasitin modelini gorme      2
    Tasitin km'sini gorme       3
    Tasit miktarini guncelle    4
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
        miktar = tasit1.tasit_sayisi
        tasit1.tasit_miktari()
