# ==========================================
# Program 12: 12_InventoryManagement.py
# Description: Mini Project - Inventory Management System
# Features: Add, View, Update, Delete, Search, Value, Low Stock
# ==========================================

def main():
    # Initializing with dummy data (Keys are Product IDs)
    inventory = {
        "P101": {"name": "Laptop", "quantity": 15, "price": 850.00},
        "P102": {"name": "Mouse", "quantity": 4, "price": 25.00},
        "P103": {"name": "Keyboard", "quantity": 45, "price": 45.00},
        "P104": {"name": "Monitor", "quantity": 2, "price": 150.00}
    }

    # Setting a threshold for "Low Stock"
    LOW_STOCK_LEVEL = 5

    while True:
        print("\n" + "="*45)
        print("📦 INVENTORY MANAGEMENT SYSTEM 📦")
        print("="*45)
        print("1. Add Product")
        print("2. View All Products & Total Value")
        print("3. Update Stock (Add/Remove Quantity)")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Show Low-Stock Products")
        print("7. Exit")
        print("="*45)
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            print("\n--- Add New Product ---")
            prod_id = input("Enter Product ID (e.g., P105): ").strip().upper()
            if prod_id in inventory:
                print("❌ Error: Product ID already exists!")
            else:
                try:
                    name = input("Enter Product Name: ").title()
                    qty = int(input("Enter Quantity: "))
                    price = float(input("Enter Price per unit: "))
                    inventory[prod_id] = {"name": name, "quantity": qty, "price": price}
                    print(f"✅ Product '{name}' added successfully!")
                except ValueError:
                    print("❌ Invalid input! Quantity must be a whole number and Price must be a number.")

        elif choice == '2':
            print("\n--- All Products ---")
            if not inventory:
                print("Inventory is empty.")
            else:
                total_inventory_value = 0
                print(f"{'ID':<6} | {'NAME':<15} | {'QTY':<5} | {'PRICE':<8} | {'TOTAL VALUE'}")
                print("-" * 55)
                for prod_id, info in inventory.items():
                    # Calculate total value per item
                    item_value = info['quantity'] * info['price']
                    total_inventory_value += item_value
                    print(f"{prod_id:<6} | {info['name']:<15} | {info['quantity']:<5} | ${info['price']:<7.2f} | ${item_value:.2f}")
                
                # Bonus Challenge: Calculate Total Inventory Value
                print("-" * 55)
                print(f"Total Products in Catalog: {len(inventory)}")
                print(f"Total Value of Inventory: ${total_inventory_value:.2f}")

        elif choice == '3':
            print("\n--- Update Stock ---")
            prod_id = input("Enter Product ID to update: ").strip().upper()
            if prod_id in inventory:
                print(f"Current Quantity of {inventory[prod_id]['name']}: {inventory[prod_id]['quantity']}")
                try:
                    # Allowing negative numbers if the user wants to reduce stock
                    change = int(input("Enter amount to add (or negative number to reduce): "))
                    new_qty = inventory[prod_id]['quantity'] + change
                    
                    if new_qty < 0:
                        print("❌ Error: Stock cannot drop below 0.")
                    else:
                        inventory[prod_id]['quantity'] = new_qty
                        print(f"✅ Stock updated! New Quantity: {new_qty}")
                except ValueError:
                    print("❌ Invalid input! Must be a whole number.")
            else:
                print("❌ Product not found.")

        elif choice == '4':
            print("\n--- Delete Product ---")
            prod_id = input("Enter Product ID to delete: ").strip().upper()
            if prod_id in inventory:
                removed = inventory.pop(prod_id)
                print(f"✅ Product '{removed['name']}' deleted successfully!")
            else:
                print("❌ Product not found.")

        elif choice == '5':
            print("\n--- Search Product ---")
            prod_id = input("Enter Product ID to search: ").strip().upper()
            if prod_id in inventory:
                info = inventory[prod_id]
                print(f"✅ Found: ID: {prod_id} | Name: {info['name']} | QTY: {info['quantity']} | Price: ${info['price']:.2f}")
            else:
                print("❌ Product not found.")

        elif choice == '6':
            # Extra Challenge: Show Low-Stock Products
            print(f"\n--- Low-Stock Alert (Below {LOW_STOCK_LEVEL}) ---")
            low_stock_found = False
            for prod_id, info in inventory.items():
                if info['quantity'] < LOW_STOCK_LEVEL:
                    print(f"⚠️ {info['name']} (ID: {prod_id}) - Only {info['quantity']} left!")
                    low_stock_found = True
            
            if not low_stock_found:
                print("✅ All products are sufficiently stocked.")

        elif choice == '7':
            print("\nExiting Inventory Management System. Goodbye! 🚀")
            break

        else:
            print("❌ Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()
    