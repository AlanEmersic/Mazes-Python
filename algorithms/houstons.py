from entity import Grid
import random
from itertools import islice


class Houstons:
    @staticmethod
    def create(grid: Grid) -> None:
        unvisited = []

        for cell in grid.eachCell():
            unvisited.append(cell)

        threshold = int(grid.size / 3)
        current = grid.randomCell()
        unvisited.remove(current)

        while threshold != 0:
            neighbor = current.neighbors[random.randrange(len(current.neighbors))]

            if len(neighbor.links()) == 0:
                current.link(neighbor)
                unvisited.remove(neighbor)
                threshold -= 1

            current = neighbor

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
