# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 00:39:22 2019

@author: HP
"""

# 12. hafta odevi...
#Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari isimli
#bir bos liste tanimlayiniz. Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili gibi obje
# ozellikleri(instance attributes) olsun. Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin. 
#Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek niteligi tanimlayin ve degeri 4 olsun. 
#Ayrica bu objenin su methodlari olmalidir:

# 1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali  
# 2.modelini goster (tasitin modelini ekrana yazdirmali)
# 3. km_durumunu al (tasitin kilometre durumunu return etmeli) 
# 4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.

# - bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
# - class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.

class Tasit():
    tasitlar=[]
    __tasit_miktari=0
    def __init__(self,marka,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili):
        self.marka=marka
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.modeli=modeli
        self.satis_yili=satis_yili
        self.tekerlek_sayisi=4
        self.tasit_ekle()
        
    def koltuk_sayisi_goster(self):
        print(f'{self.modeli} aracin koltuk sayisi ; {self.koltuk_sayisi}')
    def tasit_modeli_goster(self):
        print(f'Bu aracin modeli; {self.modeli}')
    def km_durumunu_goster(self):
        print(f'{self.marka} arac {self.km_durumu} km dedir')
    def tasit_ekle(self):
        self.tasitlar.append(self.marka)
        return self.tasitlar
    @classmethod
    def tasit_miktari_sondurum(cls):
        cls.__tasit_miktari=len(cls.tasitlar)
        #cls.tasit_sayisi_son=cls.__tasit_miktari
        print('Tasit Sayisi ;',cls.__tasit_miktari)#tasit_sayisi_son)
# Orneklemler ;
auto1=Tasit('Toyota','110hp',6,135000,2010,2011)
auto2=Tasit('Honda','75hp',5,195000,2004,2004)
auto3=Tasit('Hundai','60hp',4,100000,2008,2007)
print(f'\n{auto1.marka} -----------')
print(f'{auto1.marka} aracin tekerlek sayisi ;',auto1.tekerlek_sayisi)
print(f'{auto1.modeli} model bu aracin markasi ;',auto1.marka)
print(f'{auto1.marka} aracin satis_yili ;',auto1.satis_yili)
print(f'{auto1.marka} aracin motor_gucu ;',auto1.motor_gucu)
auto1.tasit_modeli_goster()
auto1.koltuk_sayisi_goster()
auto1.km_durumunu_goster()

Tasit.tasit_miktari_sondurum()
print(Tasit.tasitlar)

# ===============================================================
# Ikinci Bolum Miras Alarak

# Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. 
#Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir ornek niteligi tanimlayiniz
# ve bu nitelik her orneklenme durumunda parametre olarak verilsin. Bu sinifta su methodlari tanimlayiniz;

# 1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
# 2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
# 3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
# 4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
# “Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
# miras alinmamistir.’ seklinde yazsin)
#Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve 
#‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.
    
class Araba(Tasit):
    def __init__(self,marka,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili,max_hiz):
        super().__init__(marka,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili)
        self.max_hiz=max_hiz
       
    def arabayi_durdur(self):
        print('Araba durdu.')
    def gaza_bas(self):
        print("Araba hizlaniyor...")
    def araba_yasalat(self):
        print("Araba yavasliyor...")
    @classmethod
    def arabanin_durumu(cls):
        if issubclass(Araba,Tasit):
            print("Araba sinifi Tasit sinifindan miras alinmisti")
        else:
            print(" Araba sinifi Tasit sinifindan miras alinmamistir.")
            
    def tasit_modeli_goster(self):
        super().tasit_modeli_goster()
        print("Araba sinifinin metodu... ve modeli;",self.modeli)
# Orneklemler
araba=Araba('Tesla','150hp',5,1000,2019,2019,200)
#print(araba.marka)
#print(araba.satis_yili)
#print(araba.max_hiz)
#araba.tasit_modeli_goster()
#Araba.tasit_miktari_sondurum()
#Araba.arabanin_durumu()
# ===============================================
print("""
Arac Kullanma
1. Arabanin durumu
2. Arabayi hizlandir
3. Aracin max hizi
4. Fren yap ve yavasla
5. Araci durdur
6. Arabanin modeli
7. Arabanin km durumu
8. Tasit Listesi
9. Sistemdeki tasit miktari
Çıkmak için 'q' ya basın.
""")
while True:
    islem = input("İşlemi Seçiniz:")
    if (islem == "q"):
       print("Program Sonlandırılıyor...")
       break
    elif (islem == "1"):
        araba.arabanin_durumu()
    elif (islem == "2"):
        araba.gaza_bas()
    elif (islem == "3"):
        print(araba.max_hiz)
    elif (islem == "4"):
        araba.araba_yasalat()
    elif (islem == "5"):
        araba.arabayi_durdur()
    elif (islem == "6"):
        araba.tasit_modeli_goster()
    elif (islem == "7"):
        araba.km_durumunu_goster()
    elif (islem == "8"):
        print(Araba.tasitlar)
    elif (islem == "9"):
        Araba.tasit_miktari_sondurum()
    





