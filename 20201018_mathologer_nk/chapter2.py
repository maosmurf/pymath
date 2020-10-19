from itertools import chain, islice, takewhile


def generator():
    i = 1
    while True:
        yield i
        i += 1


def yellow():
    return generator()


def green():
    return map(lambda k: 2 * k + 1, generator())


def steps():
    return chain.from_iterable(zip(yellow(), green()))


def positions():
    position = 1
    _steps = steps()
    while True:
        yield position
        position += next(_steps)


def factors():
    while True:
        yield 1
        yield 1
        yield -1
        yield -1


def summand(_sequence, tup):
    a = tup[0]
    idx = len(_sequence) - tup[1]
    b = _sequence[idx]
    return a * b


def summands(_sequence, n):
    _positions = takewhile(lambda p: p < n, positions())
    _factors = factors()
    return map(lambda tup: summand(_sequence, tup), zip(_factors, _positions))


def sequence():
    n = 1
    _item = 1
    _sequence = [_item]
    while True:
        print('n: {n}, item: {item}'.format(n=n, item=_item))
        yield _item
        n += 1
        _item = sum(summands(_sequence, n), 0)
        _sequence.append(_item)


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


print(take(666, sequence()))
