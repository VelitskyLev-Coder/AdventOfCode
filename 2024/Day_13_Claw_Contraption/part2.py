from typing import NamedTuple
import re


class XYPair(NamedTuple):
    X: int
    Y: int


class MachineSpec(NamedTuple):
    A: XYPair
    B: XYPair
    Prize: XYPair



def parse_input()-> list[MachineSpec]:
    with open('input.txt') as input_file:
        lines = [e.strip() for e in filter(lambda s: s.strip(), input_file)]
    machines: list[MachineSpec] = list()
    for a, b, prize in zip(lines[::3], lines[1::3], lines[2::3]):
        pattern_a = re.compile(r'^Button A: X(?P<x_a>[\-+]\d+), Y(?P<y_a>[\-+]\d+)$')
        pattern_b = re.compile(r'^Button B: X(?P<x_b>[\-+]\d+), Y(?P<y_b>[\-+]\d+)$')
        pattern_prize = re.compile(r'^Prize: X=(?P<x>\d+), Y=(?P<y>\d+)$')
        match_a = re.match(pattern_a, a)
        match_b = re.match(pattern_b, b)
        match_prize = re.match(pattern_prize, prize)

        machines.append(MachineSpec(
            A=XYPair(
                X=int(match_a.group('x_a')),
                Y=int(match_a.group('y_a'))
            ),
            B=XYPair(
                X=int(match_b.group('x_b')),
                Y=int(match_b.group('y_b'))
            ),
            Prize=XYPair(
                X=int(match_prize.group('x')) + 10000000000000,
                Y=int(match_prize.group('y')) + 10000000000000
            ),
        ))
    return machines


class SingularError(ValueError):
    pass

def get_min_prize(machine: MachineSpec)-> int:
    det = machine.A.X*machine.B.Y - machine.A.Y*machine.B.X
    if det == 0:
        raise SingularError('This function is designed to 1 possible solution. But the system is singular')

    t_2_with_det = machine.A.X*machine.Prize.Y-machine.Prize.X*machine.A.Y
    t_1_with_det = -(machine.B.X*machine.Prize.Y-machine.Prize.X*machine.B.Y)

    if t_1_with_det%det != 0 or t_2_with_det%det !=0:
        raise ValueError('No integer solutions!')

    t1 = t_1_with_det//det
    t2 = t_2_with_det//det
    print(f'{machine} -> {t1=}, {t2=}, {t1*3+t2=}')
    return t1*3+t2


def main():
    machines = parse_input()
    result = 0
    for machine in machines:
        try:
            result += get_min_prize(machine)
        except SingularError:
            raise
        except ValueError:
            print(f'No solutions for {machine}')



    print(result)

if __name__ == '__main__':
    main()