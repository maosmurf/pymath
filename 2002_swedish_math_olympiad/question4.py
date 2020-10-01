def fn(n):
    return pow(n, (1 / (n - 7)))


for x in range(10, 25):
    y = fn(x)
    print('{x} -> {y}'.format(x=x, y=y))
    if y.is_integer(): break
