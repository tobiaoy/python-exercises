import json

filename = 'fav_num.json'

def get_fav_num():
    """Gets fav num if it exists"""
    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        pass
    else:
        return num
    
def get_new_fav():
    """Prompts user for their fav num"""
    num = input("Please enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(num, f)
    return num

def read_fav_num():
    num = get_fav_num()
    if num:
        print("I found your favorite number, it's {num}".format(num=num))
    else:
        num = get_new_fav()
        print("I'll remember that for next time, it's {num}".format(num = num))
        
read_fav_num()