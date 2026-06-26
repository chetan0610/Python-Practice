Name = input("Enter name: ")
Age = int(input("Enter your age: "))
Ticket = input("Do you have a ticket?(True/False): ")

if Age < 18:
    print("You must be 18 or older")
elif Age >= 18 and Ticket == "True":
    print("Entery Allowed")
else:
    print("Please buy a ticket")
