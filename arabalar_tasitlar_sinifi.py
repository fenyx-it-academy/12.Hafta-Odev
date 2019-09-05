print("Tasit ve Arac isimli classlarla class ozellikleri calismalari")
class Tasit():
    tasitlar=[]
    tasit_miktari=0
    def __init__(self,arac_adi='', modeli='',motor_gucu='',koltuk_sayisi='',km_durumu='0',satis_yili=''):
        self.arac_adi=arac_adi
        self.modeli=modeli
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.satis_yili=satis_yili
        self.tekerlek_sayisi=4

    def __str__(self):
        return "{}".format(self.arac_adi)

    def koltuk_sayisi(self):
        print(f"{self} aracinin kotuk sayisi :    {self.koltuk_sayisi}")

    def model(self):
        print(f"{self} aracinin modeli :    {self.modeli}")
    @property
    def kmdurumu(self):
        return self.km_durumu

    @classmethod
    def tasit_ekle(cls):
        a = input("Tasitin adi(cikis icin (q):    ")
        b = input("Tasitin modeli:    ")
        c = input("Tasitin motor gucu:    ")
        d = input("Tasitin kotuk sayisi:     ")
        e = input("Tasitin km durumu:     ")
        f = input("Tasitin satis yili:    ")

        yeni_tasit = Tasit(a, b, c, d, e, f)
        if yeni_tasit not in Tasit.tasitlar:
            Tasit.tasitlar.append(yeni_tasit)
            Tasit.tasit_miktari += 1
            print("yeni tasit eklendi.")
        else:
            print("bu arac tasitlar class inda mevcut")

    @classmethod
    def __tasit_miktari(cls):
        if __name__ == "__main__":
            g = Tasit()
            print(f'Tasit miktari : {g.tasit_miktari}')
        else:
            print("bu sayfada tasit sayisini ogrenme izniniz yok")


    def tasit_islemleri(self):
        print("Tasit sinifindan bir arac sorguluyorsunuz \n")
        while True:
            print("""
                1       Tasit ekle
                2       koltuk sayisi
                3       model
                4       km durumu
                5       tasit miktari
                q       cikis""")
            print()
            islem = input(" yapmak istediginiz islem numarasini giriniz:")
            if islem == "q":
                break
            elif islem == "1":
                Tasit.tasit_ekle()
            elif islem == "2":
                Tasit.koltuk_sayisi(self)
            elif islem == "3":
                Tasit.model(self)
            elif islem == "4":
                print(self.kmdurumu)
            elif islem == "5":
                self.__tasit_miktari()




class Araba(Tasit):
    arabalar = []

    def __init__(self, arac_adi, modeli, motor_gucu, koltuk_sayisi, km_durumu, satis_yili, max_hiz=''):
        Tasit.__init__(self, arac_adi, modeli, motor_gucu, koltuk_sayisi, km_durumu, satis_yili)
        self.max_hiz = max_hiz

    @classmethod
    def araba_ekle(cls):
        a = input("Arabanin adi(cikis icin (q):    ")
        b = input("Arabanin modeli:    ")
        c = input("Arabanin motor gucu:    ")
        d = input("Arabanin kotuk sayisi:     ")
        e = input("Arabanin km durumu:     ")
        f = input("Arabanin satis yili:    ")
        g = input("Arabanin max hizi:")
        yeni_araba = Araba(a, b, c, d, e, f, g)
        if yeni_araba not in Araba.arabalar:
            Araba.arabalar.append(yeni_araba)
        else:
            print("bu arac araba class inda zaten mevcut")


    def arabayi_durdur(self):
        print("araba durdu")

    def gaza_bas(self):
        print("araba hizlaniyor")
    def arabayi_yavaslat(self):
        print("Araba yavasliyor")
    def arabanin_durumu(self):
        print("Bu sinif Tasit sinifindan miras alinmistir" if issubclass(Araba,Tasit)==True
              else "Araba sinifi Tasit sinifindan miras alinmamistir." )

    def model(self):
        Tasit.model(self)
        print("Araba sinifinin methodudur...")

    @staticmethod
    def araclari_goster():
        print('----Tasitlar-----\n')
        for i in Tasit.tasitlar:
            print(i)
        print("----Arabalar----\n")
        for i in Araba.arabalar:
            print(i)

    def araba_islemleri(self):
        print("Araba sinifindan bir arac sorguluyorsunuz \n")
        while True:
            print("""
                        1       Araba ekle
                        2       koltuk sayisi
                        3       arabanin modeli
                        4       km durumu
                        5       arabayi durdur
                        6       gaza bas
                        7       arabayi yavaslat
                        8       arabanin durumu
                        q       cikis""")
            print()
            islem = input(" yapmak istediginiz islem numarasini giriniz:")
            if islem == "q":
                break
            elif islem == "1":
                Araba.araba_ekle()
            elif islem == "2":
                Araba.koltuk_sayisi(self)
            elif islem == "3":
                Tasit.model(self)
            elif islem == "4":
                print(self.kmdurumu)
            elif islem == "5":
                Araba.arabayi_durdur(self)
            elif islem == "6":
                Araba.gaza_bas(self)
            elif islem == "7":
                Araba.arabayi_yavaslat(self)
            elif islem == "8":
                Araba.arabanin_durumu(self)
tasit1=Tasit('tasit1','model1','motorg1','koltuk1','km1','yil1')
Tasit.tasitlar.append(tasit1)
araba1=Araba("araba1","model11",'guc11','koltuk11','km11','yil11','hi11')
Araba.arabalar.append(araba1)
tasitisimlerilist = ["tasit1"]
arabaisimlerlist=["araba1"]
while True:
    print("Kayitli olan Tasit ve Arabalar \n")
    Araba.araclari_goster()

    for i in Tasit.tasitlar:
        tasitisimlerilist.append(i.arac_adi)


    for i in Araba.arabalar:
        arabaisimlerlist.append(i.arac_adi)


    if Araba.arabalar == [] and Tasit.tasitlar == []:
        islem = input("""
        1       tasit ekle
        2       araba ekle
        q       cikis
        :""")
        if islem == "1":
            Tasit.tasit_ekle()
        elif islem =="2":
            Araba.araba_ekle()
        elif islem == "q":
            break
        else:
            print("gecersiz islem adi")
    else:
        arac = input("islem yapmak istediginz aracin ismini giriniz(cikis icin q):")

        if arac in tasitisimlerilist:
            print("tasitlardan bir isim sectiniz")
            indeks = tasitisimlerilist.index(arac)
            Tasit.tasit_islemleri(Tasit.tasitlar[indeks])

        elif arac in arabaisimlerlist:
            print("Arabalardan bir isim sectiniz")
            indeks = arabaisimlerlist.index(arac)
            Araba.araba_islemleri(Araba.arabalar[indeks])
        elif arac == "q":
            break

        else:
            print("kayitli olmayan bir arac adi girdiniz.")



