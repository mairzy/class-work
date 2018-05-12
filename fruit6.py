index = 0
fruit = input('Type fruit name:')

while index > (0 - len(fruit)):
    letter = fruit[index - 1]
    print(letter)
    index = index - 1