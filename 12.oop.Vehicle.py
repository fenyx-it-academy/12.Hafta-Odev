print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")
import time


"""Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari
 isimli bir bos liste tanimlayiniz. Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli,
 satis_yili gibi obje ozellikleri(instance attributes) olsun. Ve her orneklenme durumunda bu ozellikler
 parametre olarak verilsin. Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek
 niteligi tanimlayin ve degeri 4 olsun. Ayrica bu objenin su methodlari olmalidir:
1. koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
2. modelini goster (tasitin modelini ekrana yazdirmali)
3. km_durumunu al (tasitin kilometre durumunu return etmeli)
4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.
- bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
- class method olarak tasit_miktarini gosterecek bir method tanimlayiniz."""


class Vehicle:

    vehicles = []
    no_wheel = 4
    __no_vehicle = 0                                     # '__' 2 adet underscore ile kod gizlendi. Class disindan baska goremez
    current_speed = 0

    def __init__(self, merk, engine_power, color, no_seat, km_situ, model, sale_year):
        self.merk = merk
        self.engine_power = engine_power
        self.color = color
        self.km_situ = km_situ
        self.model = model
        self.sale_year = sale_year
        self.no_seat = no_seat
        Vehicle.vehicles.append(self)                                   # marka farketmeksizin ekleme yapildi
        Vehicle.__no_vehicle += 1                                       # her eklenen tasit +1 arttirdi

    def show_merk(self):
        print(f'Merk name: {self.merk}')

    def number_seat(self):
        print(f'Number of Seat: {self.no_seat}')

    def show_model(self):
        print(f'Model of vehicle: {self.model}')

    def km_statu(self):
        return f'Km statu: {self.km_situ} km'

    def info_tasit(self):
        print(f'Merk: {self.merk},\nModel of vehicle: {self.model},\nColor: {self.color},\nStatu of the vehicle: {self.km_situ},\nNumber of seat: {self.no_seat}')

    def no_vehicle_update(self):
        return self.__no_vehicle

    @classmethod
    def vehicles_no(cls):
        print(f'There are/is {len(Vehicle.vehicles)} vehicle(s).')                 # listeye eklenen tasit sayisi

# araba = Vehicle('Mazda', 1800, 'yesil', 7, 123, 2016, 2017)
# print(araba.km_statu())
# araba.info_tasit()


"""Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. 
Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir 
ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin. 
Bu sinifta su methodlari tanimlayiniz;
1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
“Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
miras alinmamistir.’ seklinde yazsin)
Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz 
ve ‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz."""

class Car(Vehicle):
    def __init__(self, merk, engine_power, color, no_seat, km_situ, model, sale_year, max_speed):
        super().__init__(merk, engine_power, color, no_seat, km_situ, model, sale_year)

        self.max_speed = max_speed

    def car_stop(self):
        Vehicle.current_speed = 0
        time.sleep(3)
        print(f"Car has stopped. Current Speed: {Vehicle.current_speed}")

    def speedUp(self):
        Vehicle.current_speed += 10
        time.sleep(3)
        print(f"Car is going speedup. Current Speed: {Vehicle.current_speed}")

    def car_slow(self):
        Vehicle.current_speed -= 10                                                #Bunun icin dongu kurulursa guzel olur aksi halde eksi hiz yoktur
        time.sleep(3)
        print(f"Car is going backwards. Current Speed: {Vehicle.current_speed}")

    def car_statu(self):
        if issubclass(Car, Vehicle):
            print("This class is inherited from the Vehicle class.")
        else:
            print("This class is NOT inherited from the Vehicle class.")

    def car_show_model(self):                                               # over ride yaptik
        super().info_tasit()
        print(f'Max Speed: {self.max_speed}\n' + f'Method of Car class...')


car1 = Car('Audi A5', 'Power of Engine: 3000', 'Color: Red', 5, 120000, 2019, 2020, 320)
car2 = Car('Tesla Model S', 'Power of Engine: 2000', 'Color: Green', 6, 220000, 2019, 2020, 340)
car3 = Car('Mazda Model 5', 'Power of Engine: 3000', 'Color: Blue', 5, 110000, 2020, 2020, 360)


# car1.show_merk()
# print(car1.engine_power)
# print(car1.color)
# car1.number_seat()
# print(car1.km_statu())
# car1.show_model()
# print(f'Sale of year: {car1.sale_year}')
# print(f'Max speed: {car1.max_speed} km/h')
# car1.info_tasit()
# car1.car_statu()
# Vehicle.vehicles_no()
# car1.car_stop()
# car1.speedUp()
# car1.car_slow()
# print(f'Number of wheel: {car1.no_wheel}')
print("\t".center(33), "~ WELCOME YOUR CAR ~")

while True:
    enter = input("""
          1. Chose a Vehicle
          2. Chose a Car
          3. Exit
          Please Make Your Choice: 
          """)

    if enter == "1":
        vehicles = []
        vehicle_add = input("Enter name of Vehicle: ")
        vehicles.append(vehicle_add)
        engine_power = int(input("Enter engine power of Vehicle: "))
        color = input("Enter a Color: ")
        no_seat = int(input("Enter seat capacity of Vehicle: "))
        km_situ = int(input("Enter km of Vehicle: "))
        model = int(input("Enter model of Vehicle: "))
        sale_year = int(input("Enter sale year of Vehicle: "))

        MakeVehicle = Vehicle(vehicle_add, engine_power, color, no_seat, km_situ, model, sale_year)
        while True:
            print("""Please Enter:
           1. Show the seat capacity of vehicle
           2. Show model of vehicle
           3. Show how much used km of vehicle
           4. Update numbers of vehicle
           5. Back to Menu
           """)
            choice =input("Choice your vehicle: ")
            if choice == "1":
                MakeVehicle.number_seat()
            if choice == "2":
                MakeVehicle.show_model()
            if choice == "3":
                MakeVehicle.km_statu()
            if choice == "4":
                MakeVehicle.vehicles_no()
            if choice == "5":
                break
    elif enter == "2":
        vehicles = []
        car_add = input("Enter name of Car: ")
        vehicles.append(car_add)
        car_enginepower = int(input("Enter engine power of Car: "))
        color = input("Enter a Color: ")
        car_no_seat = int(input("Enter seat capacity of Car: "))
        car_km_situ = int(input("Enter km of Car: "))
        car_model = int(input("Enter model of Car: "))
        car_sale_year = int(input("Enter sale year of Car: "))
        car_max_speed = int(input("Enter maximum speed of Car: "))
        NewCar = Car(car_add, car_enginepower, color, car_no_seat, car_km_situ, car_model, car_sale_year, car_max_speed)
        while True:
            print("""Please Enter:
                   1. Stopping Car
                   2. Speeding up Car
                   3. Slowing down Car
                   4. Show model of Car
                   5. Show information about Car
                   6. Back to Menu
                   """)
            choice = input("Choice your Car: ")
            if choice == "1":
                NewCar.car_stop()
            elif choice == "2":
                NewCar.speedUp()
            elif choice == "3":
                NewCar.car_slow()
            elif choice == "4":
                NewCar.show_model()
            elif choice == '5':
                NewCar.info_tasit()
            elif choice == "6":
                break
    elif enter == "3":
        quit()