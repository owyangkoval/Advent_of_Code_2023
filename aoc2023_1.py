f = open("/Users/angelaowyang/Desktop/Coding/Advent_of_Code_2023/inputs/input.txt")
lines = f.readlines()
ulti_sum = 0

for char in lines:
    list = []
    for val in char:
        if val.isdigit():
            list.append(val)
    first = list[0]
    last = list[len(list)-1]
    sum = first + last
    ulti_sum += int(sum)
    print(ulti_sum)
