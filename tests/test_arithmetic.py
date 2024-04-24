"""
Arithmetic tests updated by Luke Durtschi
"""

# __author__ = "Luke Durtschi"
# __version__ = "0.1.0"
# __license__ = "MIT"

import unittest
from main import *

class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def test_can_add_four_digits_1(self):
        """
        TEST #1 - 4/24/2024
        Tests to make sure the user can add four
        digit numbers to the accumulator.
        Inputs - (string) 1050
        Expected Output - accumulator.value = (int) 2100
        """
        self.cpu.memory.data[10] = "1050"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3010"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 2100)

    def test_can_add_six_digits_2(self):
        """
        TEST #2 - 4/24/2024
        Tests to make sure the user can add six
        digit numbers to the accumulator.
        Inputs - (string) 5000
        Expected Output - accumulator.value = (int) 10000
        """
        self.cpu.memory.data[10] = "5000"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3010"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 10000)

    def test_can_subtract_four_digits_3(self):
        """
        TEST #3 - 4/24/2024
        Tests to make sure the user can subtract four
        digit numbers to the accumulator.
        Inputs - (string) 3050, (string) 1040
        Expected Output - accumulator.value = (int) 2010
        """
        self.cpu.memory.data[10] = "3050"
        self.cpu.memory.data[11] = "1040"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3111"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 2010)

    def test_can_subtract_six_digits_4(self):
        """
        TEST #4 - 4/24/2024
        Tests to make sure the user can subtract six
        digit numbers to the accumulator.
        Inputs - (string) -9000, (string) 2000
        Expected Output - accumulator.value = (int) -11000
        """
        self.cpu.memory.data[10] = "-9000"
        self.cpu.memory.data[11] = "2000"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3111"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, -11000)

    def test_can_divide_four_digits_5(self):
        """
        TEST #5 - 4/24/2024
        Tests to make sure the user can divide four
        digit numbers to the accumulator.
        Inputs - (string) 8000, (string) 2000
        Expected Output - accumulator.value = (int) 4
        """
        self.cpu.memory.data[10] = "8000"
        self.cpu.memory.data[11] = "2000"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3211"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 4)

    def test_can_divide_six_digits_6(self):
        """
        TEST #6 - 4/24/2024
        Tests to make sure the user can divide six
        digit numbers to the accumulator.
        Inputs - (string) 8000, (string) 4000
        Expected Output - accumulator.value = (int) 16000
        """
        self.cpu.memory.data[10] = "8000"
        self.cpu.memory.data[11] = "4000"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3211"
        self.cpu.memory.data[1] = "3010"
        self.cpu.memory.data[1] = "3010"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 16000)

    def test_can_multiply_four_digits_7(self):
        """
        TEST #7 - 4/24/2024
        Tests to make sure the user can multiply a four
        digit number to the accumulator.
        Inputs - (string) 3, (string) 2500
        Expected Output - accumulator.value = (int) 7500
        """
        self.cpu.memory.data[10] = "3"
        self.cpu.memory.data[11] = "2500"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3311"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 7500)

    def test_can_multiply_six_digits_8(self):
        """
        TEST #8 - 4/24/2024
        Tests to make sure the user can multiply a six
        digit number to the accumulator.
        Inputs - (string) 8000, (string) 20
        Expected Output - accumulator.value = (int) 160000
        """
        self.cpu.memory.data[10] = "8000"
        self.cpu.memory.data[11] = "20"
        self.cpu.memory.data[0] = "3010"
        self.cpu.memory.data[1] = "3311"
        self.cpu.memory.data[2] = "END"
        self.cpu.process_code()

        result = self.cpu.accumulator.value
        self.assertEqual(result, 160000)

    def tearDown(self):
        self.cpu.memory.clearMemory()

if __name__ == '__main__':
    unittest.main()