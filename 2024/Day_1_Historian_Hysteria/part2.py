from collections import Counter
pairs = []
with open('input.txt') as input_file:
    for line in input_file:
        if line.strip():
            pairs.append(tuple(map(int, line.split())))

list1, list2 = list(zip(*pairs))

counter = Counter(list2)
result = 0

for n in list1:
    result += n*counter.get(n, 0)

print(result)