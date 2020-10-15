def coeff(coeffs, n, k):
    left = coeffs[k - 1] if 0 < k else 0
    right = coeffs[k] if k < n else 0
    return left + right


def row(coeffs, n):
    return [coeff(coeffs, n, k) for k in range(0, n + 1)]


def odds(n, _row, _odds_prev):
    _len_prev = n * (n + 1) / 2
    _len_this = n + 1
    _len_total = _len_prev + _len_this

    _odds_this = sum(1 for _ in filter(lambda x: x & 1, _row))
    _odds_total = _odds_prev + _odds_this

    _ratio = _odds_total / _len_total * 100

    return _odds_total, _len_total, _ratio


def pascal(n):
    if n == 0:
        return [1], 1, 1
    _coeffs, _odds_prev, _total_prev = pascal(n - 1)
    _row = row(_coeffs, n)
    _odds, _total, _ratio = odds(n, _row, _odds_prev)
    print(n, _ratio)
    return _row, _odds, _total


_pascal = pascal(127)
