from typing import List


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._grid = _read_input(input_file_path)

    def solve(self) -> int:
        m, n = len(self._grid), len(self._grid[0])
        visible = [[False] * n for _ in range(m)]

        for i in range(m):
            row = self._find_visible(self._grid[i])
            reverse_row = self._find_visible(self._grid[i], reverse=True)
            for j in range(n):
                visible[i][j] = row[j] or reverse_row[j]

        for j in range(n):
            grid_col = [self._grid[i][j] for i in range(m)]
            col = self._find_visible(grid_col)
            reverse_col = self._find_visible(grid_col, reverse=True)
            for i in range(m):
                visible[i][j] = col[i] or reverse_col[i] or visible[i][j]

        result = 0
        for i in range(m):
            for j in range(n):
                result += 1 if visible[i][j] else 0
        return result

    @staticmethod
    def _find_visible(sequence: List[int], *, reverse: bool = False) -> int:
        result = [False] * len(sequence)
        result[0] = result[-1] = True

        if reverse:
            sequence = sequence[::-1]

        max_seen = sequence[0]
        for i in range(1, len(sequence) - 1):
            if sequence[i] > max_seen:
                result[i] = True
            max_seen = max(sequence[i], max_seen)

        if reverse:
            return result[::-1]
        return result


def _read_input(input_file_path: str) -> List[List[int]]:
    grid = []
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            grid.append(list(map(int, line.strip())))
    return grid


if __name__ == "__main__":
    print(Solution("input").solve())
