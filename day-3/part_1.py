from typing import List


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)

    def solve(self) -> int:
        result = 0
        for rucksack in self._input:
            n = len(rucksack) // 2
            common_item_set = set(rucksack[:n]) & set(rucksack[n:])
            common_item = common_item_set.pop()
            result += Solution._priority(common_item)
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
