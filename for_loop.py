# for loop = execute a block of code a fixed number of times.
# you can iterate over a range, string, sequence, etc.

for x in range(1,11): # that base type for loop also we need +1 in result to get our wanted result
    print(x) # and also x in 4th line that just name class to print after it we can rename it easy if we want

# iterate backward 

for nw in reversed(range(1,11)):
    print(nw)

print("HAPPY NEW YEAR YAY")

# step 

for step in range(1,11,2): # in this loop we got range(#- first number what number from start our loop # - second number where we will end)
    print(step) # and (# - third number that a step and this number will counts by  in how many in our 2 they will print us only every 2nd number)


# iterate over a string 

credit_card = "1234-5678-9012-3456"

for cred in credit_card:
    print(cred) # we just print all credit number and we print every number from next line 

# continue keyword 

for cont in range(1,31):
    if cont == 24:
        continue # it just skip a number or something what we typed in iteration that can be useful sometimes ig
    else:
        print(cont)

# break keyword

for brek in range(1,21):
    if brek == 11:
        break # break key word just stop our iterate when we getting our if and write all numbers or strings before if 
    print(brek)
# that might useful tbh