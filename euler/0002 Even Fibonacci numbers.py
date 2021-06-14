sumOfEvens = 0

limit = 4000000

a = 1
b = 2

while a <= limit:
    if a % 2 == 0:
        sumOfEvens += a
    c = a
    d = b
    a = b
    b = c + d

print(sumOfEvens)
