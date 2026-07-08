# ==========================================
# Program 14: 14_MergeDictionaries.py
# Description: Demonstrating multiple ways to merge dictionaries,
# including handling overlapping keys.
# ==========================================
import json

def display_dict(title, data):
    print(f"\n========== {title} ==========")
    print(json.dumps(data, indent=4))

def main():
    # Setup: Notice that "Bob" exists in both dictionaries!
    team_a = {"Alice": 95, "Bob": 80}
    team_b = {"Bob": 90, "Charlie": 85}
    team_c = {"David": 92, "Eve": 88}

    print("🛠️ ORIGINAL DICTIONARIES")
    print(f"Team A: {team_a}")
    print(f"Team B: {team_b}")
    print(f"Team C: {team_c}")

    # ------------------------------------------
    # 🎯 METHOD 1: update()
    # Modifies the original dictionary. Keys from team_b will overwrite team_a.
    # ------------------------------------------
    # Creating a copy so we don't ruin team_a for the other examples
    method1_dict = team_a.copy()
    method1_dict.update(team_b)
    display_dict("METHOD 1: update()", method1_dict)

    # ------------------------------------------
    # 🎯 METHOD 2: The Pipe Operator | (Python 3.9+)
    # Creates a brand new dictionary. Extremely clean syntax.
    # ------------------------------------------
    method2_dict = team_a | team_b
    display_dict("METHOD 2: Pipe Operator (|)", method2_dict)

    # ------------------------------------------
    # 🎯 METHOD 3: Dictionary Unpacking **
    # Creates a brand new dictionary using the ** operator.
    # ------------------------------------------
    method3_dict = {**team_a, **team_b}
    display_dict("METHOD 3: Unpacking (**)", method3_dict)

    # ------------------------------------------
    # 🎯 BONUS CHALLENGE: Merge Three Dictionaries
    # ------------------------------------------
    # You can chain the pipe operator to merge as many as you want!
    all_teams = team_a | team_b | team_c
    display_dict("BONUS: Merge Three Dictionaries", all_teams)

    # ------------------------------------------
    # 🔥 EXTRA CHALLENGE: Merge Without Overwriting
    # ------------------------------------------
    print("\n========== EXTRA: NO OVERWRITE ==========")
    # Goal: Combine Team A and Team B, but keep Team A's original score for Bob (80).
    safe_merge = team_a.copy()
    
    for key, value in team_b.items():
        # Only add the key if it doesn't already exist in our dictionary
        if key not in safe_merge:
            safe_merge[key] = value
            
    print(json.dumps(safe_merge, indent=4))
    print("\nNotice that Bob's score remained 80 (from Team A), not 90 (from Team B)!")

    print("\nProgram Completed Successfully! 🚀")

if __name__ == "__main__":
    main()