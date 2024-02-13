class Present:
    def __init__(self, name, weigth) -> None:
        self.name = name
        self.weight = weigth

    def __str__(self) -> str:
        return f"{self.name} ({self.weight}g)"
    
class Box:
    def __init__(self) -> None:
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        total_weight = 0

        for present in self.presents:
            total_weight += present.weight
        return total_weight
    
book =Present("Ta-Nehisi Coates:The Water Dancer",200)
box = Box()
box.add_present(book)
print(box.total_weight())
cd =Present("Pink Floyd: Dark Side of the Moon",50)
box.add_present(cd)
print(box.total_weight())