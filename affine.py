
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            result += chr(((a * x + b) % 26) + ord('A'))
        else:
            result += char  
    return result


def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)  
    for char in cipher.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            result += chr(((a_inv * (y - b)) % 26) + ord('A'))
        else:
            result += char
    return result






ciphertext="WVZCPSCFZQCUUIMC"
key = [1,3,5,7,9,11,15,17,19,21,23,25]

for i in key:
    for j in range (26):
        decrypted=affine_decrypt(ciphertext,i,j)
        print(i ,j, decrypted)