# File: task2.py
# Author: Jasmin Fränti
# Description: Task 2 of exercise 4

class Item:
    def __init__(self, name, weight) -> None:
        self.__name = name
        self.__weight = weight

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name}, {self.__weight}g"
    
class Suitcase:
    def __init__(self, max_weight) -> None:
        self.__max_weight = max_weight
        self.__items = []

    def get_total_weight(self):
        weight = 0

        for item in self.__items:
            weight += item.get_weight()

        return weight

    def __within_max_weight(self, weight):
        if self.get_total_weight() + weight <= self.__max_weight:
            return True
        else:
            return False
        
    def add_item(self, item: Item):
        
        if self.__within_max_weight(item.get_weight()):
            self.__items.append(item)
        else:
            print("Exeeding max weight")

    def print_items(self):
        for item in self.__items:
            print(item)

    def get_heaviest_item(self):
        heaviest = None

        if self.__items:
            heaviest_weight = 0
            for item in self.__items:
                if item.get_weight() > heaviest_weight:
                    heaviest_weight = item.get_weight()
                    heaviest = item
            return heaviest
        else:
            return heaviest

    def __str__(self) -> str:
        
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.get_total_weight()} g)"
        else:
            return f"{len(self.__items)} items ({self.get_total_weight()} g)"
        
class CargoHold:
    def __init__(self, max_weight) -> None:
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def within_max_weight(self, weight):
        if self.get_total_weight() + weight <= self.__max_weight:
            return True
        else:
            return False
        
    def add_suitcase(self, suitcase: Suitcase):
        if self.within_max_weight(suitcase.get_total_weight()):
            self.__suitcases.append(suitcase)
        else:
            print("Too heavy")


    def get_total_weight(self):
        weight = 0

        for suitcase in self.__suitcases:
            weight += suitcase.get_total_weight()

        return weight
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self) -> str:
        if len(self.__suitcases) == 1:
            return f"1 suitcase, space for {self.__max_weight - self.get_total_weight()}g"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.get_total_weight()}g"
        
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)

adas_suitcase=Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

print("Heaviest item:", adas_suitcase.get_heaviest_item())

peters_suitcase=Suitcase(1000)
peters_suitcase.add_item(brick)

cargo_hold=CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()