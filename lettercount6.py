
def count():
    word = input('Type any word: ')
    total = 0
    a = input('Which letter shall I count? ')

    for letter in word: 
        if letter == a:
            total = total + 1

    print(total)
    
count()
    
