import numpy as np

file = open('file.txt', 'r')
lines = file.readlines()

size = lines[0].split(' ')
map_t = lines[1:size[1]]

dev_list = lines[size[1]:]
dev_list = [line.split(' ') for line in dev_list]

"""

dev_list looks like -> [<company_name>, <bonus amount>, <skills amount>, <skills>, ...]

"""

print(size)
print(map_t)
