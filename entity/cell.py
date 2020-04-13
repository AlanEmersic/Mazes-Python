from typing import Dict, List


class Cell:

    def __init__(self, row: int, col: int):
        self._row = row
        self._col = col

        self.east: "Cell" = None
        self.west: "Cell" = None
        self.north: "Cell" = None
        self.south: "Cell" = None

        self._links: Dict["Cell", bool] = {}

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    @property
    def neighbors(self) -> List["Cell"]:
        list: List["Cell"] = []

        if self.north is not None:
            list.append(self.north)
        if self.south is not None:
            list.append(self.south)
        if self.east is not None:
            list.append(self.east)
        if self.west is not None:
            list.append(self.west)

        return list

    def link(self, cell: "Cell", bidirectional=True) -> "Cell":
        self._links[cell] = True

        if bidirectional:
            cell.link(self, False)

        return self

    def unlink(self, cell: "Cell", bidirectional=True) -> "Cell":
        del self._links[cell]

        if bidirectional:
            cell.unlink(self, False)

        return self

    def links(self) -> List["Cell"]:
        return list(self._links.keys())

    def isLinked(self, cell: "Cell") -> bool:
        if cell is None:
            return False
        return self._links.__contains__(cell)
