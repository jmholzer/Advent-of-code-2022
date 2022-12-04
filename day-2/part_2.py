from typing import Tuple


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)
        self._move_score_map = {"A": 1, "B": 2, "C": 3}
        self._win_map = {"A": "B", "B": "C", "C": "A"}
        self._lose_map = {"A": "C", "B": "A", "C": "B"}
        self._draw_map = {"A": "A", "B": "B", "C": "C"}

    def solve(self) -> int:
        score = 0
        for game in self._input:
            if game[1] == "X":
                score += self._move_score_map[self._lose_map[game[0]]] + 0
            elif game[1] == "Y":
                score += self._move_score_map[self._draw_map[game[0]]] + 3
            elif game[1] == "Z":
                score += self._move_score_map[self._win_map[game[0]]] + 6
        return score


def _read_input(input_file_path: str) -> Tuple[str]:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            yield tuple(line.strip().split(" "))


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
