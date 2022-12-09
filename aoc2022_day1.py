lines = open('aoc_day1_input.txt','r').readlines()

# print(type(lines))

calories = 0
elves = list()

for line in lines:
    if not line == "\n":
        calories = calories + int(line)
    elif line == "\n":
        elves.append(calories)
        calories = 0

print(max(elves))
print(elves.index(max(elves)))
elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])
