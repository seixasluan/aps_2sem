def safe_int(prompt: str) -> int:
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Plese, enter a valid integer number.")

def get_file_name(prompt: str) -> str:

    file_name = input(prompt).strip()
    if file_name.lower().endswith(".txt"):
        file_name = file_name[:-4] 
    return file_name + ".txt"

def shift_char(ch: str, key: int, encrypt: bool = True) -> str:

    if 'A' <= ch <= 'Z':
        k = key if encrypt else -key
        return chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        k = key if encrypt else -key
        return chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    else:
        return ch  


def encrypt(message: str, key: int):
   
    encrypted = "".join(shift_char(ch, key, encrypt=True) for ch in message)
    file_name = get_file_name("Enter the file name to save the encrypted message: ")

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(encrypted)
        print(f"\n✅ Message encrypted and saved to '{file_name}'\n")
    except Exception as e:
        print(f"❌ Error to save file: {e}")


def decrypt(file_name: str, key: int):
   
    file_name = file_name.strip()
    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            encryptedMsg = file.read()
    except FileNotFoundError:
        print(f"❌ File '{file_name}' not found!")
        return
    except Exception as e:
        print(f"❌ Error to read file: {e}")
        return

    decrypted = "".join(shift_char(ch, key, encrypt=False) for ch in encryptedMsg)
    print(f"\n🔓 Decrypted message:\n{decrypted}\n")


def main():
 
    while True:
        print("\n=== MAIN MENU ===")
        option = input("[1] Encrypt 🔒\n[2] Decrypt 🔓\nEnter 1 or 2: ").strip()

        if option == "1":
            message = input("Enter a message to encrypt: ")
            key = safe_int("Enter a key to encrypt (only number): ")
            encrypt(message, key)
            break

        elif option == "2":
            file_name = input("Enter the file name to decrypt: ")
            key = safe_int("Enter a key to decrypt (only number): ")
            decrypt(file_name, key)
            break

        else:
            print("⚠️ Invalid Answer. Please, enter 1 or 2.")

if __name__ == "__main__":
    main()