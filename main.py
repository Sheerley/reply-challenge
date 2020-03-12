import numpy as np
import copy
import fitness as fit
import genetic as genlib

class worker():
    def __init__(self,kind,company,bonusPoints, skills):
        self.kind = kind
        self.company = company
        # self.bonusPoints = bonusPoints
        self.skills = skills
        self.potential = 0
        self.workPotential = 0
        self.bonusPotential = bonusPoints


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

workers = []


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

mapa = np.array(map_t)
print(mapa)

POPULATION_SIZE = 50
POPULATION_MULTIPLIER = 10
ITERATIONS = 50

population = []
for _ in range(POPULATION_SIZE):
    population.append(genlib.generate_map(mapa, developers, menagers))

print(population[30])


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



# genetic algorithm
#for iteration in range(ITERATIONS):
#    new_population = []
#    for _ in range(POPULATION_SIZE * (POPULATION_MULTIPLIER - 1)):
#        parent1 = population[np.random.choice(range(len(population)))]
#        parent2 = population[np.random.choice(range(len(population)))]
#        new_baby = genlib.crossover(mapa, parent1, parent2)

#        new_population.append([copy.deepcopy(new_baby), fit.fitness(get_map_of_workers(mapa, new_baby))])
#    for parent in population:
#        new_population.append([copy.deepcopy(parent), fit.fitness(get_map_of_workers(mapa, new_baby))])

#    sorted_population = [copy.deepcopy(mapa_[0]) for mapa_ in sorted(new_population, key = lambda x: x[1], reverse = True)]
#    del population
#    del new_population
#    population = sorted_population[:POPULATION_SIZE]
#    #print(iteration, fit.fitness(get_map_of_workers(mapa, population[-1])), population[-1])

dobry = [[-1, -1, -1, -1, -1], [-1, 4, -1, -1, 7], [-1, 2, 0, 2, 0]]

num_map = get_map_of_workers(mapa, dobry)
print(fit.fitness(num_map))
