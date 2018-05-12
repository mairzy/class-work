fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in fhand:
    words = line.split()
    if (len(words) == 0 or words[0] != 'From'): continue
    counts[words[1]] = (counts.get(words[1], 0) + 1) 

first = list()

for key, val in list (counts.items()):
    first.append((val, key))

first.sort(reverse = True)

for key, val in first[:1]:
    print(key, val)
    

