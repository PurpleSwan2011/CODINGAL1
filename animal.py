from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Runs"

class Cat(Animal):
    def sound(self):
        return "Meow"

    def move(self):
        return "Jumps"

class Bird(Animal):
    def sound(self):
        return "Chirp"

    def move(self):
        return "Flies"

def animal_actions(animal):
    print(f"The animal makes a sound: {animal.sound()}")
    print(f"The animal moves by: {animal.move()}")

dog = Dog()
cat = Cat()
bird = Bird()

animal_actions(dog)
animal_actions(cat)
animal_actions(bird)
