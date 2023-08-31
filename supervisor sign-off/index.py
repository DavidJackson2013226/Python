# supervisor sign-off

"""Python code"""


passwordDatabase = {}

def addCredentials(website, username, password):
    if website not in passwordDatabase:
        passwordDatabase[website] = {"username": username, "password": password}
        print("Credentials added for", website)
    else:
        print("Website already exists in the database.")

def viewCredentials(website):
    if website in passwordDatabase:
        credentials = passwordDatabase[website]
        print("Website:", website)
        print("Username:", credentials["username"])
        print("Password:", credentials["password"])
    else:
        print("Website not found in the database.")

def main():
    while True:
        print("Welcome to Password Manager!")
        print("1. Add Credentials")
        print("2. View Credentials")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            addCredentials(website, username, password)
        elif choice == "2":
            website = input("Enter website: ")
            viewCredentials(website)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()


"""Create a filename"""

filename = "credentials.txt"


    
with open(filename, "r"):
    print("File already exists.")
    
with open(filename, "w") as file:
    print("File created for credential storage.")

"""Append new records"""

filename = "credentials.txt"

new_record = "New record to append\n"


with open(filename, "a") as file:
    file.write(new_record)

"""Text file Content display"""

def display_credentials(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    print("Credentials:")
    print("=" * 20)

    for line in lines:
        line = line.strip()
        if line:
            heading, value = line.split(":")
            print(f"{heading.strip()}: {value.strip()}")
        else:
            print()

    print("=" * 20)

filename = "credentials.txt"
display_credentials(filename)

"""Handle any input"""

def add_record():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    


def main():
    while True:
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

"""Include embedded explanatory"""

def add_record():
    
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    

def view_records():
    
    pass

def main():
    while True:
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_record()  # Call the function to add a new record
        elif choice == "2":
            view_records()  # Call the function to view records
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()


"""Provide simple rot3 encryption"""

def rot3_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 3
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A' if char.isupper() else 'a') + offset) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A' if char.isupper() else 'a') + offset) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


plaintext = "Hello, World!"
encrypted_text = rot3_encrypt(plaintext)
print("Encrypted:", encrypted_text)
