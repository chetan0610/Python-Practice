Name = input("Enter student name: ")
Marks = int(input("Enter Marks: "))

print("Hello,", Name)
if Marks >= 90:
    print("Result: Excellent")
elif Marks >= 75:
    print("Result: Very Good")
elif Marks >= 50:
    print("Reslut: Good")
else:
    print("Result: Fail")