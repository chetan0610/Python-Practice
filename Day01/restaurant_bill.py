Name = input("Enter your name: ")
Items = input("Enter your food Item: ")
Price = int(input("price: "))
Quantity = int(input("Enter the quantity: "))
GST = int(input("GST of the food item: "))
Tip = int(input("Tip you wanna give it to the waiter: "))

Subtotal = Price * Quantity
GST_Amount = int(Subtotal*GST)/100
Final_Bill = Subtotal + GST_Amount + Tip

print()
print("=================== RESTAURANT BILL ===================")
print("Coustomer Name                        : ", Name)
print("Item                                  : ", Items)
print("Price                                 : ", Price)
print("Quantitiy                             : ", Quantity)
print("Total GST                             : ", str(GST_Amount) + "%")
print("Tip                                   : ", Tip)

print("=========================================================")
print("TOTAL                                 : ", Final_Bill)
print("=========================================================")