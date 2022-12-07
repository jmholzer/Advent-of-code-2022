from collections import Counter, defaultdict
from typing import Dict, List, Tuple


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)

    def solve(self, message_length: int) -> int:
        count = Counter(self._input[:message_length])
        if len(count) == message_length:
            return message_length
        l = 0
        for r in range(message_length, len(self._input)):
            count[self._input[r]] += 1
            count[self._input[l]] -= 1
            if count[self._input[l]] == 0:
                del count[self._input[l]]
            l += 1
            if len(count) == message_length:
                return r + 1

def _read_input(input_file_path: str) -> str:
    with open(input_file_path, "r") as input_file:
        return input_file.read().strip()

if __name__ == "__main__":
    solution = Solution("input")
    print(f"part 1 solution: {solution.solve(4)}")
    print(f"part 2 solution: {solution.solve(14)}")