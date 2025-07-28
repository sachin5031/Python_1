# Encryption function
def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Handle uppercase and lowercase letters
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)  # Shift letter
            result += new_char
        else:
            result += char  # If not a letter, add it as is (for spaces, punctuation)
    return result

# Decryption function
def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Handle uppercase and lowercase letters
            new_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)  # Reverse the shift
            result += new_char
        else:
            result += char  # If not a letter, add it as is
    return result

# Program loop for user interaction
while True:
    # Display menu
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    # Get user's choice
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':  # Encryption
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message: ", encrypted_message)
    
    elif choice == '2':  # Decryption
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted Message: ", decrypted_message)
    
    elif choice == '3':  # Exit
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and program
    
    else:
        print("Invalid choice, please try again.")
