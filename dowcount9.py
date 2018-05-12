fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
        print('File cannot be opened:', fname)
        exit()
count = {}
for line in fhand:
    words = line.split()
    if (len(words) == 0 or words[0] != 'From'): continue
    count[words[2]] = (count.get(words[2], 0) + 1) 
    
print(count)


        