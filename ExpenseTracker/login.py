import json
import getpass
from utils import load_user_data, save_user_data

USER_FILE = "users.json"

def manual(username):
    from Function import data
    from limits import limits
    
    print(f"\nHi {username}!!")
    choice = input("Would you like a Startup Tutorial (y/n): ").lower()
    
    if choice == 'y':
        print("Let's start with setting your limits and total amount:\n")
        user_data = data()
        limits(user_data)
        save_user_data(username, user_data)

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def login():
    users = load_users()
    while True:
        print("\n1. Login\n2. Create Account\n3. Exit")
        choice = input("Enter Your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            
            if users.get(username) and users[username]["password"] == password:
                print("Login successful!")
                user_data = load_user_data(username) 
                return username, user_data
            print("Invalid username or password!")

        elif choice == '2':
            username = input("Enter a new username: ")
            if username in users:
                print("Username already exists!")
                continue
                
            password = getpass.getpass("Enter a new password: ")
            users[username] = {"password": password}
            save_users(users)
            manual(username)
            return username, load_user_data(username)

        elif choice == '3':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice!")