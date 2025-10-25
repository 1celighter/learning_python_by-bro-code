# if = do some code  only IF some condition is True
# elif = else + if just checking what we can do some more  
#   else do something else

age = int(input("Enter your age: "))
if age >= 100: 
    print("You are too old to get credit card")
elif age >= 18:
    print("You are signed up to ur credit card!")
elif age < 0:
    print("you haven't born yet!")
else:
    print("You must be 18+ to sign up for credit card")