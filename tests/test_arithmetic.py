"""
Arithmetic tests written by Luke Durtschi
"""

__author__ = "Luke Durtschi"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from main import *

class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def test_can_add(self):
        self.cpu.execute_WRITE(0, "7")
        self.cpu.add(0)
        result = self.cpu.accumulator.value

        self.assertEqual(result, 7)
        self.assertNotEqual(result, 0)
    
    def test_can_subtract(self):
        self.cpu.accumulator.value = 7

        self.cpu.execute_WRITE(0, "4")
        self.cpu.subtract(0)
        result = self.cpu.accumulator.value

        self.assertEqual(result, 3)
        self.assertNotEqual(result, 7)

    def test_can_divide(self):
        self.cpu.accumulator.value = 20

        self.cpu.execute_WRITE(0, "4")
        self.cpu.divide(0)
        result = self.cpu.accumulator.value

        self.assertEqual(result, 5)
        self.assertNotEqual(result, 20)

    def test_can_multiply(self):
        self.cpu.accumulator.value = 6

        self.cpu.execute_WRITE(0, "3")
        self.cpu.multiply(0)
        result = self.cpu.accumulator.value

        self.assertEqual(result, 18)
        self.assertNotEqual(result, 3)

    def tearDown(self):
        self.cpu.memory.clearMemory()

if __name__ == '__main__':
    unittest.main()