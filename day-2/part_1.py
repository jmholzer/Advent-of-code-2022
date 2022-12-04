from typing import List, Tuple


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)
        self._move_score_map = {"X": 1, "Y": 2, "Z": 3}
        self.outcome_map = {
            ("A", "X"): 3,
            ("A", "Y"): 6,
            ("A", "Z"): 0,
            ("B", "X"): 0,
            ("B", "Y"): 3,
            ("B", "Z"): 6,
            ("C", "X"): 6,
            ("C", "Y"): 0,
            ("C", "Z"): 3,
        }

    def solve(self) -> int:
        return sum(self._score(game) for game in self._input)

    def _score(self, game: Tuple[int]) -> int:
        return self._move_score_map[game[1]] + self.outcome_map[game]


def _read_input(input_file_path: str) -> List[str]:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            yield tuple(line.strip().split(" "))


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
