import itertools
import math
from solution_part1 import get_input, Graph


class GhostGraph(Graph):
    def ghost_walk_length(self, pattern: str) -> int:
        currents = [node for node in self.nodes_map.values() if node.name.endswith('A')]
        z_periods = [self.calc_z_period(node, pattern) for node in currents]
        return math.lcm(*z_periods)

    def calc_z_period(self, node, pattern):
        visited: dict[tuple[str, int], int] = dict()
        visited[(node.name, 0)] = 0
        for counter, direction in enumerate(itertools.cycle(pattern), start=1):
            node_pattern_statkey = (node.name, counter % len(pattern))
            node = self.get_next_node(node, direction)
            if node_pattern_statkey in visited:
                length = counter - visited[node_pattern_statkey]
                return length
            else:
                visited[node_pattern_statkey] = counter


def main():
    input_data = get_input()
    graph = GhostGraph(input_data.vertices, input_data.lefts, input_data.rights)
    print(graph.ghost_walk_length(input_data.walk_pattern))


if __name__ == '__main__':
    main()
