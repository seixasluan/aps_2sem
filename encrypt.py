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

    
    file_name = input('Enter the file name to record your encrypted message: ')
    file_name = file_name + ".txt"
    file_content = encrypted

    with open(file_name, 'w') as file:
        file.write(file_content)
    
    print(f"File '{file_name}' created and written to.")

def decrypt(file_name, key):
    file_name = file_name + ".txt"
    with open(file_name, "r") as file:
        encryptedMsg = file.read()
    
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

def main():
    while True:
        option = input("Do you deserve to encrypt (1) or decrypt (2) a message? answer with 1 or 2: ")
        if option == "1": 
            message = input("Enter a message to encrypt: ")
            key = int(input("Enter a key to encrypt (only number): "))
            encrypt(message, key)
            break
        elif option == "2":
            file_name = input("Enter the file name to decrypt: ")
            key = int(input("Enter a key to decrypt (only number): "))
            decrypt(file_name, key)
            break
        else:
            print("Your answer is not valid, please answer it again!")

if __name__ == "__main__":
    main()