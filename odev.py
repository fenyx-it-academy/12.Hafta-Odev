class Tasit:
    __tasit_miktari = []
    def __init__(self, motor_gucu, koltuk_sayisi, model, km_durumu, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.model = model
        self.km_durumu = km_durumu
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4
        self.tasit_sayisi = 0
        self.tasit_miktarini_guncelle()

    def koltuk_sayisi_goster(self):
        print(f"\nBu Aracin Koltuk sayisi {self.koltuk_sayisi} dir.\n")

    def model_goster(self):
        print(f"\nBu aracin modeli {self.model} dir.\n")

    def km_durumunu_al(self):
        return self.km_durumu

    def tasit_miktarini_guncelle(self):
        self.__tasit_miktari +=[1]


    @classmethod
    def tasit_miktari(cls):
        print(f"\nToplam tasit miktari {sum(cls.__tasit_miktari)} dir.")






class Araba(Tasit):

    def __init__(self, motor_gucu, koltuk_sayisi, model, km_durumu, satis_yili, max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, model, km_durumu, satis_yili)
        self.max_hiz = max_hiz
    def arabayi_durdur(self):
        print("\n Araba Durdu.........\n")

    def gaza_bas(self):
        print("\nAraba hizlaniyor.....\n")

    def arabayi_yavaslat(self):
        print("\n Araba yavsliyor....\n")

    def arabanin_durumunu_goster(self):
        if 'koltuk_sayisi_goster' in self.__dir__():
            print("Araba sinifi Tasit sinifindan miras alinmistir.")
        else :
            print("Araba sinifi Tasit sinifindan miras alinmamistir.")

    def model_goster(self):
        print(f"\nBu Araba Sinifina ait modeldir.\n")



