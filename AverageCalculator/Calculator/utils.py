def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    """Check if a number is a Fibonacci number."""
    x1 = 5 * (n**2) + 4
    x2 = 5 * (n**2) - 4
    return int(x1**0.5)**2 == x1 or int(x2**0.5)**2 == x2

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if a number is odd."""
    return n % 2 != 0
