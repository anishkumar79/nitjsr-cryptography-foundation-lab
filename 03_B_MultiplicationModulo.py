def poly_mul_mod2(a, b, mod_poly):
    result = 0
    while b:  # standard shift-and-add multiplication
        if b & 1:  # if lowest bit of b is 1
            result ^= a  # add (XOR)
        b >>= 1
        a <<= 1
        if a.bit_length() >= mod_poly.bit_length():
            a ^= mod_poly
    return result



if __name__ == "__main__":
     mod_poly = 0b10011
     a = 0b1011
     b = 0b0110
    
     result = poly_mul_mod2(a, b, mod_poly)
     print("Result (binary):", bin(result))
     print("Result (decimal):", result)
