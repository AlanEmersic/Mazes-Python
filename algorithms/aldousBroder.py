from entity import Grid
import random


class AldousBroder:
    @staticmethod
    def create(grid: Grid) -> None:
        cell = grid.randomCell()
        unvisited = grid.size - 1

        while unvisited > 0:
            neighbor = cell.neighbors[random.randrange(len(cell.neighbors))]

            if len(neighbor.links()) == 0:
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor
