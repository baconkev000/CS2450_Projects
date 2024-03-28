# """
# Branch and halt function tests
# """

# __author__ = "Damian Sacks"
# __version__ = "0.1.0"
# __license__ = "MIT"

# import unittest
# from main import *
# from unittest import mock

# class BranchAndHalt(unittest.TestCase):
#     def setUp(self):
#         self.cpu = CPU()

#     def test_can_branch(self):
#         location = '03'
#         self.cpu.branch(location)
#         self.assertEqual(self.cpu.pointer,'03')

#     def test_can_branch_negative(self):
#         location = '03'
#         self.cpu.accumulator.value = -1
#         self.cpu.branchneg(location)
#         self.assertEqual(self.cpu.pointer,'03')

#     def test_can_branch_zero(self):
#         location = '03'
#         self.cpu.accumulator.value = 0
#         self.cpu.branchzero(location)
#         self.assertEqual(self.cpu.pointer,'03')

#     def test_can_halt(self):
#         temp = self.cpu.pointer
#         with mock.patch('builtins.input', return_value='test'):
#             self.cpu.halt()
#             self.assertEqual(self.cpu.pointer, temp+1)#verify the system continues after the pause

#     def tearDown(self):
#         self.cpu.memory.clearMemory()

# if __name__ == '__main__':
#     unittest.main()