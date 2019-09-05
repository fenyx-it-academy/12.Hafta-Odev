##12.Hafta-Odev
##Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi 
##(class method) olarak tasit_miktari isimli bir bos liste tanimlayiniz. 
##Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili gibi 
##obje ozellikleri(instance attributes) olsun. Ve her orneklenme durumunda bu ozellikler 
##parametre olarak verilsin. Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli 
##bir ornek niteligi tanimlayin ve degeri 4 olsun. Ayrica bu objenin su methodlari olmalidir:
##
##1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali  
##2.modelini goster (tasitin modelini ekrana yazdirmali)
##3. km_durumunu al (tasitin kilometre durumunu return etmeli) 
##4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.
##
##- bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde 
##gizleyiniz.
##- class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.
##Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. 
##Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir ornek 
##niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin. 
##Bu sinifta su methodlari tanimlayiniz;
##
##1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
##2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
##3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
##4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi 
##ise 
##“Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit 
##sinifindan 
##miras alinmamistir.’ seklinde yazsin)
##Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve 
##‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.

class Tasit():
    __tasit_miktari=[]                  #***mudahale yapilmamasi icin gizlenmistir
    tekerlek_sayisi=4
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.motor_gucu=motor_gucu          #***bilgileri eklyebilecek sekilde self. olarak secenekler eklendi
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.modeli=modeli
        self.satis_yili=satis_yili
        Tasit.__tasit_miktari.append(self)
    def koltuk_sayisi_goster(self):
        print("Koltuk sayisi: ",self.koltuk_sayisi)
    def modelini_goster(self):
        print("Tasitin modeli: ",self.modeli)
    def km_durumunu_goster(self):
        self.km_durumu
        print("Tasitin km'si: ",self.km_durumu)
    def tasit_miktarini_guncelle(self):
        self.__tasit_miktari+=1
        print(len(self.__tasit_miktari))
    @classmethod                        #***cls metoduyla gosterildi
    def tasit_miktari(cls):
        return len(cls.__tasit_miktari)
araba=Tasit(2.0,4,120000,"HB",2008)     
print("Araba budur!!! :)",araba.modeli)

class Araba(Tasit):                 #***Araba sinifi Taist sinifindan miras alinarak olusturulup eklemeler yapildi
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
        if "i" in self.__dir__():
            return print('Bu sinif Tasit sinifindan miras alinarak yapilmistir...')
        else:
            return print('Araba sinifi Tasit sinifindan miras alinmamistir...')

    def modelini_goster(self): 
        print("Araba sinifinin methodu….")
        super().modelini_goster()


Toyota=Araba( 2.0, 4, 120000, "Corolla", 2007, 240)
print("Toyota bu!!!...","Toyota",Toyota.gaza_bas())
Ford=Araba(2.4,4,60000,"Mustang",2008,350)
print("Efsane geliyor...","Ford",Ford.arabanin_durumu())
Honda=Araba(1.4,4,50000,2012,"Jazz",200)
print("Japon mu o?","Honda",Honda.modeli)

#********Burdan asagisi menu ile yapilmak istenen secenekler soruluyor.
#********Fakat bazi secenekler hata veriyor guncelleyip tekrar yuklenecek...

##print("""
##            ARAC BILGI SISTEMI
##            1- Arac Eklemek
##            2- Arac Bilgisi Sorgulamak
##                1-Motor Gucu
##                2-Koltuk Sayisi
##                3-Km Durumu
##                4-Modeli
##                5-Satis Yili
##                6-Max Hiz
##            3- Arac Miktari
##            4- Arac Testi
##                1-Hizlandir
##                2-Yavaslat
##                3-Durdur
##                4-Aracin durumu
##                
##            5-Programdan Cikmak
##            
##            """)
##
##while True:
##    islem=int(input("Seciminizi yapiniz: "))
##    if 4<islem<1:
##        print("Lutfen gecrli bir islem giriniz...")
##        continue
##    if islem==5:
##        print("Cikiliyor")
##        break
##    if islem==1:
##        print("Eklemek istediginiz arac bilgilerini giriniz...")
##        motor_gucu=input("Motor gucunu giriniz: ")
##        koltuk_sayisi=input("Koltuk sayisini giriniz: ")
##        km_durumu=input("Km durumunu giriniz: ")
##        modeli=input("Modeli giriniz: ")
##        satis_yili=input("Satis yilini giriniz: ")
##        max_hiz=input("Maksimum hiz: ")
##        Toyota=Araba(motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili,max_hiz)
##    elif islem==2:
##        print("""
##        Bilgilerini goremek istediginiz
##        Araci Seciniz:
##        1- Toyota
##        2- Ford
##        3- Honda
##
##        4- Cikis
##
##""")
##        sec=int(input("Araci seciniz: "))
##        if sec==1:
##            sec=Toyota
##            islem2=int(input("Bu arac ile ilgili yapmak istediginiz islemi seciniz: "))
##            if islem2==1:
##                sec.motor_gucu()
##            elif islem2==2:
##                sec.koltuk_sayisi()
##            elif islem2==3:
##                sec.km_durumunu_goster()
##            elif islem2==4:
##                sec.modelini_goster()
##            elif islem2==5:
##                sec.satis_yili()
##            elif islem2==6:
##                sec.max_hiz()
##        elif sec==2:
##            sec=Ford
##            islem2=int(input("Bu arac ile ilgili yapmak istediginiz islemi seciniz: "))
##            if islem2==1:
##                sec.motor_gucu()
##            elif islem2==2:
##                sec.koltuk_sayisi()
##            elif islem2==3:
##                sec.km_durumunu_goster()
##            elif islem2==4:
##                sec.modelini_goster()
##            elif islem2==5:
##                sec.satis_yili()
##            elif islem2==6:
##                sec.max_hiz()
##        elif sec==3:
##            sec=Honda
##            islem2=int(input("Bu arac ile ilgili yapmak istediginiz islemi seciniz: "))
##            if islem2==1:
##                sec.motor_gucu()
##            elif islem2==2:
##                sec.koltuk_sayisi()
##            elif islem2==3:
##                sec.km_durumunu_goster()
##            elif islem2==4:
##                sec.modelini_goster()
##            elif islem2==5:
##                sec.satis_yili()
##            elif islem2==6:
##                sec.max_hiz()
##        else:
##            print("Yanlis secim yaptiniz. Tekrar deneyin...")
##            continue
##    elif islem==3:
##        Tasit.tasit_miktari()
##    elif islem==4:
##        
##        print("""
##        Test etmek istediginiz
##        Arac Listesi:
##        
##        1- Toyota
##        2- Ford
##        3- Honda
##
##        4- Cikis
##
##""")
##        sec2=input("Test etmmek istediginiz araci seciniz: ")
##        sec2=Araba(motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili,max_hiz)
##        islem3=int(input("Bu arac ile ilgili test etmek istediginiz islemi seciniz: "))
##        if islem3==1:
##            sec2.gaza_bas()
##        elif islem3==2:
##            sec2.arabayi_yavaslat()
##        elif islem3==3:
##            sec2.arabayi_durdur()
##        elif islem3==4:
##            sec2.arabanin_durumu()
##        else:
##            print("Yanlis secim yaptiniz. Tekrar deneyin...")
##            continue
##    else:
##        print("Hatali giris yaptiniz. Tekrar deneyin...")
##        continue
