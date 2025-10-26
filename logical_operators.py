
# logical operators = used on conditional statements

#       and = checks two or more conditions are True

#       or = checks if at least one condition is True

#       not = True if condition is False, and vice versa

temp = 16 

# how works and operator: we need both or more conditions to be true and they will give us true print

if temp > 0 and temp < 20:
    print("temperature is good!")
else:
    print("temperature is bad")

# how works or operator: we need only one condition is true from two or more

temp2 = -21

if temp2 >= 15 or temp2 >= 30:
    print("Temperature is not bad for may")
else:
    print("temperature so bad for may really!")

# how works not operator: its swap something that true to false or if it originaly was false to true 

sunny = True 

if not sunny: 
    print("its cloudly today")
else:
    print("its sunny today!") 

# see? 