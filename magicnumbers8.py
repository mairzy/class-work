
num = None
numlist = list()

while True:
    inp = input('Enter a number: ')
    if inp == "done" : 
        break
    try:
        num = float(inp)
        numlist.append(num)
    except:
        print ('Invalid input')
        continue
              
        
print ('Maximum is ', max(numlist))
print ('Minimum is ', min(numlist))
