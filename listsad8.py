fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
        print('File cannot be opened:', fname)
        exit()
count = 0
for line in fhand:
    words = line.split()
    if (len(words) == 0 or words[0] != 'From'): continue
    count = count + 1
    print(words[1])
    
print('There were', count, 'lines in the file with From as the first word.')
    