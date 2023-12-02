import re

input = []


colors = ("red", "green", "blue")

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        line = line.replace("Game ", "")
        input.append(line.rstrip())

total = 0


def check_color(color, max_dict, count):
    if count > max_dict[color]:
        return count
    else:
        return max_dict[color]


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


for line in input:
    game_number = re.search(r'\d+', line)
    line = line.replace(str(game_number.group()) + ": ", "")
    set_list = line.split(";")
    count = 0
    colors_max = {"red": 0, "green": 0, "blue": 0}
    for s in set_list:
        s = s.replace(",", "")
        s = s.split(" ")

        colors_count = {"red": 0, "green": 0, "blue": 0}


        for color in colors:
            try:
                colors_count[color] += int(s[s.index(color)-1])
                colors_max[color] = check_color(color, colors_max, colors_count[color])
            except ValueError:
                pass

    total += multiplyList(list(colors_max.values()))

print(total)

