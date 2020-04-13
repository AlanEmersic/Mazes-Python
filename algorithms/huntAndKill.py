from entity import Grid
import random


class HuntAndKill:
    @staticmethod
    def create(grid: Grid) -> None:
        current = grid.randomCell()

        while current is not None:
            unvisitedNeighbors = list(filter(lambda e: len(e.links()) == 0, current.neighbors))

            if any(unvisitedNeighbors):
                neighbor = unvisitedNeighbors[random.randrange(len(unvisitedNeighbors))]
                current.link(neighbor)
                current = neighbor
            else:
                current = None

                for cell in grid.eachCell():
                    visitedNeighbors = list(filter(lambda e: any(e.links()), cell.neighbors))

                    if len(cell.links()) == 0 and any(visitedNeighbors):
                        current = cell
                        neighbor = visitedNeighbors[random.randrange(len(visitedNeighbors))]
                        current.link(neighbor)
                        break
