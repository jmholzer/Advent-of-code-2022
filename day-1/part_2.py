import heapq
from typing import List


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)

    def solve(self) -> int:
        heap = []
        calories = 0
        for line in self._input:
            if line == "":
                if len(heap) < 3:
                    heapq.heappush(heap, calories)
                elif calories > heap[0]:
                    heapq.heapreplace(heap, calories)
                calories = 0
            else:
                calories += int(line)
        return sum(heap)


def _read_input(input_file_path: str) -> List[str]:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            yield line.strip()


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
