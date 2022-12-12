from typing import List


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._grid = _read_input(input_file_path)

    def solve(self) -> int:
        m, n = len(self._grid), len(self._grid[0])

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, self._calc_scenic_score(i, j))
        return result

    def _calc_scenic_score(self, i: int, j: int) -> int:
        m, n = len(self._grid), len(self._grid[0])
        height = self._grid[i][j]

        # calculate top
        top = 0
        for r in range(i - 1, -1, -1):
            top += 1
            if self._grid[r][j] >= height:
                break

        # calculate bottom
        bottom = 0
        for r in range(i + 1, m):
            bottom += 1
            if self._grid[r][j] >= height:
                break

        # calculate left
        left = 0
        for c in range(j - 1, -1, -1):
            left += 1
            if self._grid[i][c] >= height:
                break

        # calculate right
        right = 0
        for c in range(j + 1, n):
            right += 1
            if self._grid[i][c] >= height:
                break

        return top * bottom * left * right


def _read_input(input_file_path: str) -> List[List[int]]:
    grid = []
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            grid.append(list(map(int, line.strip())))
    return grid


if __name__ == "__main__":
    print(Solution("input").solve())
