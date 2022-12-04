from typing import List


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)

    def solve(self) -> int:
        result = 0
        group = []
        for rucksack in self._input:
            group.append(rucksack)
            if len(group) < 3:
                continue
            badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
            result += Solution._priority(badge)
            group = []
        return result

    @staticmethod
    def _priority(item: str) -> int:
        if item.islower():
            return ord(item) - ord("a") + 1
        else:
            return ord(item) - ord("A") + 27


def _read_input(input_file_path: str) -> List[str]:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            yield line.strip()


if __name__ == "__main__":
    solution = Solution("input")
    print(solution.solve())
