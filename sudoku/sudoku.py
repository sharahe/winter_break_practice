def check_full_puzzle(puzzle):
    return True


def solve_puzzle(puzzle):
    return puzzle


if __name__ == '__main__':
    # now that you know more than just lists, you can change
    # this to any data structure you want
    puzzle = [[0, 9, 6, 0, 0, 8, 0, 7, 3],
              [7, 0, 3, 4, 0, 1, 0, 0, 6],
              [0, 5, 0, 0, 3, 0, 0, 0, 1],
              [0, 0, 8, 0, 0, 0, 1, 4, 5],
              [6, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 1, 9, 0, 0, 0, 3, 0, 0],
              [5, 0, 0, 0, 7, 0, 0, 1, 0],
              [4, 0, 0, 5, 0, 9, 2, 0, 7],
              [9, 6, 0, 1, 0, 0, 5, 3, 0]]

    if not check_full_puzzle(puzzle):
        print("the input puzzle is no good")

    solved_puzzle = solve_puzzle(puzzle)

    print("I solved it!")
    for row in solved_puzzle:
        print(row)
