def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L:
        lens = [len(s) for s in L]
        mean = sum(lens) / len(L)
        return (sum([(i - mean)**2 for i in lens]) / len(L)) ** 0.5
    else:
        return float('NaN')


from math import sqrt


def std(ls):
    mean = sum(ls) / len(ls)
    stdev = sqrt(sum([(i - mean)**2 for i in ls]) / len(ls))
    return mean, stdev / mean


#print(std([10, 4, 12, 15, 20, 5]))
#print(stdDevOfLengths(['a', 'z', 'p']))
#print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))


import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    balls = [0, 0, 0, 1, 1, 1]
    success = 0
    for _ in range(numTrials):
        res = sum(random.sample(balls, 3))
        if res == 0 or res == 3:
            success += 1
    return success / numTrials


def getExt(numTrials):
    results = []
    for _ in range(numTrials):
        results.append(noReplacementSimulation(numTrials))
    m, s = std(results)
    print(f"mean = {m}, s = {s}")
    return s


def estimate(precision, numTrials):
    std = getExt(numTrials)
    while std * 1.96 >= precision:
        std = getExt(numTrials)
        numTrials *= 2


estimate(0.05, 100)
