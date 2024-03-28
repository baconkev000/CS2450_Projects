# """
# I/O tests written by Kevin Bacon
# """

# __author__ = "Kevin Bacon"
# __version__ = "0.1.0"
# __license__ = "MIT"

# import unittest
# from contextlib import redirect_stdout
# from io import StringIO
# from main import *
# class TestWrite(unittest.TestCase):
#     def setUp(self):
#         self.cpu = CPU()

#     def test_can_write(self):
#         """
#         testing that a user can write a word into memory given a valid location
#         """
#         self.cpu.execute_WRITE(0,"test")
#         result = self.cpu.memory.getMemoryLoc(0)

#         self.assertEqual(result, "test")
#         self.assertNotEqual(result, "Not Test")
    
#     def test_can_read(self):
#         """
#         testing that a user can read a word or instruction from memory given a valid location
#         """
#         self.cpu.execute_WRITE(0,"read")
#         result = self.cpu.execute_READ(0)

#         self.cpu.execute_WRITE(1,5)
#         result2 = self.cpu.execute_READ(1)

#         self.assertEqual(result2, 5)
#         self.assertEqual(result, "read")
#         self.assertNotEqual(result, "Not read")

#     def test_cannot_overwrite_memory(self):
#         """
#         testing that a user cannot overwrite memory and exception is raised
#         """
#         self.cpu.execute_WRITE(0,"test")
#         result = self.cpu.execute_READ(0)

#         self.assertEqual(result, "test")
#         with redirect_stdout(StringIO()):
#             self.assertRaises(Exception, self.cpu.execute_WRITE(0,"test2"))


#     def test_can_read_unwritten_location(self):
#         """
#         testing that a user can read from an unwritten location and it returns None
#         """
#         cpu = CPU()
#         result = cpu.execute_READ(0)
#         self.assertEqual(result, None)

#     def tearDown(self):
#         self.cpu.memory.clearMemory()

# if __name__ == '__main__':
#     unittest.main()