# File: task2.py
# Author: Jasmin Fränti
# Description: Task 2 of exercise 7
# Python code implementation of the UML State Diagram

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
        self.__state = ""

    def eat(self):
        self.set_state("eating")
        print(f"{self.get_name()} has eaten and is content")

    def rest(self):
        self.set_state("resting")
    
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
        
    def move_to_habitat(self, habitat):
        self.set_habitat(habitat)
        print(f"{self.get_name()} moves to {habitat.get_name()}")
        
    def set_state(self, state):
        self.__state = state
        print(f"{self.__name} is {self.__state}")
        
        if state == "resting":
            self.set_state("hungry")
        
    def get_state(self):
        return self.__state

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
    
    def set_state(self, state):
        super().set_state(state)
        
        if self.get_state() == "hungry":
            gazelle = Gazelle("Gaz", 5, "sawannah", 30)
            self.hunt(gazelle)
            
    def hunt(self, prey):
        self.__state = "hunting"
        print(f"{self.get_name()} is hunting {prey.get_name()}")
        prey.escape(self)
        
    def try_hunting_again(self):
        print(f"{self.get_name()} is trying to hunt another prey")
        print("The pray is caught")
        self.eat()

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
            predator.try_hunting_again()
        else:
            print(f"{self.get_name()} got caught by {predator.get_name()}")
            predator.eat()
            
lion = Lion("Simba", 6, "sawannah", "Golden")
print(f"{lion.get_name()} got tired")
lion.rest()
