fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
count = 0
total = 0
average = 0

for line in fhand:
   if line.startswith('X-DSPAM-Confidence:'):
        atpos = line.find(':')
        snum = line[atpos+1:].rstrip()
        num = float(snum)        
        total = total + num
        count = count + 1
        average = total / count

print ('Average spam confidence:', average, )
