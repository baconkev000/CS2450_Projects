from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog

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
        #Holds all data for UVSim
        self.data = [None] * size
        #Keeps the users instructions
        self.instructions = []
        #Used to point to where we are in the program
        self.pointer = 0
    
    def getMemoryLoc(self, loc):
        return self.data[loc]
    
    def updateMemory(self, loc, word):
        self.data[loc] = word

    def clearMemory(self):
        self.data = [None] * 100  

class Window:
    def __init__(self, cpu):
        self.cpu = cpu
        self.program = Tk()
        self.program.title('UVSim')
        self.program['bg'] = 'darkgrey'
        self.program.geometry('1000x600')#set the window size
        self.program.resizable(width=False,height=False)
        self.create_widgets()

    def saveFile(self):
       '''Saves file to computer as txt file'''
       file = filedialog.asksaveasfile(defaultextension = '.txt',
                                       filetypes=[("Text file", ".txt")])
       
       if file is None:
          return
       filetext = str(self.command_text.get(1.0,END))
       file.write(filetext)
       file.close()

    def loadFile(self):
      '''Loads file to UVSim'''

      try:

        filepath = filedialog.askopenfilename(title="Open BasicML Program", filetypes=[("Text file", ".txt")])
        file = open(filepath, 'r')
        text = file.read()
        self.command_text.insert("1.0", text)
        file.close()

      except:
         return

    def create_widgets(self):
        '''Creates different parts of the GUI'''

        self.create_command_text()
        self.create_console()
        self.create_compile_button()

    def create_console(self):
        '''Creates a console for I/O'''
        self.console = Text(self.program,height=10,width=100)
        self.console.config(bg='black', fg='green', insertbackground='green')
        self.console.pack()

    def create_command_text(self):
        '''Creates Textbox for command line'''
        self.command_text = Text(self.program)
        self.command_text.configure(bg='lightgrey', fg='black')
        self.command_text.pack(pady=20)

    def create_compile_button(self):
        '''Creates Save, Load, and Compile button'''
        button = Button(self.program, command=self.get_code, text="COMPILE")
        button.place(x=875,y=25)
        save_button = Button(self.program, command=self.saveFile, text ="SAVE")
        save_button.place(x=875, y=60)
        load_button = Button(self.program, comman=self.loadFile, text="LOAD")
        load_button.place(x=875, y=95)

    def get_code(self):
        '''Adds ability to call get_code from the Window class'''
        self.cpu.get_code(self.command_text)

    def display(self):
        '''Enables the console and displays a welcome message'''
        self.console.insert("1.0", "Welcome to UVSim! After each instruction, press enter.\nEvery instruction (including halt) is formatted #### (Command)(Location)\nMake sure to type END to mark the end of your instruction.\nPress compile when finished.\n")
        #self.disable_console()
        self.program.mainloop()


