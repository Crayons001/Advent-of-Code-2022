# THIS IS THE SOLUTION FOR PART TWO

myfile = open("F:\ManuC\strategy_guide.txt", "r");
points = 0
total = 0

# Dictionary that dictates the points gained depending on the shape selected
points_dict = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

lines = myfile.readlines()
my_shape = " "  # Holds the shape that you play

for line in lines:
    line = line.replace("\n", "")   # Removing new line characters to make it easier to compare strings
    # Determining shape you are supposed to play depending on the strategy guide
    if line == "A Y" or line == "B X" or line == "C Z":
        my_shape = "A"
    elif line == "A Z" or line == "B Y" or line == "C X":
        my_shape = "B"
    else:
        my_shape = "C"

    # Determining score based on whether round is won, lost or drawn
    if line[2] == "Z":
        points = 6
    elif line[2] == "Y":
        points = 3
    else:
        points = 0

    shape_score = points_dict[my_shape]
    total += points + shape_score

print(f"The total score is {total}")




