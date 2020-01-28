import random


def select(population, populationScores, x, selectionProbability):
    maxScore = max(populationScores) + 1

    preparedScores = []
    for i in range(len(populationScores)):
        preparedScores.append(maxScore - populationScores[i])

    scoresSum = sum(preparedScores)

    outputPopulation = []
    indexes = []
    for i in range(len(population)):
        randomSum = random.randint(1, scoresSum - 1)

        tempSpecimenIndex = 0
        tempScoresSum = 1

        while randomSum >= tempScoresSum:
            tempScoresSum += preparedScores[tempSpecimenIndex]
            tempSpecimenIndex += 1

        outputPopulation.append(population[tempSpecimenIndex - 1][:])
        indexes.append(tempSpecimenIndex - 1)

    indexes.sort()
    return outputPopulation
