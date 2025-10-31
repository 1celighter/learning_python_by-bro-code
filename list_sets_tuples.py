# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# list

fruit = ["apple", "orange", "banana", "coconut"]

print(fruit) # they will give us all of this list but with '' this quotes 

# if we need pick only one index from this list we can use []

colors = ["blue" , "green" , "red", "purple"]

print(colors[2]) # also yeah we need count from zero | zero one two 

# we can also check range [0:2] like that

print(colors[0:2]) # our index we are starting from zero it count from zero but about second number it count like default from 1 

# and if we want check every index by number we can use step 

print(colors[::2]) # every second element from zero index 

# we can also use backwards

print(fruit[::-1]) # there we go 

# we also can use loop with collections 

# we can also reassign one of value if we want with that command 

fruit[0] = "grape" # yeah also that need add before last print list 

# well but if we need add some items to the end of a list use append buildin function

fruit.append("waterlemon") # and yeah that too need use before last print 

# for remove a element we should use 

fruit.remove("banana") 

# we can also insert a value at a given index 

fruit.insert(0, "apple") # first number we are placing our index and "" second we are give a name or number 

fruit.sort() # just sort to alphabetical order now

# if we need reversed method 

fruit.reverse() # also if we use fruit.sort first and after that fruit reverse we will reverse a alphabetical order 

# if we need clear list we can use clear method

# fruit.clear() # we are clear all list

# if we need to know what index got any number or word in list 

print(fruit.index("waterlemon"))

# if we needd to know how many we got some value we got count command

print(fruit.count("apple")) # we got one apple
 
for fruits in fruit:
    print(fruits) # here we go 

# dir function that just for help
 
# print(dir(fruit))
# help(fruit) 

# if we need to know length we can use this function 

print(len(fruit)) # it is count from 1 no from zero

# if we need check boolean in our list it was also applies to other collections types 

print("pineapple" in fruit)

print(fruit)

# false because we dont have pineapple


# sets {} it is unordered and we cant alter these values can add/ remove but no duplicates

# we also can use help function and dir too but i so lazy to write it all and also a little want to sleep

bolkre = {"some", "adventure", "hay","yay"}

print(bolkre)

print(len(bolkre))

print("some" in bolkre) # we too can find something in the set

# print(bolkre[0]) # WE CANT INDEXING because sets is unordered

# we cant change the values but we can add or remove some heeh

bolkre.add("pineapple patch")

bolkre.remove("some")

bolkre.pop() # that random removing a index

# we also can clear but i dont want do it 

#bolkre.clear() that if we want do it 

print(bolkre)

# now we got tuples tuples faster than lists and sets but we cant change it and it is ordered duplicates are okay for this collection

idk = ("i","want","want","sleep")

# we can use help with help funct and dir funct

# print(help(idk))

# print(dir(idk))

# we can also find values in tuples 

print("i" in idk)

# we also can index in this collection method

print(idk.index("want"))

# and we can count duplicates

print(idk.count("want"))