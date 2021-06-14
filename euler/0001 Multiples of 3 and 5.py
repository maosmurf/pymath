sumOfMultiples = 0

limit = 1000

for x in range(1, limit):
    if (x % 3 == 0) or (x % 5 == 0):
        sumOfMultiples += x

print(sumOfMultiples)
