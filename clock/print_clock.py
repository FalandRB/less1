import time
import os

# Printing symbols in dependendency of symdol size. In our case 7*5


def print_clock(time):
    for row in range(0, 5):
        print(time[0][row] + time[1][row] + ' ' + time[2][row] + ' ' + time[3][row] +
              time[4][row] + ' ' + time[5][row] + ' ' + time[6][row] + time[7][row])

# Simple clear sreen


def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
