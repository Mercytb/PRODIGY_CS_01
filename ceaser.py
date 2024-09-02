def main():
    letters = {chr(i): i - 65 for i in range(65, 91)}

    def encrypt_message(shift):
        message = input("Enter a message: ").upper().replace(" ", "")
        print("Message:", message)
        cipher_text = ""
        for char in message:
            if char in letters:
                sum = (letters[char] + shift) % 26
                cipher_text += chr(sum + 65)
            else:
                cipher_text += char
        print("Cipher Text:", cipher_text)

    def decrypt_message(shift):
        message = input("Enter a message: ").upper().replace(" ", "")
        print("Message:", message)
        plain_text = ""
        for char in message:
            if char in letters:
                sum = (letters[char] - shift) % 26
                plain_text += chr(sum + 65)
            else:
                plain_text += char
        print("Plain Text:", plain_text)

    while True:
        choice = input("Encryption or Decryption (or type 'quit' to exit): ").upper()
        if choice in ["ENCRYPTION", "DECRYPTION"]:
            try:
                shift = int(input("Enter the shift value (integer): "))
            except ValueError:
                print("Error: Invalid shift value. Please enter an integer.")
                continue

            if choice == "ENCRYPTION":
                encrypt_message(shift)
            elif choice == "DECRYPTION":
                decrypt_message(shift)
        elif choice == "QUIT":
            print("Thank You")
            break
        else:
            print("Error: Invalid choice")

if __name__ == '__main__':
    main()

