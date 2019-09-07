
class Auto():


    __auto_numbers = []

    def __init__(self,enginepower,numberofseats,kmofauto,model,sales_date):
        self.enginepower = enginepower
        self.numberofseats=numberofseats
        self.kmofauto=kmofauto
        self.model=model
        self.sales_date=sales_date
        self.numberoftyres=4
        Auto.__auto_numbers.append(self)

    def show_numberofseats(self):
        print("Number of the seats: ", self.numberofseats)

    def show_kmofauto(self):
        print("km of auto is: ", self.kmofauto)

    def show_engine(self):
        print("The engine power is: ", self.enginepower)

    def show_model(self):
        print("The model of the auto is: ", self.model)

    @classmethod
    def show_numberofautos(cls):
        print("Number of autos: ", len(cls.__auto_numbers))

class Car(Auto):
    def __init__(self,enginepower,numberofseats,kmofauto,model,sales_date,max_speed):
        super().__init__(enginepower,numberofseats,kmofauto,model,sales_date)
        self.max_speed = max_speed

    def gear_up(self):
        print("Car gears up ")

    def stop_car(self):
        print("Car has stopped")

    def gear_down(self):
        print("Car gears down ")

    def show_model(self):
        print("The model of the car is: ", self.model)


    def situation_of_car(self):
        if issubclass(Car,Auto):
            print('Inherited from Car Class…')
        else:
            print("not inherited from Car Class")


car1=Auto(200,4,150000,2001,2015)
car1.show_kmofauto()
car1.show_numberofseats()
car1.show_engine()
car1.show_model()
car1.show_numberofautos()

car2=Car(180,4,170000,2005,2012)
car2.show_kmofauto()
car2.show_numberofseats()
car2.show_model()
car2.show_numberofautos()
