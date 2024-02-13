class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name}, {self.height}"

class Room:
    def __init__(self) -> None:
        self.people = []

    def add_person(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if self.people:
            return False
        else:
            return True
    
    def print_contents(self):
        for person in self.people:
            print(person)

    def shortest_person(self):
        shortest = self.people[0]

        if self.people:
            for person in self.people:
                if person.height < shortest.height:
                    shortest = person
            return shortest

        else:
            return None
        
    def remove_shortest(self, shortest):
        if shortest == None:
            return None
        else:
            self.people.remove(shortest)
            return shortest

room =Room()
print("Is the room empty?",room.is_empty())
room.add_person(Person("Lea",183))
room.add_person(Person("Kenya",172))
room.add_person(Person("Ally",166))
room.add_person(Person("Nina",162))
room.add_person(Person("Dorothy",175))
print("Is the room empty?",room.is_empty())
room.print_contents()
print("Shortest person: ", room.shortest_person())
print("Shortest person removed: ", room.remove_shortest(room.shortest_person()))
room.print_contents()

