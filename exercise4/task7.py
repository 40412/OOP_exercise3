# File: task7.py
# Author: Jasmin Fränti
# Description: Task 7 of exercise 4 
# Phonebook

class Person:
    def __init__(self, name):
        self.name = name
        self.phone_numbers = []
        self.address = None

    def add_number(self, number):
        self.phone_numbers.append(number)

    def add_address(self, address):
        self.address = address

    def numbers(self):
        return self.phone_numbers

    def get_address(self):
        return self.address
    
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name, number):
        person = Person(name)
        person.add_number(number)
        if not name in self.__persons.keys():
            self.__persons[name] = person
        else:
            self.__persons[name].add_number(number)

    def get_numbers(self, name):
        if not name in self.__persons.keys():
            return None
        else:
            return self.__persons[name].numbers()
        
    def add_address(self, name, address):
        person = Person(name)
        if not name in self.__persons.keys():
            self.__persons[name] = person
        self.__persons[name].add_address(address)
        
    def get_address(self, name):
        if not name in self.__persons.keys():
            return None
        else:
            return self.__persons[name].get_address()
           
        
class PhoneBookApplication:
    def __init__(self) -> None:
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands:")
        print("0 Exit\n1 Add Number\n2 Search\n3 Add Address")
        
    def add_entry(self):
        name = input("Name: ")
        number = input("Number: ")
        self.__phonebook.add_number(name, number)
        
    def search(self, name):
        numbers = self.__phonebook.get_numbers(name)
        address = self.__phonebook.get_address(name)
        print(f"Name: {name}")
        
        if numbers == None or not numbers:
            print("Number unknown")
            return
        for number in numbers:
            print(number)
        
        if address == None:
            print("Address unknown")
        else:
            print(f"Address: {address}")

    def execute(self):
        self.help()

        while True:
            command = input("Command: ")

            if command == "0":
                break
            elif command == "1":
                name = input("Name: ")
                number = input("Number: ")
                self.__phonebook.add_number(name, number)
            elif command == "2":
                name = input("Search Name: ")
                self.search(name)
            elif command == "3":
                name = input("Name: ")
                address = input("Address: ")
                self.__phonebook.add_address(name, address)


if __name__ == "__main__":
    person = Person("Eric")
    print(person.name)
    print(person.numbers())
    print(person.address)
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers())
    print(person.address)

    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    print(phonebook.get_numbers("Eric"))
    print(phonebook.get_numbers("Eric"))
    print(phonebook.get_numbers("Emily"))
    
    # Example usage:
    emily_entry = phonebook.get_numbers("Emily")
    if emily_entry:
        print(f"{emily_entry.name}: {emily_entry.get_address()}")
    else:
        print("Emily not found in the phone book.")
        
    application = PhoneBookApplication()
    application.execute()