fhand = open('word.txt')

eng2jp = {}

with fhand as f:
  for line in f:
      key, value = line.split(":")
      eng2jp[key] = value


while True:
    inp = input('Enter a word in English: ')
    if inp == "done" : 
        break
    try:
        print(eng2jp[inp])
    except:
        print ('Not in Dictionary')
        continue