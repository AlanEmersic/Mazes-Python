from entity import Grid
import random


class RecursiveBacktracker:
    @staticmethod
    def create(grid: Grid) -> None:
        start = grid.randomCell()
        stack = [start]

        while any(stack):
            current = stack[-1]
            neighbors = list(filter(lambda e: len(e.links()) == 0, current.neighbors))

            if len(neighbors) == 0:
                stack.pop()
            else:
                neighbor = neighbors[random.randrange(len(neighbors))]
                current.link(neighbor)
                stack.append(neighbor)
