def blink(nums: list[int]) -> list[int]:
    result = list()
    for num in nums:
        if num == 0:
            result.append(1)
        elif len(num_as_str := str(num)) % 2 == 0:
            half1 = num_as_str[:len(num_as_str)//2]
            half2 = num_as_str[len(num_as_str)//2:]
            result.append(int(half1))
            result.append(int(half2))
        else:
            result.append(num*2024)
    return result


def main():
    with open('input.txt') as input_file:
        nums = map(int, input_file.read().split())

    for _ in range(25):
        nums = blink(nums)
        #print(nums)

    print(len(nums))

if __name__ == '__main__':
    main()