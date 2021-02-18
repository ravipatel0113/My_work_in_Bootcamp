# Take input of you and your neighbor
name = input("What is your name?")
ne_name = input("What is the neighbor name?")
# Take how long each of you have been coding
Time_code = int(input("How long have you been coding?"))
netime_code = int(input("How long your neighbour " +ne_name+" have been coding?"))
# Add total month
sum = Time_code+netime_code

# Print results
print(f"your name is {name} and my neighbour name is {ne_name}")
print("Total month coded together " +str(sum) + " months!")