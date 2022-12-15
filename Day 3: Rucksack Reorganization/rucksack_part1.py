# Function that calculates priority using ASCII values of the letters
def priority_calc(item):
    value = ord(item)       # Storing the ASCII value of item in variable 'value'
    if(value>=97):
        value -= 96
    else:
        value -= 38

    return value

# Determining the item (letter) that has been repeated
# Think of a 'rucksack' simply as a single line on the puzzle input file ('_rucksack.txt')
def compare(rucksack):
    range_size = int(len(rucksack)/2)
    for i in range(0, range_size):      # Goes through the first half of the line
        for j in range(range_size, range_size*2):       # Goes through the second half of the line
            if(rucksack[i]==rucksack[j]):
                common_item = rucksack[i]

    return common_item

myfile = open("F:\ManuC\_rucksack.txt", "r")
lines = myfile.readlines()
sum = 0     # Stores the sum of the priorities of the repeated letters in each line

for line in lines:
    line = line.replace("\n", "")
    common_item = compare(line)
    sum += priority_calc(common_item)

print(sum)
