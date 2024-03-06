# File: task5.py
# Author: Jasmin Fränti
# Description: Task 5 of exercise 4 
# Dice

import random

class Die:
    def __init__(self, name: str) -> None:
        self.name = name
        self.current_side = 1

    def roll(self):
        self.current_side = random.randint(1,6)
    
    def show_side(self):
        return self.current_side
    
class Player():
    def __init__(self, id: int, name: str) -> None:
        self.__id = id
        self.__name = name
        self.pet = None
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id: int):
        self.__id = id

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def __str__(self) -> str:
        return f"Player ID: {self.__id} Player name: {self.__name}"
    
class Round():
    def __init__(self, player: Player, rnum: int, dice: list = []) -> None:
        self.round_number = rnum
        self.dice = dice
        self.roll = []
        self.player = player

    def get_sum(self):
        sum = 0

        for die in self.roll:
            sum += die[1]

        return sum
    
    def add_die(self, die):
        self.dice.append(die)

    def roll_dice(self):
        
        for die in self.dice:
            die.roll()
            self.roll.append((die.name, die.show_side()))

    def print_roll(self):
        
        for die in self.roll:
            print(die[0], die[1])

class Game():
    def __init__(self, name: str) -> None:
        self.name = name
        self.rounds = []
        self.winner = None

    def add_round(self, round):
        self.rounds.append(round)

    def print_rounds(self):
        print(f"Game: {self.name}")
        print()

        for round in self.rounds:
            print(f"Player: {round.player.get_name()}")
            round.print_roll()
            print(f"Sum of this roll: {round.get_sum()}")
            print()

    def tie_breaker(self, winners: dict):
        tie_breaker_die = Die("Tiebreaker Die")

        print("Starting Tiebreaker")

        while len(winners) > 1:
            rolls = dict()

            for key in winners:
                print(f"{key} rolls:")
                tie_breaker_die.roll()
                roll = tie_breaker_die.show_side()
                print(roll)
                rolls[key] = roll

            best_roll = max(rolls.values())
            winners = {k: v for k, v in rolls.items() if v == best_roll}

        return next(iter(winners))
                   
    def show_winner(self):
        results = {}
        winners = dict()

        for roll in self.rounds:
            results[roll.player] = roll.get_sum()
        
        max_sum = max(results.values())
        
        for key, value in results.items():
            if value == max_sum:
                winners[key] = value
        
        if len(winners) > 1:
            return self.tie_breaker(winners)
        else:
            return next(iter(winners))
        
class Mammal:
    def __init__(self, ID, species, name, size, weight):
        self.ID = ID
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

    def __str__(self) -> str:
        return f"\nAnimal ID: {self.ID}\nSpecies: {self.species}\nName: {self.name}\nSize: {self.size} \nWeight: {self.weight}"
    

player1 = Player(1, "Jasmin")
player2 = Player(2, "Ville")

red_die = Die("Red Die")
blue_die = Die("Blue Die")
green_die = Die("Green Die")
yellow_die = Die("Yellow Die")

dice_list = [red_die, blue_die, green_die]
game1 = Game("Ville vs Jasmin")

round1 = Round(player1, 1, dice_list)
round2 = Round(player2, 2, dice_list)

round1.add_die(yellow_die) # Adds to all Round objects because the list is shared due to the default value in __init__

game1.add_round(round1)
game1.add_round(round2)

round1.roll_dice()
round2.roll_dice()

round1.print_roll()
round2.print_roll()
print()
game1.print_rounds()
print(f"The winner is: {game1.show_winner()}")

# Part 3
print()
print("Part 3 starts")
players = {}
players[player1] = green_die
players[player2] = red_die

for player, die in players.items():
    print(f"Player {player} rolls:")
    die.roll()
    print(die.show_side())

# Part 4
    
mammal1 = Mammal(ID=1, species="Bear", name="Buddy", size="Large", weight=200)
mammal2 = Mammal(ID=2, species="Cat", name="Luna", size="Small", weight=4)
mammal3 = Mammal(ID= 3, species="Wolf", name="Remus", size="Medium", weight=20)

mammals = [mammal1, mammal2, mammal3]

# Part 5

print("\nPart 5 starts\n")
player1.pet = mammal1
player2.pet = mammal2
print(player1, player1.pet)
print(player2, player2.pet)

# Part 6

small = None
medium = None
large = None

for animal in mammals:
    if animal.weight > 70:
        large = animal
    elif animal.weight > 15 and animal.weight < 70:
        medium = animal
    else:
        small = animal

for player in players.keys():
    green_die.roll()
    yellow_die.roll()
    print(f"{player.get_name()} rolls:")
    print(green_die.show_side())
    print(yellow_die.show_side())
    sum = green_die.show_side() + yellow_die.show_side()

    if sum < 5:
        player.pet = small
    elif sum > 4 and sum < 9:
        player.pet = medium
    else:
        player.pet = large

print(f"\n{player1}{player1.pet}")
print(f"\n{player2}{player2.pet}")

