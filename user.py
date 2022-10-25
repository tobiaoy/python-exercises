class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_type = 'standard'
        self.login_attempts = 0
        
    def describe_user(self):
        print("User Summary")
        print("First Name: {name}".format(name=self.first_name))
        print("Last Name: {name}".format(name=self.last_name))
        print("User Type: {type}".format(type=self.user_type))
        
    def greet_user(self):
        print("Hello {first} {last}".format(first=self.first_name, last=self.last_name))
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
marcus = User('Marcus', 'Rashford')
ronaldo = User('Christiano', 'Ronaldo')
lisandro = User('Lisandro', 'Martinez')
david = User('David', 'De Gea')

david.increment_login_attempts()
david.increment_login_attempts()
david.increment_login_attempts()
david.increment_login_attempts()
david.increment_login_attempts()
david.increment_login_attempts()
david.increment_login_attempts()
david.increment_login_attempts()

team = [marcus, ronaldo, lisandro, david]

for player in team:
    player.describe_user()
    print("")
    player.greet_user()
    print("")
    
print(david.login_attempts)
david.reset_login_attempts()
print(david.login_attempts)



#special admin class
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.user_type = 'admin'
        self.privileges = Privileges()
        
        
class Privileges:
    def __init__(self):
        self.privileges = []
        
    def add_privilege(self, priv):
        self.privileges.append(priv)
        
    def show_privileges(self):
        print(self.privileges)
        
