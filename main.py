from crypto_utils import encrypt_file, decrypt_file
from password_manager import PasswordManager
from steganography import hide_message, extract_message

def menu():
    print("\n=== Cryptography Toolkit ===")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Password Manager")
    print("4. Hide Message in Image")
    print("5. Extract Message from Image")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        f = input("Input file: ")
        out = input("Output file: ")
        pwd = input("Password: ")
        encrypt_file(f, out, pwd)

    elif choice == "2":
        f = input("Encrypted file: ")
        out = input("Output file: ")
        pwd = input("Password: ")
        decrypt_file(f, out, pwd)

    elif choice == "3":
        master = input("Master password: ")
        pm = PasswordManager(master)

        print("1. Add Entry")
        print("2. Get Entry")
        print("3. List Services")

        sub = input("Choose: ")

        if sub == "1":
            s = input("Service: ")
            u = input("Username: ")
            p = input("Password: ")
            pm.add_entry(s, u, p)

        elif sub == "2":
            s = input("Service: ")
            print(pm.get_entry(s))

        elif sub == "3":
            print(pm.list_services())

    elif choice == "4":
        img = input("Image path: ")
        msg = input("Message: ")
        out = input("Output image: ")
        hide_message(img, msg, out)

    elif choice == "5":
        img = input("Image path: ")
        print("Hidden Message:", extract_message(img))

    elif choice == "6":
        break

    else:
        print("Invalid choice")