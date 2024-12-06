from solution_part1 import get_input
from Day_10_Pipe_Maze.graph import Graph


def main():
    graph = Graph(get_input())
    print(len(graph.get_inside_tiles()))


if __name__ == '__main__':
    main()
