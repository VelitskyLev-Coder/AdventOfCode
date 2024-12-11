import functools


@functools.cache
def count_how_many_after_steps(num: int, steps: int) -> int:
    if steps == 0:
        return 1
    if num == 0:
        return count_how_many_after_steps(1, steps-1)
    if len(num_as_str := str(num)) % 2 == 0:
        half1 = num_as_str[:len(num_as_str) // 2]
        half2 = num_as_str[len(num_as_str) // 2:]
        return count_how_many_after_steps(int(half1), steps-1) + count_how_many_after_steps(int(half2), steps-1)
    return count_how_many_after_steps(num*2024, steps-1)


def main():
    with open('input.txt') as input_file:
        nums = map(int, input_file.read().split())

    steps = 75
    print(sum(count_how_many_after_steps(x, steps) for x in nums))

    print(f"Cache size: {count_how_many_after_steps.cache_info().currsize}")

if __name__ == '__main__':
    main()