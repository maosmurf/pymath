import copy

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    else:
        for i in range(2, (x // 2 + 1)):
            if (x % i) == 0:
                return False
        return True


def init(n):
    _graph = {}
    for x in range(1, n + 1):
        _graph[x] = []
        for y in range(1, x):
            if is_prime(x + y):
                _graph[x].append(y)
                _graph[y].append(x)

    for v in _graph:
        if not _graph[v]:
            print('Game ¯\_(ツ)_/¯ Over {v}'.format(v=v))
            exit(-1)

    return _graph

def remove_vertex(_graph, v):
    _sub = copy.deepcopy(_graph)
    v2s = _sub[v]
    for v2 in v2s:
        _sub[v2].remove(v)
    del _sub[v]
    return _sub


def hampaths(pre, graph):
    v1 = pre[-1]
    if not graph:
        return []
    if not graph[v1]:
        if (len(graph) == 1 and next(iter(graph.keys())) == v1):
            return [pre]
        else:
            return []

    paths = []
    for v2 in graph[v1]:
        sub = remove_vertex(graph, v1)
        subpaths = hampaths(pre + [v2], sub)
        for subpath in subpaths:
            paths.append(subpath)

    return paths


_graph = init(9)

print(_graph)
# {1: [2, 4, 6], 2: [1, 3, 5, 9], 3: [2, 4, 8], 4: [1, 3, 7, 9], 5: [2, 6, 8], 6: [1, 5, 7], 7: [4, 6], 8: [3, 5, 9], 9: [2, 4, 8]}

_hampaths = hampaths([1], _graph)

print(len(_hampaths))
# 30

print(_hampaths)
# [
#   [1, 2, 3, 4, 7, 6, 5, 8, 9],
#   [1, 2, 3, 4, 9, 8, 5, 6, 7],
#   [1, 2, 3, 8, 5, 6, 7, 4, 9],
#   [1, 2, 3, 8, 9, 4, 7, 6, 5],
#   [1, 2, 5, 6, 7, 4, 3, 8, 9],
#   [1, 2, 5, 6, 7, 4, 9, 8, 3],
#   [1, 2, 9, 4, 3, 8, 5, 6, 7],
#   [1, 2, 9, 4, 7, 6, 5, 8, 3],
#   [1, 2, 9, 8, 3, 4, 7, 6, 5],
#   [1, 2, 9, 8, 5, 6, 7, 4, 3],
#   [1, 4, 3, 2, 9, 8, 5, 6, 7],
#   [1, 4, 3, 8, 9, 2, 5, 6, 7],
#   [1, 4, 7, 6, 5, 2, 3, 8, 9],
#   [1, 4, 7, 6, 5, 2, 9, 8, 3],
#   [1, 4, 7, 6, 5, 8, 3, 2, 9],
#   [1, 4, 7, 6, 5, 8, 9, 2, 3],
#   [1, 4, 9, 2, 3, 8, 5, 6, 7],
#   [1, 4, 9, 8, 3, 2, 5, 6, 7],
#   [1, 6, 5, 2, 3, 8, 9, 4, 7],
#   [1, 6, 5, 2, 9, 8, 3, 4, 7],
#   [1, 6, 5, 8, 3, 2, 9, 4, 7],
#   [1, 6, 5, 8, 9, 2, 3, 4, 7],
#   [1, 6, 7, 4, 3, 2, 5, 8, 9],
#   [1, 6, 7, 4, 3, 2, 9, 8, 5],
#   [1, 6, 7, 4, 3, 8, 5, 2, 9],
#   [1, 6, 7, 4, 3, 8, 9, 2, 5],
#   [1, 6, 7, 4, 9, 2, 3, 8, 5],
#   [1, 6, 7, 4, 9, 2, 5, 8, 3],
#   [1, 6, 7, 4, 9, 8, 3, 2, 5],
#   [1, 6, 7, 4, 9, 8, 5, 2, 3]
# ]

