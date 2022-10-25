import unittest
from employee import Employee

class TestEmployeeCase(unittest.TestCase):
    """Tests for the employee class"""
    
    def setUp(self):
        self.my_employee = Employee('Kendall', 'Roy', 150000)
        
    def test_give_default(self):
        """Testing to add the default raise amount"""
        self.my_employee.give_raise()
        self.assertTrue(self.my_employee.salary, 155000)
        
    def test_give_custom_raise(self):
        """Testing to add a custom raise amount"""
        self.my_employee.give_raise(4500)
        self.assertTrue(self.my_employee.salary, 154500)
        
if __name__ == '__main__':
    unittest.main()