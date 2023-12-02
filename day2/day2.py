import re

input = []

colors_max = {"red": 12, "green": 13, "blue": 14}
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
        return False
    else:
        return True


for line in input:
    game_number = re.search(r'\d+', line)
    line = line.replace(str(game_number.group()) + ": ", "")
    set_list = line.split(";")
    count = 0

    for s in set_list:
        s = s.replace(",", "")
        s = s.split(" ")

        colors_count = {"red": 0, "green": 0, "blue": 0}
        colors_check = {"red": True, "green": True, "blue": True}

        for color in colors:
            try:
                colors_count[color] += int(s[s.index(color)-1])
                colors_check[color] = check_color(color, colors_max, colors_count[color])
            except ValueError:
                pass

        if False in colors_check.values():
            count +=1
            break

    if count < 1:
        total += int(game_number.group())


print(total)
