from __future__ import annotations

from typing import Optional


class Solution:
    def __init__(self, input_file_path: str) -> None:
        self._input = _read_input(input_file_path)
        self._fs_tree = FSTreeNode("/")
        self._pointer = self._fs_tree

    def solve(self) -> int:
        self._build_fs_tree()
        yield self._find_sum_of_dirs_below_limit(100000)
        yield self._find_smallest_directory_to_delete()

    def _build_fs_tree(self):
        for line in self._input:
            if line[0] == "$":
                self._process_command(line)
            else:
                line = line.split(" ")
                if line[0] == "dir":
                    size, name = 0, line[1]
                else:
                    size, name = line
                self._pointer.children.append(
                    FSTreeNode(name, size=int(size), parent=self._pointer)
                )
        self._find_dir_sizes(self._fs_tree)

    def _process_command(self, command: str) -> None:
        command = command.split(" ")[1:]
        if command[0] == "cd":
            self._process_cd(command[1])

    def _process_cd(self, arg: str) -> None:
        if arg == "/":
            self._pointer = self._fs_tree
        elif arg == "..":
            if self._pointer == self._fs_tree:
                return
            self._pointer = self._pointer.parent
        else:
            for child in self._pointer.children:
                if child.name == arg:
                    self._pointer = child
                    break

    def _find_dir_sizes(self, node) -> None:
        if node.children:
            node.size += sum(self._find_dir_sizes(c) for c in node.children)
        return node.size

    def _find_sum_of_dirs_below_limit(self, limit):
        result = 0
        stack = [self._fs_tree]
        while stack:
            node = stack.pop()
            if node.children and node.size <= limit:
                result += node.size
            stack.extend(node.children)
        return result

    def _find_smallest_directory_to_delete(self):
        target = 30000000 - (70000000 - self._fs_tree.size)

        stack = [self._fs_tree]
        result = self._fs_tree.size
        while stack:
            node = stack.pop()
            if node.children and node.size >= target:
                result = min(result, node.size)
            stack.extend(node.children)
        return result


class FSTreeNode:
    def __init__(
        self, name: str, size: Optional[int] = 0, parent: Optional[FSTreeNode] = None
    ) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []


def _read_input(input_file_path: str) -> str:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            yield line.strip()


if __name__ == "__main__":
    solution = Solution("input").solve()
    print(next(solution))
    print(next(solution))
