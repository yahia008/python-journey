n = int(input("Enter the number: "))

numbers = input("Enter the numbers: ").split()

for i in range(0, n):
    numbers[i] = int(numbers[i])

print(numbers)