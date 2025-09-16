class Car:
    wheels=4
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f'{self.brand}, {self.model}, {self.wheels}')

my_car= Car("Toyota","Corolla")
my_car.display_info()

