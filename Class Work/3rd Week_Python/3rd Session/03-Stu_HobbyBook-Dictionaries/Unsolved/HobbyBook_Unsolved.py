# Dictionary full of info
my_info = {
    "name": ["Ravi", "Patel"],
    "age": 22,
    "hobbies":[
        "reading Books",
        "play video Games",
        "football",
        "watch animenation"
    ]
}
weekend = {
    "week": "10am"
}

# Print out results are stored in the dictionary
print(f'My name is: {my_info["name"][0]}')
print(f'I am {my_info["age"]} year old')
print(f'My hobbies are: {my_info["hobbies"]}')
print(f'On weekend I wake up at: {weekend["week"]}')
print(f'{my_info.keys()} {weekend.keys()}')
for k,v in my_info.items():
    print(k,v)