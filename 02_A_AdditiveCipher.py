def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():  # only shift alphabets
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char  # keep spaces/punctuation unchanged
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


# Example usage:
plaintext = "HELLO WORLD"
key = 3

ciphertext = caesar_encrypt(plaintext, key)
decrypted = caesar_decrypt(ciphertext, key)

print("Plaintext: ", plaintext)
print("Encrypted: ", ciphertext)
print("Decrypted: ", decrypted)
