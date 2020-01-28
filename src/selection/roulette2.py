import random


def select(population, populationScores, x, selectionProbability):
    newPopulation = []

    populationLength = len(population)

    maxScore = max(populationScores) + 1

    rouletteScores = []
    for i in range(populationLength):
        rouletteScores.append(maxScore - populationScores[i])

    rouletteScoresSum = sum(rouletteScores)

    for i in range(populationLength):
        randomSum = random.randint(1, maxScore)
        tempSum = 1
        specimenToAddIndex = 0

        while tempSum <= randomSum:
            tempSum += rouletteScores[specimenToAddIndex]
            specimenToAddIndex += 1

        newPopulation.append(population[specimenToAddIndex - 1][:])

    return newPopulation


def prepareScores(populationScores):
    preparedScores = []
