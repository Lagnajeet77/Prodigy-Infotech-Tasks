def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Shift character within alphabet
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return

    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter a number.")
        return

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
