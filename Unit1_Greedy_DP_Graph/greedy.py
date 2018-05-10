class Food():
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return f"{self.name}: <{self.value}, {self.calories}>"


def buildMenu(names, values, calories):
    return [Food(names[i], values[i], calories[i]) for i in range(len(values))]


def greedy(items, maxCost, keyFun):
    """Assumes items a list, maxCost >= 0,
      keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key=keyFun, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)


def testGreedy(items, constraint, keyFun):
    taken, val = greedy(items, constraint, keyFun)
    print("Toal value of items taken =", val)
    for item in taken:
        print('   ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate ', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate ', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
    print('\nUse greedy by density to allocate ', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)


def maxVal(toConsider, avail):
    """Assumes toConsider a list of itmes, avail a weight
    return a tutple of total value of a solution to 0/1 knapsack
    problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        return (0, [])
    elif toConsider[0].getCost() > avail:
        return maxVal(toConsider[1:], avail)
    else:
        cur = toConsider[0]
        # taked
        t_val, t_subSol = maxVal(toConsider[1:], avail - cur.getCost())
        #not take
        nt_val, nt_subSol = maxVal(toConsider[1:], avail)
        if t_val + cur.getValue() > nt_val:
            return (t_val + cur.getValue(), [cur] + t_subSol)
        return (nt_val, nt_subSol)


def fastMaxVal(toConsider, avail, memo):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, [])
    elif toConsider[0].getCost() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        cur = toConsider[0]
        t_val, t_sub = fastMaxVal(toConsider[1:], avail - cur.getCost(), memo)
        nt_val, nt_sub = fastMaxVal(toConsider[1:], avail, memo)
        if t_val + cur.getValue() > nt_val:
            result = (t_val + cur.getValue(), [cur] + t_sub)
        else:
            result = (nt_val, nt_sub)
    memo[(len(toConsider), avail)] = result
    return result


def testBruteForce(items, constraint):
    val, taken = maxVal(items, constraint)
    print('\nUse bruteforce to allocate ', constraint, 'calories')
    print("\nToal value of items taken =", val)
    for item in taken:
        print('   ', item)


testGreedys(foods, 1000)
testBruteForce(foods, 1000)


# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


#_ _, a _, _ a, ab _, _ ab, a b, b a, b _, _ b
# 0, 1, 10, 11, 100, 101, 110, 111, 1000
# 0 1 2 10 11 12 20
# 0 1 2 3  4  5  6

from itertools import chain
from itertools import combinations


def powerSet2(items):
    tupleSet = chain.from_iterable(combinations(items, i)
                                   for i in range(len(items) + 1))
    for i in tupleSet:
        yield list(i)


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bag1, bag2 = [], []
        for j in range(N):
            if i % 3 == 1:
                bag1.append(items[j])
            if i % 3 == 2:
                bag2.append(items[j])
            i //= 3
        yield (bag1, bag2)
