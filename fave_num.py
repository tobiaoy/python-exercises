import json
filename = 'fav_num.json'

num = input("Please enter your favorite number? ")
    
with open(filename, 'w') as f:
    json.dump(num, f)
    print(f"I'll remember that, it's {num}")