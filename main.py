"""
Module Docstring
"""

__author__ = "Kevin Bacon"
__version__ = "0.1.0"
__license__ = "MIT"

from operations.write.write import Write


class Register:
    def __init__(self):
        self.value = 0

class Memory:
    def __init__(self, size = 100):
        self.size = size
        self.data = [0] * size
    
    def getMemoryLoc(self, loc):
       return self.data[loc]
    
    def updateMemory(self, loc, word):
       self.data[loc] = word
    

class CPU:
    def __init__(self):
        accumulator = Register()
        self.memory = Memory()
        #Will be used for the user to debug their program
        self.pointer = 0
        #List of valid commands
        self.valid_commands = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        #Keeps the users instructions
        self.instructions = []

    def execute_READ(self, memory_location):
    # Read a word from the keyboard into a specific memory_location in memory
      return self.memory.getMemoryLoc(memory_location)

    def execute_WRITE(self, memory_location, word):
    # Write a word from a specific memory_location in memory to the screen changes
      return self.memory.updateMemory(memory_location, word)
        
    def load(self, memory_location):
        print('load')
    
    def store(self, memory_location):
        print('store')
    
    def add(self, memory_location):
        print('add')

    def subtract(self, memory_location):
        print('subtract')

    def divide(self, memory_location):
        print('divide')

    def multiply(self, memory_location):
       print('multiply')

    def branch(self, memory_location):
        print('branch')

    def branchneg(self, memory_location):
        print('branchneg')
    
    def branchzero(self, memory_location):
        print('branchzero')
    
    def halt(self):
        print('halt')

    def get_code(self):
      '''Gets the user's code from the consol and stores it in the list instructions'''
      #Welcome message
      print("Welcome to UVSim! After each instruction, press enter.")
      print("Type Compile, when your program is complete: \n")

      #User input, BasicML code
      ui = ""

      #Loops to get the code from the user
      while ui != "compile".upper():
          ui = str(input()).upper()

          if ui.upper() != "COMPILE":
            self.instructions.append(ui)
    
    def process_code(self):
      '''Processes the user's code
      Splits each line of the user's code into two, the command and memory location (command, location)
      Does input validation and turns the command and location into ints
      If the user's input is not valid, it will print an error message and the line the error is on (self.pointer)
      If the input is valid, it will call on the function the user called
      '''

      #Loops through the user's code and executes the appropriate function
      for code in self.instructions:

          #Keeps track of the line number for error handling
          self.pointer += 1
          #Chooses which operation is performed
          command = code[:2]
          #Ensures that there is a valid int for choosing location in memory
          if code[2] != '0':
            location = code[2:]
          else:
            if len(code[1:]) == 2:
              location = code[3]

            else:
              print(f'Error on line {self.pointer}.')
              print('Memory location out of bounds.')
              exit()

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              print(f"Error on line {self.pointer}.")
              print('Expected a four digit int.')
              exit()

          if command not in self.valid_commands:
              print(f'Error on line {self.pointer}.')
              print('Invalid command.')
              exit()

          elif location <= 0 or location > 99:
              print(f'Error on line {self.pointer}.')
              print('Memory location out of bounds.')
              exit()


          #Code is valid and can be processed, calls the function the user called
          if command == 10:
            self.execute_READ(location)
        
          elif command == 11:
            self.execute_WRITE(location)
          
          elif command == 20:
            self.load(location)

          elif command == 21:
            self.store(location)

          elif command == 30:
            self.add(location)

          elif command == 31:
            self.subtract(location)

          elif command == 32:
            self.divide(location)

          elif command == 33:
            self.multiply(location)

          elif command == 40:
            self.branch(location)

          elif command == 41:
            self.branchneg(location)

          elif command == 42:
            self.branchzero(location)

          elif command == 43:
            self.halt()
def main():
    """ Main entry point of the app """
    
    #Creates the cpu object
    cpu = CPU()
    cpu.get_code()
    cpu.process_code()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()