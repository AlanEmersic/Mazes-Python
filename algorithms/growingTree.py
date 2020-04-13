from entity import Grid, Cell
import random


class GrowingTree:
    @staticmethod
    def create(grid: Grid) -> None:
        start = grid.randomCell()
        active = [start]

        while any(active):
            index = random.randrange(4)
            cell: Cell

            if index == 0:
                cell = active[0]  # oldest
            elif index == 1:
                cell = active[len(active) - 1]  # newest
            elif index == 2:
                cell = active[round(len(active) / 2)]  # middle
            else:
                cell = active[random.randrange(len(active))]  # random

            availableNeighbors = list(filter(lambda e: len(e.links()) == 0, cell.neighbors))

            if any(availableNeighbors):
                neighbor = availableNeighbors[random.randrange(len(availableNeighbors))]
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)
