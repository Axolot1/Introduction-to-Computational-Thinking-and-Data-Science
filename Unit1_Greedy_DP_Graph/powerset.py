from itertools import chain
from itertools import combinations


def powerSet(items):
    tupleSet = chain.from_iterable(combinations(items, i)
                                   for i in range(len(items) + 1))
    for i in tupleSet:
        yield list(i)
