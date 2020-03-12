import numpy as np
import copy
import random
from copy import deepcopy



# Krzysztof
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

# Krzysztof Koniec

# Arek + Mateusz
def fitness(board):
    totalTotalpotential = 0
    for rowInd,row in enumerate(board):
        for placeInd, place in enumerate(row):
            if place.kind == '#':
                #print('dupa #')
                pass
            elif(place.kind == 'M'):
                #print('dupa m')
                ##creating submatrix
                submatrix = test_slice(board,rowInd,placeInd,len(row),len(board))
                ## skills update for given cell
                bonusPotential = 0
                workPotential = 0
                for rowsub in submatrix:
                    for placesub in rowsub:
                        if(placesub == place):
                            pass
                        else:
                            if placesub.company == place.company:
                                bonusPotential += placesub.potential*(place.potential)
                place.workPotential = 0
                place.bonusPotential = bonusPotential
                totalTotalpotential += (workPotential + bonusPotential)         
            elif(place.kind == "_"):
                #print('dupa _')
                ##creating submatrix
                submatrix = test_slice(board,rowInd,placeInd,len(row),len(board))
                ## skills update for given cell
                bonusPotential = 0
                workPotential = 0
                for rowsub in submatrix:
                    for placesub in rowsub:
                        if(placesub == place):
                            pass
                        
                        else:
                            if placesub.company == place.company:
                                bonusPotential += placesub.potential*(place.potential)
                            if placesub.kind == '_':
                                skill_sum = place.skills + placesub.skills
                                skill_sum = list( dict.fromkeys(skill_sum))
                                skill_difference  = [x for x in skill_sum if x not in place.skills]
                                workPotential += len(skill_difference) * (len(skill_sum) - len(skill_difference))

                place.workPotential = workPotential
                place.bonusPotential = bonusPotential
                totalTotalpotential += (workPotential + bonusPotential)
            else:
                print("we are screwed")
    return totalTotalpotential


def test_slice(m,i,j,max_x,max_y):
    sliceOfMatrix = [[m[a][b] for b in range(max(j-1,0), min((j + 2),max_x))] for a in range(max(i-1,0), min((i + 2),max_y))]
    return sliceOfMatrix





class worker():
    def __init__(self,kind,company,bonusPoints, skills):
        self.kind = kind
        self.company = company
        # self.bonusPoints = bonusPoints
        self.skills = skills
        self.potential = 0
        self.workPotential = 0
        self.bonusPotential = bonusPoints
# AREK + Mateusz KONIEC

# Damian + Mateusz

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
    

file = open(input('give me the name of the file + .txt'), 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
size, dev_number, dev_start, men_number, men_start = get_numbers(lines)
map_t = lines[1:size[1] + 1]
developers = lines[dev_start:men_number]
menagers = lines[men_start:]
workers = []
dev_number = int(lines[dev_number])
men_number = int(lines[men_number])

def create_dev_from_string(string):
    developer = string.split(' ')
    dev_comp = developer[0]
    dev_bonus = developer[1]
    dev_skills = developer[3:]
    return worker('_',dev_comp, dev_bonus, dev_skills)

def create_men_from_string(string):
    developer = string.split(' ')
    men_comp = developer[0]
    men_bonus = developer[1]
    return worker('M', men_comp, men_bonus, [])

###

def get_results(original_map, mapa):

    used_menagers = []
    used_menagers_coords = []
    used_developers = []
    used_developers_coords = []

    output = []
    original_map = np.array(original_map)
    
    for i in range(size[1]):
        for j in range(size[0]):
            if mapa[i][j] != -1:
                if original_map[i][j] == '_':
                    used_developers.append(int(mapa[i][j]))
                    used_developers_coords.append([j, i])
                else:
                    used_menagers.append(int(mapa[i][j]))
                    used_menagers_coords.append([j, i])
    k = 0
    for i in range(dev_number):
        if i in used_developers:
            output.append("{} {}".format(str(used_developers_coords[k][0]), str(used_developers_coords[k][1])))
            k+=1
        else:
            output.append('X')
    k = 0
    for i in range(men_number):
        if i in used_menagers:
            output.append("{} {}".format(str(used_menagers_coords[k][0]), str(used_menagers_coords[k][1])))
            k+=1
        else:
            output.append('X')
    
    return '\n'.join(output)

mapa = np.array(map_t)

#Damian + Mateusz Koniec

# Krzysztof ALGORYTM GENETYCZNY

POPULATION_SIZE = 50
POPULATION_MULTIPLIER = 5
ITERATIONS = 10

population = []
for _ in range(POPULATION_SIZE):
    population.append(generate_map(mapa, developers, menagers))


def get_map_of_workers(map, numeric_map):
    map_of_workers = []
    for i in range(len(numeric_map)):
        new_line = []
        for j in range(len(numeric_map[i])):
            if map[i][j] == '#':
                new_line.append(worker('#', 0, 0, 0))
            elif map[i][j] == '_':
                new_line.append(create_dev_from_string(developers[numeric_map[i][j]]))
            elif map[i][j] == 'M':
                new_line.append(create_men_from_string(menagers[numeric_map[i][j]]))
        map_of_workers.append(copy.deepcopy(new_line))
        del new_line
    return map_of_workers




for iteration in range(ITERATIONS):
    new_population = []
    for _ in range(POPULATION_SIZE * (POPULATION_MULTIPLIER - 1)):
        parent1 = population[np.random.choice(range(len(population)))]
        parent2 = population[np.random.choice(range(len(population)))]
        new_baby = crossover(mapa, parent1, parent2)

        new_population.append([copy.deepcopy(new_baby), fitness(get_map_of_workers(mapa, new_baby))])
    for parent in population:
        new_population.append([copy.deepcopy(parent), fitness(get_map_of_workers(mapa, new_baby))])

    sorted_population = [copy.deepcopy(mapa_[0]) for mapa_ in sorted(new_population, key = lambda x: x[1], reverse = True)]
    del population
    del new_population
    population = sorted_population[:POPULATION_SIZE]
    print(iteration, fitness( get_map_of_workers(mapa, population[0])))
    #if input('continue? [y]/n') != 'n':
    #    continue
    #else:
    #    break
print(get_results(mapa , population[0]))

# Krzysztof Koniec






