"""
Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari isimli bir bos liste tanimlayiniz.
Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili gibi obje ozellikleri(instance attributes) olsun.
Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin. Ayrica her ornekte degismeyecek sekilde;
tekerlek sayisi isimli bir ornek niteligi tanimlayin ve degeri 4 olsun. Ayrica bu objenin su methodlari olmalidir:

1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
2.modelini goster (tasitin modelini ekrana yazdirmali)
3. km_durumunu al (tasitin kilometre durumunu return etmeli)
4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.

- bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
- class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.
Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. Tasit sinifindan miras aldiginiz
init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda
parametre olarak verilsin. Bu sinifta su methodlari tanimlayiniz;

1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise
“Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan
miras alinmamistir.’ seklinde yazsin)
Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve ‘Araba sinifinin methodu….’
 seklinde ekrana cikti veriniz ve modeli yazdiriniz.
"""
class Vehicle():
    vehicle_quantity=[]
    #print("The Quantity of vehicle is :",vehicle_quantity)
    def __init__(self,motorpower,seating_capacitiy,km_of_vehicle,model,date_of_sell,number_of_tires=4):
        self.motorpower=motorpower
        self.seating_capacitiy=seating_capacitiy
        self.km_of_vehicle=km_of_vehicle
        self.model=model
        self.date_of_sell=date_of_sell
        self.number_of_tires=number_of_tires
        print("This class was inherited from the Vehicle class ")

    def show_seating_capacitiy(self):
        print("The seating capacity of Vehicle is: ",self.seating_capacitiy)

    def show_model(self):
        print("The model of Vehicle is: ",self.model)

    def show_milage(self):
        print("The milage of Vehicle is: ",self.km_of_vehicle)
        return self.km_of_vehicle
    def update_vehicle_quantity(self):
        print(self.vehicle_quantity.append(Vehicle))
        #4.tasit miktarini_guncelle.Sinif her orneklendiginde tasit miktarini 1 artirmali.
class Car(Vehicle):
    def __init__(self,motorpower, seating_capacitiy, km_of_vehicle, model, date_of_sell, number_of_tires,maximum_speed):
        super().__init__(motorpower, seating_capacitiy, km_of_vehicle, model, date_of_sell, number_of_tires=4)
        self.maximum_speed=maximum_speed
        print("This class was not inherited from the Vehicle class ")
    def stop_car(self):
        print("Car Stopped!!!!!!!")
    def speed_up(self):
        print("Car is Speed Up!!!!!!")
    def slow_down(self):
        print("Car is Slow Down")
    def show_model(self):
        print("This class was NOT inherited from the Vehicle class ")
        print("The model of Car is: ",self.model)

print("Welcome to the Vehicle Application")
while True:
    answer=input("""
          1-Prepare a Vehicle
          2-Prepare a Car
          3-Quit
          Please Make Your Choice:
          """)

    if answer == "1":
        vehicle_quantity=[]
        vehicle_add=input(("Please Enter The Name Of Vehicle To Add:"))
        vehicle_quantity.append(vehicle_add)
        smotorpower = int(input("Please Enter The Motor Power of Vehicle:"))
        sseating_capacitiy = int(input("Please Enter The Seating Capacity of Vehicle:"))
        skm_of_vehicle = int(input("Please Enter The KM of Vehicle:"))
        smodel = int(input("Please Enter The Model of Vehicle:"))
        sdate_of_sell = int(input("Please Enter The Date of Sell of Vehicle:"))
        snumber_of_tires = int(input("Please Enter The Numbers of Tires of Vehicle:"))
        newvehicle= Vehicle(smotorpower,sseating_capacitiy,skm_of_vehicle,smodel,sdate_of_sell,snumber_of_tires)
        while True:
            print("""Please Enter:
           1-Show The Seating Capacity of Vehicle
           2-Show Model of Vehicle
           3- Show Milage of Vehicle
           4-Update The Quantity of Vehicle
           5-To The Up Menu
           """)
            key =input("Please Make Your Vehicle Choice: ")
            if key == "1":
                newvehicle.show_seating_capacitiy()
            if key == "2":
                newvehicle.show_model()
            if key == "3":
                newvehicle.show_milage()
            if key == "4":
                newvehicle.update_vehicle_quantity()
            if key == "5":
                break
    if answer == "2":
        vehicle_quantity = []
        car_add = input(("Please Enter The Name Of Car To Add:"))
        vehicle_quantity.append(car_add)
        car_motorpower = int(input("Please Enter The Motor Power of Car:"))
        car_seating_capacitiy = int(input("Please Enter The Seating Capacity of Car:"))
        car_km_of_vehicle = int(input("Please Enter The KM of Car:"))
        car_model = int(input("Please Enter The Model of Car:"))
        car_date_of_sell = int(input("Please Enter The Date of Sell of Car:"))
        car_number_of_tires = int(input("Please Enter The Numbers of Tires of Car:"))
        car_maximum_sepped = int(input("Please Enter The Maximum Speed of Car: "))
        newcar = Car(car_motorpower, car_seating_capacitiy, car_km_of_vehicle, car_model, car_date_of_sell,car_number_of_tires,car_maximum_sepped)
        while True:
            print("""Please Enter:
                   1-Stop The Car
                   2-Speed Up The Car
                   3- Slow Down The Car
                   4-Show Model Of Car
                   5-To The Up Menu
                   """)
            key = input("Please Make Your Car Choice: ")
            if key == "1":
                newcar.stop_car()
            if key == "2":
                newcar.speed_up()
            if key == "3":
                newcar.slow_down()
            if key == "4":
                newcar.show_model()
            if key == "5":
                break
    if answer == "3":
        quit()


