import string

lines = open("aoc2022_day3_input.txt", "r").readlines()
#print(len(lines))

letters = list(string.ascii_letters)
#print(len(letters))
#testline = 'tJHJvLJVVttNsvTtTvgHHSVwCsQRQQZCZZMqQMQBnqBMQs\n'
#testline = testline[:-1]
#print(testline)

priority = 0
noLines = 0
groupMembers = 0
group = list();

for line in lines:
    line = line[:-1]
    numberOfLetters = len(line)
    if numberOfLetters % 2 != 0:
        print("ODD!")
    #print(numberOfLetters)
    middleIndex = numberOfLetters//2
    #print(middleIndex)
    lastIndex = numberOfLetters
    #print(lastIndex)
    #print(len(testline))
    firstPart = line[0:middleIndex]
    #print(len(firstPart))
    #print(firstPart)
    secondPart = line[middleIndex:lastIndex]
    #print(len(secondPart))
    #print(secondPart)
    
    if len(firstPart) != len(secondPart):
        print("Not the same!")
    
    found = False
    for letter in letters:
        if firstPart.find(letter) != -1 and secondPart.find(letter) != -1:
            #print(letter)
            priority = priority + letters.index(letter) + 1
            noLines = noLines + 1
            found = True
     
    if found == False:
        print(line)    
     
    #if groupMembers < 3:
    #    group.append(line)
    #    groupMembers = groupMembers + 1
    
    #if groupMembers == 3:
        
    
    
           
print(priority)
#print(noLines)


 