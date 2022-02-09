data = [int(x) for x in input().split()]

result = []
for el in range(len(data)):
    result.append(data.pop())

print(" ".join([str(x) for x in result]))