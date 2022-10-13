import sys
from functools import reduce
from itertools import chain, combinations

def readInput():
    n = int(sys.stdin.readline())
    puzzles = list(map(int, sys.stdin.readline().strip("\n").split(" ")))
    return puzzles

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def sol(puzzles):
    power_puzzles = list(powerset(puzzles))
    filtered = list(filter(lambda a: a != (), power_puzzles))
    sum = 0
    for subset in power_puzzles:
        res = reduce(lambda x, y: x | y, subset)
        sum = sum + res

    return sum

def main():
    puzzles = readInput()
    print(sol(puzzles))



if __name__ == "__main__":
    main()