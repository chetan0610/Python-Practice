customer_ages = [12, 25, 67, 8, 40]

print("🎟️ Ticket Price Calculator 🎟️\n")

for age in customer_ages:
    
    # 'if-else' statements to decide the ticket price
    if age < 13:
        price = 5
        category = "Child"
    elif age >= 65:
        price = 7
        category = "Senior"
    else:
        price = 12
        category = "Adult"
        
    print(f"Age {age} ({category}): ${price}")

print("\nAll prices calculated successfully!")
