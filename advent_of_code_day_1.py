# part 1
print(sum(x < y for x, y in zip(numbers, numbers[1:])))

# part 2
print(sum(x < y for x, y in zip(numbers, numbers[3:])))
