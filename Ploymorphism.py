class Cat:
    def speak(self):
        print("Meow !!")

class Dog:
    def speak(self):
        print("Woof !!")

animals = [Cat(), Dog()]

for animal in animals:
    animal.speak() # Different behaviour bases on object