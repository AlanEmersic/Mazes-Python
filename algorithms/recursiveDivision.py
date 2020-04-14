from entity import Grid
import random


class RecursiveDivision:
    @staticmethod
    def create(grid: Grid) -> None:

        for cell in grid.eachCell():
            for neighbor in cell.neighbors:
                cell.link(neighbor, False)

        RecursiveDivision.divide(0, 0, grid.rows, grid.cols, grid)

    @staticmethod
    def divide(row: int, col: int, height: int, width: int, grid: Grid) -> None:
        # if height <= 1 or width <= 1 or height < 5 and width < 5 and random.randrange(4) == 0:  # for rooms
        if height <= 1 or width <= 1:
            return

        if height > width:
            RecursiveDivision.divideHorizontally(row, col, height, width, grid)
        else:
            RecursiveDivision.divideVertically(row, col, height, width, grid)

    @staticmethod
    def divideHorizontally(row: int, col: int, height: int, width: int, grid: Grid) -> None:
        divideSouthOf = random.randrange(height - 1)
        passageAt = random.randrange(width)

        for x in range(width):
            if passageAt == x:
                continue

            cell = grid.cells[row + divideSouthOf][col + x]
            cell.unlink(cell.south)

        RecursiveDivision.divide(row, col, divideSouthOf + 1, width, grid)
        RecursiveDivision.divide(row + divideSouthOf + 1, col, height - divideSouthOf - 1, width, grid)

    @staticmethod
    def divideVertically(row: int, col: int, height: int, width: int, grid: Grid) -> None:
        divideEastOf = random.randrange(width - 1)
        passageAt = random.randrange(height)

        for y in range(height):
            if passageAt == y:
                continue

            cell = grid.cells[row + y][col + divideEastOf]
            cell.unlink(cell.east)

        RecursiveDivision.divide(row, col, height, divideEastOf + 1, grid)
        RecursiveDivision.divide(row, col + divideEastOf + 1, height, width - divideEastOf - 1, grid)
