import numpy as np
from itertools import combinations
from itertools import permutations

# DEFINE

def check_borders(board, row, col):
    if row == 0:
        is_up_match = True
    else:
        # place: low <--> up 
        is_up_match = board[row, col, 0] + board[row -1, col, 2] == 9 
    if col == 0:
        is_left_match = True
    else:
        # place: right <--> left
        is_left_match = board[row, col, 3] + board[row, col -1, 1] == 9 

    is_match = is_up_match and is_left_match
    return is_match

# GLOBALS

# Card specifications, 4 border numbers, clockwise
# each number is a different border

c1 = [1, 7, 2, 3]
c2 = [8, 3, 7, 5]
c3 = [1, 6, 7, 4]
c4 = [1, 3, 7, 5]
c5 = [8, 5, 7, 3]
c6 = [1, 8, 6, 5]
c7 = [3, 4, 7, 5]
c8 = [1, 4, 2, 6]
c9 = [8, 3, 4, 2]

card_arr = np.array([c1, c2, c3, c4, c5, c6, c7, c8, c9])

mapsize = (3,3)
n_places = mapsize[0] * mapsize[1]
trialcount = 0
n_solutions = 0

# dictionary

fish_dict = {1 : "head", 
    2 : "double head", 
    3 : "triple head",
    4 : "head tail head",
    5 : "tail head tail",
    6 : "triple tail",
    7 : "double tail",
    8 : "tail"
    }
# matching borders sum up to 9.

### PROCESS ###

card_images = np.hstack((card_arr, card_arr))
# slice card images from 0:4, 1:5, 2:6, 3:7 for different rotations 
empty_board = np.zeros((3,3,4))
board = empty_board.copy()


for orientation_first_tile in range(0,4):
    if orientation_first_tile == 0:
        pass
    else:
        print("Turning the first card clockwise")
        turned_card_arr = np.hstack((card_arr[:, orientation_first_tile:], 
            card_arr[:, :orientation_first_tile]))
        card_images = np.hstack((turned_card_arr, turned_card_arr))

    for permutation in permutations(card_images, n_places):
        # iterate over every place on the board
        for i in range(0,n_places):
            row = int(i / mapsize[1])
            col = i % mapsize[1]
            #print(row, col)
            #print(i)
            # iterate over orientations
            for j in range(0,4):
                board[row, col, :] = permutation[i][j:j+4]
                trialcount += 1
                if i == 0:
                    is_match = True
                    break
                else:
                    #check whether borders match
                    is_match = check_borders(board, row, col)
                    if is_match == True:
                        #print("Tile number", i+1, "matched in row/column", row, col)
                        break
            if is_match == False:
                # break board placement
                break
        # the last tile was a match! combination is valid!
        if is_match == True:
            print("combination has been found:")
            print("board state")
            print(board)
            n_solutions += 1
            continue

# OUTPUT

#print(fish_dict)
#print(card_arr)
#print(card_arr.shape)

#print("card images: \n", card_images, card_images.shape)

print("You tried this many combinations:", trialcount)
print("There are", n_solutions, "solutions to this puzzle!")
print("(check for rotationally equivalent ones)")
print("Well done, now make your own version of the puzzle.")
