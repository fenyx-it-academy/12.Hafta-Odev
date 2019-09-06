import time
class Vehicle():
    __vehicle_number=[]
    def __init__(self,brand_name,engine_power,seating_capacity,km,model,year_of_sale,number_of_wheel=4):
        self.brand_name=brand_name
        self.engine_power=engine_power
        self.seating_capacity=seating_capacity
        self.km=km
        self.model=model
        self.year_of_sale=year_of_sale
        self.number_of_wheel=number_of_wheel
        Vehicle.__vehicle_number.append(self)
    def display_seat(self):
        print("Seating capacity is: ",self.seating_capacity)
    def display_model(self):
        print("The model of vehichle is: ",self.model)
    def display_km(self):
        return print("The KM is: ",self.km)
    def update_vehiclenumber(self):
        print("Updated number of vehicle is",len(self.__vehicle_number))
    def __str__(self):
        return "Name of Brand: {}\nEngine Power: {}\nSeating Capacity: {}\nKM: {}\nModel: {}\nYear of Sale:{}\nNumber of Wheel: {}".format(self.brand_name, self.engine_power,self.seating_capacity,self.km,self.model,self.year_of_sale,self.number_of_wheel)
    @classmethod
    def display_vehicle(cls):
        print("The number of vehicle is:",len(cls.__vehicle_number))

class Car(Vehicle):
    def __init__(self,brand_name,engine_power,seating_capacity,km,model,year_of_sale,max_speed):
        super().__init__(brand_name,engine_power,seating_capacity,km,model,year_of_sale)
        self.max_speed=max_speed
    def stop(self):
        print("Car stopped!!!")
    def accelerator(self):
        print("Car is accelerating")
    def slow_down(self):
        print("Car is slowing down")
    def status_of_car(self):
        if issubclass(Car,Vehicle):
            print("This Class is inherited from Vehicle Class")
        else:
            print("The Class of Car is not inherited from the Vehicle Class")
    def display_model(self):
        print("The method of Car Class...The model of vehicle is: ",self.model)
    def __str__(self):
        return "Name of Brand: {}\nEngine Power: {}\nSeating Capacity: {}\nKM: {}\nModel: {}\nYear of Sale:{}\nNumber of Wheel: {}\nMax Speed: {}".format(self.brand_name, self.engine_power,self.seating_capacity,self.km,self.model,self.year_of_sale,self.number_of_wheel,self.max_speed)

bmw=Vehicle("BMW",120,4,12000,"520-d",2015)
mercedes=Vehicle("Mercedes",150,4,1500,"E200",2018)
audi=Car("Audi",165,7,1200,"Q7",2019,260)
volkswagen=Car("Volkswagen",115,4,112000,"Passat",2014,280)
print(bmw)
bmw.display_seat()
bmw.display_model()
bmw.display_km()

print(mercedes)
mercedes.display_seat()
mercedes.display_model()
mercedes.display_km()

print(audi)
audi.stop()
audi.accelerator()
audi.slow_down()
audi.status_of_car()
audi.display_model()

print(volkswagen)
volkswagen.stop()
volkswagen.accelerator()
volkswagen.slow_down()
volkswagen.status_of_car()
volkswagen.display_model()

bmw.update_vehiclenumber()
volkswagen.display_vehicle()