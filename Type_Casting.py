# typecasting it is process of converting a value of one data type to another 
# like ( string, integer, float, boolean )
# Explicit vs Implicit 
# i will commit one more tmwr bc i so tired for today and me need go to sleep

# to check what type of casting we are have we need write some code 

# its all Explicit 

name = "bro"
age = 22
gpa = 2.2
student = True 

print(type(name)) # type function just check what type of casting this class in () we writing class to check 
print(type(age))
print(type(gpa))
print(type(student))

# well now to casting our type 

age = float(age) # with this line we convert our age to float number 
print(age)
print(type(age)) # now we converted our type from int to float ! 


gpa = int(gpa)
print(type(gpa))
print(gpa)

student = str(student)
print(student)
print(type(student))

# what will be wrong if we convert int to boolean? 

age = bool(age)
print(age) # it will be always be true if we got number positive or negative  but it will be false if we get zero
print(type(age))

# where it can be get useful? when we trying ask from user he's name or age or something if we get answer we give access if not = no access

name1 = ""

name1 = bool(name1)
print(name1)
print(type(name1))

# here we are 

# now we are understand explicit type casting that just manually converting with keywords its not auto we need write it all 
# by yourself and all new classes too if we add something new and we need it to convert we need write some code to convert they type
# but if we need auto we can use Implicit type casting yeah its converting automaticaly lets check it out 

x = 2 
y = 2.0
x = x / y
print(x) # and in command line we got answer 1.0 yeah its automaticaly converted to float number because y is float

