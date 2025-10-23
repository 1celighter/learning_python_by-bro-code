
item = input("What item you would like to buy?: ")  
price = float(input("What is the price"))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}") # construction {round(total, 2 )} needs only for round up our total and number 2 mean 
# how we will round it up if it less .50 we will round it to zero if more we round it to fully number 1
 
# here we go 