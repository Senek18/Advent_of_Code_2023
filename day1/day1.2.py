import re
input = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        numbers = {"one":-1, "two":-1, "three":-1, "four":-1, "five":-1, "six":-1, "seven":-1, "eight":-1, "nine":-1}
        rnumbers = {"one": -1, "two": -1, "three": -1, "four": -1, "five": -1, "six": -1, "seven": -1, "eight": -1,
                   "nine": -1}
        numbers_swap = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                        "eight": "8", "nine": "9"}
        for key in numbers:
            if line.count(key) > 1:
                numbers[key] = line.find(key)
                rnumbers[key] = line.rfind(key)
            numbers[key] = line.find(key)

        numbers = sorted(numbers.items(), key=lambda x:x[1])
        rnumbers = sorted(rnumbers.items(), key=lambda x: x[1])
        count = 0
        for i in numbers:
            if i[1] == -1:
                continue
            line = line[:i[1]+count] + numbers_swap[i[0]] + line[i[1]+count:]
            count += 1

        for i in rnumbers:
            if i[1] == -1:
                continue
            line = line[:i[1]+count] + numbers_swap[i[0]] + line[i[1]+count:]
            count += 1

        input.append(line.rstrip())

print(input)

sum = 0
val = []

for i in input:
    temp = re.findall(r'\d', i)
    res = list(map(int, temp))
    print(res)

    if len(res) == 1:
        number = str(res[0]) + str(res[0])
        sum += int(number)
    else:
        number = str(res[0]) + str(res[-1])
        val.append(number)
        sum += int(number)
print(sum)

