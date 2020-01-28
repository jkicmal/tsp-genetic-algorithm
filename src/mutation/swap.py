import random


def mutatePopulation(population, mutationProbability):
    populationLength = len(population)
    specimenLength = len(population[0])

    for i in range(0, populationLength):
        if random.random() < mutationProbability:
            firstGeneToSwap = random.randint(0, specimenLength - 1)
            secondGeneToSwap = random.randint(0, specimenLength - 1)

            population[i][firstGeneToSwap], population[i][secondGeneToSwap] = population[i][secondGeneToSwap], population[i][firstGeneToSwap]
