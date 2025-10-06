import random

def is_prime_fermat(n, k=5):
    """
    Fermat Primality Test
    n: number to test
    k: number of iterations (more iterations -> more accuracy)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)  # choose random a
        # Fermat's little theorem check
        if pow(a, n-1, n) != 1:
            return False  # definitely composite

    return True  # probably prime

# Test the function
test_numbers = [2, 3, 4, 5, 17, 20, 23, 25, 561]  # 561 is a Carmichael number
for num in test_numbers:
    print(f"{num} is prime? {is_prime_fermat(num)}")
