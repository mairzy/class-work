fname = ('mbox-short.txt')
try:
    fhand = open(fname)
except:
    print('File not found:," fname)
    quit()

count = 0
try:
    for line in fhand:
        words = line.split()
        # print 'Debug:', words
        if (len(words) == 0 or words[0] != 'From'): continue
        print(words[2])
except:
    print("File:", fname, "contains no data.")
    quit()

