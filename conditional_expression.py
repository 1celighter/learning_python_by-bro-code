
# conditional expression = A one-line shortcut for the if-else statement (ternary operator)

# Print or assign one of two values based on a condition

# X if condition else - this is formula 

num = 20 
print("This number is positive!" if num > 0 else "this number is negative!")

num2 = 10 
result = "EVEN" if num2 % 2 == 0 else "ODD"
print(result)

a = 6
b = 9

max_num = a if a > b else b 
min_num = a if a < b else b 

print(max_num, min_num)

age = 17 
status = "Adult" if age >= 18 else "child" 

print(status)

temperature = 25 
weather = "is hot today" if temperature >20 else "is cold today"

print(weather)

user_role = "admin"

access_level = "full access" if user_role == "admin" else "limited access!"

print(access_level)
