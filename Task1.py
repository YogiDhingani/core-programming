n = int(input("Enter number of values: "))
numbers = []

for i in range(0,n):
    value = int(input())
    numbers.append(value)

def largest(numbers):

    max = numbers[0]

    for i in range(0,n):
        if numbers[i] > max:
            max = numbers[i]

    return max

print("Largest number is:",largest(numbers))
