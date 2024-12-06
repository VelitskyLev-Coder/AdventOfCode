from solution_part1 import get_input, hash_1a


class Box:
    def __init__(self):
        self.lances: dict[str, int] = dict()

    def remove_lance(self, label: str):
        if label in self.lances:
            self.lances.pop(label)

    def add_lens(self, label, focal_length):
        self.lances[label] = focal_length

    def get_focusing_power(self) -> int:
        focusing_power = 0
        for position, (_, focal_length) in enumerate(self.lances.items(), start=1):
            focusing_power += position * focal_length
        return focusing_power


class Hashmap:
    def __init__(self):
        self.boxes = [Box() for _ in range(256)]

    def process_step(self, step: str):
        if step.endswith('-'):
            label = step.removesuffix('-')
            hash_value = hash_1a(label)
            self.boxes[hash_value].remove_lance(label)
            return

        label, focal_power_str = step.split('=')
        hash_value = hash_1a(label)
        focal_power = int(focal_power_str)
        self.boxes[hash_value].add_lens(label, focal_power)

    def get_focusing_power(self) -> int:
        focusing_power = 0
        for position, box in enumerate(self.boxes, start=1):
            focusing_power += position * box.get_focusing_power()
        return focusing_power


def main():
    hash_map = Hashmap()

    for step in get_input():
        hash_map.process_step(step)

    print(hash_map.get_focusing_power())


if __name__ == '__main__':
    main()
