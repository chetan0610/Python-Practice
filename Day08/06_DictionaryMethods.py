# ==========================================
# Program 06: 06_DictionaryMethods.py
# Description: Demonstrating all major dictionary methods
# using a menu-driven car dictionary.
# ==========================================
import json

def display_dict(title, data):
    print(f"\n========== {title} ==========")
    print(json.dumps(data, indent=4))

def main():
    # Initializing the Car Dictionary
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "color": "red"
    }

    while True:
        print("\n" + "="*30)
        print("🚗 CAR DICTIONARY MANAGER")
        print("="*30)
        print("1. View Dictionary")
        print("2. keys() - Show all keys")
        print("3. values() - Show all values")
        print("4. items() - Show key-value pairs")
        print("5. get() - Safely get a value")
        print("6. update() - Update or add items")
        print("7. setdefault() - Add key if missing")
        print("8. pop() - Remove specific key")
        print("9. popitem() - Remove last item")
        print("10. copy() - Make a separate copy")
        print("11. fromkeys() - Create new dict with default values")
        print("12. clear() - Empty the dictionary")
        print("13. Exit")
        
        choice = input("\nSelect a method to test (1-13): ").strip()

        if choice == '1':
            display_dict("CURRENT CAR DICTIONARY", car)
            
        elif choice == '2':
            print(f"\nKeys: {list(car.keys())}")
            
        elif choice == '3':
            print(f"\nValues: {list(car.values())}")
            
        elif choice == '4':
            print("\nItems:")
            for key, value in car.items():
                print(f" - {key}: {value}")
                
        elif choice == '5':
            key = input("Enter key to get: ")
            # Returns "Not Found" if key doesn't exist, preventing a crash
            print(f"Value: {car.get(key, 'Not Found')}")
            
        elif choice == '6':
            print("Let's update the mileage.")
            car.update({"mileage": 45000, "color": "blue"})
            print("\nUpdated mileage to 45000 and color to blue.")
            display_dict("UPDATED DICTIONARY", car)
            
        elif choice == '7':
            key = input("Enter key to check/add: ")
            val = input("Enter default value if missing: ")
            result = car.setdefault(key, val)
            print(f"\nReturned Value: {result}")
            display_dict("AFTER SETDEFAULT", car)
            
        elif choice == '8':
            key = input("Enter key to pop: ")
            if key in car:
                removed = car.pop(key)
                print(f"\nPopped Value: {removed}")
            else:
                print("\nKey not found!")
                
        elif choice == '9':
            if car:
                removed = car.popitem()
                print(f"\nPopped Item (Tuple): {removed}")
            else:
                print("\nDictionary is empty!")
                
        elif choice == '10':
            car_copy = car.copy()
            print("\nCreated a copy. Let's modify the copy to prove they are separate.")
            car_copy["brand"] = "Tesla"
            display_dict("ORIGINAL CAR", car)
            display_dict("COPIED CAR (Modified)", car_copy)
            
        elif choice == '11':
            keys = ['engine', 'transmission', 'wheels']
            default_val = input("\nEnter default value for new keys: ")
            new_dict = dict.fromkeys(keys, default_val)
            display_dict("NEW DICTIONARY USING FROMKEYS", new_dict)
            
        elif choice == '12':
            car.clear()
            print("\nDictionary cleared!")
            display_dict("CLEARED DICTIONARY", car)
            
        elif choice == '13':
            print("\nExiting Dictionary Manager. Great job! 🚀")
            break
            
        else:
            print("\nInvalid input! Please select a number from 1 to 13.")

if __name__ == "__main__":
    main()
    