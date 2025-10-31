# nested loop = a loop within another loop (outer, inner)
# outer loop: 
#   inner loop:
# very situation 

for x in range(1, 11):
    print(x)

for an in range(3):
    for am in range(1,11):
        print(am, end="-") # end word meaning our loop will be all in one line and in "" we can type anything to need type after one word or number

rows = int(input("Enter numbers of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use")

for tri in range(rows):
    for ang in range(columns):
        print(symbol, end="")
    print()