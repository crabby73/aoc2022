
rps_combinations_1 = {
    "A X\n": 4,
    "A Y\n": 8,
    "A Z\n": 3,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 7,
    "C Y\n": 2,
    "C Z\n": 6
}

rps_combinations_2 = {
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7
}


lines = open("aoc2022_day2_input.txt","r").readlines()
result_1 = 0
result_2 = 0
for line in lines:
    result_1 = result_1 + rps_combinations_1[line]
    result_2 = result_2 + rps_combinations_2[line]
    
print(result_1)
print(result_2)