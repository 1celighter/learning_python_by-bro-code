
# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places

# :(number) = allocate that many spaces

# :0(number) = allocate and zero pad that many spaces

# :< = left justify

# :> = right justify

# :^ = center align

# :+ = use a plus sign to indicate positive value

# := = place sign to leftmost position

# :  = insert a space before positive numbers

# :, = comma separator


price1 = 3.412512
price2 = -3239
price3 = 124.123

print(f"Price is ${price1:.2f}")

print(f"Price is ${price2:.2f}")

print(f"Price is ${price3:.2f}")

# allocate 

price4 = 2135.412
price5 = -1241.213
price6 = 124.6435

print(f"Price is {price4:10}")
print(f"Price is {price5:5}")
print(f"Price is {price6:2}") 

# numbers in classes also need count like to get 3 space me need write atleast :3 me need write 6 if we pick number is 213 for example

# we also can use paddings like that 

price7 = 214.3 

print(f"That price is {price7:010}")

# justify left< >right 

price8 = 694.6

print(f"price is {price8:>10}") 

# it is do justify from left to right 

price9 = 432.5

print(f"price is {price9:<10}") # but there we are do align from rigth to left 


# center aglin 

price10 = 104.1

print(f"price is {price10:^10}") # that how many need center this number from right and left sides


# if we need indicate a plus value we can use buildin funct + 

price11 = 106.3
price12 = -43

print(f"price is {price11:+}") # all positive numbers will be with + 
print(f"price is {price12:+}") # but a negative with - 

# or we can use just space to check it if we dont have - in a line that a positive number! 

price13 = -32
price14 = 35

print(f"price is {price13: }")
print(f"price is {price14: }")

# here we go

# if we need make some big numbers more easy to read we can use it , 

price15 = 15921571295

print(f"this number is {price15:,}") #this thing a very useful ngl 

# we also can combine all of this format together 

price16 = 125812.4132

print(f"Number is: {price16:<10,.2f}")

# here we go