from typing import List, Generator
from PIL import Image, ImageDraw
from entity import Cell
import random


class Grid:
    def __init__(self, rows: int, cols: int, seed: int):
        self._rows = rows
        self._cols = cols
        self._size: int = self._rows * self._cols
        random.seed(seed)

        self._cells = self.prepareGrid()
        self.configureCells()

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def size(self) -> int:
        return self._size

    @property
    def cells(self) -> List[List[Cell]]:
        return self._cells

    def prepareGrid(self) -> List[List[Cell]]:
        return [[Cell(row, col) for col in range(self._cols)] for row in range(self._rows)]

    def configureCells(self) -> None:
        for cell in self.eachCell():
            row = cell.row
            col = cell.col

            cell.north = self.checkCell(row - 1, col)
            cell.south = self.checkCell(row + 1, col)
            cell.west = self.checkCell(row, col - 1)
            cell.east = self.checkCell(row, col + 1)

    def checkCell(self, row: int, col: int) -> Cell:
        if row < 0 or row >= self._rows:
            return None
        if col < 0 or col >= self._cols:
            return None
        return self.cells[row][col]

    def randomCell(self) -> Cell:
        row = random.randrange(self._rows)
        col = random.randrange(self._cols)

        return self._cells[row][col]

    def eachRow(self) -> Generator[List[Cell], None, None]:
        for row in range(self._rows):
            yield self._cells[row]

    def eachCell(self) -> Generator:
        for cellRow in self.eachRow():
            for cell in cellRow:
                yield cell

    def toPNG(self, cellSize: int = 100):
        imgWidth = cellSize * self._cols
        imgHeight = cellSize * self.cols

        penWidth = int(round(cellSize * 0.1))

        mazeImg = Image.new("RGB", (imgWidth + 1, imgHeight + 1), "white")
        img = ImageDraw.Draw(mazeImg)

        for cell in self.eachCell():
            x1 = cell.col * cellSize
            y1 = cell.row * cellSize
            x2 = (cell.col + 1) * cellSize
            y2 = (cell.row + 1) * cellSize

            if cell.north is None:
                img.line((x1, y1, x2, y1), fill=(0, 0, 0), width=penWidth)
            if cell.west is None:
                img.line((x1, y1, x1, y2), fill=(0, 0, 0), width=penWidth)
            if not cell.isLinked(cell.east):
                img.line((x2, y1, x2, y2), fill=(0, 0, 0), width=penWidth)
            if not cell.isLinked(cell.south):
                img.line((x1, y2, x2, y2), fill=(0, 0, 0), width=penWidth)

        mazeImg.save("maze.png")
        mazeImg.show()
