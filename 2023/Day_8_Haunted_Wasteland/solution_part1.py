import itertools
from typing import NamedTuple, Optional
import re


class InputData(NamedTuple):
    vertices: list[str]
    lefts: list[str]
    rights: list[str]
    walk_pattern: str


class Node:
    def __init__(self, name: str):
        self.name = name
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return f'Node({self.name})'


class Graph:
    def __init__(self, vertices_names: list[str], lefts: list[str], rights: list[str]):
        self.nodes_map: dict[str, Node] = {name: Node(name) for name in vertices_names}
        for node_name, left, right in zip(vertices_names, lefts, rights):
            self.nodes_map[node_name].left = self.nodes_map[left]
            self.nodes_map[node_name].right = self.nodes_map[right]

    def get_next_node(self, node: Node, direction: str):
        if direction == 'L':
            return self.nodes_map[node.left.name]
        elif direction == 'R':
            return self.nodes_map[node.right.name]
        else:
            raise ValueError(f'Only L or R direction is possible, but {direction} was given')

    def walk_length(self, start: str, finish: str, pattern: str):
        current = self.nodes_map[start]
        if current.name == finish:
            return 0
        for counter, direction in enumerate(itertools.cycle(pattern), start=1):
            current = self.get_next_node(current, direction)
            if current.name == finish:
                return counter


def get_input() -> InputData:
    with open('input_1.txt') as input_stram:
        walk_pattern = input_stram.readline().strip()
        vertices = list()
        lefts = list()
        rights = list()
        for line in input_stram:
            if not line.strip():
                continue
            node_match = re.match(r'^(\w+)\s+=\s+\((\w+),\s+(\w+)\)\s*$', line).groups()
            vertex, left, right = node_match
            vertices.append(vertex)
            lefts.append(left)
            rights.append(right)

        return InputData(
            walk_pattern=walk_pattern,
            vertices=vertices,
            lefts=lefts,
            rights=rights
        )


def main():
    input_data = get_input()
    graph = Graph(input_data.vertices, input_data.lefts, input_data.rights)
    print(graph.walk_length('AAA', 'ZZZ', input_data.walk_pattern))


if __name__ == '__main__':
    main()
