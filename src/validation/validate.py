def validateSpecimen(specimen):
    validSpecimen = [i for i in range(len(specimen))]

    specimenToCompare = specimen[:]
    specimenToCompare.sort()

    for i in range(len(specimen)):
        if specimenToCompare[i] != validSpecimen[i]:
            return False

    return True


def validatePopulation(population):
    validSpecimen = [i for i in range(len(population[0]))]

    for specimen in population:
        validation = validateSpecimen(specimen)
        if validation == False:
            return False

    return True
