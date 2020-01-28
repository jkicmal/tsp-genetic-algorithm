import random


def readDistancesFromFile(path):
    file = open(path)

    # Use splitlines to remove \n
    allLines = file.read().splitlines()

    # First line is a cities count
    citiesCount = int(allLines[0])

    # Initialize distances array
    distances = [[None for j in range(citiesCount)] for i in range(citiesCount)]

    # Rest lines are distances represented in format:
    # 0
    # 1 0
    # 5 3 0 etc
    distancesLines = allLines[1:]
    for i in range(citiesCount):
        values = distancesLines[i].strip().split(" ")
        for j in range(len(values)):
            value = int(values[j])
            distances[i][j] = value
            distances[j][i] = value

    return distances


def createInitialPopulation(populationSize, specimenSize):
    population = []

    for _ in range(populationSize):
        specimen = [i for i in range(specimenSize)]
        random.shuffle(specimen)
        population.append(specimen)

    return population
