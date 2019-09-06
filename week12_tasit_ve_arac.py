# Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi
# (class method)olarak tasit_miktari isimli bir bos liste tanimlayiniz.
# Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli,
# satis_yili gibi obje ozellikleri(instance attributes) olsun.
# Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin.
# Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek niteligi
# tanimlayin ve degeri 4 olsun.
# Ayrica bu objenin su methodlari olmalidir:
# 1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
# 2.modelini goster (tasitink modelini ekrana yazdirmali)
# 3. km_durumunu al (tasitin kilometre durumunu return etmeli)
# 4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.
#
# - bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
# - class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.#
# Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. 
#Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir
# ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin.
# Bu sinifta su methodlari tanimlayiniz;
#
# 1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
# 2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
# 3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
# 4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise
# “Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan
# miras alinmamistir.’ seklinde yazsin)

## ****TAŞIT MİKTARI OLAYINI YAPAMADIM****###

import time

class Tasit():
    __tasitMiktari: []
    
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi=4  
        
        
        #Tasit.__tasitMiktari.append(self)
        
        
        
    def motor_gucuShow(self):
        print(self.modeli, "modelinin motor gücü\t--»", self.motor_gucu,"cc")

    def koltuk_sayisiShow(self):
        print(self.modeli, "modelinin koltuk sayısı\t--»", self.koltuk_sayisi)

    def modeliShow(self):
        print("------------------»TAŞIT«------------------")
        print('Mevcut model\t\t\t--»', self.modeli)

    def km_durumuShow(self):
        print(self.modeli, "modelinin km'si\t\t--»", self.km_durumu)

    def satis_yiliShow(self):
        print(self.modeli, "modelinin satış yılı\t--»", self.satis_yili)
    def tekerlek_sayisiShow(self):
        print(self.modeli, "modelinin tekerlek sayısı--»", self.tekerlek_sayisi)
        print("-------------------------------------------\n")
        time.sleep(2)
    @classmethod
    def tasit_miktariShow(cls):
        return len(cls.__tasitMiktari)

moongo=Tasit (1800,7, 98000,"Moongo",2015) 
moongo.modeliShow()
moongo.motor_gucuShow()
moongo.koltuk_sayisiShow()
moongo.km_durumuShow()
moongo.satis_yiliShow()
moongo.tekerlek_sayisiShow()

























############################################################################################3

class Araba(Tasit):
    tekerlek_sayisi=4
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili, max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz=max_hiz
        self.hiz = 70
        self.tekerlek_sayisi=4
    
    def arabayi_durdur(self):
        print("Araba durduruluyor")
        time.sleep(1)
        print("Araba durduu!!")
        time.sleep(1)
    
    def gaza_bas (self):
        if self.hiz >= 100 :
            print("!--Daha hızlı gitmeniz uygun değil--!!")
            time.sleep(1)
            pass
        else:
            print("Gaza basılıyor!!")
            time.sleep(1)
            self.hiz += 15
            if self.hiz >= 55 :
                print("Hız {}km/h, lütfen dikkat ediniz!!".format(self.hiz))
            else:
                 print("Hız {}km/h".format(self.hiz))
            time.sleep(1)
       
    def arabayi_yavaslat (self):
        if self.hiz <= 10 : 
            print("Hız rölantide!!! Budan sonrası aracı durdurmanız gerekiyor!")
            time.sleep(1)
            pass
        else:    
            print("Araç yavaşlatıyor..!")
            time.sleep(1)
            self.hiz -= 10
            if self.hiz <= 55:
                print("{}km/h ile seyir halindesiniz!!".format(self.hiz))
            else:
                print("Hız {}km/h, lütfen dikkat ediniz!!".format(self.hiz))
            time.sleep(1)
            
    def arabanin_durumuShow(self):
        if issubclass(Araba, (list, Tasit)):
              print("Sorgulanan sınıf 'Taşıt' sınıfından mirastır!!")
              time.sleep(1)
        else:
            print("Sorgulana sınıf 'Taşıt' sınıfından miras DEĞİLDİR!!!") 
            time.sleep(1)

    

    def araba_infoShow(self):
        print(f"""\n
-----------» Araba «----------- 
-Model              : {self.modeli}  -
-Motor gücü         : {self.motor_gucu} cc -
-Koltuk sayısı      : {self.koltuk_sayisi}       -
-Km'si              : {self.km_durumu}  -
-Satış yılı         : {self.satis_yili}    -
-Maksimum hızı      : {self.max_hiz} km/h- 
-Tekerlek sayısı    : {self.tekerlek_sayisi}       -    
-------------------------------\n
 """)
        time.sleep(1)        
        
        
sungoo=Araba(1400, 5, 156000, "Sungoo", 2012,225)


while True:
   
    sel = input("_Lütfen seçim yapınız_\n"
                "*1--» Arabayı hızlandırın\n"
                "*2--» Arabayı yavaşlatın\n"
                "*3--» Arabayı durdurun\n"
                "*4--» Araba durumuna bakın\n"
                "*5--» Araba infosuna bakın\n"
                "*Diğerleri ile çıkış yapın*\n")
    if sel == '1':
        sungoo.gaza_bas()
    
    elif sel == '2':
        sungoo.arabayi_yavaslat()
    
    elif sel == '3':
        sungoo.arabayi_durdur()
    
    elif sel =='4':
        sungoo.arabanin_durumuShow()
    
    elif sel =='5':
        sungoo.araba_infoShow()
    
    else:
        print('Program sonlandırılıyor!!')
        time.sleep(1)
        print("Goodbye!!")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
