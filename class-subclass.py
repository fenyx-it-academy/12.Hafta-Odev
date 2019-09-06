class Voertuig:
    voertuig_hoeveelheid=['auidi','BMW','Mercedes']
    # arac sayısı

    def __init__(self,model,motorvermogen,aantal_zitplaatsen,km_status,verkoopjaar):
        self.aantal_wielen=4
        # tekerlek sayısı
        self.motorvermogen=motorvermogen
        # motor gücü
        self.aantal_zitplaatsen=aantal_zitplaatsen
        # koltuk sayısı
        self.km_status=km_status
        # km durumu
        self.model=model
        # arac modeli
        self.verkoopjaar=verkoopjaar
        # satıs yılı
        self.voertuig_hoeveelheid='ARAÇ LİSTESİNİ GÖRME YETKİNİZ YOK!'
        # arac listesine ornek uzerinden erisimi engellemek icin class instance
        # ile aynı isimli instance attribuite olusturuldu.

    def toon_aantal_zitplaatsen(self):
        # koltuk sayısını goster
        print(self.aantal_zitplaatsen)

    def toon_model(self):
        # arac modelini goster
        return (self.model)

    def krijg_km_status(self):
        # km durumunu al
        return(self.km_status)

    def voeg_voertuig_toe(self,nieuw_voertuig):
        # arac ekle
        self.voertuig_hoeveelheid.append(nieuw_voertuig)
        # arac sayısı listesine append method ile arac eklenir

    @classmethod
    def toon_voertuiglijst(cls):
        # arac listesini gosteren classmethod
        sayac=0
        for i in Voertuig.voertuig_hoeveelheid:
            sayac+=1
            print(sayac,i)

class Auto(Voertuig):
    def __init__(self, motorvermogen, aantal_zitplaatsen, km_status, model, verkoopjaar, maimale_snelheid):
        super().__init__(motorvermogen, aantal_zitplaatsen, km_status, model, verkoopjaar)
        self.maximale_snelheid=maimale_snelheid

    def stop_auto(self):
        # araba durdur modulu
        print('ARABA DURDU...')

    def sneller(self):
        # arabayı hızlandırma modulu
        print('ARABA HIZLANIYOR...')

    def traag(self):
        # arabayı yavaslatma modulu
        print('ARABA YAVAŞLIYOR')

    def toon_model(self,auto_model):
        # arac modelini goster
        self.auto_model=auto_model
        print(f'ARACINIZIN MODELİ: {self.auto_model}')

def toon_auto_status(auto):
    # arabanın durumunu gosteren foksiyon
    if isinstance(auto,Voertuig)==True:
        # arbanın özellikleri araclar sınıfından alınıp-alınmadıgı sorgulanıyor
        print(f'{auto.toon_model()} MARKA ARABANIN ÖZELLİKLERİ ARAÇLARDAN INHERITANCE EDİLMİŞTİR...')
    else:
        print(f'{auto} MARKA ARABANIN ÖZELLİKLERİ ARAÇLARDAN INHERITANCE EDİLMEMİŞTİR...')


BMW=Voertuig('BMW','180HP',5,12000,2018)
print(BMW.voertuig_hoeveelheid)
# print(*Voertuig.voertuig_hoeveelheid)
Voertuig.toon_voertuiglijst()

b='toyota'
toon_auto_status(b)
toon_auto_status(BMW)
BMW.toon_model()
# print(isinstance(a,Voertuig))

JEEP=Auto(210,6,24000,'JEEP',2016,12)
JEEP.toon_model('JEEP')
JEEP.sneller()