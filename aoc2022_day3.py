import string

lines = open("aoc2022_day3_input.txt", "r").readlines()
letters = list(string.ascii_letters)

def solvePartOne(lines, letters):
    priority = 0

    for line in lines:
        line = line[:-1]
        numberOfLetters = len(line)

        if numberOfLetters % 2 != 0:
            print("ODD!")

        middleIndex = numberOfLetters//2
        lastIndex = numberOfLetters
        firstPart = line[0:middleIndex]
        secondPart = line[middleIndex:lastIndex]
        
        if len(firstPart) != len(secondPart):
            print("Not the same!")
        
        found = False
        for letter in letters:
            if firstPart.find(letter) != -1 and secondPart.find(letter) != -1:
                priority = priority + letters.index(letter) + 1
                    
    return priority  

def solvePartTwo(lines, letters):
    group = [0, 0, 0]
    groupMembers = 0
    priority = 0
    
    for line in lines:
        line = line[:-1]
        if groupMembers < 3:
            group[groupMembers] = line
            groupMembers = groupMembers + 1
    
        if groupMembers == 3:
            groupMembers = 0
            for letter in letters:
                groupMemberOneLetter = group[0].find(letter)
                groupMemberTwoLetter = group[1].find(letter)
                groupMemberThreeLetter = group[2].find(letter)
                
                if groupMemberOneLetter != -1 and \
                   groupMemberTwoLetter != -1 and \
                   groupMemberThreeLetter != -1:
                       priority = priority + letters.index(letter) + 1
            
    return priority

resultPartOne = solvePartOne(lines, letters)
print(resultPartOne)
resultPartTwo = solvePartTwo(lines, letters)
print(resultPartTwo)


 