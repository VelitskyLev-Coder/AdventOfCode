
def get_input() -> list[str]:
    with open('input_1.txt') as input_stram:
        return input_stram.read().strip().split(',')


def hash_1a(string: str) -> int:
    result = 0
    for ch in string:
        ascii_code = ord(ch)
        result += ascii_code
        result *= 17
        result %= 256
    return result


def main():
    print(sum(map(hash_1a, get_input())))


if __name__ == '__main__':
    main()
