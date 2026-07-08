# ==========================================
# Program 10: 10_WordFrequency.py
# Description: Counting word frequency in a string,
# ignoring case, and finding the most frequent word.
# ==========================================

def main():
    print("📝 WORD FREQUENCY COUNTER 📝")
    print("="*35)
    
    # Take input from the user
    text = input("Enter a sentence:\n")
    
    # ------------------------------------------
    # 🎯 CORE & BONUS CHALLENGE
    # ------------------------------------------
    # 1. lower() ignores capitalization (Bonus)
    # 2. split() breaks the sentence into a list of words based on spaces (Core)
    words_list = text.lower().split()
    
    word_count = {}
    
    # Loop through each word in our new list
    for word in words_list:
        # Just like the character counter, get() safely adds or updates the count
        word_count[word] = word_count.get(word, 0) + 1
        
    print("\n========== FREQUENCY ==========")
    for word, count in word_count.items():
        print(f"{word} : {count}")
        
    # ------------------------------------------
    # 🔥 EXTRA CHALLENGE
    # ------------------------------------------
    if word_count:
        # Find the highest number in our dictionary's values
        max_occurrences = max(word_count.values())
        
        # List comprehension to handle "ties" if multiple words share the top spot
        most_frequent_words = [word for word, count in word_count.items() if count == max_occurrences]
        
        print("\n========== MOST FREQUENT ==========")
        print(f"Word(s): {', '.join(most_frequent_words)}")
        print(f"Occurrences: {max_occurrences}")
    else:
        print("\nNo words were entered!")

    print("\nProgram Completed Successfully! 🚀")

if __name__ == "__main__":
    main()
    