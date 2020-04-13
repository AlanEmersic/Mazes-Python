from entity import Grid, Cell
import random


class Sidewinder:
    @staticmethod
    def create(grid: Grid) -> None:
        for eachRow in grid.eachRow():
            run = []
            for cell in eachRow:
                run.append(cell)
                atEasternBoundary = cell.east is None
                atNorthernBoundary = cell.north is None
                shouldCloseOut = atEasternBoundary or (atNorthernBoundary is not None and random.randrange(0, 2) == 0)

                if shouldCloseOut:
                    member: Cell = run[random.randrange(len(run))]

                    if member.north is not None:
                        member.link(member.north)

                    run.clear()
                else:
                    cell.link(cell.east)
