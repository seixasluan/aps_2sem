def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else: 
                encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted += char
    
    print(f"encrypted message: {encrypted}")
    return encrypted

def decrypt(encryptedMsg, key):
    decrypted = ""
    for char in encryptedMsg:
        if char.isalpha():
            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else: 
                decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted += char
        
    print(f"decrypted message: {decrypted}")
    return decrypted

def main():
    while True:
        option = input("Do you deserve to encrypt (1) or decrypt (2) a message? answer with 1 or 2: ")
        if option == "1": 
            message = input("Enter a message to encrypt: ")
            key = int(input("Enter a key to encrypt (only number): "))
            encrypt(message, key)
            break
        elif option == "2":
            message = input("Enter a message to decrypt: ")
            key = int(input("Enter a key to decrypt (only number): "))
            decrypt(message, key)
            break
        else:
            print("Your answer is not valid, please answer it again!")

if _name_ == "_main_":
    main()