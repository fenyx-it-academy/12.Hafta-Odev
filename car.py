from vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, *args, max_speed, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_speed = max_speed
    def stop_car(self):
        print("The car has been stoped.")
    def accelerate(self):
        print("The car is accelerating.")
    def slow_down(self):
        print("The car is slowing down.")
    def show_situation(self):
        if issubclass(Car, Vehicle):
            print("This class is inherited from vehicle class.")
        else:
            print("This class is not inherited from vehicle class.")
    def show_model(self):
        super().show_model()
        print("Class of Car's method.")
            
mazda = Car("mazda", "B2500", 2.5, 5, 80000, 2005, max_speed = 180)
mazda.show_situation()
mazda.stop_car()
mazda.accelerate()
mazda.slow_down()
mazda.show_model()
