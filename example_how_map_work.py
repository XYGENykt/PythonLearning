string = input("введите числа через пробел")

list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))

print(list_of_numbers)