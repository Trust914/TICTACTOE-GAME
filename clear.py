from os import system, name


def clear_terminal():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
