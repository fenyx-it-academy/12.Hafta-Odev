class Tasit():
    __tasitMiktari = []  # private

    def __init__(self, motorGucu, koltukSayisi, kmDurumu, modeli, satisYili):
        self.motorGucu = motorGucu
        self.koltukSayisi = koltukSayisi
        self.kmDurumu = kmDurumu
        self.modeli = modeli
        self.satisYili = satisYili
        self.tekerlek_sayisi = 4
        Tasit.__tasitMiktari.append(self)
    def __str__(self):
        return "\n\nAraba ozellikleri: \nmotorGucu:{}\n koltukSayisi:{}\n kmDurumu:{}\n modeli:{}\n satisYili:{}".format(self.motorGucu,self.koltukSayisi, self.kmDurumu, self.modeli, self.satisYili)

    def koltukSayisiniGoster(self):
        print("Aracın koltuk sayisi: ", self.koltukSayisi)

    def modeliniGoster(self):
        print("Aracın modeli: ", self.modeli)

    def kmDurumuGoster(self):
        print("Aracın km durumu: ", self.kmDurumu)
        return self.kmDurumu

    @classmethod
    def tasitMiktariGoster(cls):
        print("Taşıt miktarı: ", len(cls.__tasitMiktari))
        return len(cls.__tasitMiktari)

   


t1 = Tasit(3.2, 5, 23412, 2014, 2019)
t2 = Tasit(1.6, 4, 12345, 2013, 2015)

t1.koltukSayisiniGoster()
t1.modeliniGoster()
t1.kmDurumuGoster()
t1.tasitMiktariGoster()

print("------------------------------------------------")

# inherit
class Araba(Tasit):
    def __init__(self, motorGucu, koltukSayisi, kmDurumu, modeli, satisYili, maxHiz):
        super().__init__(motorGucu, koltukSayisi, kmDurumu, modeli, satisYili)  # parent class attr degismesin
        self.maxHiz = maxHiz  # ek olarak bu attr olsun

    def arabayiDurdur(self):
        print("Araba durdu.")

    def gazaBas(self):
        print("Arabanın hızı arttı.")

    def arabayiYavaslat(self):
        print("Arabanın hızı azaldı.")

    def arabaninDurumu(self):
        if issubclass(Araba, Tasit) == True:
            print("Araba sınıf Tasit sinifindan miras alınmıştır.")
        else:
            print("Araba sınıfı Tasit sınıfından miras alınmamıştır.")

    #tasit sınıfının metodu override ediliyor
    def modeliniGoster(self):
        print("Araba sınıfının methodu: ", self.modeli)

a1 = Araba(2.4, 6, 43124, 2016, 2018, 250)
a2 = Araba(1.6, 5, 123344, 2005, 2011, 260)

a1.arabayiDurdur()
a1.gazaBas()
a1.arabayiYavaslat()
a1.arabaninDurumu()

a1.modeliniGoster()

print(t1,t2,a1,a2)
