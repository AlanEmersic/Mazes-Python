from entity import Grid
import random


class Prims:
    @staticmethod
    def create(grid: Grid) -> None:
        start = grid.randomCell()
        active = [start]

        while any(active):
            cell = active[random.randrange(len(active))]
            availableNeighbors = list(filter(lambda e: len(e.links()) == 0, cell.neighbors))

            if any(availableNeighbors):
                neighbor = availableNeighbors[random.randrange(len(availableNeighbors))]
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)
