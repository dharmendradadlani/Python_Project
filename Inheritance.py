class Animal:
     def speak(self):
          print("Animal speark")

class Dog(Animal):  # Class dog inherit from animal
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
            print(f'{self.name}, {self.breed}')
        
dog1 = Dog("Buddy","Golden Retriever")
dog1.bark()
dog1.speak()  # Calls dog speak method
