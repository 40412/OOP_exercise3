class Item:
    def __init__(self, name, weight) -> None:
        self.__name = name
        self.__weight = weight

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight
    
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

            for item in self.__items:
                if item.get_weight() > heaviest:
                    heaviest = item
            return heaviest
        else:
            return heaviest

    def __str__(self) -> str:
        
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.get_total_weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.get_total_weight()} kg)"
        
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
            print(suitcase.print_items())

    def __str__(self) -> str:
        if len(self.__suitcases) == 1:
            return f"1 suitcase, space for {self.__max_weight - self.get_total_weight()}kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.get_total_weight()}kg"