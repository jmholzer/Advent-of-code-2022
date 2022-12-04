from typing import List


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)

    def solve(self) -> int:
        result = 0
        for range_1, range_2 in self._input:
            if self._overlaps(range_1, range_2):
                result += 1
        return result

    @staticmethod
    def _overlaps(range_1, range_2):
        return not (range_1[1] < range_2[0] or range_1[0] > range_2[1])


def _read_input(input_file_path: str) -> List[str]:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            yield [list(map(int, r.split("-"))) for r in line.strip().split(",")]


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
