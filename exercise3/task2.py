class  NumberStats:
    def __init__(self):
        #no need to add any new varibales here, just change the
        #initialization of the self.numbers variable.
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(int(number))

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        sum = 0

        for num in self.numbers:
            sum += num

        return sum

    def average(self):
        if len(self.numbers):
            return self.get_sum() / len(self.numbers)
        else:
            return 0

if __name__ == "__main__":
    #Part 1 test prints:
    stats = NumberStats()
    """stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    #Part 2 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average()) """

def main():

    stats_all = NumberStats()
    stats_even = NumberStats()
    stats_odd = NumberStats()

    while True:

        number = input("Please type integer numbers: ")

        if number == "-1":
            break
        elif int(number) % 2 == 0:
            stats_even.add_number(number)
        else:
            stats_odd.add_number(number)

        stats_all.add_number(number)

    print("Numbers added:", stats_all.count_numbers())
    print("Sum of numbers:", stats_all.get_sum())
    print("Mean of numbers:", stats_all.average())
    print("Sum of even numbers:", stats_even.get_sum())
    print("Sum of odd numbers:", stats_odd.get_sum())

main()