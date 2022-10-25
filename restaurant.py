from unicodedata import name


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("The restaurant {name} serves {cuisine_type} and has served {num}".format(name = self.name, cuisine_type=self.cuisine_type, num=self.number_served))
        
    def open_restaurant(self):
        print("The restaurant {name} is open".format(name=self.name))
        
    def set_number_served(self, num):
        if num < 0:
            return
        else:
            self.number_served = num
    
    def increment_number_served(self, num):
        if num < 0:
            return
        else: 
            self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
        
    def showFlavors(self):
        print(flavors)
    
    def addFlavor(self, flavor):
        self.flavors.append(flavor)
        
ben_and_jerry = IceCreamStand('Ben and Jerrys', 'Dessert')

flavors = ['strawberry', 'chocolate', 'vanilla', 'mint']
for f in flavors:
    ben_and_jerry.addFlavor(f)
    
ben_and_jerry.showFlavors()