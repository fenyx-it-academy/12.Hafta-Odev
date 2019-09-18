from time import sleep
class Tasit:
#classimizi attributes icin basina iki tane '_' koymamiz gerektigini ogrendik
#e bunu uyguladik
    __tasit_sayisi=[]
    def __init__(self,motor_gucu,koltuk_sayisi,km_durumu,model,satis_yili):
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.model=model
        self.satis_yili=satis_yili
        self.teker_sayisi=4
        Tasit.__tasit_sayisi.append(self)
#instance attributes olusturduk ve bilgilerin girilmesini istedik
#burada tasit sayisini herdefasinda listeye ekledik
    def goruntule_koltuk(self):
        print('Arac koltuk sayisi:',self.koltuk_sayisi)
    def goruntule_model(self):
        print('Araba modeli:',self.model)
    def goruntule_km(self):
        print('Arac km durumu:',self.km_durumu)
    def goruntule_motorgucu(self):
        print(f'Aracin motor gucu {self.motor_gucu} tork\'dur')
    def goruntule_satisyili(self):
        print('Arac satis yili :',self.satis_yili)
#yukasrida methot lar ile kullaniciya istedigi bilgileri goruntuledik
#classmethod ile classda kac tane kayit oldugunu gosterdik
    def tasit_guncelle(self):
        return print('Guncel listenizde {} arac bulunmaktadir. '.format(len(self.__tasit_sayisi)))
    @classmethod
    def goruntule_tasitsayisi(cls):
        print('Kayitli tasit sayisi',len(cls.__tasit_sayisi))
class Araba(Tasit):
    def  __init__(self,motor_gucu,koltuk_sayisi,km_durumu,model,satis_yili,max_hiz):
       super().__init__(motor_gucu,koltuk_sayisi,km_durumu,model,satis_yili)
       self.max_hiz=max_hiz
    def araba_dursun(self):
        print('Araba durduruluyor...')
    def araba_hizlansin(self):
        print('Araba hizi artiriliyor...')
    def araba_yavaslat(self):
        print('Araba hizi dusuruldu...')

    def goruntule_model(self):
        print('Araba sinifinin methodu…')
        sleep(1)
        super().goruntule_model()
    def goruntule_araba_durumu(self):
#subclass ile araba classinin tasit classindan miras alip almadigi sorguladik
        if issubclass(Araba,Tasit):
            print('Bu sinif Tasit sinifindan miras alinmistir.')
        else:
            print('Araba sinifi Tasit sinifindan miras alinmamistir!')
woswos=Tasit(185,4,235000,1993,2019)
woswos.goruntule_km()
woswos.goruntule_koltuk()
woswos.goruntule_model()
woswos.goruntule_motorgucu()
woswos.goruntule_satisyili()
woswos.goruntule_tasitsayisi()
hacimurat=Araba(185,5,50000,1976,2010,101)
hacimurat.goruntule_satisyili()
hacimurat.goruntule_motorgucu()
hacimurat.goruntule_model()
hacimurat.goruntule_koltuk()
hacimurat.goruntule_km()
hacimurat.goruntule_tasitsayisi()
hacimurat.goruntule_araba_durumu()
hacimurat.araba_dursun()
hacimurat.araba_hizlansin()
hacimurat.araba_yavaslat()
woswos.tasit_guncelle()
