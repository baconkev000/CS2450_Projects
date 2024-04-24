"""
Load and store tests updated by Kevin Bacon
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
        TEST #9 - 4/24/2024
        Tests that user can load 4 digits into acumulator
        Inputs - (string) 2024
        Expected Output - accumulator.value = (int) 2024
        """
        self.cpu.memory.data[10] = '2024'
        self.cpu.memory.data[0] = '2010'
        self.cpu.memory.data[1] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 2024)
    
    def test_can_load_six_digits_10(self):
        """
        TEST #10 - 4/24/2024
        Tests that user can load 6 digits into acumulator
        Inputs - (string) 202428
        Expected Output - accumulator.value = (int) 202428
        """

        self.cpu.memory.data[10] = '202428'
        self.cpu.memory.data[0] = '2010'
        self.cpu.memory.data[1] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 202428)

    def test_can_store_four_digits_11(self):
        """
        TEST #11 - 4/24/2024
        Tests that user can store 4 digits into memory
        Inputs - (string) 2000
        Expected Output - accumulator.value = (int) 2000
        """

        self.cpu.accumulator.value = 2000
        self.cpu.memory.data[0] = "2110"
        self.cpu.memory.data[1] = "3010"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()


        result = self.cpu.accumulator.value
        self.assertEqual(result, 4000)
    
    def test_can_store_six_digits_12(self):
        """
        TEST #12 - 4/24/2024
        Tests that user can store 6 digits into memory
        Inputs - (string) 5000
        Expected Output - accumulator.value = (int) 10000
        """

        self.cpu.accumulator.value = 5000
        self.cpu.memory.data[0] = "2110"
        self.cpu.memory.data[1] = "3010"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()


        result = self.cpu.accumulator.value
        self.assertEqual(result, 10000)

    def tearDown(self):
        self.cpu.memory.clearMemory()

if __name__ == '__main__':
    unittest.main()