# From codereview.stackexchange.com
#[1, 2, 3, 4]
# [{}, {}] [a, b

# [1,2,3] [[1]] [[1] [2]] [[1, 2]]
#[[2, 3]] [[3], [2]]


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_) // 2):
        parts = [set(), set()]
        for item in set_:
            parts[i & 1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]] + b


# This is a helper function that will fetch all of the available
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

# Uncomment the following code  and run this file
# to see what get_partitions does if you want to visualize it:


# for item in (get_partitions(['a', 'b', 'c', 'd'])):
#    print(item, len(item))

# for i in partition(['a', 'b', 'c', 'd']):
#    print(i, len(i))
