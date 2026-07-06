#Combines multiple set concepts to solve a practical problem.
coding_club = {"Rahul", "Priya", "Amit", "Sneha", "Kiran"}
robotics_club = {"Priya", "Sneha", "Vijay", "Arjun", "Kiran"}

print("Coding Club:")
print(coding_club)

print("\nRobotics Club:")
print(robotics_club)

print("\n--------------------------\n")

all_members = coding_club.union(robotics_club)
print("All Club Members:")
print(all_members)

print("\n--------------------------\n")
both_clubs = coding_club.intersection(robotics_club)
print("Students in Both Clubs:")
print(both_clubs)

print("\n--------------------------\n")

only_coding = coding_club.difference(robotics_club)
print("Only Coding Club:")
print(only_coding)

print("\n--------------------------\n")

only_one_club = coding_club.symmetric_difference(robotics_club)
print("Only One Club:")
print(only_one_club)

print("\n--------------------------\n")
print(f"Total Unique Students: {len(all_members)}")