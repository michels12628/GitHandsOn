#!/usr/bin/python3
# Simple TicTacToe game in Python - EAO
import random
import sys

#define board 
board=[]


# Corners, Center and Others, respectively
moves=((),(),())
# Winner combinations
winners=()
# Table
tab=range(1,10)

def print_board():
	#write the function logic to display the board
        print(char,end=end)
        
def select_char():
    return chars

def can_move(brd, player, move):
    return False

def can_win(brd, player, move):
    return win

def make_move(brd, player, move, undo=False):
    return (False, False)

# AI goes here
def computer_move():
    # If I can win, others don't matter.
        # If player can win, block him.
        # Otherwise, try to take one of desired places.
    return make_move(board, computer, move)

def space_exist():
    return board.count('X') + board.count('O') != 9

player, computer = select_char()

print('Player is [%s] and computer is [%s]' % (player, computer))
result='%%% Deuce ! %%%'

while space_exist():
        break;

print_board()
print(result)
