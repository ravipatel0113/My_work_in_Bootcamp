# Initial variable to track shopping status
shop ="y"

# List to track pie purchases
pie_purchases=[0,0,0,0,0,0,0,0,0,0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")


# While we are still shopping...
while shop =="y":
    print("Choose the pie you want form the list...")
    select= input("Select the pie")
    choose_index = int(select)-1
   
    pie_purchases[choose_index] += 1
    shop = input("Would you like to have more pie yes/no...")
    print("your purchase...")
   # tot = tot +  1
# Loop starts here
for pie_index in range(len(pie_list)):
    pie_count = str(pie_purchases[pie_index])
    pie_name = str(pie_list[pie_index])
    # Loop end here
    # Once the pie list is complete
    print(pie_count+ "  "+pie_name )
    print("------------------------------------------------------------------------")
    #print("You purchased a total of " + str(tot) + ".")
    