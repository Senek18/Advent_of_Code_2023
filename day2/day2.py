import re

input = []

colors_max = {"red": 12, "green": 13, "blue": 14}
colors = ("red", "green", "blue")

with open("input1.txt", 'r') as file:
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

    for s in set_list:

        colors_count = {"red": 0, "green": 0, "blue": 0}
        colors_check = {"red": True, "green": True, "blue": True}
        for color in colors:
            for match in re.finditer(color, s):
                idx = match.start() - 4
                number = re.search(r'\d+', s[idx:])
                print(color, number)
                colors_count[color] += int(number.group())
            colors_check[color] = check_color(color, colors_max, colors_count[color])

        if False in colors_check.values():
            break

    total += int(game_number.group())


print(total)
