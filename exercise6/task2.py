# File: task2.py
# Author: Jasmin Fränti
# Description: Task 2 of exercise 6
# Python code implementation of the UML sequence diagram

import random

class Habitat:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__animals = []
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_animals(self):
        return self.__animals
    
    def add_animal(self, animal):
        self.__animals.append(animal)
        

class Mammal:
    def __init__(self, name, age, habitat):
        self.__name = name
        self.__age = age
        self.__habitat = habitat

    def eat(self):
        return f"{self.get_name()} is eating."

    def rest(self):
        print(f"{self.get_name()} is now resting in the shadow of an acacia tree")
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        
    def get_habitat(self):
        return self.__habitat
    
    def set_habitat(self, habitat):
        self.__habitat = habitat


class Lion(Mammal):
    def __init__(self, name, age, habitat, mane_color):
        super().__init__(name, age, habitat)
        self.__mane_color = mane_color
        self.__prey = "Gazelle"
        
    def get_mane_color(self):
        return self.__mane_color
    
    def set_mane_color(self, color):
        self.__mane_color = color
        
    def get_prey(self):
        return self.__prey
    
    def set_prey(self):
        return self.__mane_color

    def roar(self):
        return f"{self.__name} is roaring."
    
    def hunt(self, prey):
        print(f"{self.get_name()} is hunting {prey.get_name()}")
        
    def move_to_habitat(self, habitat):
        self.set_habitat(habitat)
        print(f"{self.get_name()} moves to {habitat.get_name()}")


class Gazelle(Mammal):
    def __init__(self, name, age, habitat, speed):
        super().__init__(name, age, habitat)
        self.running_speed = speed
        self.natural_enemy = "Lion"
        
    def get_running_speed(self):
        return self.running_speed
    
    def set_running_speed(self, speed):
        self.running_speed = speed
        
    def get_natural_enemy(self):
        return self.natural_enemy
    
    def set_natural_enemy(self, enemy):
        self.natural_enemy = enemy

    def run(self):
        return f"{self.name} is running at {self.running_speed} km/h."
    
    def escape(self, predator: Lion):
        num = random.randint(1,2)
        print(f"{self.get_name()} is trying to escape {predator.get_name()}")
        
        if num == 1:
            print(f"{self.get_name()} got away and survived")
            self.rest()
        else:
            print(f"{self.get_name()} got caught by {predator.get_name()}")
            print(predator.eat())
            
sawannah = Habitat("Sawannah")
gazelle = Gazelle("Gaz", 5, sawannah, 30)
sawannah.add_animal(gazelle)

lion = Lion("Simba", 6, "jungle", "Golden")
print(f"{lion.get_name()} is living in {lion.get_habitat()}")

lion.move_to_habitat(sawannah)

lion.hunt(gazelle)
gazelle.escape(lion)