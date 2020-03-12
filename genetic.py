import numpy as np
import random
from copy import deepcopy

def generate_map(map, developers, menagers):
    new_data = []
    used_devs = []
    used_mens = []
    for i in range(len(map)):
        new_line = []
        for j in range(len(map[i])):
            if map[i][j] != '#':
                if map[i][j] == '_':
                    while True:
                        new_developer = random.randint(0, len(developers) - 1)
                        if new_developer not in used_devs:
                            new_line.append(new_developer)
                            used_devs.append(new_developer)
                            break
                elif map[i][j] == 'M':
                    while True:
                        new_menager = random.randint(0, len(menagers) - 1)
                        if new_menager not in used_mens:
                            new_line.append(new_menager)
                            used_mens.append(new_menager)
                            break
            else:
                new_line.append(-1)
        new_data.append(deepcopy(new_line))
        del new_line
    return np.array(new_data)


def crossover(map, parent1, parent2): 
    # function responsible for crossover between parents

    # first we copy parents to separate list to avoid problems with references
    copied1 = deepcopy(parent1)
    copied2 = deepcopy(parent2)

    # next we create lists for used developers and menagers
    used_devs = []
    used_mens = []

    #next we create our new dude
    new_baby = []
    for i in range(len(copied1)):

        #we need new line
        new_line = []
        for j in range(len(copied1[i])):
            
            # if place is usable choose gene
            if map[i][j] != '#':
                if np.random.uniform(0,1) < 0.5: 
                    if (map[i][j] == '_' and copied1[i][j] not in used_devs):
                        used_devs.append(copied1[i][j])
                        new_line.append(copied1[i][j])
                    elif (map[i][j] == 'M' and copied1[i][j] not in used_mens):
                        new_line.append(copied1[i][j])
                        used_mens.append(copied1[i][j])
                    elif (map[i][j] == 'M' and copied1[i][j] in used_mens):
                        used_mens.append(copied2[i][j])
                        new_line.append(copied2[i][j])
                    elif (map[i][j] == '_' and copied1[i][j] in used_devs):
                        used_devs.append(copied2[i][j])
                        new_line.append(copied2[i][j])
                else:
                    if (map[i][j] == '_' and copied2[i][j] not in used_devs):
                        used_devs.append(copied2[i][j])
                        new_line.append(copied2[i][j])
                    elif (map[i][j] == 'M' and copied2[i][j] not in used_mens):
                        new_line.append(copied2[i][j])
                        used_mens.append(copied2[i][j])
                    elif (map[i][j] == 'M' and copied2[i][j] in used_mens):
                        used_mens.append(copied1[i][j])
                        new_line.append(copied1[i][j])
                    elif (map[i][j] == '_' and copied2[i][j] in used_devs):
                        used_devs.append(copied1[i][j])
                        new_line.append(copied1[i][j])
            # else append -1
            else:
                new_line.append(-1)
        new_baby.append(np.array(new_line))
        del new_line
        
    # return new baby
    return np.array(new_baby)