#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:46:45 2019

@author: ensarbaltas
"""
class Tasit():
    tasit_miktari = []
    def __init__(self ,motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili,tekerlek_sayisi=4):
        self.motor_gucu      = motor_gucu 
        self.koltuk_sayisi   = koltuk_sayisi
        self.km_durumu       = km_durumu 
        self.modeli          = modeli
        self.satis_yili      = satis_yili
        self.tekerlek_sayisi = 4
    def koltuk_sayisini_goster(self):
        print('Bu aracta {} adet koltuk vardir.'.format(self.koltuk_sayisi))
    def modelini_goster(self):
        print('Bu arac {} modeldir.'.format(self.modeli))
    def kilometre_durumunu_al(self):
        print('Bu arac {} kilometrededir.'.format(self.km_durumu))
    @classmethod
    def __tasit_miktarini_guncelle(cls):
        cls.tm = len(cls.tasit_miktari)
        print('Bu arac {} tanedir.'.format(cls.tm))

class Araba(Tasit):
    
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili,tekerlek_sayisi=4):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili,tekerlek_sayisi=4)
        self.max_hiz = 240
        
    def araba_hareketi(self):
        kul = input("Arabayi durdurmak icin '1'e, hizlandirmak icin '2' ye, yavaslatmak icin '3'e basiniz ,Cikmak icin 'q': ")
        while True:    
            if kul == '1':
                print('Araba durdu')
            elif kul == '2':
                print('Araba hizlaniyor')
            elif kul == '3':
                print('Araba yavasliyor')
            else:
                break
#    def araba_durumu(self):     !! burada issubclass metodu kullanilacak
#        if Araba in Tasit:
#            print("Bu araba Tasit sinifindan alinmistir")
#        else:
#            print('Bu araba Tasit sinifindan alinmamistir')



Sahin = Tasit(1600,5,230000,1989,2003)
Kartal = Tasit(1800,5,190000,1980,2001)
Dogan = Tasit(2000,5,176000,1995,2008)
Brodway = Tasit(1400,4,225000,1994,2003)
Murat = Tasit(1200,4,320000,1978,1996)
print(Sahin.koltuk_sayisi)
Sahin.koltuk_sayisini_goster()
print(Sahin.tekerlek_sayisi)
print(Dogan.tekerlek_sayisi)
print(Murat.modeli)
Murat.modelini_goster()
print(Brodway.km_durumu)
Brodway.kilometre_durumunu_al()
#Tasit.tasit_miktarini_guncelle()  burada def fonksiyonuna __str__ uygularsan 
#direk goruntu alirsin. print(Sahin) >> sahinin bilgileri basilir
#print(Tasit.tasit_miktari)  bos bir liste veriyor [] neden?
print(dir(Araba))
Ford = Araba(2000,5,120000,2010,2015,180)
Kia = Araba(2400,7,85000,2013,2017,230)
print(Ford.koltuk_sayisi)
Ford.koltuk_sayisini_goster()
print(Kia.tekerlek_sayisi)
print(Kia.modeli)
Kia.modelini_goster() 
print(Ford.max_hiz)
print(Kia.max_hiz)   
Araba.araba_hareketi(Sahin)
Araba.araba_hareketi(Kartal)
#Tasit.araba_durumu(Kia)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
