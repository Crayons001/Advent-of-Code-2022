myfile = open("F:\ManuC\strategy_guide.txt", "r");
points = 0
total = 0

# Dictionary that dictates the points gained depending on the shape selected
points_dict = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

lines = myfile.readlines()
for line in lines:
    line = line.replace("\n", "")
    if line == "A Y" or line == "B Z" or line == "C X":     # winning combinations
        points = 6
    elif line == "A X" or line == "B Y" or line == "C Z":   # drawing combinations
        points = 3
    else:                                                   # losing combinations
        points = 0

    shape_score = points_dict[line[2]]
    total += points + shape_score

print(f"The total score is {total}")