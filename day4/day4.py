import re
input = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        line = line.split(": ")[1]

        input.append(line.rstrip())

print(len(input))
lst = [0] * len(input)
print(lst)

total = 0

for idx, game in enumerate(input):
    win_numbers = game.split(" | ")[0]
    temp = re.findall(r'\d+', win_numbers)
    win_numbers = list(map(int, temp))
    numbers = game.split(" | ")[1]
    temp = re.findall(r'\d+', numbers)
    numbers = list(map(int, temp))

    win_point = 0
    win_count = 0

    for i in numbers:
        if i in win_numbers:
            if win_count == 0:
                win_point = 1
                win_count += 1
            else:
                win_point = win_point * 2
                win_count += 1

    check = lst[idx]
    lst[idx] += 1
    while win_count > 0:
        idx += 1
        lst[idx] += 1 + check
        win_count -= 1

    total += win_point

print(lst)

print(sum(lst))

print(total)

