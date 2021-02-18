# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")  # will not come
else:
    print("oooo needs some work")   #will be printed


# 2.
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!")  #will be printed
else:
    print("Still missing out")  # not printed

# 3.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")    # will be printed
else:
    print("Oh good you can count")   # will not be printed

# 4.
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]  
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")  # not printed
elif name in group_two:
    print(name + " is in group two")    #not printed
elif name in group_three:
    print(name + " is in group three")  # will be printed
else:
    print(name + " does not have a group")  # will not print


# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")    #will not print
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")   # will not print
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")  # will not print
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")   # will be printed
else:
    print("Stick to lazy river")    # will not print
