import os
import pickle
import random
import sys
import time


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# check if selection is the same as any element of actual, return user input (may ask for re-input if invalid)
def valid_input(selection, actual):
    valid = False
    for i in actual:
        if selection == i:
            valid = True
    while not valid:
        selection = input('Invalid input. Try again: ')
        for i in actual:
            if selection == i:
                valid = True
    return selection

# given path to file, return array containing each line of file
def list_from_file(file_path):
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line.strip())
    f.close()
    return lines

# print something slowly, as if a human was typing it
def print_slowly(str, typing_speed):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
