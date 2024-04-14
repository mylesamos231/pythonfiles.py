'''
Name: Myles Amos
Date: January 19,2024
Lab01c.py program: Code to allow user to enter the three different items, their prices, and the quantites.
Calculate everything before tax and give the total after tax.
'''
#Welcome message 
print(f"Welcome to Myles Shop where you make your own prices. ")
input(f" How are you? here's a list of foods we're selling today")
#Display list of foods 
fruits = ['apples', 'oranges', 'bananas', 'strawberries']
print(fruits)
#Ask the questions when I run the code 
item1 = input("What is your first item? ")
item2 = input("What is your second item? ")
item3 = input("What is your third item? ")
#Get the price for each item
price1 = float(input("What is the price of your first item? $"))
price2 = float(input("What is the price of your second item? $"))
price3 = float(input("What is the price of your third item? $")) 
#Add this tax percentage for the sales tax rate. 
tax_rate = .07
#Make sure to have a quantity for the items
quantity1 = int(input("What is the quantity of your first item? "))
quantity2 = int(input("What is the quantitiy of your second item? "))
quantity3 = int(input("What is the quantity of your third item? "))
#Calcuate to get the total 
total1 = price1 * quantity1 + tax_rate
total2 = price2 * quantity2 + tax_rate
total3 = price3 * quantity3 + tax_rate
#Multipy the subtotal times the sales tax for the purchase 
purchase = total1 * tax_rate 
#Get the total for each purchased item 
print(f"You purchased {quantity1} of {item1} for {price1}, the total is: ${total1:.2f} ")
print(f"You purchased {quantity2} of {item2} for {price2}, the total is: ${total2:.2f} ")
print(f"You purchased {quantity3} of {item3} for {price3}, the total is: ${total3:.2f} ")
#This is the Grand Total 
GrandTotal = total1 + total2 + total3 
#Display the Grand Total 
print(f"The Grand Total for all your groceries is ${GrandTotal:.2f} ")