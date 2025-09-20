from utils import save_user_data

def limits(data, username=None):
    while True:
        print("\nSet Limits")
        print("1. Total Amount\n2. Food\n3. Stationary\n4. Clothes\n5. Other\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '6':
            print("Exiting...")
            break

        categories = ['Total Amount', 'Food', 'Stationary', 'Clothes', 'Other']
        if choice in map(str, range(1, 6)):
            category = categories[int(choice)-1]
            try:
                limit_user = float(input(f"Enter limit for '{category}': ₹"))
                data[category]['limit'] = limit_user
                print(f"₹{limit_user} limit set for {category}")
                if username:
                    save_user_data(username, data)
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! (1-6 only)")

        if input("\nSet more limits? (y/n): ").lower() != 'y':
            break