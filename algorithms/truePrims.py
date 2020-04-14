from entity import Grid
import random
from functools import reduce


class TruePrims:
    @staticmethod
    def create(grid: Grid) -> None:
        start = grid.randomCell()
        active = [start]
        costs = {}

        for cell in grid.eachCell():
            costs[cell] = random.randrange(100)

        while any(active):
            cell = reduce(lambda minValue, nextValue: minValue if costs[minValue] < costs[nextValue] else nextValue,
                          active)
            availableNeighbors = list(filter(lambda e: len(e.links()) == 0, cell.neighbors))

            if any(availableNeighbors):
                neighbor = reduce(
                    lambda minValue, nextValue: minValue if costs[minValue] < costs[nextValue] else nextValue,
                    availableNeighbors)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)
