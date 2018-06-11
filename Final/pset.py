
import random
import pylab


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    samples = [0] * 4 + [1] * 4
    count = 0
    for _ in range(numTrials):
        draws = sum(random.sample(samples, 3))
        if draws == 3 or draws == 0:
            count += 1
    return count / numTrials


# You are given this function
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot / len(X))**0.5
    return mean, std

# You are given this class


class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2


def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


def findLongest(ls):
    pre = None
    longest, count = 0, 0
    for i in ls:
        if i == pre:
            count += 1
        else:
            count = 1
            pre = i
        if count > longest:
            longest = count
    return longest


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    longestes = []
    for _ in range(numTrials):
        rollResults = [die.roll() for _ in range(numRolls)]
        longestes.append(findLongest(rollResults))
    makeHistogram(longestes, 10, "Longest Run", "Count")
    return sum(longestes) / len(longestes)


# One test case
# print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))
# print(getAverage(Die([1, 1]), 10, 1000))

# If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
# If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
# If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
import numpy as np


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    choicesArray = np.array(choices)
    lens = len(choices)
    combsNum = 2 ** lens
    bestSum, bestResult = 0, np.array([0] * lens)
    for each in range(combsNum):
        bins = [int(c) for c in bin(each)[2:]]  # to binary representation
        result = np.array([0] * (lens - len(bins)) + bins)  # add leading 0
        curSum = sum(result * choicesArray)
        if bestSum < curSum <= total or (bestSum == curSum and sum(result) < sum(bestResult)):
            bestSum, bestResult = curSum, result
    return bestResult


#print(find_combination([3, 10, 2, 1, 5], 12))

a = [(10, 4), (30, 10), (90, 5), (100, 1), (120, 1), (60, 6)]

import sys


def getCAF(ls):
    farV, cloV = 0, sys.maxsize
    farP, cloP = None, None
    for i, e in enumerate(ls):
        for j, e2 in enumerate(ls):
            if i == j:
                continue
            dis = (e[0] - e2[0]) ** 2 + (e[1] - e2[1]) ** 2
            if dis > farV:
                farP, farV = (i + 1, j + 1), dis
            if dis < cloV:
                cloP, cloV = (i + 1, j + 1), dis
    return cloP, farP


print(getCAF(a))
