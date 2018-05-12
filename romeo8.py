fhand = open('romeo.txt')

script = list()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        newword = word.lower()
        script.append(newword)
        
print(sorted(script))