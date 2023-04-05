def _current(n):
    return n * (n + 1) / 2


def _next(n):
    return (n + 1) * (n + 2) / 2


for i in range(1000):
    print(_current(i + 1) == _next(i))
