# File: task1.py
# Author: Jasmin Fränti
# Description: Task 1 of exercise 5
# UML Class Diagram code implementation

import random

class Mammal:
    def __init__(self, name, age, habitat):
        self.__name = name
        self.__age = age
        self.__habitat = habitat

    def eat(self):
        return f"{self.__name} is eating."

    def sleep(self):
        return f"{self.__name} is sleeping."
    
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
        print(f"{self.__name} is hunting {prey}")


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
        print(f"{self.__name} is trying to escape {predator.get_name()}")
        
        if num == 1:
            print(f"{self.__name} got away and survived")
        else:
            print(f"{self.__name} got eaten my {predator.get_name()}")