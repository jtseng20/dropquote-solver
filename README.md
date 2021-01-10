# dropquote-solver

Made for MIT Mystery Hunt 2021. Uses frequency analysis on quadrigrams alongside the SOWPODS dictionary as an objective function, and simulated annealing to traverse the search space.

## Usage
The size of the grid may be changed with global variables. Two strings are taken in to represent a dropquote puzzle: one string, with one character per square, read column by column, where a ```1``` represents an entry and a ```2``` represents a space (black square), and another string, which contains all the dropping letters, read one column at a time. Note: this tool will probably never completely solve the puzzle, but will get you close quite fast.
