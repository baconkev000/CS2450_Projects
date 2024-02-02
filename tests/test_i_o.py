"""
I/O tests written by Kevin Bacon
"""

__author__ = "Kevin Bacon"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from main import *

class TestWrite(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def test_can_write(self):
        self.cpu.execute_WRITE(0,"test")
        result = self.cpu.memory.getMemoryLoc(0)

        self.assertEqual(result, "test")
        self.assertNotEqual(result, "Not Test")
    
    def test_can_read(self):
        self.cpu.execute_WRITE(0,"read")
        result = self.cpu.execute_READ(0)

        self.cpu.execute_WRITE(1,5)
        result2 = self.cpu.execute_READ(1)

        self.assertEqual(result2, 5)
        self.assertEqual(result, "read")
        self.assertNotEqual(result, "Not read")

    def test_can_overwrite_memory(self):
        self.cpu.execute_WRITE(0,"test")
        result = self.cpu.execute_READ(0)

        self.assertEqual(result, "test")


        self.cpu.execute_WRITE(0,"test2")
        result = self.cpu.execute_READ(0)

        self.assertNotEqual(result, "test")
        self.assertEqual(result, "test2")

    def test_can_read_unwritten_location(self):
        cpu = CPU()
        result = cpu.execute_READ(0)
        self.assertEqual(result, 0)

    def tearDown(self):
        self.cpu.memory.clearMemory()

if __name__ == '__main__':
    unittest.main()