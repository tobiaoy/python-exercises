import json

username = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f) #so the data is passed in first and then the file object, in this case f
    print(f"We'll remember you when you come back, {username}")
