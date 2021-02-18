fish = "halibut"

# Loop through each letter in the string
# and push to an array
letters = []

# List comprehensions provide concise syntax for creating lists
letters = [letter for letter in fish]

print(letters)

# We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.lower())
    if capital_letters[0] ==capital_letters[0].lower():
        capital_letters[0] = capital_letters[0].upper()
print(capital_letters)

# List Comprehension for the above
#capital_letters = [letter for letter in fish if ]
#print(capital_letters)

# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
print(hot_days)

# List Comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if temperature >90]
print(hot_days)
