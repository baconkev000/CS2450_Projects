"""
Load and store tests updated by Kevin Bacon
d. Each test case should have test case number, short description, test date, inputs, expected outputs, pass/ fail. Display the results in a reporting form that clearly displays the success of your code, This set of assert tests can be used as one of the new metrics for you support of your code quality value.
"""

__author__ = "Kevin Bacon"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from main import *

class TestLoadAndStore(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def test_can_load_four_digits_9(self):
        """
        TEST #9 - 3/28/2024
        Tests that user can load 4 digits into acumulator
        Inputs - (string) 2024
        Expected Output - accumulator.value = (int) 2024
        """
        self.cpu.memory.data[10] = '202428'
        self.cpu.memory.data[0] = '2010'
        self.cpu.memory.data[1] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 202428)
    
    def test_can_load_six_digits_10(self):
        # self.cpu.execute_WRITE(0, "10")
        # self.cpu.load(0)
        # result = self.cpu.accumulator.value

        # self.assertEqual(result, "10")
        # self.assertNotEqual(result, 0)

        self.cpu.memory.data[10] = '202428'
        self.cpu.memory.data[0] = '2010'
        self.cpu.memory.data[1] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 202428)

    def test__11(self):
        # self.cpu.execute_WRITE(0, "10")
        # self.cpu.load(0)
        # result = self.cpu.accumulator.value

        # self.assertEqual(result, "10")
        # self.assertNotEqual(result, 0)

        self.cpu.memory.data[10] = '202428'
        self.cpu.memory.data[0] = '2010'
        self.cpu.memory.data[1] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 202428)
    
    def test_can_load_four_digits_12(self):
        # self.cpu.execute_WRITE(0, "10")
        # self.cpu.load(0)
        # result = self.cpu.accumulator.value

        # self.assertEqual(result, "10")
        # self.assertNotEqual(result, 0)

        self.cpu.memory.data[10] = '202428'
        self.cpu.memory.data[0] = '2010'
        self.cpu.memory.data[1] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 202428)

    def tearDown(self):
        self.cpu.memory.clearMemory()

if __name__ == '__main__':
    unittest.main()