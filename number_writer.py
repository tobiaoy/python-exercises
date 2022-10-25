import json

numbers = [2,3,5,7,9,11,12,14]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)