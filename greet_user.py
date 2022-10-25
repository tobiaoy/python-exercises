import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username"""
    username = input("What's your name friend? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greets the user by name"""
    username = get_stored_username()
    verified = input("Is this the correct name: {username}? y/n \n".format(username=username))

    if verified == 'y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll definitely remember {username}")
        
greet_user()