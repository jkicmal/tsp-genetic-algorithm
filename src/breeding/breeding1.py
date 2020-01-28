import random


def breedNewPopulation(population, breedingProbability):
    newPopulation = []

    populationLength = len(population)
    specimenLength = len(population[0])

    for i in range(0, len(population), 2):
        if random.random() < breedingProbability:
            crossPointL = random.randint(0, specimenLength - 1)
            crossPointR = random.randint(0, specimenLength - 1)

            if crossPointR < crossPointL:
                crossPointR, crossPointL = crossPointL, crossPointR

            childA, childB = crossSpecimens(population[i], population[i+1], crossPointL, crossPointR)

            newPopulation.append(childA)
            newPopulation.append(childB)
        else:
            newPopulation.append(population[i][:])
            newPopulation.append(population[i+1][:])

    return newPopulation


def crossSpecimens(parentA, parentB, crossPointL, crossPointR):
    childA = [None for i in range(0, crossPointL)] + parentA[crossPointL:crossPointR] + [None for i in range(crossPointR, len(parentA))]
    childB = [None for i in range(0, crossPointL)] + parentB[crossPointL:crossPointR] + [None for i in range(crossPointR, len(parentA))]

    specimenLength = len(parentA)

    crossGenes(parentA, childB, crossPointL, crossPointR, 0, crossPointL)
    crossGenes(parentA, childB, crossPointL, crossPointR, crossPointR, specimenLength)

    crossGenes(parentB, childA, crossPointL, crossPointR, 0, crossPointL)
    crossGenes(parentB, childA, crossPointL, crossPointR, crossPointR, specimenLength)

    return childA, childB


def crossGenes(parent, child, crossPointL, crossPointR, indexFrom, indexTo):
    for i in range(indexFrom, indexTo):
        gene = parent[i]
        while gene in child[crossPointL:crossPointR]:
            gene = parent[child.index(gene)]
        child[i] = gene
