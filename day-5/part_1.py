from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._stacks = _read_stacks(input_file_path)
        self._moves = _read_moves(input_file_path)

    def solve(self) -> int:
        for move in self._moves:
            amount, from_idx, to_idx = move
            for _ in range(amount):
                self._stacks[to_idx].append(self._stacks[from_idx].pop())
        return "".join(self._stacks[i][-1] for i in range(1, len(self._stacks) + 1))


def read_stacks(input_file_path: str) -> Dict[int, List[str]]:
    with open(input_file_path) as input_file:
        stacks = defaultdict(list)
        for line in input_file:
            if line == "\n":
                break
            for i in range(len(line)):
                if (i - 1) % 4 == 0 and line[i] != " " and not line[i].isnumeric():
                    stacks[(i - 1) // 4 + 1].append(line[i])
        for i in stacks:
            stacks[i].reverse()
        return stacks


def read_moves(input_file_path: str) -> Tuple[int]:
    with open(input_file_path) as input_file:
        for line in input_file:
            if line == "\n":
                break
        for line in input_file:
            line = line.strip().split(" ")
            yield tuple(int(w) for w in line if w.isnumeric())


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
