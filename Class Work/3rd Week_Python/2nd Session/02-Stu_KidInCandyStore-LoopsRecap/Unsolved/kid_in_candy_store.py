# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for i in range(len(candy_list)):
    print("[" +str(i)+ "]" + candy_list[i])

ans = "yes"
while ans== "yes":
    print("Which candy you want to have...? ")
    selected = input("select the candy number you want...")
    candy_cart.append(candy_list[int(selected)])
    print(candy_cart)
    ans =input("Would you like to have more candy yes/no...")

print("I brought this many things for you...")
for candy in candy_cart:
    print(candy)