from time import sleep
class Tasit():
    __tasit_miktari=[]
    def __init__(self,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili):
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.modeli=modeli
        self.satis_yili=satis_yili
        self.tekerlek_sayisi=4
        self.tasit_miktarini_guncelle()
    def ozellikleri_goster(self):
        print("""
        Tasit sinifinin Ozellikleri:
        1) Motor Gucu       :{}
        2) Koltuk sayisi    :{}
        3) KM durumu        :{}
        4) Modeli           :{}
        5) Satis Yili       :{}
        6) Teker Sayisi     :{}""".format(self.motor_gucu,self.koltuk_sayisi,self.km_durumu,self.modeli,self.satis_yili,self.tekerlek_sayisi))
    def koltuk_sayisi(self):
        print("Aracin koltuk sayisi",self.koltuk_sayisi)
    def modelini_goster(self):
        print("Aracin modeli:",self.modeli)
    def km_durumunu_al(self):
        print(self.km_durumu)
    @classmethod
    def tasit_miktarini_guncelle(cls):
        Tasit.__tasit_miktari.append(1)
        print(len(cls.__tasit_miktari))

class Araba(Tasit):

    def __init__(self,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili,max_hiz,hiz = 0):
        super().__init__(motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili)
        self.max_hiz=max_hiz
        self.hiz = hiz
    def arabayi_durdur(self):
        sleep(1)
        if self.hiz != 0:
            print("Araba durduruluyor...")
            sleep(1)
            self.hiz=0
            print("Araba Durdu...")
        else:
            print("Araba zaten duruyor...")
    def gaza_bas(self):
        if self.hiz<self.max_hiz:
            print("Hiziniz...",self.hiz)
            print("Hizlaniliyor...")
            sleep(1)
            self.hiz+=10
            print("Hiziniz:",self.hiz)
        else:
            print("maximum hiza ulastiniz...",self.max_hiz)
    def arabayi_yavaslat(self):
        if self.hiz > 0:
            print("Yavaslaiyoruz..")
            sleep(1)
            self.hiz-=10
            print("Hiziniz:",self.hiz)
        elif self.hiz==0:
            print("Arac Durdu...")
        else:
            print("Hareket halinde degiliz...",self.hiz)
    def modelini_goster(self):
        print("Araba sinifinin modeli:",self.modeli)
    def arabanin_durumunu_goster(self):
        if issubclass(Araba,Tasit):
            print("Bu sinif Tasit sinifindan miras alinmistir.")
        else:
            print('Araba sinifi Tasit sinifindan miras alinmamistir.')


arabaaa=Araba(120,5,171000,2000,2000,190)
arabaaa.arabanin_durumunu_goster()
print("Araba sinifina ait arabanin modeli",arabaaa.modeli)
araba1=Tasit(120,5,171000,2011,2012)
print("Tasit sinifina ait arabanin modeli",araba1.modeli)
#print(araba1._Tasit__tasit_miktari) Gizli ogeye ulasmak icin



while True:
    print("""
    TASIT-ARABA Sinifina Hosgeldiniz
    1) Tasit sinifinin ozellikleri icin 1'e.
    2) Araba sinifinin ozellikleri icin 2'ye,
    3) Tasit olusturmak icin 3'e,
    4) Araba olusturmak icin 4'e,
    5) Araci Test etmek icin 5'e,
    6) Cikmak icin 6'ya basiniz...""")
    giris=input("Seciminiz:")
    if not giris:
        print("Lutfen giris yapiniz.")
        continue
    elif not giris.isnumeric():
        print("Lutfen giris yapiniz.")
        continue
    if giris=="1":
        araba1.ozellikleri_goster()
    elif giris=="2":
        arabaaa.arabanin_durumunu_goster()
    elif giris=="3":
        tasit_adi=(input("Tasit adi giriniz:"))
        tasit_adi=Tasit(input("motor_gucu:"),input("koltuk_sayisi:"),input("km_durumu:"),input("modeli:"),input("satis_yili:"))
        print("Tasit sinifina ait {} objesi basariyla olusturuldu.".format(tasit_adi))
        Tasit.tasit_miktarini_guncelle()
    elif giris=="4":
        arac_adi=(input("Araba adi giriniz:"))
        arac_adi=Araba(input("motor_gucu:"),input("koltuk_sayisi:"),input("km_durumu:"),input("modeli:"),input("max_hiz:"),input("satis_yili:"),input("arabanin_modeli:"))
        print("Araba sinifina ait {} objesi basariyla olusturuldu.".format(arac_adi))
        Araba.tasit_miktarini_guncelle(arac_adi)
    elif giris == "5":
        print("Arac Test icin hazir lutfen kemerinizi taktiktan sonra gaza basiniz.")
        while True:
            gaz=input("Gaza basmak icin (+),\ndurmak icin (-) basiniz.")
            if gaz=="+":
                arabaaa.gaza_bas()
                continue
            elif gaz=="-":
                arabaaa.arabayi_yavaslat()
                arabaaa.arabayi_durdur()
                continue
            else:
                print("Hatali giris yaptiniz...")
    elif giris=="6":
        print("Programdan cikiliyor...")
        quit()
    else:
        print("Yanlis giris yaptiniz. Lutfen kontrol ediniz...")
        continue
