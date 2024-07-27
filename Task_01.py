def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = encrypt(text, shift)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(text, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        
        another = input("Would you like to encrypt/decrypt another message? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
