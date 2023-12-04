import re
input = []

with open("input1.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        input.append(line.rstrip())
        print(line)

input_lenght = len(input) - 1


def check_digit(line_idx, number_idx, lenght, input_lenght):
    pattern = r'[!@#$%^&*()_+\-=\[\]{};\':\"\\|,<>\/?]'
    if number_idx == 0:
        start_idx = number_idx
    else:
        start_idx = number_idx - 1

    end_index = number_idx + lenght

    symbols = []

    if line_idx == 0:
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx])])
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx+1])])
    elif line_idx == input_lenght:
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx])])
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx - 1])])
    else:
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx-1])])
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx])])
        symbols.append([m.start(0) for m in re.finditer(pattern, input[line_idx+1])])

    for i in symbols:
        for j in i:
            check = (j in range(start_idx, end_index+1))
            if check:
                return check

    return False


total = 0

for idx, line in enumerate(input):
    digits = re.findall(r'\d+', line)
    for n in digits:
        number_idx = line.find(n)
        check = check_digit(idx, number_idx,len(n),input_lenght)
        if check:
            total += int(n)
print(total)