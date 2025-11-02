
# 2d list = is this a list made up of lists can be useful when need grid or matrix data like exel spreadsheet

fruit = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruit, vegetables, meats]

# when we using default list we replacing like that  fruit[0] = pineapple, and we print it like that print(fruit) and we get 
# only fruit list data 
# but in 2d lists we have a little different

print(groceries) # if we print 2d list we will get all lists data in fruit, vegetables and meat in our situation

print(groceries[0]) # that we are select a row - zero is fruit row 

# but if we need select one row and any index from this row we can do it like that

print(groceries[2][2]) # here we pick are orange index in fruit and also [0] - row [1] is column here that like cordinats 

# also it count from zero all 

# to declarate a 2d list we need just replace it like this 

somethin = [["something", "else", "hello", "buddy"],
            ["yo","sup","ez","pal"],
            ["idk", "tbh", "three words", "ggwp"]]

print(somethin[2][3]) # we are can do it same like with groceries

# but if we need iterate our list we can use a nested loops 

for collection in somethin:
    for collect in collection:
        print(collect, end=" ")
    print()

# we also can use whatever sets tuples or lists what better - use it 

