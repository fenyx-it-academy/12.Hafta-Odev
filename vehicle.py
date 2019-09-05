class Vehicle():
    __num_of_vehicle = []
    def __init__(self, vehicle_name, model, engine_power, num_of_seat,
                 km, year_of_sale, num_of_wheel = 4):
        self.vehicle_name = vehicle_name
        self.engine_power = engine_power
        self.num_of_seat = num_of_seat
        self.km = km
        self.model = model
        self.year_of_sale = year_of_sale
        self.num_of_wheel = num_of_wheel
        self.add_num_of_vehicle()
    def show_num_of_seat(self):
        print(f"This vehicle has {self.num_of_seat} seat.")
    def show_model(self):
        print(f"This vehicle's model is {self.model}.")
    def amount_of_km(self):
        return self.km
    def add_num_of_vehicle(self):
        self.__num_of_vehicle.append(self.vehicle_name)
        print(f"{self.vehicle_name} has been added.")
    @classmethod
    def show_num_of_vehicle(cls):
        print("Vehicles:")
        for i in cls.__num_of_vehicle:
            print("-",i) 


bmw = Vehicle("bmw", "320i", 1.8, 5, 20000, 2010) 
mercedes = Vehicle("mercedes", "E200", 1.8, 5, 30000, 2009)
toyota = Vehicle("toyota", "corolla", 1.4, 5, 40000, 2017)

bmw.show_num_of_seat()
bmw.show_model()
print(bmw.amount_of_km())
Vehicle.show_num_of_vehicle()
