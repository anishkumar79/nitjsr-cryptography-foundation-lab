def poly_mul_mod2_efficient(a, b, mod_poly):
    result = 0
    deg_mod = mod_poly.bit_length() - 1  # degree of mod_poly
    
    while b:
        if b & 1:  # if current bit of b is 1
            result ^= a  # add current a
        b >>= 1
        a <<= 1
    
        if a.bit_length() > deg_mod:
            a ^= mod_poly
    return result



if __name__ == "__main__":
    
    mod_poly = 0b10011
    a = 0b1011
    b = 0b0110
    
    result = poly_mul_mod2_efficient(a, b, mod_poly)
    print("Result (binary):", bin(result))
    print("Result (decimal):", result)

    
    
    
   