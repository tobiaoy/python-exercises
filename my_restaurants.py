from restaurant import Restaurant as RNT

mcd = Restaurant('Mcdonalds', 'Fast Food')
mcd.describe_restaurant()
mcd.increment_number_served(1000)
mcd.describe_restaurant()

dominos = Restaurant('Dominos', 'Pizza')
dominos.describe_restaurant()
dominos.increment_number_served(500)
dominos.describe_restaurant()

osmows = Restaurant('Osmows', 'Mediterranean')
osmows.describe_restaurant()
osmows.increment_number_served(700)
osmows.describe_restaurant()