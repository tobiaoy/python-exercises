import unittest
from city_functions import make_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_city_country(self):
        """Do inputs like santiago and chile work?"""
        location = make_city_country('santiago', 'chile')
        self.assertEqual(location, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """Do inputs with a population parameter work?"""
        location = make_city_country('santiago', 'chile', 5000000)
        self.assertEqual(location, 'Santiago, Chile - population 5000000')
        
if __name__ == '__main__':
    unittest.main()