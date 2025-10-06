import random

def is_prime_miller_rabin(n, k=5):
    """Miller-Rabin Primality Test"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Step 1: Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Step 2: Repeat test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # compute a^d % n

        if x == 1 or x == n - 1:
            continue  # this round passed

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # composite

    return True  # probably prime

# Test the function
test_numbers = [2, 3, 4, 5, 17, 20, 23, 25, 561]  # 561 is a Carmichael number
for num in test_numbers:
    print(f"{num} is prime? {is_prime_miller_rabin(num)}")
