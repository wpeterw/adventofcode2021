counter = 0
for i,x in enumerate(numbers):
    if i > 0 and numbers[i] > numbers[i-1]:
        print(f"{numbers[i]} is higher than {numbers[i-1]}")
        counter += 1
print(counter)