class CPU:
    def __init__(self):
        #A register
        self.accumulator = Register()
        #A list where instructions are held
        self.memory = Memory()
        #Window used for GUI
        self.window = Window(self)
        #List of valid commands
        self.valid_commands = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        self.consoleAcceptingInput = False

    def reset_CPU(self):
       '''Resets the CPU after an error message or end instruction is hit'''
       self.memory.pointer = 0
       self.memory.instructions = []
       self.memory.clearMemory()

    def update_console(self, message):
       '''Updates the message on the console'''
       #Learned to put END before inserting from AI
       self.window.console.insert(END, "\n")
       self.window.console.insert(END, message)
       self.window.console.insert(END, "\n")

    def get_code(self, text):
      '''Clears the Console and gets the user's code from the console and stores it in the list instructions'''
      #GPT taught me the below line
      #Gets the text the user entered
      #self.window.enable_console()
      self.window.console.delete("1.0", END)
      self.window.console.insert("1.0", "Welcome to UVSim! After each instruction, press enter.\nEvery instruction (including halt) is formatted #### (Command)(Location)\nMake sure to type END to mark the end of your instruction.\nPress compile when finished.\n")
      #self.window.disable_console()

      user_input = text.get("1.0", END)

      #Splits the input into a list to read
      self.memory.instructions = user_input.split('\n')
      #The last value is empty and it takes it out
      self.memory.instructions.pop()
      
      #Checks to make sure there is an END instruction
      contains_end = False
      for items in self.memory.instructions:
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
      If the user's input is not valid, it will print an error message and the line the error is on (self.memory.pointer)
      '''
      #Will be used to store instructions at a certain area in memory starting from 0
      memory_location = 0

      #Loops through the user's code and checks for errors
      for code in self.memory.instructions:

          #Keeps track of the line number for error handling
          self.memory.pointer += 1
          #Checks if command is END
          if code.upper() == 'END':
             self.memory.data[memory_location] = code
             self.process_code()
             break
          
          #Ensures the instruction is at least 4 digits
          if len(code) != 4:
             error_message = "\nError on line " + str(self.memory.pointer) + ".\nInvalid instruction."
             self.update_console(error_message)
             self.reset_CPU()
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
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nMemory location out of bounds."
              self.update_console(error_message)
              self.reset_CPU()

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nExpected a four digit int."
              self.update_console(error_message)
              self.reset_CPU()
              
          if command not in self.valid_commands:
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nInvalid command."
              self.update_console(error_message)
              self.reset_CPU()

          elif location < 0 or location > 99:
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nMemory location out of bounds."
              self.update_console(error_message)
              self.reset_CPU()

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

      self.memory.pointer = 0

      #Processes the code until a halt instruction is reached or a valid instruction is overwritten
      while True:
          
          code = self.memory.getMemoryLoc(self.memory.pointer)
          
          #Checks if the memory location has instructions
          if code == None:
             self.update_console("\nError, branched to a location with no defined instruction.")
             self.reset_CPU()


          elif code.upper() == 'END':
             #Checks if the code is an end instruction resets the program if it is
             self.reset_CPU()
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
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nData Overwriting"
              self.update_console(error_message)
              self.reset_CPU()

          #Input validation, if the code is not valid, a message is given and the program is exited
          #Ensures input is an int, the command is valid, and the memory location is in bounds
          try: 
              location = int(location)
              command = int(command)

          except:
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nData Overwriting"
              self.update_console(error_message)
              self.reset_CPU()

          if command not in self.valid_commands:
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nData Overwriting"
              self.update_console(error_message)
              self.reset_CPU()

          elif location < 0 or location > 99:
              error_message = "\nError on line " + str(self.memory.pointer) + ".\nData Overwriting"
              self.update_console(error_message)
              self.reset_CPU()

          #Instruction at the location is valid and can be processed
          if command == 10:
            '''READ function'''
            #Learned simplediaglog method from AI
            #Creates a pop-up box asking for a word
            self.window.console.delete('1.0',END)
            self.update_console("Enter a word\n")
            while True:#this while loop is used to allow input from the console
                self.window.program.update()#updates the window while waiting for valid user input
                words  = self.window.console.get('1.0',END)[:-1]
                if len(words) > 1 and words[-1] == '\n':#when the program gets two new lines in a row this statement is true
                    word = words[:-1].split('\n')[-1]#gets newest line and verifies that it is a valid input
                    if len(word) > 1 and word != 'Prog: Enter a word':
                        user_input = word
                        break
            #Updates the memory on whatever the user entered
            self.memory.updateMemory(location, user_input)
            self.memory.pointer += 1
        
          elif command == 11:
            '''WRITE from memory to console.'''
            try:
              to_print = self.memory.getMemoryLoc(location)
              self.update_console(to_print)
            except Exception as inst:
              error_message = "\n" + str(type(inst)) + "\n" + str(inst) + "\nError cannot process None-Type as Instruction"
              self.update_console(error_message)
            self.memory.pointer += 1
          
          elif command == 20:
            '''LOAD value from memory into accumulator'''
            self.accumulator.value = int(self.memory.data[int(location)])
            self.memory.pointer += 1

          elif command == 21:
            '''STORE a word from the accumulator into memory'''
            self.memory.data[int(location)] = self.accumulator.value
            self.memory.pointer += 1

          elif command == 30:
            # Add a word from a specific memory_location to the accumulator
            self.accumulator.value += int(self.memory.data[location])
            self.memory.pointer += 1

          elif command == 31:
            # Subtract a word from a specific memory_location from the word in the accumulator
            self.accumulator.value -= int(self.memory.data[location])
            self.memory.pointer += 1

          elif command == 32:
            # Divide the word in the accumulator by a word from a specific memory_location
            self.accumulator.value /= int(self.memory.data[location])
            self.memory.pointer += 1

          elif command == 33:
            # Multiply a word from a specific memory_location to the accumulator
            self.accumulator.value *= int(self.memory.data[location])
            self.memory.pointer += 1

          elif command == 40:
            #BRANCH to a location in memory
            if self.memory.pointer != location:#helps to avoid infinite loops
                self.memory.pointer = location
            else:
                self.update_console("\nCannot Branch to Self")
                self.memory.pointer += 1

          elif command == 41:
            #BRANCHNEG
            if self.accumulator.value < 0:#checks if accumulator is negative
                if self.memory.pointer != location:
                    self.memory.pointer = location
                else:
                    self.update_console("\nCannot Branch to Self")
                    self.memory.pointer += 1
            else:
                self.memory.pointer += 1

          elif command == 42:
            #BRANCHZERO
            if self.accumulator.value == 0:#checks if accumulator is zero
                if self.memory.pointer != location:
                    self.memory.pointer = location
                else:
                    self.update_console("\nCannot Branch to Self")
                    self.memory.pointer += 1
            else:
                self.memory.pointer += 1

          elif command == 43:
            #HALT
            simpledialog.askstring("Input", "Paused. Press Ok or cancel to continue")
            self.memory.pointer +=1

def main():
    """ Main entry point of the app """
    #Creates the cpu object
    cpu = CPU()
    #Displays GUI window
    cpu.window.display()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
