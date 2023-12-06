import re
import numpy as np
input = []

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        input.append(line.rstrip())

data = {
0: [],
1: [],
2: [],
3: [],
4: [],
5: [],
6: [],
7: [],
}
idx = 0

for i in input:
    if i == '':
        idx += 1
        continue
    temp = re.findall(r'\d+', i)
    l = list(map(int, temp))
    if len(l) > 0:
        data[idx].append(l)

seeds = data[0][0]
new_seeds = []
for jdx, j in enumerate(seeds):
    if jdx % 2 == 0:
        new_seeds = new_seeds + [*range(j, j+seeds[jdx+1], 1)]
print(new_seeds)


def map_to(sources, destinations):
    new_sources = []
    for idx, source in enumerate(sources):
        for destination in destinations:
            if source in range(destination[1], destination[1]+destination[2]):
                new_sources.append(destination[0] - destination[1] + source)
                break
        if len(new_sources) != idx + 1:
            new_sources.append(source)
    return new_sources


soils = map_to(new_seeds, data[1])
fertilizer = map_to(soils, data[2])
water = map_to(fertilizer, data[3])
light = map_to(water, data[4])
temperature = map_to(light, data[5])
humidity = map_to(temperature, data[6])
location = map_to(humidity, data[7])
print(np.min(location))