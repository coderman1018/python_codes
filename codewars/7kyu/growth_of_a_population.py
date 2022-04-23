import math
def nb_year(population, percent, arrival, maximum):
    x = 0
    while population<maximum:
        population = math.floor(population+(population*(percent/100))+arrival)
        x+=1
    return x
