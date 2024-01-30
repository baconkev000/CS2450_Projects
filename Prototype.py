from tkinter import *
from operations.write.write import Write
'''
This code still has some bugs and does not
include every function.
Some of the functions do work and it could
be a good starting point.
'''

def save():
  '''Creates 100 memory spots for items'''
  memory = []
  for items in range(100):
    memory.append([])

  return memory

def input_validation(items, line_num):
  '''Ensures input is correct'''

  valid_c = ['10', '11', '20', '21', '30', '31', '32', '33', '40', '41', '42', '43']

  #Splits the items into command and memory location
  command = items[0:2]
  location = items[2:]

  #Ensures command is long enough
  if len(items) > 4:
    print(f'Error on line: {line_num}')
    print('Expected a four digit number')
    exit()

  #Input validation for command
  if command not in valid_c:
    print(f'Error on line: {line_num}')
    print('Command is not valid')
    exit()

  #FIXME make sure a decimal number or a string is not entered for location

  #Input validation for location
  if int(location) > 99 or int(location) < 0:
    print(f'Error on line: {line_num}')
    print('Memory location is out of bounds')
    exit()

def read_word():
  '''Creates a window for the user to input a message and closes it when submit is pressed'''

  ui = ""
  def process_text(message):
    '''Helper function, processes code input by the user when submit is pressed'''
    nonlocal ui
    ui = message.get("1.0", END)

    #Ensures the input was in int, if not, it exits the function and prints an error message in process_code
    try:
      ui = int(ui)
      #Closes the input window
      input_line.destroy()
    except:
      print("Input is not a number")
      input_line.destroy()

  #Creates an entry box 
  input_line = Tk()

  #Creates textbox
  text = Text(input_line)
  text.pack()

  #Creates button for submitting an entry
  button = Button(input_line, text="SUBMIT", command=lambda: process_text(text))
  button.pack()

  #GPT taught me the below line
  #Waits for the window to be closed so it can return what was inputed from the keyboard
  input_line.wait_window()

  #Returns what the user entered
  return ui

def process_code(text):
  '''Gets the code and processes it'''
  #GPT taught me the below line
  #Gets the text the user entered
  user_input = text.get("1.0", END)
  
  #Creates 100 memory spots (0-99)
  memory = save()

  #Splits the input into a list to read
  input_lyst = user_input.split('\n')
  #The last value is empty and it takes it out
  input_lyst.pop()

  #Used to point out which line has an error
  line_num = 0

  #Used to keep track of the last value for the accumulator
  accumulator = None

  for items in input_lyst:

    #Increments line number for error handling
    line_num += 1

    #Passes every command into input_validation to ensure the commands are correct
    input_validation(items, line_num)
    command = items[0:2]
    location = int(items[2:])
    
    if command == '10':
      #READ command
      word = read_word()

      #Ensures that the input was an int
      if isinstance(word, int):
        #Stores the input from the keyboard at the specified location in memory 
        memory[location] = word
      else:
        #Input was not an int, prints out error message and exits
        print(f'Error on line{line_num}')
        print('Input was not an int')
        exit()

    elif command == '11':
      write = Write()
    elif command == '20':
      #LOADs a value from memory into the accumulator
      accumulator = memory[location]

    elif command == '21':
      #STOREs a value from the accumulator into memory
      memory[location] = accumulator

    elif command == '30':
      #ADD command

      #Checks if there is a value loaded in the accumulator and if
      #that location in memory has a value to add it
      if accumulator != None and isinstance(memory[location], int):
        accumulator += memory[location]

      else:
        print(f'Error on line: {line_num}')
        print('Not enough values have been entered to perform addition')
        exit()

    elif command == '31':
      #SUBTRACT command

      #Checks if there is a value loaded in the accumulator and if
      #that location in memory has a value as well
      if accumulator != None and isinstance(memory[location], int):
        accumulator -= memory[location]

      else:
        print(f'Error on line: {line_num}')
        print('Not enough values have been entered to perform subtraction')
        exit()
    elif command == '32':
      #ADD command

      #Checks if there is a value loaded in the accumulator and if
      #that location in memory has a value to multiply it
      if accumulator != None and isinstance(memory[location], int):
        accumulator *= memory[location]

      else:
        print(f'Error on line: {line_num}')
        print('Not enough values have been entered to perform Multiplication')
        exit()
    elif command == '33':
      #ADD command

      #Checks if there is a value loaded in the accumulator and if
      #that location in memory has a value to divide it
      if accumulator != None and isinstance(memory[location], int):
        accumulator /= memory[location]

      else:
        print(f'Error on line: {line_num}')
        print('Not enough values have been entered to perform addition')
        exit()
    elif command == '40':
      pass
    elif command == '41':
      pass
    elif command == '42':
      pass
    elif command == '43':
      pass

def display_window():
  '''Creates the window, text box, and submit button. Passes text to get_code when button is clicked'''
  command_line = Tk()
  
  #Creates Textbox for command line
  text = Text(command_line)
  text.configure(bg='black', fg='green')
  text.pack()


  #Creates button and passes text to process_code when hit for command line
  button = Button(command_line, command=lambda: process_code(text), text="RUN")
  button.pack()
  
  command_line.mainloop()

def main():
  display_window()

if __name__=='__main__':
  main()

