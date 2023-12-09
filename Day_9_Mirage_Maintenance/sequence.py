import itertools
from typing import Iterable


class Sequence:
    def __init__(self, numbers: Iterable[int]):
        self.sequence = list(numbers)

    def get_difference_seq(self) -> 'Sequence':
        return Sequence((b - a for a, b in itertools.pairwise(self.sequence)))

    def interpolate_one_forward(self):
        if all(a == 0 for a in self.sequence):
            self.sequence.append(0)
            return
        difference_seq = self.get_difference_seq()
        difference_seq.interpolate_one_forward()
        self.sequence.append(self.get_last() + difference_seq.get_last())

    def interpolate_one_backward(self):
        if all(a == 0 for a in self.sequence):
            self.sequence.insert(0, 0)
            return
        difference_seq = self.get_difference_seq()
        difference_seq.interpolate_one_backward()
        self.sequence.insert(0, self.get_first() - difference_seq.get_first())

    def get_last(self) -> int:
        return self.sequence[-1]

    def get_first(self) -> int:
        return self.sequence[0]

    def __repr__(self):
        return str(self.sequence)
