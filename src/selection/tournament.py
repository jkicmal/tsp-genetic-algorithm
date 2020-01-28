import random


def select(population, populationFitness, tournamentSize, selectionProbability):
    populationAfterSelection = []

    populationSize = len(population)

    for specimen in population:
        if random.random() < selectionProbability:
            bestSpecimenIndex = random.randint(0, populationSize - 1)
            for _ in range(tournamentSize):
                randomSpecimenIndex = random.randint(0, populationSize - 1)
                if populationFitness[bestSpecimenIndex] > populationFitness[randomSpecimenIndex]:
                    bestSpecimenIndex = randomSpecimenIndex
            populationAfterSelection.append(population[bestSpecimenIndex][:])
        else:
            populationAfterSelection.append(specimen[:])

    return populationAfterSelection
