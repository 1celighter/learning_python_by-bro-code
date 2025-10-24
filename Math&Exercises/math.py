
# math! 
# addition operation = + | += 
friends = 1 
friends = friends + 1 # answer will be 2 but we have antoher method with less text 

friends2 = 1 
friends2 += 1 

print(friends)
print(friends2)
 
# here we are complited with additions but what about decreasing? = - |  -=

pals = 0 
pals = pals - 2

# lets check can we use less text variation 

pals2 = 1
pals2 -= 2  
print(pals) 
print(pals2)

# and yeah we can use this variation! 

# now multiplication = *  |  *=

pizza = 3 
pizza = pizza * 5 
print(pizza) 
# yay we got 15 pizza 

# and lets check can we do less code? 

pizza2 = 5 
pizza2 *= 2
print(pizza2)
# and yeah we can!

# divide = / | /=

traders = 4 
traders = traders / 2
print(traders)

# less code variant 

traders2 = 6 
traders2 /= 2
print(traders2)

# power up to (exponentiation) = ** | **=

people = 10
people = people ** 4    
print(people)

# less code variant 

people2 = 9 
people2 **= 3
print(people2)

# modulus operator = & | &= 

item = 10 
item = item & 3 
print(item)

# less code variant 

item1 = 14
item1 &= 3
print(item1)

# build-in functions 

x = 3.14
y = -4
z = 5

result = round(x) # any numbers will be rounded up
result2 = abs(y) # abs = absolute value its just give us information how many we need numbers to get back into to zero to absolute value
result3 = pow(4, 3) # pow meaning exponentiation ( ** ) and we will get result 64 like how we will exponentiation it by yourselfs
result4 = max(x,y,z) # just give us max value from this list 
result5 = min(x,y,z) # just give us min value from this list no more 
print(result)
print(result2)
print(result3)
print(result4)
print(result5)

print('')
print('')
print('')


# math module and first my import 

import math

# now if we need something from this import we must write math. and some what we need in my opinion its pi 

x = 8

print(math.pi)
print(math.e)
sqrt = math.sqrt(x)
print(sqrt)

y = 4.2

ceil = math.ceil(y) # ceil funct always round up number
print(ceil) # 5 is our answer

z = 9.9

floor = math.floor(z) # floor always will be round down our number 
print(floor) # 9 is our answer

