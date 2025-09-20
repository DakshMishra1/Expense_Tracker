def check_spending(data):
    if not data:
        print("No data available!")
        return

    print("\n--- Spending Summary ---")
    total_limit = data.get('Total Amount', {}).get('limit', 0)
    print(f"Total Amount Available: ₹{total_limit}")

    print("\n{:<12} {:<10} {:<10} {:<10} {:<10}".format(
        "Category", "Limit", "Spent", "Remaining", "Status"
    ))
    print("-" * 50)

    total_spent = 0

    for category, details in data.items():
        if category == 'Total Amount':
            continue

        limit = details.get('limit', 0)
        spent = sum(expense.get('amount', 0) for expense in details.get('expenses', []))
        remaining = limit - spent
        status = "Within Limit" if remaining >= 0 else "Over Limit"

        print(f"{category:<12} ₹{limit:<10} ₹{spent:<10} ₹{remaining:<10} {status}")
        total_spent += spent

    total_remaining = total_limit - total_spent
    print("\nTotal Spent: ₹", total_spent)
    print("Total Remaining: ₹", total_remaining) 
   