# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step] start : end mean we need pick number from start 0 : and any number what we want to write

credit_card = "1234-5678-9123-1234"

print(credit_card[4]) # there case with alone in result it must give us 1 num and if we taking only one we must count from zero

phone_number = "314-3524-221" 

print(phone_number[0:3]) # there i was pick 314 number from my phone number but if we taking more than one we must count from 1

# so that we getting first three numbers from the index 

# also here are not differense if we print [:3] or [0:3] we will get same result

print(phone_number[:3]) # here we go 

print(credit_card[5:9])

# and if we need end of index we can pick it like that 

print(credit_card[5:]) # and there we go 

# we can also reverse with negative number and our list going from the last numbers to forward 

print(credit_card[-2])

# we also have a step - step only write us numbers with an intervals 

print(phone_number[::2]) # there is result 

