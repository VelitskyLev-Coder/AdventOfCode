import functools

class Checker:
    def __init__(self, towels: list[str]):
        self._towels = tuple(towels)

    @functools.cache
    def can_create_design(self, design: str) -> bool:
        if not design:
            return True
        for towel in self._towels:
            if design.startswith(towel):
                if self.can_create_design(design[len(towel):]):
                    return True

        return False


def main():
    towels: list[str]
    designs: list[str] = list()
    with open('input.txt') as input_file:
        towels = input_file.readline().strip().split(',')
        towels = [t.strip() for t in towels]
        towels.sort(key=len, reverse=True)
        for line in input_file:
            if line.strip():
                designs.append(line.strip())


    checker = Checker(towels)
    result = 0
    for design in designs:
        if checker.can_create_design(design):
            result += 1

    print(result)



if __name__ == '__main__':
    main()