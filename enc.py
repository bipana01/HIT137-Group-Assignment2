def encrypt(raw, n, m):
    encrypted = ''
    for c in raw:
        if 'a' <= c <= 'm':
            encrypted += chr((ord(c) - ord('a') + (n * m)) % 13 + ord('a'))
        elif 'n' <= c <= 'z':
            encrypted += chr((ord(c) - ord('n') - (n + m)) % 13 + ord('n'))
        elif 'A' <= c <= 'M':
            encrypted += chr((ord(c) - ord('A') - n) % 13 + ord('A'))
        elif 'N' <= c <= 'Z':
            encrypted += chr((ord(c) - ord('N') + (m ** 2)) % 13 + ord('N'))
        else:
            encrypted += c
    return encrypted

def decrypt(encrypted, n, m):
    decrypted = ''
    for c in encrypted:
        if 'a' <= c <= 'm':
            decrypted += chr((ord(c) - ord('a') - (n * m)) % 13 + ord('a'))
        elif 'n' <= c <= 'z':
            decrypted += chr((ord(c) - ord('n') + (n + m)) % 13 + ord('n'))
        elif 'A' <= c <= 'M':
            decrypted += chr((ord(c) - ord('A') + n) % 13 + ord('A'))
        elif 'N' <= c <= 'Z':
            decrypted += chr((ord(c) - ord('N') - (m ** 2)) % 13 + ord('N'))
        else:
            decrypted += c
    return decrypted

def verify(raw, decrypted):
    return raw == decrypted

# Main block
try:
    # Input validation
    while True:
        try:
            n = int(input("Enter integer n: "))
            m = int(input("Enter integer m: "))
            break
        except ValueError:
            print("Invalid input. Please enter integer values for n and m.")

    # Read raw text
    try:
        with open('raw_text.txt', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")
        exit(1)

    # Encrypt and save to file
    encrypted_text = encrypt(raw_text, n, m)
    try:
        with open('encrypted_text.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted_text)
        print("\nEncrypted Text:")
        print(encrypted_text)
    except Exception as e:
        print("Error writing to 'encrypted_text.txt':", e)
        exit(1)

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, n, m)
    print("\nDecrypted Text:")
    print(decrypted_text)

    # Verify the result
    is_correct = verify(raw_text, decrypted_text)
    print("\nDecryption Correct:", is_correct)

except Exception as e:
    print("An unexpected error occurred:", str(e))
