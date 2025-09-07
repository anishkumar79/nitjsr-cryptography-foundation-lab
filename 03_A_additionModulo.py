def poly_add_mod2(p1, p2):
    return p1 ^ p2   

if __name__ == "__main__":
  
    p1 = 0b1011
    p2 = 0b0111

    result = poly_add_mod2(p1, p2)
    print("Result (binary):", bin(result))
    print("Result (decimal):", result)
