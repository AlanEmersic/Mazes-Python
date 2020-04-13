from entity import Grid
import random
from itertools import islice


class Wilsons:
    @staticmethod
    def create(grid: Grid) -> None:
        unvisited = []

        for cell in grid.eachCell():
            unvisited.append(cell)

        first = unvisited[random.randrange(len(unvisited))]
        unvisited.remove(first)

        while any(unvisited):
            cell = unvisited[random.randrange(len(unvisited))]
            path = [cell]

            while cell in unvisited:
                cell = cell.neighbors[random.randrange(len(cell.neighbors))]
                position = -1
                if cell in path:
                    position = path.index(cell)

                if position >= 0:
                    path = list(islice(path, position + 1))
                else:
                    path.append(cell)

            for index in range(len(path) - 1):
                path[index].link(path[index + 1])
                unvisited.remove(path[index])
