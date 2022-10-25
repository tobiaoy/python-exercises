from user import User

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