import random
import os
import timeit

from breeding.breeding2 import breedNewPopulation
from selection.tournament import select
from mutation.reverse import mutatePopulation
from fitness.fitnessCalculator import getPopulationFitness
from readers.file import readDistancesFromFile


def createInitialPopulation(populationSize, specimenSize):
    population = []

    for _ in range(populationSize):
        specimen = [i for i in range(specimenSize)]
        random.shuffle(specimen)
        population.append(specimen)

    return population


def run(graphPath, populationSize, iterations, tournamentSize, selectionProbability, breedingProbability, mutationProbability):
    distances = readDistancesFromFile(graphPath)
    population = createInitialPopulation(populationSize, specimenSize=len(distances))

    timeStart = timeit.default_timer()

    bestFitness = float("inf")

    timeSelection = 0
    timeBreeding = 0
    timeMutation = 0

    for i in range(iterations):

        # FITNESS
        timeBeforeFitness = timeit.default_timer()
        populationFitness = getPopulationFitness(distances, population)
        timeFitness = (timeit.default_timer() - timeBeforeFitness)

        # PRINT
        bestFitnessInGeneration = min(populationFitness)
        if bestFitness > bestFitnessInGeneration:
            # Best Fitness
            bestFitness = bestFitnessInGeneration
            bestFitnessInGenerationIndex = populationFitness.index(bestFitnessInGeneration)
            print("\nBEST FITNESS: ", bestFitness)
            print("SPECIMEN: ", population[bestFitnessInGenerationIndex])

            # PRINT Times
            # print("Fitness Calculation Time", timeFitness)
            # print("Selection Time", timeSelection)
            # print("Breeding Time", timeBreeding)
            # print("Mutation Time", timeMutation)

            # PRINT Validation
            # isPopulationValid = validatePopulation(population)
            # print("Population valid: ", isPopulationValid)

        # SELECTION
        # timeBeforeSelection = timeit.default_timer()
        population = select(population, populationFitness, tournamentSize, selectionProbability)
        # timeSelection = (timeit.default_timer() - timeBeforeSelection)

        # BREEDING
        # timeBeforeBreeding = timeit.default_timer()
        population = breedNewPopulation(population, breedingProbability)
        # timeBreeding = (timeit.default_timer() - timeBeforeBreeding)

        # MUTATION
        # timeBeforeMutation = timeit.default_timer()
        mutatePopulation(population, mutationProbability)
        # timeMutation = (timeit.default_timer() - timeBeforeMutation)

    # timeStop = timeit.default_timer()
    # print(timeStop - timeStart)
    # print(bestFitness)


run(
    graphPath="graphs/berlin52.txt",
    populationSize=50,
    iterations=100000,
    tournamentSize=5,
    selectionProbability=1,
    breedingProbability=0.9,
    mutationProbability=0.05
)
