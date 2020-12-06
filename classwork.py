# Test your function with the following:

def average (num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

def avg (num):
    return sum(num)/len(num)

print(average([1, 5, 9]))

print(average(range(11)))

print("The Average is ", avg([1, 5, 9,10,20]))


names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names

lowercased = [names.lower() for name in names]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [names.title() for name in lowercased] 

  #print(f"Dear {name}, please come to the wedding this Saturday! " for name in titlecased)
#for invitation in invitation