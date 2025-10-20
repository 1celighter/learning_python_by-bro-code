# Variable = a container for a value (string, integer, float, boolean)
# a variable behaves as if it was the value it conains 

# that all strings 
 
first_name = "Dany"
food = "pizza"
email = "bro123@fake.com"

print(f"wassup {first_name}")
print(f"your fav food is:{food}")
print(f"your email is:{email}")

# that all integers 

age = 25 
quantity = 3 
num_of_students = 30

print(f"you are {age} old")
print(f"you are buying {quantity}")
print(f"stuents here in class: {num_of_students}")

# that all floats 

price = 33.33
gpa = 3.6
distance = 3.1

print(f"price for this item is: {price}")
print(f"your gpa is {gpa}")
print(f"distance u was ran is {distance}")

# booleans 

is_student = True 

print(f"you are a student? {is_student}")

# better will be text it there

student = False

if student:
    print("You are a student")
else:
    print("You are not a student")


for_sale = True 

if for_sale:
    print("this item avaible for sale")
else:
    print("this item is not avaible for sale")