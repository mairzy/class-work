fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = dict()

for line in fhand:
    words = line.split()
    if (len(words) == 0 or words[0] != 'From'): continue
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos+1:]
        if domain not in count:
            count[domain] = 1
        else:
            count[domain] += 1 
    
print(count)
