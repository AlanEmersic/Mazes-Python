from entity import Grid
import random


class BinaryTree:
    @staticmethod
    def create(grid: Grid) -> None:
        for cell in grid.eachCell():
            neighbors = []
            if cell.north is not None:
                neighbors.append(cell.north)
            if cell.east is not None:
                neighbors.append(cell.east)

            if len(neighbors) > 0:
                neighbor = random.choice(neighbors)
                cell.link(neighbor)
