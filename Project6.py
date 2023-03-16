#Chase Key IS 204-QL Intro to Business Programming
#Creates Appropriates Variables
itemName = ""
itemQuantity = ""
itemPrice = ""
extendedPrice = ""
receiptTotal = ""
totalPrice = ""
#Loop created to enter item name, quantity, and price
#Loop then appends total price to a list to be summed later and formats all numbers to display within two decimals
looping = True
price = list()
while(looping):
    itemName = input("Please input the name of the item: ")
    itemQuantity = input("Please input the quantity of the item: ")
    itemPrice = input("Please input the cost of the item: ")
    extendedPrice = (int(itemQuantity) * float(itemPrice))
    formatted_ExtendedPrice = "{:.2f}".format(extendedPrice)
    float_extendedPrice = float(formatted_ExtendedPrice)
    print(f"{itemName} {itemQuantity} {itemPrice} {formatted_ExtendedPrice}")
    price.append(float_extendedPrice)
    totalPrice += ((itemName) + ", " + (itemQuantity) + ", " + (itemPrice) + ", " + str(formatted_ExtendedPrice) + "\n")
    if (input("would you like to enter another item? Enter yes or no: ") == "no"):
        looping = False
#Creates a file to save input information and calculations to and then closes it
fileName = input("Please input the name of the file you would like to create:")
fileName += ".txt"
writeFile = open(fileName, "w")
writeFile.write (totalPrice)
writeFile.close ()
#Sums the previously calculated prices and prints it to the console
priceSum = (f"{sum(price)}")
formatted_priceSum = "{:.2f}".format(float(priceSum))
print (formatted_priceSum)
#Calculates the discount if one is necessary and the resulting sales total after discount and prints it to the console
quotient = 1/10
percentage = quotient * float(priceSum)
discountString = (percentage) if float(priceSum) >= 100 else float(priceSum)
salesTotalString = float(priceSum) - float(percentage) if float(priceSum) >= 100 else float(priceSum)
formatted_salesTotalString = "{:.2f}".format(salesTotalString)
formatted_discountString = "{:.2f}".format(discountString)
print(formatted_discountString)
print(formatted_salesTotalString)
#Calculates sales tax and prints it to the console
taxQuotient = 2/25
salesTax = float(discountString) * taxQuotient
formatted_saleTax = "{:.2f}".format(salesTax)
print(formatted_saleTax)
#Calculates the final total of the sale and prints it to the console
salesTotal = float(formatted_salesTotalString) + float(formatted_saleTax)
formatted_salesTotal = "{:.2f}".format(salesTotal)
print(formatted_salesTotal)
