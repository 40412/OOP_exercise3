# File: task5.py
# Author: Jasmin Fränti
# Description: Task 5 of exercise 4 
# Secret magic potion

class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, pword: str):
        super().__init__(name)
        self.password = pword

    def add_ingredient(self, ingredient: str, amount: float, pword: str):
        if pword == self.password:
            return super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong password!")
    
    def print_recipe(self, pword: str):
        if pword == self.password:
            return super().print_recipe()
        else:
            raise ValueError("Wrong password!")
        
diminuendo=SecretMagicPotion("Diminuendo maximus","hocuspocus")
diminuendo.add_ingredient("Toadstool",1.5,"hocuspocus")
diminuendo.add_ingredient("Magic sand",3.0,"hocuspocus")
diminuendo.add_ingredient("Frogspawn",4.0,"hocuspocus")
diminuendo.print_recipe("hocuspocus")
diminuendo.print_recipe("pocushocus")# WRONG password!