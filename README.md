# Sudoku-Solver
This is a sudoku solver implemented in python3 using pygame. The program allows you to both play a sudoku board, and also implements a backtracking algorithm to solve any given board.

## Instructions for use:
1. Download the source files
2. Run "runner.py". This should open up a pygame window

## In-game Instruction:
* To input a value into a cell, simply hover your cursor over the cell and type a number
* To clear the board, click the "Clear Board" button
* To execute the backtracking algorithm...
  1. Click the "Solve Board" button. This will call the backtracking algorithm and visually walk you through its execution. (Runs slower)
  2. Click the "Solve Quick" button. This will call the backtracking algorithm without any visual feedback and will update the board only once it has been solved. (Runs faster)
* To play on a different/custom board, simply edit the contents of "board.txt" with the board you wish to play on.
  * Input a '0' for empty cells and a value from 1-9 for non-empty cells
 

