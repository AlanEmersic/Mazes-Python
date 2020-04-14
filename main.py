import cProfile
import random
import sys
from entity import Grid
from algorithms import *


def main():
    generateGridMaze(10)


def generateGridMaze(size: int):
    seed = random.randint(-sys.maxsize, sys.maxsize)
    grid = Grid(size, size, seed)
    TruePrims.create(grid)
    grid.toPNG()
    print("seed: %d" % seed)


main()
# cProfile.run("main()")
