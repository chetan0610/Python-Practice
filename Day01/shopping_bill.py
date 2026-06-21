product_name = input("Enter the product name: ")
price = int(input("Price of the product: "))
quantity = int(input("Number of of quantity: "))
discount = int(input("Enter discount if its available: "))

total = price*quantity
dicount = total*discount/100 
final_bill = total-dicount 

print("==========SHOPPING BILL==========")
print("Name of the product : ",product_name)
print("Quantity            : ", quantity)
print("Total               : ", total)
print("Discount amount     :", dicount)
print("Final Bill          : ", final_bill)