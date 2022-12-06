from collections import deque

from part_1 import read_moves, read_stacks


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._stacks = read_stacks(input_file_path)
        self._moves = read_moves(input_file_path)

    def solve(self) -> int:
        for move in self._moves:
            amount, from_idx, to_idx = move
            crates = deque()
            for _ in range(amount):
                crates.appendleft(self._stacks[from_idx].pop())
            self._stacks[to_idx].extend(crates)
        return "".join(self._stacks[i][-1] for i in range(1, len(self._stacks) + 1))


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
