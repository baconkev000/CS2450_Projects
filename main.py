from tkinter import *
from tkinter import simpledialog

"""
CS 2450 - Project
Contributions:
    Kevin Bacon: I/O functions, I/O tests, main.py base setup, ReadMe.md
    Luke Durtschi: Arithmetic functions and tests, load and store functions
    Matt Scott: Also provided skeleton and created compiler for instructions to processed
    Damian Sacks: Branching functions and tests, halt function and tests
"""

__author__ = "Kevin Bacon, Luke Durtschi, Matt Scott, Damian Sacks"
__version__ = "0.1.0"
__license__ = "MIT"


class Register:
    def __init__(self):
        self.value = 0

class Memory:
    def __init__(self, size = 100):
        self.size = size
        self.data = [None] * size
    
    def getMemoryLoc(self, loc):
       return self.data[loc]
    
    def updateMemory(self, loc, word):
       self.data[loc] = word

    def clearMemory(self):
       self.data = [None] * 100  

class CPU:
    def __init__(self):
        #A register
        self.accumulator = Register()
        #A list where instructions are held
        self.memory = Memory()
        #Used to point where we are in the program
        self.pointer = 0
        #List of valid commands
        self.valid_commands = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        #Keeps the users instructions
        self.instructions = []

        self.program = Tk()

        #Creates a console and displays a welcome message
        self.console = Text()
        self.console.config(bg='black', fg='green', insertbackground='green')
        self.console.pack()

        #Creates Textbox for command line
        self.command_text = Text(self.program)
        self.command_text.configure(bg='white', fg='black')
        self.command_text.pack()

    def update_console(self, message):
       '''Updates the message on the console'''
       self.enable_console()
       #Learned to put END before inserting from AI
       self.console.insert(END, "\n")
       self.console.insert(END, message)
       self.console.insert(END, "\n")
       self.disable_console()

    def disable_console(self):
       '''Disables the users ability to type to the console'''
       self.console.config(state='disabled')

    def enable_console(self):
       '''Enables the users ability to type to the console'''
       self.console.config(state='normal')


    def get_code(self, text):
      '''Clears the Console and gets the user's code from the console and stores it in the list instructions'''
      #GPT taught me the below line
      #Gets the text the user entered
      self.enable_console()
      self.console.delete("1.0", END)
      self.console.insert("1.0", "Welcome to UVSim! After each instruction, press enter.\nEvery instruction (including halt) is formatted #### (Command)(Location)\nMake sure to type END to mark the end of your instruction.\nPress compile when finished.")
      self.disable_console()

      user_input = text.get("1.0", END)

      #Splits the input into a list to read
      self.instructions = user_input.split('\n')
      #The last value is empty and it takes it out
      self.instructions.pop()
      
      #Checks to make sure there is an END instruction
      contains_end = False
      for items in self.instructions:
         if items.upper() == 'END':
            contains_end = True
            break
         
      if contains_end == False:
         #Prints an error message if there is no end instruction
         no_end = "\nError: No END instruction."
         self.update_console(no_end)

      else:
         #There was an end instruction, code is ready to compile
         self.compile()
    
    def compile(self):
      '''Processes the user's code and catches an error before running it
      Splits each line of the user's code into two, the command and memory location (command, location)
      Does input validation and turns the command and location into ints
      If the user's input is not valid, it will print an error message and the line the error is on (self.pointer)
      '''
      #Will be used to store instructions at a certain area in memory starting from 0
      memory_location = 0

      #Loops through the user's code and checks for errors
      for code in self.instructions:

          #Keeps track of the line number for error handling
          self.pointer += 1
          #Checks if command is END
          if code.upper() == 'END':
             self.memory.data[memory_location] = code
             self.process_code()
             break
          
          #Ensures the instruction is at least 4 digits
          if len(code) != 4:
             error_message = "\nError on line " + str(self.pointer) + ".\nInvalid instruction."
             self.update_console(error_message)
             break
             
          #Chooses which operation is performed
          command = code[:2]
          #Ensures that there is a valid int for choosing location in memory
          if code[2] != '0':
            location = code[2:]
          else:
            if len(code[2:]) == 2:
              location = code[3]

            else:
              error_message = "\nError on line " + str(self.pointer) + ".\nMemory location out of bounds."
              self.update_console(error_message)

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              error_message = "\nError on line " + str(self.pointer) + ".\nExpected a four digit int."
              self.update_console(error_message)
              
          if command not in self.valid_commands:
              error_message = "\nError on line " + str(self.pointer) + ".\nInvalid command."
              self.update_console(error_message)

          elif location < 0 or location > 99:
              error_message = "\nError on line " + str(self.pointer) + ".\nMemory location out of bounds."
              self.update_console(error_message)

          else:
             #Code was valid and is added to a location in memory
             self.memory.data[memory_location] = code
             memory_location += 1
   
    def process_code(self):

      '''
      Executes the program
      Still checks to make sure the instruction is valid in case the user 
      stores data at a location that previously held an instruction
      If code is valid, it will execute the appropriate function
      '''

      self.pointer = 0

      #Processes the code until a halt instruction is reached or a valid instruction is overwritten
      while True:
          
          code = self.memory.getMemoryLoc(self.pointer)
          
          #Checks if the memory location has instructions
          if code == None:
             self.update_console("\nError, branched to a location with no defined instruction.")


          elif code.upper() == 'END':
             #Checks if the code is an end instruction resets the program if it is
             self.memory.clearMemory()
             self.pointer = 0
             break
          
          #Chooses which operation is performed
          command = code[:2]
          #Ensures that there is a valid int for choosing location in memory
          if code[2] != '0':
            location = code[2:]
          else:
            if len(code[2:]) == 2:
              location = code[3]

            else:
              error_message = "\nError on line " + str(self.pointer) + ".\nData Overwriting"
              self.update_console(error_message)

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              error_message = "\nError on line " + str(self.pointer) + ".\nData Overwriting"
              self.update_console(error_message)

          if command not in self.valid_commands:
              error_message = "\nError on line " + str(self.pointer) + ".\nData Overwriting"
              self.update_console(error_message)

          elif location < 0 or location > 99:
              error_message = "\nError on line " + str(self.pointer) + ".\nData Overwriting"
              self.update_console(error_message)

          #Instruction at the location is valid and can be processed
          if command == 10:
            '''READ function'''
            self.enable_console()
            #Learned simplediaglog method from AI
            #Creates a pop-up box asking for a word
            user_input = simpledialog.askstring("Input", "Enter a word")
            #Updates the memory on whatever the user entered
            self.memory.updateMemory(location, user_input)
            self.pointer += 1
        
          elif command == 11:
            '''WRITE from memory to console.'''
            try:
              to_print = self.memory.getMemoryLoc(location)
              self.update_console(to_print)
            except Exception as inst:
              error_message = "\n" + str(type(inst)) + "\n" + str(inst) + "\nError cannot process None-Type as Instruction"
              self.update_console(error_message)
            self.pointer += 1
          
          elif command == 20:
            '''LOAD value from memory into accumulator'''
            self.accumulator.value = int(self.memory.data[int(location)])
            self.pointer += 1

          elif command == 21:
            '''STORE a word from the accumulator into memory'''
            self.memory.data[int(location)] = self.accumulator.value
            self.pointer += 1

          elif command == 30:
            # Add a word from a specific memory_location to the accumulator
            self.accumulator.value += int(self.memory.data[location])
            self.pointer += 1

          elif command == 31:
            # Subtract a word from a specific memory_location from the word in the accumulator
            self.accumulator.value -= int(self.memory.data[location])
            self.pointer += 1

          elif command == 32:
            # Divide the word in the accumulator by a word from a specific memory_location
            self.accumulator.value /= int(self.memory.data[location])
            self.pointer += 1

          elif command == 33:
            # Multiply a word from a specific memory_location to the accumulator
            self.accumulator.value *= int(self.memory.data[location])
            self.pointer += 1

          elif command == 40:
            #BRANCH to a location in memory
            if self.pointer != location:#helps to avoid infinite loops
                self.pointer = location
            else:
                self.update_console("\nCannot Branch to Self")
                self.pointer += 1

          elif command == 41:
            #BRANCHNEG
            if self.accumulator.value < 0:#checks if accumulator is negative
                if self.pointer != location:
                    self.pointer = location
                else:
                    self.update_console("\nCannot Branch to Self")
                    self.pointer += 1
            else:
                self.pointer += 1

          elif command == 42:
            #BRANCHZERO
            if self.accumulator.value == 0:#checks if accumulator is zero
                if self.pointer != location:
                    self.pointer = location
                else:
                    self.update_console("\nCannot Branch to Self")
                    self.pointer += 1
            else:
                self.pointer += 1

          elif command == 43:
            #HALT
            simpledialog.askstring("Input", "Paused. Press Ok or cancel to continue")
            self.pointer +=1

    def display_window(self):
      '''Creates the window, text box, and submit button. Passes text to get_code when button is clicked'''
      self.enable_console()
      self.console.insert("1.0", "Welcome to UVSim! After each instruction, press enter.\nEvery instruction (including halt) is formatted #### (Command)(Location)\nMake sure to type END to mark the end of your instruction.\nPress compile when finished.")
      self.disable_console()
      #Creates button and passes text to process_code when hit for command line
      button = Button(self.program, command=lambda: self.get_code(self.command_text), text="COMPILE")
      button.pack()

def main():
    """ Main entry point of the app """
    
    #Creates the cpu object
    cpu = CPU()
    cpu.display_window()
    #AI suggested putting main loop in main function to fix bug
    cpu.program.mainloop()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

