# CS 2450 Projects

License: MIT

## Getting Started

These instructions will get you through launching phase of this project.

### Launching Project

- Clone this repository

### Running Project

- Start Project by running ```python3 main.py```

### Testing
- Run the command ```python3 -m unittest discover tests```

### Instructions Help

- Be sure to include two integer location after each instruction (including HALT)

**
I/O operation:

READ = 10                       Read a word from the keyboard into a specific location in memory.

WRITE = 11                     Write a word from a specific location in memory to screen.

Load/store operations:

LOAD = 20                      Load a word from a specific location in memory into the accumulator.

STORE = 21                     Store a word from the accumulator into a specific location in memory.

Arithmetic operation:

Add = 30                         Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)

SUBTRACT = 31             Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)

DIVIDE = 32                    Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).

MULTIPLY = 33              multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operation:

BRANCH = 40                 Branch to a specific location in memory

BRANCHNEG = 41         Branch to a specific location in memory if the accumulator is negative.

BRANCHZERO = 42       Branch to a specific location in memory if the accumulator is zero.

HALT = 43                       Pause the program
**
