import random


def crossSpecimens(parentA, parentB):
    specimenSize = len(parentA)

    leftIndex = random.randint(0, specimenSize - 1)
    rightIndex = random.randint(0, specimenSize - 1)

    if leftIndex > rightIndex:
        leftIndex, rightIndex = rightIndex, leftIndex

    parentBCenter = parentB[leftIndex:rightIndex]

    child = parentBCenter + [el for el in parentA[:] if el not in parentBCenter]

    return child


def breedNewPopulation(population, breedingProbability):
    populationAfterBreeding = []

    for i in range(0, len(population), 2):
        if random.random() < breedingProbability:
            # indexOfSpecimenToBreedWith = random.randint(0, len(population) - 1)
            populationAfterBreeding.append(crossSpecimens(population[i][:], population[i+1][:]))
            populationAfterBreeding.append(crossSpecimens(population[i+1][:], population[i][:]))
        else:
            populationAfterBreeding.append(population[i][:])
            populationAfterBreeding.append(population[i+1][:])

    return populationAfterBreeding
