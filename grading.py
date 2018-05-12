grade = input('Enter score:')
try:
    g = float(grade)
except:
    print('Bad score value')    
    quit()
if g > 1.0:
    print('Bad score value')
elif g >= 0.9:
    print('Your score is an A')
elif g >= 0.8:
    print ('Your score is a B')
elif g >= 0.7:
    print ('Your score is a C')
elif g >= 0.6:
    print ('Your score is a D')
elif g <= 0.5:
    print ('Your score is an F')
else:
    print ('Bad score value')