"""Solve this Sudoku Puzzle!"""
import numpy as np


def solve_puzzle(puzzle: np.array):
    """Write your main function loop here"""
    # [loop over all rows and columns looking for the next space to fill]
    for row in [None]:
        for col in [None]:
            # [check if this is a square that needs to be filled]
            if True:
                # [Start trying out all of the potential numbers]:
                for number in [None]:
                    # [Assign the number to the correct puzzle square
                    puzzle[None, None] = None
                    if check_full_puzzle(None):
                        # That number works with the puzzle so far. Pass it off
                        # to the next level!
                        solution = solve_puzzle(puzzle.copy())

                        # If the solution is false, try the next number. If the solution is not
                        # False, you want to pass it up to the next level
                        if solution is None:
                            return None
    # One last check that the puzzle is legit (if there was no puzzle solution, the puzzle will be
    # full of bad things)
    if check_full_puzzle(puzzle):
        return puzzle
    else:
        return False


def check_number_ok(i, j, puzzle):
    """Check if this number if OK with the numbers around it"""
    my_number = puzzle[i, j]

    # [If the number is 0, its ok]

    # [Check that it is the only one of that number in its column]

    # [Check that it is the only one of that number in its column]

    # Now you need to check the specific 3x3 block that the number is in.
    # [figure out which super-row (0,1,2) or super-column (0,1,2) this number is in]
    row_block = None
    col_block = None

    # Now that you know this, figure out how to loop over the indexes of numbers that you have to
    # check against
    # [Check against the numbers in the super-block]

    # You have passed all tests!
    return True


def check_full_puzzle(puzzle):
    """This is a super brute force way of checking a puzzle's validity. We are just going to check
    That every single number is valid"""
    for i in range(9):
        for j in range(9):
            if not check_number_ok(i, j, puzzle):
                return False
    return True


if __name__ == '__main__':
    puzzle = np.array([[0, 9, 6, 0, 0, 8, 0, 7, 3],
                       [7, 0, 3, 4, 0, 1, 0, 0, 6],
                       [0, 5, 0, 0, 3, 0, 0, 0, 1],
                       [0, 0, 8, 0, 0, 0, 1, 4, 5],
                       [6, 0, 0, 0, 0, 0, 0, 0, 2],
                       [2, 1, 9, 0, 0, 0, 3, 0, 0],
                       [5, 0, 0, 0, 7, 0, 0, 1, 0],
                       [4, 0, 0, 5, 0, 9, 2, 0, 7],
                       [9, 6, 0, 1, 0, 0, 5, 3, 0]])

    if not check_full_puzzle(puzzle):
        print("the input puzzle is no good")

    solved_puzzle = solve_puzzle(puzzle)

    print("I solved it!")
    print(solved_puzzle)

# [
