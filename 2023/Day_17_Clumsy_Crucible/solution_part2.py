from graph import Direction, SpecialVertex
from solution_part1 import get_input, init_graph, visualize


def constrain_part_2(cur_direction: Direction, new_direction: Direction, cur_consecutive_blocks,
                     new_consecutive_blocks: int):
    return (cur_direction == new_direction or cur_consecutive_blocks >= 4) and new_consecutive_blocks <= 10


def main():
    grid = get_input()
    graph = init_graph(grid, constrain_part_2, 10, 4)
    distance, previous = graph.dijkstra(SpecialVertex.START)
    visualize(grid, previous, SpecialVertex.START, SpecialVertex.END)
    print(f'Min heat loss = {distance[SpecialVertex.END]}')


if __name__ == '__main__':
    main()
