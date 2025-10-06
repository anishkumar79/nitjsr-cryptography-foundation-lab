import math

def is_prime(n):
    # Step 1: Handle small numbers
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Step 2: Check divisibility by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Step 3: Check for divisibility from 5 to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # check next possible divisor
    
    return True

# Test the function
test_numbers = [1, 2, 3, 4, 5, 17, 20, 23, 25]
for num in test_numbers:
    print(f"{num} is prime? {is_prime(num)}")
