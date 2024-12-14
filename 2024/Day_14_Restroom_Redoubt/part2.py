import functools
import os
from typing import NamedTuple
import re

from tqdm import tqdm


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



def create_robots_grid(robots, width, height, steps):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for x, y in map(functools.partial(get_robot_position, width=width, height=height, steps=steps), robots):
        grid[y][x] += 1
    return grid


def main():
    robots = parse_input()

    #width = 11
    #height = 7
    width = 101
    height = 103
    with open('output.txt', 'w') as f:
        for steps in tqdm(range(0, 10000)):
            grid = create_robots_grid(robots, width, height, steps)
            f.write('_'*100)
            f.write(f'\nImage -> Step = {steps}\n')
            f.write('\n')
            f.write('\n'.join(''.join(map(lambda d: '.' if d==0 else str(d), row)) for row in grid))
            f.write('\n')



if __name__ == '__main__':
    main()