import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    birthPro = 1 - CURRENTRABBITPOP / MAXRABBITPOP
    for _ in range(CURRENTRABBITPOP):
        if random.random() < birthPro:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    birthPro, diePro = 1 / 3, 9 / 10
    sucHuntPro = CURRENTRABBITPOP / MAXRABBITPOP
    for _ in range(CURRENTFOXPOP):
        if random.random() < sucHuntPro and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() < birthPro:
                CURRENTFOXPOP += 1
        else:
            if random.random() < diePro and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    if CURRENTRABBITPOP < 10 or CURRENTFOXPOP < 10:
        return [CURRENTRABBITPOP] * numSteps, [CURRENTFOXPOP] * numSteps
    rabbitPops, foxPops = [], []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPops.append(CURRENTRABBITPOP)
        foxPops.append(CURRENTFOXPOP)
    return rabbitPops, foxPops


def plot():
    rp, fp = runSimulation(200)
    rabbitCoeff = pylab.polyfit(range(len(rp)), rp, 2)
    foxCoeff = pylab.polyfit(range(len(fp)), fp, 2)
    pylab.plot(rp, label="rabbit")
    pylab.plot(fp, label="fox")
    pylab.plot(pylab.polyval(rabbitCoeff, range(len(rp))), label="rabbitEst")
    pylab.plot(pylab.polyval(foxCoeff, range(len(fp))), label="foxEst")
    pylab.xlabel("time step")
    pylab.ylabel("population")
    pylab.legend(loc="best")
    pylab.show()


plot()
