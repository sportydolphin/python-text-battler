import os
import pickle


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# check if selection is the same as any element of actual, return user input (may ask for re-input if invalid)
def valid_input(selection, actual):
    valid = False
    for i in actual:
        if selection == i:
            valid = True
    while not valid:
        selection = input("Invalid input. Try again: ")
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


# input poop, output 112 111 111 112
def get_ASCII(inputstring):
    output = ""
    for i in range(len(inputstring)):
        output += str(ord(inputstring[i : i + 1])) + " "
    return output


# input poop, output 112 111 111 112.txt
def get_file_name(inputstring):
    return get_ASCII(inputstring)
