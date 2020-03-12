import numpy as np
import os
import sys


def win():
    global play_matrix
    save_summa = np.zeros((8,), dtype=int)
    for elem in range(3):
        save_summa[elem] = np.sum(play_matrix[elem])
        save_summa[elem+3] = np.sum(play_matrix[:,elem])
        save_summa[6] +=np.sum(play_matrix[elem,elem])
        save_summa[7] +=np.sum(play_matrix[elem,2 - elem])
    if 24 in save_summa or 9 in save_summa:
        print('WINNER')
        sys.exit()
    elif 0 not in play_matrix:
        print('TIE')
        sys.exit()


def sign(user,num):
    global play_matrix
    keys = {
        "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
        "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
        "C1": (2, 0), "C2": (2, 1), "C3": (2, 2),
    }
    try:
        user_sign = input('sign {}:'.format(user))
        rows = keys[user_sign][0]
        column = keys[user_sign][1]
        if play_matrix[rows][column] == 0:
            play_matrix[rows][column] = num
            os.system('clear')
        else:
            sign(user, num)
    except KeyError:
        sign(user,num)


def user_field():
    global play_matrix
    keys = {0: '.', 3: 'O',8: 'X',}
    user_matrix = np.array(play_matrix, dtype=str)
    for row in range (3):
        for column in range(3):
            if play_matrix[row][column] == 3:
                user_matrix[row][column] = keys[3]
            elif play_matrix[row][column] == 8:
                user_matrix[row][column] = keys[8]
            else:
                user_matrix[row][column] = keys[0]
    print("    1   2   3  ")
    print("  .............")
    print("A |", user_matrix[0][0], " ",user_matrix[0][1], " ", user_matrix[0][2], "|")
    print("               ")
    print("B |", user_matrix[1][0], " ", user_matrix[1][1], " ", user_matrix[1][2], "|")
    print("               ")
    print("C |", user_matrix[2][0], " ", user_matrix[2][1], " ", user_matrix[2][2], "|")
    print("  .............\n")

# ----------------------MAIN LOOP GAME-------------------------
play_matrix = np.zeros((3, 3), dtype=int)
user_field()
for i in range(9):
    if i%2 == 0:
        sign('X', 8)
        win()
        user_field()
    else:
        sign('O', 3)
        win()
        user_field()




