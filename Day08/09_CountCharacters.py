# ==========================================
# Program 09: 09_CountCharacters.py
# Description: Counting character frequency in a string,
# ignoring spaces and case, and finding the most frequent character.
# ==========================================

def main():
    print("🔠 CHARACTER FREQUENCY COUNTER 🔠")
    print("="*35)
    
    # Take input from the user
    text = input("Enter a word or sentence:\n")
    
    # ------------------------------------------
    # 🎯 CORE & BONUS CHALLENGE
    # ------------------------------------------
    # 1. Convert to lowercase to ignore capitalization (Bonus)
    # 2. Replace spaces with nothing to ignore them (Core)
    processed_text = text.lower().replace(" ", "")
    
    char_count = {}
    
    # Loop through each character in the processed text
    for char in processed_text:
        # The get() method returns the current count, or 0 if it doesn't exist yet.
        # Then we simply add 1 to it!
        char_count[char] = char_count.get(char, 0) + 1
        
    print("\n========== FREQUENCY ==========")
    for char, count in char_count.items():
        print(f"{char} : {count}")
        
    # ------------------------------------------
    # 🔥 EXTRA CHALLENGE
    # ------------------------------------------
    if char_count:
        # Find the highest number in our dictionary's values
        max_occurrences = max(char_count.values())
        
        # Using a list comprehension to find all characters that share that max number
        # (This handles "ties" if two letters appear the same amount of times)
        most_frequent_chars = [char for char, count in char_count.items() if count == max_occurrences]
        
        print("\n========== MOST FREQUENT ==========")
        # Join the list into a neat string separated by commas
        print(f"Character(s): {', '.join(most_frequent_chars)}")
        print(f"Occurrences: {max_occurrences}")
    else:
        print("\nNo characters were entered!")

    print("\nProgram Completed Successfully! 🚀")

if __name__ == "__main__":
    main()
    