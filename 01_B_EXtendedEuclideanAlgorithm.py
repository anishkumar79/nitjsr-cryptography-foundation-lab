def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1

# User input
a = int(input("Enter a: "))
b = int(input("Enter b: "))

g, x, y = extended_gcd(a, b)

print("gcd:", g)
print("x:", x)
print("y:", y)
