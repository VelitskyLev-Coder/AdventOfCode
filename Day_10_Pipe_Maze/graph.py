import itertools
from typing import NamedTuple, Optional


class Direction(NamedTuple):
    y: int
    x: int


class Directions:
    WEST = Direction(0, -1)
    EAST = Direction(0, 1)
    NORTH = Direction(-1, 0)
    SOUTH = Direction(1, 0)


class Node:
    node_id_producer = itertools.count()

    def __init__(self, ch: str):
        self.connections: list['Node'] = list()
        self.node_id = next(Node.node_id_producer)
        self.ch = ch

    def __hash__(self):
        return self.node_id

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.node_id == other.node_id

    def add_connection(self, other_node: 'Node'):
        self.connections.append(other_node)


class Graph:
    def __init__(self, char_map: list[list[str]]):
        self.rows_number = len(char_map)
        self.column_number = len(char_map[0])
        self.node_map = [[Node(ch) for ch in row] for row in char_map]
        self.s_node = next((node for node in itertools.chain(*self.node_map) if node.ch == 'S'))
        self.s_neighbours = set()
        self.create_connections(char_map)

    def create_connections(self, char_map):
        s_directions = set()
        dir_map = {
            '|': [Directions.NORTH, Directions.SOUTH],
            '-': [Directions.EAST, Directions.WEST],
            'L': [Directions.NORTH, Directions.EAST],
            'J': [Directions.NORTH, Directions.WEST],
            '7': [Directions.SOUTH, Directions.WEST],
            'F': [Directions.SOUTH, Directions.EAST],
        }
        for i, row in enumerate(char_map):
            for j, ch in enumerate(row):
                possible_directions: list[Direction] = list()

                match ch:
                    case '|' | '-' | 'L' | 'J' | '7' | 'F':
                        possible_directions = dir_map[ch]
                    case '.' | 'S':
                        pass
                    case _:
                        raise ValueError(f'Unknown character {ch}')
                for direction in possible_directions:
                    y, x = i + direction.y, j + direction.x
                    if self.is_inside(y, x) and self.node_map[y][x].ch != '.':
                        self.node_map[i][j].add_connection(self.node_map[y][x])
                        if self.node_map[y][x] is self.s_node:
                            self.s_neighbours.add(self.node_map[i][j])
                            s_directions.add(Direction(-direction.y, -direction.x))

        for ch, directions in dir_map.items():
            if sorted(directions) == sorted(s_directions):
                self.s_node.ch = ch



    def is_inside(self, y, x) -> bool:
        return 0 <= x < self.column_number and 0 <= y < self.rows_number

    def get_longest_cycle(self) -> set[Node]:
        visited_nodes = set()
        cycles = []
        for s_neighbour in self.s_neighbours:
            current = s_neighbour
            visited_nodes.clear()
            visited_nodes.add(self.s_node)
            visited_nodes.add(current)
            while current is not self.s_node:
                for cur_neighbour in current.connections:
                    if cur_neighbour not in visited_nodes:
                        current = cur_neighbour
                        visited_nodes.add(current)
                        break
                else:
                    if self.s_node in current.connections:
                        current = self.s_node
                    else:
                        break
            else:
                cycles.append(set(visited_nodes))

        return max(cycles, key=len)

    def get_inside_tiles(self) -> set[Node]:
        cycle = self.get_longest_cycle()
        inside_tiles = set()
        for i, row in enumerate(self.node_map):
            for j, node in enumerate(row):
                if node in cycle:
                    continue
                east_nodes = set((self.node_map[i][x] for x in range(j) if self.node_map[i][x].ch in ['J', 'L', '|']))
                east_cycle_nodes = east_nodes.intersection(cycle)
                if len(east_cycle_nodes) % 2 == 1:
                    inside_tiles.add(node)
        return inside_tiles
