Name = input("Enter your name: ")
Principle_Amount= int(input("Principle amount: "))
Rate = int(input("Intrest rate: "))
Time = int(input("Taken (in years): "))

Sample_Interest = (Principle_Amount *Rate *Time)/100
Final_Amount = Sample_Interest+Principle_Amount

print()
print("========== BANK INTEREST =========")
print("Customer Name   : ", Name + ".")
print("Principle amount: ", Principle_Amount)
print("Interest Rate   : ", str(Rate) + "%")
print("Time (years)     : ", Time)
print("Sample Intrest  : ", Sample_Interest)
print("Total amount    : ", Final_Amount)