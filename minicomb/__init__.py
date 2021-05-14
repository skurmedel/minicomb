
def factorial(k: int):
    """Calculates the factorial of a given integer k. Negative numbers are not allowed.

    Since the size of a factorial grows quickly, it may be more useful to use the Factorial class.

    This is not the fastest implementation available.

    >>> factorial(2)
    2
    >>> factorial(4)
    24
    """
    k = int(k)
    if k < 0:
        raise ValueError("k is negative.")
    if k == 0:
        return 1

    # TODO: use a better algorithm
    # TODO: maybe use a lookup for low numbers.

    n = 1
    for i in range(1, k + 1):
        n *= i
    return n


def binomial(n: int, k: int) -> int:
    """Calculates the binomial coefficient of (n, k).

    Defined as 

        \frac{n!}{k! \cdot (n-k)!}
    
    We also have the following equality:

        TODO: fill me in

    Can be used to calculate unordered selections of k items from n possible.
    
    >>> binomial(4, 2)
    6

    Or the number of unordered selections of k items from n possible with repetitions:

    >>> binomial(4 + 2 - 1, 2)
    10

    n must be non-negative. For k <= 0, this returns zero no matter what, which is mostly for 
    convenience.

    For k > n, this returns zero.
    """
    n, k = int(n), int(k)
    if n < 0:
        raise ValueError("negative n is not allowed.")
    if k > n or  k < 0:
        return 0
    
    # TODO: make this more efficient
    return factorial(n) // (factorial(k) * factorial(n - k))
