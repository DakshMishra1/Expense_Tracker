import login
import limits
import spending
import Function
from utils import save_user_data

def menu(username, categories_data):
    while True:
        print("\nExpense Tracker Menu")
        print("1. View History\n2. Add Expenses\n3. Set Limits\n4. Track Spending\n5. Exit")
        
        try:
            choice = int(input("Enter Your choice: "))
            
            if choice == 1:
                Function.entries(categories_data, view_only=True)
            elif choice == 2:
                Function.entries(categories_data)
                save_user_data(username, categories_data)
            elif choice == 3:
                limits.limits(categories_data)
                save_user_data(username, categories_data)
            elif choice == 4:
                spending.check_spending(categories_data)
            elif choice == 5:
                save_user_data(username, categories_data)
                print("Data saved. Exiting...")
                break
            else:
                print("Choose 1-5 only")
                
        except ValueError:
            print("Numbers only please!")

if __name__ == "__main__":
    username, user_data = login.login()
    print(f"Welcome, {username}!")
    menu(username, user_data)