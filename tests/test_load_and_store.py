"""
Load and store tests written by Luke Durtschi
"""

__author__ = "Luke Durtschi"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from main import *

class TestLoadAndStore(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def test_can_load(self):
        self.cpu.execute_WRITE(0, "10")
        self.cpu.load(0)
        result = self.cpu.accumulator.value

        self.assertEqual(result, "10")
        self.assertNotEqual(result, 0)
    
    def test_can_store(self):
        self.cpu.accumulator.value = "5"

        self.cpu.store(1)
        result = self.cpu.memory.data[1]

        self.assertEqual(result, "5")
        self.assertNotEqual(result, 0)

    def test_can_load_overwrite_accumulator(self):
        self.cpu.accumulator.value = 15

        self.cpu.execute_WRITE(0, "6")
        self.cpu.load(0)
        result = self.cpu.accumulator.value

        self.assertEqual(result, "6")
        self.assertNotEqual(result, "15")

    def test_can_store_overwrite_memory_location(self):
        self.cpu.execute_WRITE(0, "3")
        self.cpu.accumulator.value = "11"

        self.cpu.store(0)
        result = self.cpu.memory.data[0]

        self.assertEqual(result, "11")
        self.assertNotEqual(result, "3")

    def tearDown(self):
        self.cpu.memory.clearMemory()

if __name__ == '__main__':
    unittest.main()