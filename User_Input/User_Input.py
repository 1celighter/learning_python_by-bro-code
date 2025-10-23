# user input is easy 
#construction of this function is that input("some text to send info to user") like input("your age?") something like that
# well lets dance with our code 

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hi Howdy your name is: {name}")
print(f"Your age is: {age}")

# that a basics to be honest really but also we can combine it with type casting and do something 
# like addition +1 to age bc why not?

age_inc = input("Enter your age: ")
age_inc = int(age_inc)
age_inc = age_inc + 1 # ah yeah we must do first type casting because without it we will get error because we cant addition to string
print(age_inc)

# yeah like this but that so easy and idk where i can use it but we will see it no worry
# also we can write some better on our code i mean line with type casting 
# we can use only 1 line to type casting 

age_dany = int(input("Dany you age is? ")) # like that and we getting all works code we just combine it to one line no more 
age_dany = age_dany + 3 
print(f"you age is {age_dany} after three years!")

# well actually that all yeah input case is not so hard to be understand that a reasson why there is not so much code 