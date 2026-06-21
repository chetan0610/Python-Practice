Number_of_Items = int(input("Enter number of items: "))
Items = input("Enter the Items: ")
for i  in range(1,Number_of_Items + 1, Items):

Quantity = int(input("Enter the quantity: "))
Price = int(input("Enter the Price of the item: "))
GST = int(input("Enter the GST of the price: "))


Sub_Total = Price*Quantity
GST_Amount = int(Sub_Total*GST)/100
FInal_Bill = Sub_Total+GST_Amount

    