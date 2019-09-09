print('b.')
'''
12.Hafta-Odev
Tasit isimli bir sinif tanimlayiniz. 
Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari isimli bir bos liste tanimlayiniz. 
Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, 
satis_yili gibi obje ozellikleri(instance attributes) olsun. 
Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin. 
Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek niteligi tanimlayin ve degeri 4 olsun. 

Ayrica bu objenin su methodlari olmalidir:
1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali  
2.modelini goster (tasitin modelini ekrana yazdirmali)
3. km_durumunu al (tasitin kilometre durumunu return etmeli) 
4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.
- bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
- class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.

Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. 
Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir ornek niteligi tanimlayiniz 
ve bu nitelik her orneklenme durumunda parametre olarak verilsin. Bu sinifta su methodlari tanimlayiniz;

1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
“Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
miras alinmamistir.’ seklinde yazsin)
Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve
‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.
'''
import time
class Tasit:
    __tasit_sayisi = 0      #tasit sayisini baslangicta sifir olarak belirledik...# __ ile tasit sayisini gizledik
    tasitlar=[]             # tasit markalarini listede topladik

    def __init__(self,marka,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili):
        self.marka=marka
        self.motor_gucu=motor_gucu
        self.koltuk_sayisi=koltuk_sayisi
        self.km_durumu=km_durumu
        self.modeli=modeli
        self.satis_yili=satis_yili
        self.tekerlek_sayisi = 4            # her ornekte degismeyecek sekilde tekerlek sayisini 4 olarak belirledik
        self.tasit_durumunu_guncelle()
        Tasit.tasitlar.append(marka)

    def koltuk_sayisini_goster(self):
        print(f'tasitimizin koltuk sayisi : {self.koltuk_sayisi}')

    def model_goster(self):
        print(f'modeli : {self.modeli}')

    def km_durumunu_goster(self):
        return f'tasitin km durumu : {self.km_durumu}'

    def tasit_durumunu_guncelle(self):
        Tasit.__tasit_sayisi += 1           # her orneklemde tasit sayisi 1 artacak

    @classmethod                            # classmethod tanimladik
    def tasit_sayisini_goster(cls):         # tasit miktarini gosteren bir cls method tanimladik
        print(f'tasit miktari :{cls.__tasit_sayisi}')


class Araba(Tasit):                                 # child class

    def __init__(self,marka,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili,max_hiz):
        super().__init__(marka,motor_gucu,koltuk_sayisi,km_durumu,modeli,satis_yili)
        self.max_hiz=max_hiz
        self.araba_hizi=0                           #baslangicta araba hizini sifir aldik

    def araba_stop(self):
        self.araba_hizi=0
        if self.araba_hizi==0:
            print('araba durdu')

    def gaza_bas(self):
        self.araba_hizi += 10                        # gaza bas her calistiginda hizi +10 arttirdik
        if self.araba_hizi==0:
            Araba.araba_stop(self)
        elif self.araba_hizi < self.max_hiz:
            print(f'araba hizlaniyor........hiziniz : {self.araba_hizi}')
        elif self.araba_hizi == self.max_hiz:
            print('max hiza ulastinizzzz')

    def arabayi_yavaslat(self):
        self.araba_hizi -= 10
        if self.araba_hizi < 0:
            self.araba_hizi=0                        # hizin negatif degere dusmemesi icin hizini 0 a esitledik
            Araba.araba_stop(self)                   # hiz sifir olunca araba_stop metodunu cagirdik
            print('araba duruyor...gaza basmayi dene')
        elif self.araba_hizi == 0:
            Araba.araba_stop(self)
        elif self.araba_hizi < self.max_hiz:
            print(f'araba yavasliyorrrr........hiziniz : {self.araba_hizi}')

    def model_goster(self):                          # modeli goster metodunu overding yaptik
        print('Araba sinifinin methodu….')
        super().model_goster()

    def durum(self):                                 # issubclass ile inheritance durumunu sorguladik
        if issubclass(self.marka, Tasit):            
            print('Bu sinif Tasit sinifindan miras alinmistir')
        else:
            print('Araba sinifi Tasit sinifindan miras alinmamistir.')

bmv=Araba('bmv', 2000, 2, 1000, 2015, 2017, 300)
audi=Araba('audi',3000,4,2000,2016,2018,250)
mercedes=Araba('mercedes',3800,5,5000,2018,2019,350)

araba = input("""\nHangi arabanin ozelliklerini gormek ve test etmek istersiniz?
        1-Audi
        2-Mercedes
        3-BMW
Seciminizi yapiniz....:""")
if araba == '1':
    araba = audi
elif araba == '2':
    araba = mercedes
elif araba == '3':
    araba = bmv

menu='''
*************************************************************
*            1-markasini goster                             *
*            2-modelini_goster                              *
*            3-koltuk_sayisini_goster                       *
*            4-km_durumunu_goster                           *
*            5-max hizini goster                            *
*            6-arabayi test et...( hiz testi )              *
*-----------------------------------------------------------*
*            7-arabanin inheritance durumunu goster         *
*            8-overriding............                       *
*            9-sisteme kayitli tasit miktarini goster       *
*            10-sisteme kayitli arabalari goster            *           
*            11-Yeni Arac Kayit                             *
*            .......cikis icin bir tusa basiniz             *
*************************************************************    '''
araba_test_et = '''
-----------.........HIZ TESTI........--------------------
-                1-arabayi durdur                       -
-                2-gaza bas                             -
-                3-frene bas                            -
-          cikis icin bir tusa basiniz                  -
---------------------------------------------------------  '''
while True:
    print(menu)
    cvp=input('Lutfen secim yapiniz...:')
    if cvp=='1':
        print(f'markasi :{araba.marka}')
    elif cvp == '2':
        print(f'{araba.marka} modeli..:{araba.modeli}')
    elif cvp == '3':
        araba.koltuk_sayisini_goster()
    elif cvp == '4':
        print(f'{araba.marka} km durumu..:{araba.km_durumu} km')
    elif cvp == '5':
        print(f'{araba.marka} max hizi :{araba.max_hiz}')
    elif cvp == '6':                    # araba hiz testi yaptik
        anahtar = 1                     # araba hiz testini while dongusu ile yaptik
        while anahtar == 1:
            print(araba_test_et)
            hiz_secim=input('SECIM YAPINIZ.....:')
            if hiz_secim=='1':
                araba.araba_stop()
            elif hiz_secim == '2':
                araba.gaza_bas()
            elif hiz_secim == '3':
                araba.arabayi_yavaslat()
            else:
                print('cikiliyorrrr...')
                time.sleep(3)
                anahtar=0
    elif cvp == '7':
        araba.durum()
    elif cvp == '8':
        araba.model_goster()            # model_goster metodunu overring yaptik
    elif cvp == '9':
        Tasit.tasit_sayisini_goster()   # cls metot ile tasit sayisini gosterdik
    elif cvp == '10':
        for i in Tasit.tasitlar:
            print(*i)                   # kayitli arabalari yazdirdik
    elif cvp == '11':
        markasi = input('araba markasini giriniz...:')
        motor_gucu=input('motor gucunu giriniz...:')
        koltuk_sayisi=input('koltuk sayisini giriniz...:')
        km_durumu=input('km durumunu giriniz...:')
        model=input('modelini giriniz...:')
        satis_yili=input('satis yilini giriniz...:')
        max_hiz=input('max hizi giriniz...:')

        markasi=Araba(markasi,motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili, max_hiz)

    else:
        print('cikiliyorrrrrr')
        quit()
