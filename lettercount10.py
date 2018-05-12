import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = 0
lettercounts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts +=1
            if letter not in lettercounts:
                lettercounts[letter] = 1
            else:
                lettercounts[letter] += 1

first = list()
for key, val in list(lettercounts.items()):
    first.append((val, key))

first.sort(reverse = True)

for key, val in first:
    print(key, val)