import functools

class Checker:
    def __init__(self, towels: list[str]):
        self._towels = tuple(towels)

    @functools.cache
    def can_create_design(self, design: str) -> int:
        if not design:
            return 1

        result = 0
        for towel in self._towels:
            if design.startswith(towel):
                result += self.can_create_design(design[len(towel):])

        return result



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
        result += checker.can_create_design(design)

    print(result)
    print(checker.can_create_design.cache_info())



if __name__ == '__main__':
    main()