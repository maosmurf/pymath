start = 100
end = 999
x = 0


def is_palindrome(x):
    s = str(x)
    r = s[::-1]
    return s == r


for n in range(end, start - 1, -1):
    for m in range(end, n - 1, -1):
        p = n * m
        if is_palindrome(p) and p > x:
            x = p

print(x)
