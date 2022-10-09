#! /bin/python3

# A python script to setup a new challenge writeup within my PicoCTF file structure
# Author: Eric Shelley

import os
import sys
from pathlib import Path

ctfCategory = ""
ctfChallenge = ""

# Template? How? base64? txt file? 

# Get user input? Either by argument or if none supplied ask user once program starts
numArgs = len(sys.argv) - 1

if(numArgs == 2): # user has entered arguments
    ctfCategory, ctfChallenge = sys.argv[1:] 
    print(ctfCategory)
    print(ctfChallenge)
    if(Path(sys.argv[1]).exists()):
        if(Path(sys.argv[1]).is_dir()):
            print("Category Already Exists")
        else:
            print("Thats a file mate! Try a different directory")

    else:
        print("Category es no bueno! and something went really wrong!")
        exit(-1)
        
elif numArgs == 0:
    # ask for user input
    print("Get user input")    
else:
    # user borked input - quit
    print("NEED INPUT!")


# check if Category directory exists, if not ask user wants to create a new category (y) create directory and continue (n) error out

# check if Challenge directory exists, if it does error and let the user know that Challenge Exists (could add ability to overwrite here)

# All checks have passed - if template exists continue, else error

# Open Template and copy its contents to a new project README.md in ./Category/Challenge folder
# Create placeholder flag and solve.py files
# Close Template
def CreateChallenge(Directory, Challenge):
    sys.exit(0)
# Show success!
