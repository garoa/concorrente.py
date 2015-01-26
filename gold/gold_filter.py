

# 10.000 simulated gold prices aproximating historical trends from 1973 to 2013

from random import randrange

with open('gold_prices2.txt', encoding='utf-8') as fp:
    lines = fp.readlines()
    while len(lines) > 10000:
        del lines[randrange(len(lines))]

for line in lines:
    print(line.strip())
