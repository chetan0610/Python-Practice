# ==========================================
# Program 13: 13_PhoneBook.py
# Description: Mini Project - Phone Book Manager
# Features: Add, Search, Update, Delete, View (Sorted), and Reverse Search
# ==========================================

def main():
    # Using Name as the primary key for our dictionary
    phonebook = {
        "Chetan Kumar": {"phone": "9876543210", "email": "chetan@example.com"},
        "Aarav Sharma": {"phone": "9123456789", "email": "aarav@example.com"}
    }

    while True:
        print("\n" + "="*45)
        print("📱 PERSONAL PHONE BOOK MANAGER 📱")
        print("="*45)
        print("1. Add Contact")
        print("2. Search Contact (by Name)")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts (Alphabetical)")
        print("6. Search by Phone Number (Reverse Search)")
        print("7. Exit")
        print("="*45)
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            print("\n--- Add Contact ---")
            # .title() automatically capitalizes the first letter of each name
            name = input("Enter Name: ").strip().title()
            
            if name in phonebook:
                print("❌ Contact already exists! Please use the Update option.")
            else:
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email: ").strip()
                
                # Create the nested dictionary for the new contact
                phonebook[name] = {"phone": phone, "email": email}
                print(f"✅ Contact '{name}' added successfully!")

        elif choice == '2':
            print("\n--- Search Contact ---")
            name = input("Enter Name to search: ").strip().title()
            
            if name in phonebook:
                info = phonebook[name]
                print(f"✅ Found: {name} | Phone: {info['phone']} | Email: {info['email']}")
            else:
                print("❌ Contact not found.")

        elif choice == '3':
            print("\n--- Update Contact ---")
            name = input("Enter Name to update: ").strip().title()
            
            if name in phonebook:
                print(f"Current Phone: {phonebook[name]['phone']}")
                print(f"Current Email: {phonebook[name]['email']}")
                
                # Pressing enter skips the update for that specific field
                new_phone = input("Enter New Phone (or press Enter to keep current): ").strip()
                new_email = input("Enter New Email (or press Enter to keep current): ").strip()
                
                if new_phone:
                    phonebook[name]['phone'] = new_phone
                if new_email:
                    phonebook[name]['email'] = new_email
                    
                print("✅ Contact updated successfully!")
            else:
                print("❌ Contact not found.")

        elif choice == '4':
            print("\n--- Delete Contact ---")
            name = input("Enter Name to delete: ").strip().title()
            
            if name in phonebook:
                del phonebook[name]
                print(f"✅ Contact '{name}' deleted successfully!")
            else:
                print("❌ Contact not found.")

        elif choice == '5':
            print("\n--- All Contacts ---")
            if not phonebook:
                print("Phone book is empty.")
            else:
                print(f"{'NAME':<20} | {'PHONE':<15} | {'EMAIL'}")
                print("-" * 55)
                
                # Bonus Challenge: Sort contacts alphabetically
                # sorted() automatically sorts the dictionary keys in alphabetical order (A-Z)
                for name in sorted(phonebook.keys()):
                    info = phonebook[name]
                    print(f"{name:<20} | {info['phone']:<15} | {info['email']}")
                    
                print("-" * 55)
                print(f"Total Contacts: {len(phonebook)}")

        elif choice == '6':
            # Extra Challenge: Search by Phone Number
            print("\n--- Reverse Search (By Phone) ---")
            search_phone = input("Enter Phone Number to search: ").strip()
            found = False
            
            # We must loop through all items because the phone number is buried inside the inner dictionary
            for name, info in phonebook.items():
                if info['phone'] == search_phone:
                    print(f"✅ Found: {name} owns the number {search_phone} (Email: {info['email']})")
                    found = True
                    break # Stop searching once we find a match
                    
            if not found:
                print("❌ No contact found with that phone number.")

        elif choice == '7':
            print("\nExiting Phone Book Manager. Goodbye! 🚀")
            break

        else:
            print("❌ Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()