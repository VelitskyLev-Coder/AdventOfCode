import itertools



def is_report_safe(report: list[int]) -> bool:
    if len(report) < 2:
        return True
    sign = report[1] > report[2]
    for a, b in itertools.pairwise(report):
        if (a > b) != sign or not (1<=abs(a-b)<=3):
            return False
    return True

def is_safe_with_remove(report: list[int]) -> bool:
    for i in range(len(report)):
        if is_report_safe(report[:i]+report[i+1:]):
            return True
    return False

def main():
    resorts = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                resorts.append(list(map(int, line.split())))

    print(sum(map(is_safe_with_remove, resorts)))


if __name__ == '__main__':
    main()