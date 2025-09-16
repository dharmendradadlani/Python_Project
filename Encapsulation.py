class Car:
    def __init__(self, brand,speed):
        self.__brand=brand  #private arribute for brand
        self.__speed=speed  #private attribute for speed
    def accelerate(self,increment):
            if increment>0:
                self.__speed+=increment
    def brake(self,decrement):
            if decrement>0 and self.__speed-decrement>=0:
                self.__speed-=decrement
    def get_speed(self):
            return self.__speed
    def get_brand(self):
            return self.__brand
        
        # def accelerate(self,increment):
        #     if increment>0:
        #         self__speed+=increment

mycar=Car("Toyota",50) #Create Car Object brand toyta and speed 50
print(mycar.get_speed())

mycar.accelerate(30)
print(mycar.get_speed())

mycar.brake(20)
print(mycar.get_speed())