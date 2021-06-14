import math

n = 600851475143
m = math.floor(math.sqrt(n))


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    else:
        for i in range(2, (math.floor(math.sqrt(x)) + 1)):
            if (x % i) == 0:
                return False
        return True


p = n

for f in range(m + 1, 1, -1):
    if n % f == 0:
        if is_prime(f):
            print(f)
            exit(0)
        if is_prime(n // f):
            p = n // f

print(p)
