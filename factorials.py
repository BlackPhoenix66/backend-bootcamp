def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)