
# while loop = execute some code while some condition remains true 

name = input("Enter your name: ")

while name == "":
    print("You didnt enter your name")
    name = input("enter ur name again. ")
else:
    print(f"Hello {name}")

# infinity loop 

name1 = input("ur name?")

while name1 == "":
    print("ezlooped")
else:
    print(f"Sup{name1}")

# to escape while inf loop press ctrl c in terminal xD
