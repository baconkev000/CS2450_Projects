import unittest
from main import *

class TestWrite(unittest.TestCase):
    def test_write(self):
        cpu = CPU()
        cpu.execute_WRITE(0,"test")
        result = cpu.memory.getMemoryLoc(0)

        self.assertEqual(result, "test")
        self.assertNotEqual(result, "Not Test")
    
    def test_read(self):
        cpu = CPU()
        cpu.execute_WRITE(0,"read")
        result = cpu.execute_READ(0)

        self.assertEqual(result, "read")
        self.assertNotEqual(result, "Not read")

if __name__ == '__main__':
    unittest.main()