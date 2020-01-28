def getPopulationFitness(distances, population):
    populationFitness = []

    for specimen in population:
        fitness = getSpecimenFitness(distances, specimen)
        populationFitness.append(fitness)

    return populationFitness


def getSpecimenFitness(distances, specimen):
    fitness = 0

    specimenSize = len(specimen)
    for i in range(specimenSize - 1):
        fitness += distances[specimen[i]][specimen[i+1]]
    fitness += distances[specimen[specimenSize - 1]][specimen[0]]

    return fitness
