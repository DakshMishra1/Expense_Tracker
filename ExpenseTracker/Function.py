from utils import get_current_date

def data():
    return {
        'Total Amount': {'limit': 0, 'expenses': []},
        'Food': {'limit': 0, 'expenses': []},
        'Stationary': {'limit': 0, 'expenses': []},
        'Clothes': {'limit': 0, 'expenses': []},
        'Other': {'limit': 0, 'expenses': []},
    }

def entries(categories_data, view_only=False):
    if view_only:
        print("\n--- All Expenses ---")
        for cat, det in categories_data.items():
            if cat == 'Total Amount':
                continue
            print(f"\n{cat}:")
            if det['expenses']:
                for exp in det['expenses']:
                    date = exp.get('date', 'Unknown date')
                    print(f"  {date} - {exp['item']}: ₹{exp['amount']}")
            else:
                print("  No expenses")
        return
    
    while True:
        print("\nAdd Expenses")
        print("1. Food\n2. Stationary\n3. Clothes\n4. Other\n5. Back")
        
        try:
            choice = int(input("Choose category (1-5): "))
            if choice == 5:
                break
                
            cats = ['Food', 'Stationary', 'Clothes', 'Other']
            if 1 <= choice <= 4:
                category = cats[choice-1]
                item = input("Item name: ").strip()
                amount = float(input("Amount: ₹"))
                date = input(f"Date ({get_current_date()}): ") or get_current_date()
                
                categories_data[category]['expenses'].append({
                    'item': item, 
                    'amount': amount,
                    'date': date
                })
                print(f"Added ₹{amount} for {item} to {category}")
                
                if input("Add more? (y/n): ").lower() != 'y':
                    break
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Numbers only please!")