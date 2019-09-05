class Tasit():
    __tasit_miktari = []
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.modeli = modeli
        self.satis_yili = satis_yili
        self.tekerlek_sayisi = 4
        self.tasit_miktarini_guncelle()
    def koltuk_sayisini_goster(self,marka):
        print('{} Koltuk sayisi: {}'.format(marka,self.koltuk_sayisi))
    def modelini_goster(self,marka):
        print('{} modeli: {}'.format(marka,self.modeli))
    def km_durumunu_al(self,marka):
        print('Km durumu: {}'.format(marka,self.km_durumu))
    def tasit_miktarini_guncelle(self):
        print('Yeni tasit eklendi!')
        self.__tasit_miktari.append(1)
    @classmethod
    def tasit_miktarini_goster(cls):
        print('Toplam tasit miktari: ', len(cls.__tasit_miktari))

class Araba(Tasit):
    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili,max_hiz):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili)
        self.max_hiz = max_hiz
    def arabayi_durdur(self,marka):
        print('{} durduruldu!'.format(marka))
    def gaza_bas(self,marka):
        print('{} hizlaniyor...'.format(marka))
    def arabayi_yavaslat(self, marka):
        print('{} yavasliyor...'.format(marka))
    def arabanin_durumu(self):
        if issubclass(Araba, Tasit):
            print('Bu sinif Tasit sinifindan miras alinmistir.')
        else:
            print('Araba sinifi Tasit sinifindan miras alinmamistir.')
    def modelini_goster(self,marka):
        print('Araba sinifinin methodu… {} modeli {}'.format(marka,self.modeli))




volkswagen = Araba('500', 5, 120000, 'golf', 2012, 240)
audi = Araba('400', 4, 80000, 'A3', 2015, 320)
minicooper = Araba('400', 4, 80000, 'countryman', 2015, 320)
Tasit.tasit_miktarini_goster()

def arabaMenuGoster():
    print('*' * 30 + '\n\n' + 'Araba Secin:'.rjust(
        22) + '\n\n' + '1.Volkswagen\n' + '2.Audi\n' + '3.Minicooper\n'
          + 'Cikis icin "q" ya basin!\n\n' + '*' * 30 + '\n')
def islemMenuGoster():
    print('*' * 30 + '\n\n' + 'Islem Secin:'.rjust(
        22) + '\n\n' + '1.Koltuk Sayisi Sorgula\n' + '2.Modeli Sorgula\n' + '3.Km Sorgula\n' + '4.Gaza Bas\n'
          + '5.Arabayi Yavaslat\n' + '6.Arabayi Durdur\n' + '7.Arabanin Durumunu Ogren\n'+ '8.Arabanin Max Hizini Ogren\n')
print(audi.max_hiz)
try:
    while True:
        arabaMenuGoster()
        islem = input('Islem yapmak istediginiz tasit markasini secin: ')
        if islem == '1':
            araba = volkswagen
            marka = 'volkswagen'
        elif (islem == '2'):
            araba = audi
            marka = 'audi'
        elif (islem == '3'):
            araba = minicooper
            marka = 'minicooper'
        elif (islem == 'q'):
            print('Programdan cikiliyor...')
            break
        else:
            print('Lutfen gecerli bir islem secin!')
            continue

        islemMenuGoster()
        islem = input('{} icin yapmak istediginiz islemi secin: '.format(marka))
        if islem == '1':
            araba.koltuk_sayisini_goster(marka)
        elif (islem == '2'):
            print('{} Modeli: {}'.format(marka, araba.modeli))
        elif (islem == '3'):
            araba.km_durumunu_al(marka)
        elif (islem == '4'):
            araba.gaza_bas(marka)
        elif (islem == '5'):
            araba.arabayi_yavaslat(marka)
        elif (islem == '6'):
            araba.arabayi_durdur(marka)
        elif (islem == '7'):
            araba.arabanin_durumu()
        elif (islem == '8'):
            print('{} Max Hizi: {}'.format(marka, araba.max_hiz))
        else:
            print('Lutfen gecerli bir islem secin!')
            continue
except:
    print('Hatali islem..')










