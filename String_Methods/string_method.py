name = input("Enter your full name: ")

# len 

result = len(name) # len = int func and it is check how many symbols we have | also we can understand it like lenght of the string also spaces too include to this 


print(result)

# find 

name2 = input("Enter your name: ")

result2 = name.find(" ") # find function work like list it count from zero we must understand it and they count space too!
# and also they will give us always first occurrence 

print(result2)

# rfind 

name3 = input("Enter your name: ")


result3 = name.rfind("o") # r meaning here reverse and it will work same like default find but it give us always last occurrence 

print(result3)

# capitalize = always will give first letter with uppercase

name4 = input("Enter your name: ")

name4 = name4.capitalize()

print(name4)

# upper = always give us all letter with uppercase

name5 = input("Enter ur name: ")

name5 = name5.upper()

print(name5)

# lower = always make ur letter to lowercase if they in uppercase or not there no differense it will always be lowercase

name6 = input("Enter your name: ")

name6 = name6.lower()

print(name6)

# isdigit = its a boolean give us only true or false gives us true only when we type some numbers false if we type letters spec symbols is false still bc its a letter

name7 = input("Enter your name: ")

name7 = name7.isdigit()

print(name7)

# isalpha = its too boolean but give us true if our string contains only alphabetical characters and false if not if we enter space we got false

name8 = input("Enter your name: ")

name8 = name8.isalpha() 

print(name8)

# count - just count something what u will text in ()

phone_number = input("Enter your phone number #:")

result4 = phone_number.count("-")

print(result4)

# replace - replace some in ("", to "something else new")

phone_num = input("Enter Your telephone number")

result5 = phone_num = phone_num.replace("-", " ")

print(result5)

# also if we need some help with strings we can use that 

print(help(str))