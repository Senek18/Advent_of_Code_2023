import re
input = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        input.append(line.rstrip())

print(input)

sum = 0

for i in input:
    temp = re.findall(r'\d', i)
    res = list(map(int, temp))
    print(res)

    if len(res) == 1:
        number = str(res[0]) + str(res[0])
        sum += int(number)
    else:
        number = str(res[0]) + str(res[-1])
        sum += int(number)
print(sum)