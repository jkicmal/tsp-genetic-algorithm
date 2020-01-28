import random


def mutatePopulation(population, mutationProbability):
    populationLength = len(population)
    specimenLength = len(population[0])

    for i in range(0, populationLength):
        if random.random() < mutationProbability:
            leftIndex = random.randint(0, specimenLength - 1)
            rightIndex = random.randint(0, specimenLength - 1)

            if leftIndex > rightIndex:
                leftIndex, rightIndex = rightIndex, leftIndex

            specimenGenesToReverse = population[i][leftIndex:rightIndex]
            specimenGenesToReverse.reverse()
            population[i] = population[i][:leftIndex] + specimenGenesToReverse + population[i][rightIndex:]
