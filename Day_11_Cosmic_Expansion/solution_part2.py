from solution_part1 import get_input, Universe


def main():
    expand_param = 1_000_000
    universe = Universe(get_input())
    initial_path_sum = universe.get_paths_sum()
    universe.expand_universe()
    expanded_once_path_sum = universe.get_paths_sum()
    expansion_inc = expanded_once_path_sum - initial_path_sum
    result_path_sum = initial_path_sum + (expand_param-1)*expansion_inc
    print(result_path_sum)


if __name__ == '__main__':
    main()
