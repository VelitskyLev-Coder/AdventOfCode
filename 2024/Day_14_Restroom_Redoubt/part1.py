import functools
import operator
from typing import NamedTuple
import re


class RobotInfo(NamedTuple):
    x_start: int
    y_start: int
    v_x: int
    v_y: int

def parse_input()-> list[RobotInfo]:
    with open('input.txt') as input_file:
        lines = [e.strip() for e in filter(lambda s: s.strip(), input_file)]
    robots: list[RobotInfo] = list()
    for line in lines:
        pattern = re.compile(r'^p=(?P<x_start>[\-+]?\d+),(?P<y_start>[\-+]?\d+) v=(?P<v_x>[\-+]?\d+),(?P<v_y>[\-+]?\d+)$')
        match = re.match(pattern, line)

        robots.append(RobotInfo(
            x_start=int(match.group('x_start')),
            y_start=int(match.group('y_start')),
            v_x=int(match.group('v_x')),
            v_y=int(match.group('v_y'))
        ))
    return robots

def get_robot_position(robot: RobotInfo, width: int, height:int, steps: int) -> tuple[int, int]:
    final_x = (robot.x_start + steps*robot.v_x) % width
    final_y = (robot.y_start + steps*robot.v_y) % height

    return final_x, final_y


def main():
    robots = parse_input()

    #width = 11
    #height = 7
    width = 101
    height = 103
    steps = 100

    robots_per_region: dict[int, int] = dict()
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for x, y in map(functools.partial(get_robot_position,width=width, height=height, steps=steps), robots):
        grid[y][x] += 1
        if x == width // 2 or y==height//2:
            continue
        region_index = x//(width//2+1)+y//(height//2+1)*2
        robots_per_region[region_index] = robots_per_region.get(region_index, 0) + 1


    print(functools.reduce(operator.mul, robots_per_region.values()))

if __name__ == '__main__':
    main()