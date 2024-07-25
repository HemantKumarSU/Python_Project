def caesar_cipher(text, shift, mode='encrypt'):
   
    result = ""
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def get_user_input():
    
    message = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")
    return message, shift

def main():
    
    while True:
        print("\nCaesar Cipher Program")
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        
        if choice not in ['e', 'd']:
            print("Invalid choice. Please select 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message, shift = get_user_input()
        
        if choice == 'e':
            result = caesar_cipher(message, shift, mode='encrypt')
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher(message, shift, mode='decrypt')
            print(f"Decrypted message: {result}")
        
        another = input("Do you want to process another message? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using the Caesar Cipher Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
