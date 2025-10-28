# email slicer 

# email = input("Enter your email: ")

# index = email.index('@')

# username = email[:index]
# domain = email[index:]

# print(f"Your username is {username}, domain is {domain}")

# but we can do this program with less amount of code 

email1 = input("Enter you email: ")

username1 = email1[:email1.index("@")]
domain1 = email1[email1.index("@") + 1:] 

print(f"Your user is {username1}, domain is {domain1}")
