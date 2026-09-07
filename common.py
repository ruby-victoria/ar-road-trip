# common.py - common/repeatable functions to be used in the game
import os
import subprocess

def clear():
    """clears screen"""
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)
    return

def stay_continue():
    """asks user whether to stay in the location or continue road trip"""
    choice = ""
    while choice != "STAY" and choice != "CONTINUE":
        choice = input("would you like to STAY here and explore for a while or CONTINUE on the road trip?: ").upper()
        if choice != "STAY" and choice != "CONTINUE":
            print()
            print("please enter either 'STAY' or 'CONTINUE'")
            print()
    return choice

def help_text():
    """general help text for game"""

    clear()
    print(r"""
to play the game, just type the action u want to do :)

the map at the top of the screen shows where u are!
    - the routes are represented with lines: _ / \ |
    - the road trip locations are represented with: @
    - your current location is represented with: X

to show this help text again, type 'help' or 'h'

have fun!!""")
    print()
    return

def erase(characters, landmarks, maps):
    """replaces given characters in a map

    characters: a list of route characters to replace with whitespace
    landmarks: a list of landmark characters to replace with @
    map: a string representing the map"""

    for character in characters:
        maps = maps.replace(character," ")

    for landmark in landmarks:
        maps = maps.replace(landmark,"@")

    return maps