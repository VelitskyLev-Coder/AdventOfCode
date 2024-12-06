pairs = []
with open('input.txt') as input_file:
    for line in input_file:
        if line.strip():
            pairs.append(tuple(map(int, line.split())))

list1, list2 = list(zip(*pairs))
result = 0
for n1, n2 in zip(sorted(list1), sorted(list2)):
    result += abs(n1-n2)

print(result)