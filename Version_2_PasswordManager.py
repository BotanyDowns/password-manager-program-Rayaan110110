# Version 2

# Creating an empty dictionary to store account name and password
passwords = {}

# Using functions to add, get, update, delete and show passwords from the passwords dictionary

# Function to add account and password to the passwords dictionary
def add_password(account, password):
    passwords[account] = password

# Function to get the password for an account from the passwords dictionary
def get_password(account):
    return passwords.get(account, None)

# Function to update the password for an account in the passwords dictionary
def update_password(account, password):
    if account in passwords:
        passwords[account] = password
        print(f"Password for {account} updated successfully")
    else:
        print(f"No password found for {account}")

# Function to delete the password for an account from the passwords dictionary
def delete_password(account):
    if account in passwords:
        del passwords[account]
        print(f"Deleted password for {account}")
    else:
        print(f"No password found for {account}")

# Function to show all the passwords stored in the passwords dictionary
def show_passwords():
    if passwords:
        print("List of stored passwords:")
        for account, password in passwords.items():
            print(f"{account}: {password}")
    else:
        print("No passwords stored yet")

#Main routine
def main():
    while True:
        # Display the menu options
        print("1. Add Password")
        print("2. Get Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Show Passwords")
        print("6. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Perform the action based on the user's choice
        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            add_password(account, password)
        elif choice == "2":
            account = input("Enter account name: ")
            password = get_password(account)
            if password:
                print(f"Password for {account}: {password}")
            else:
                print(f"No password found for {account}")
        elif choice == "3":
            account = input("Enter account name: ")
            password = input("Enter new password: ")
            update_password(account, password)
        elif choice == "4":
            account = input("Enter account name: ")
            delete_password(account)
        elif choice == "5":
            show_passwords()
        elif choice == "6":
            break
        else:
            print("Please choose between 1 and 6")

if __name__ == "__main__":
    main()
