from Day_10_Pipe_Maze.graph import Graph


def get_input() -> list[list[str]]:
    result = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            if not line.strip():
                continue
            result.append(list(line.strip()))
    return result


def main():
    graph = Graph(get_input())
    print(len(graph.get_longest_cycle()) // 2)


if __name__ == '__main__':
    main()
