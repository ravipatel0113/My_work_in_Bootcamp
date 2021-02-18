# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)
# for loop the game for more chances...
chance = int(input("Enter chances you need"))
for x in range(chance):
    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
    if computer_choice == user_choice:
        print("Your choice is " +user_choice)
        print("Computer Choice is " +computer_choice )
        print("Both tied")
    elif   ((user_choice == "r" ) and (computer_choice == "s")) or ((user_choice == "s") and (computer_choice =="p")) or ((user_choice == "p") and (computer_choice == "r")):
        print("Your choice is " +user_choice)
        print("Computer Choice is " +computer_choice )
        print("User Wins this round")
    elif ((user_choice =="r") and (computer_choice == "p")) or ((user_choice == "p") and (computer_choice == "s")) or ((user_choice == "s") and (computer_choice == "r")) :
        print("Your Choice is " +user_choice)
        print("Computer Choice is " +computer_choice )
        print("computer wins the round")

    else:
        print("no one wins the round...") 