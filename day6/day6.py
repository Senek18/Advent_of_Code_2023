import re
import numpy as np
input = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        line = line.split(": ")[1]

        input.append(line.rstrip())

print(input)


time = input[0]
temp = re.findall(r'\d+', time)
time = list(map(int, temp))
final_time = ""
for i in time:
    final_time += str(i)
final_time = int(final_time)

distance = input[1]
temp = re.findall(r'\d+', distance)
distance = list(map(int, temp))
final_distance = ""
for i in distance:
    final_distance += str(i)
final_distance = int(final_distance)

record = [0] * len(time)

for idx, _ in enumerate(time):
    velocity = 0

    for i in range(0, time[idx]+1):
        travel = velocity * (time[idx]-velocity)
        if travel > distance[idx]:
            record[idx] += 2
        velocity += 1

if True:
    velocity = 0
    final_record = 0
    for i in range(0, final_time+1):
        travel = velocity * (final_time-velocity)
        if travel > final_distance:
            final_record += 1
        velocity += 1

print(np.prod(record))
print(final_record)