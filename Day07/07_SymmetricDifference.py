# Demonstrates how to find elements that exist in either set but not in both using symmetric_difference() and the '^' operator.
cricket = {"Rahul", "Priya", "Amit", "Sneha"}
football = {"Priya", "Sneha", "Kiran", "Vijay"}

print("Cricket Players:")
print(cricket)

print("\nFootball Players:")
print(football)

print("\n--- Main Challenge ---")

unique_players = cricket.symmetric_difference(football)
print("Players in only one sport:")
print(unique_players)

print("\n--- Bonus Challenge ---")

players = cricket ^ football
print("Players using '^':")
print(players)

print("\n--- Extra Challenge ---")

search_name = input("Enter player name: ")

if search_name in players:
    print(f"{search_name} plays only one sport.")
elif search_name in cricket and search_name in football:
    print(f"{search_name} plays both sports.")
else:
    print(f"{search_name} is not registered in either sport.")