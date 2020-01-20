import random
import os
import timeit


def clear(): return os.system("cls")


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


def cross(parentA, parentB):
    specimenSize = len(parentA)

    leftIndex = random.randint(0, specimenSize - 1)
    rightIndex = random.randint(0, specimenSize - 1)

    if leftIndex > rightIndex:
        leftIndex, rightIndex = rightIndex, leftIndex

    parentBCenter = parentB[leftIndex:rightIndex]

    child = parentBCenter + [el for el in parentA[:] if el not in parentBCenter]

    return child


def breed(population, breedingProbability):
    populationAfterBreeding = []

    for i in range(0, len(population), 1):
        if random.random() < breedingProbability:
            indexOfSpecimenToBreedWith = random.randint(0, len(population) - 1)
            populationAfterBreeding.append(cross(population[i][:], population[indexOfSpecimenToBreedWith][:]))
        else:
            populationAfterBreeding.append(population[i][:])

    return populationAfterBreeding


def mutate(population, mutationProbability):
    populationAfterMutation = []

    for specimen in population:
        if random.random() < mutationProbability:
            mutatedSpecimen = specimen[:]

            # Reverse Mutation
            leftIndex = random.randint(0, len(specimen) - 1)
            rightIndex = random.randint(0, len(specimen) - 1)

            if leftIndex > rightIndex:
                leftIndex, rightIndex = rightIndex, leftIndex

            cuttedGenes = mutatedSpecimen[leftIndex:rightIndex]
            cuttedGenes.reverse()
            mutatedSpecimen = mutatedSpecimen[:leftIndex] + cuttedGenes + mutatedSpecimen[rightIndex:]

            # Swap Mutation
            # randomIndex = random.randint(0, len(specimen) - 1)
            # indexToSwapWith = random.randint(0, len(specimen) - 1)
            # mutatedSpecimen[randomIndex], mutatedSpecimen[indexToSwapWith] = mutatedSpecimen[indexToSwapWith], mutatedSpecimen[randomIndex]

            populationAfterMutation.append(mutatedSpecimen)
        else:
            populationAfterMutation.append(specimen[:])

    return populationAfterMutation


def validatePopulation(population):
    validSpecimen = [i for i in range(len(population[0]))]
    # print(validSpecimen)

    for specimen in population:
        specimenToCompare = specimen[:]
        specimenToCompare.sort()
        for i in range(len(specimen)):
            if specimenToCompare[i] != validSpecimen[i]:
                return False

    return True


def run(graphPath, populationSize, iterations, tournamentSize, selectionProbability, breedingProbability, mutationProbability):
    distances = readDistancesFromFile(graphPath)
    population = createInitialPopulation(populationSize, specimenSize=len(distances))

    timeStart = timeit.default_timer()

    bestFitness = float("inf")

    timeSelection = 0
    timeBreeding = 0
    timeMutation = 0

    for i in range(iterations):
        
        timeBeforeFitness = timeit.default_timer()
        populationFitness = getPopulationFitness(distances, population)
        timeFitness = (timeit.default_timer() - timeBeforeFitness)


        bestFitnessInGeneration = min(populationFitness)
        if bestFitness > bestFitnessInGeneration:
            bestFitness = bestFitnessInGeneration
            bestFitnessInGenerationIndex = populationFitness.index(bestFitnessInGeneration)
            print("\nBEST FITNESS: ", bestFitness)
            # print("SPECIMEN: ", population[bestFitnessInGenerationIndex])
            # print("Fitness Calculation Time", timeFitness)
            # print("Selection Time", timeSelection)
            # print("Breeding Time", timeBreeding)
            # print("Mutation Time", timeMutation)

        # Selection
        timeBeforeSelection = timeit.default_timer()
        population = select(population, populationFitness, tournamentSize, selectionProbability)
        timeSelection = (timeit.default_timer() - timeBeforeSelection)

        # Breeding
        timeBeforeBreeding = timeit.default_timer()
        population = breed(population, breedingProbability)
        timeBreeding = (timeit.default_timer() - timeBeforeBreeding)

        # Mutation
        timeBeforeMutation = timeit.default_timer()
        population = mutate(population, mutationProbability)
        timeMutation = (timeit.default_timer() - timeBeforeMutation)
       

    timeStop = timeit.default_timer()

    print(timeStop - timeStart)
    print(bestFitness)


run(
    graphPath="graphs/pr1002.txt",
    populationSize=100,
    iterations=100000,
    tournamentSize=5,
    selectionProbability=1,
    breedingProbability=1,
    mutationProbability=0.1
)