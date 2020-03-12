import numpy as np


def get_numbers(lines):
    
    dev_number = None # nr line containing nimber of developers
    dev_start = None # nr line containing developers strings
    men_number = None # nr line containing number of menagers
    men_start = None # as in 2
    size = None # list [x, y]
    
    
    size = lines[0].split(' ')
    size[1] = size[1].replace('\n', '')
    size = [int(x) for x in size]
    dev_number = size[1] + 1
    dev_start = dev_number + 1
    men_number = dev_start + int(lines[dev_number])
    men_start = men_number + 1

    return size, dev_number, dev_start, men_number, men_start
    

file = open('a_solar.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
size, dev_number, dev_start, men_number, men_start = get_numbers(lines)
map_t = lines[1:size[1] + 1]
developers = lines[dev_start:men_number]
menagers = lines[men_start:]


