from math import gcd
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  

def multiplicative_encrypt(ciphertext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26 for decryption to work.")
    
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            P = ord(char) - base
            C = (P * key) % 26
            result += chr(C + base)
        else:
            result += char
    return result


def multiplicative_decrypt(ciphertext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26 for decryption to work.")
    
    inv_key = mod_inverse(key, 26)
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            C = ord(char) - base
            P = (C * inv_key) % 26
            result += chr(P + base)
        else:
            result += char
    return result


ciphertext = "WNYJCLHAPPVSPWI"
key = [1,3,5,7,9,11,15,17,19,21,23,25]


for i in key:
    print(i)
    decrypted=multiplicative_decrypt(ciphertext,i)
    print(decrypted)
