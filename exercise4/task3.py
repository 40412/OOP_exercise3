class Computer:
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed
        
    def __str__(self) -> str:
        return f"{self.__model}, {self.__speed} MHz"

class LaptopComputer(Computer):
    def __init__(self, model, speed, weight) -> None:
        super().__init__(model, speed)
        self.__weight = weight

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.__weight}kg"
    
laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)