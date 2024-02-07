"""
Compile tests written by Matt Scott
"""

__author__ = "Matt Scott"
__version__ = "0.1.0"
__license__ = "MIT"

'''
AI wrote these tests and I learned what they
mean. I then practiced until I could write them on my own.

Process Code has the exact same code as compile() with some
additional code, meaning compile doesn't need it's own 
tests as it's covered in the tests for process_code(). 
'''

import unittest
from unittest.mock import patch
from main import CPU
import io

class TestCompiler(unittest.TestCase):

  @patch('builtins.input', side_effect=['INPUT1', 'INPUT2', 'END', 'COMPILE'])
  def test_if_correct_input_added(self, mock_input):
    
    cpu_instance = CPU()

    cpu_instance.get_code()

    self.assertEqual(cpu_instance.instructions, ['INPUT1', 'INPUT2'])

  # Test case for get_code method without "END" in the input
  @patch('builtins.input', side_effect=['INPUT1', 'INPUT2', 'COMPILE'])
  def test_input_without_end(self, mock_input):

    cpu_instance = CPU()

    with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as replacement_output:
      with self.assertRaises(SystemExit) as e:
        cpu_instance.get_code()

        self.assertEqual('Error. No END instruction written in the program.', replacement_output.getvalue())

  def test_process_code_valid_inputs(self):

    cpu_instance = CPU()

    cpu_instance.memory.updateMemory(0, '1001')

    with patch('builtins.input', return_value='42'):
      with self.assertRaises(SystemExit) as error:
        cpu_instance.process_code()

    self.assertIsNone(error.exception.code)

  def test_process_code_invalid_input(self):

    cpu_instance = CPU()

    cpu_instance.memory.updateMemory(0, 'InvalidInput')

    with patch('builtins.input', return_value = '42'):
      with self.assertRaises(SystemExit):
        cpu_instance.process_code()


if __name__ == '__main__':
  unittest.main()
