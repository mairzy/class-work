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
    else:
        colpos = words[5].find(':')
        time = words[5][:colpos+0]
        if time not in counts:
            counts[time] = 1
        else:
            counts[time] += 1 

first = list()

for key, val in list (counts.items()):
    first.append((val, key))

first.sort()

for key, val in first:
    print(key, val)
    
