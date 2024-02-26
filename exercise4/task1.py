class ListHelper:

    def greatest_frequency(my_list: list):
        most_items = 0
        most_common_item = None

        for item in my_list:
            comparison = 0
            for j in my_list:
                if item == j:
                    comparison += 1
            if comparison > most_items:
                most_items = comparison
                most_common_item = item

        return most_common_item


    def doubles(my_list: list):
        doubles = set()

        for item in my_list:
            number_of_items = 0
            for j in my_list:
                if item == j:
                    number_of_items += 1
            if number_of_items > 1:
                doubles.add(item)

        return len(doubles)

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))