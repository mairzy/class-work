hours = input('Enter hours:')
try:
    h = int(hours)
except:
    print('Error: please enter a numeric input')    
    quit()
rate = input('Enter rate:')
try:
    r = float(rate)
except:
    print('Error: please enter a numeric input')
    quit()
if h > 40:
        pay = (h - 40) * (r * 1.5) + (40 * r)
        print(pay)
else:
        def computepay():
            pay = h * r
            print(pay)
        
        computepay()