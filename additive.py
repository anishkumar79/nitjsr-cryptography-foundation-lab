def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char  
    return result



def caesar_decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result



ciphertext="PDALANWPEKJOPWNP"
for i in range(0,25):
    print(i)
    decrypted=caesar_decrypt(ciphertext,i)
    print(decrypted)


