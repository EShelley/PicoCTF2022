#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

ctfChallengeTypes = {
    'binaryexploitation': 'BinaryExploitation',
    'cryptography': 'Cryptography',#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from os import chdir
import shutil

ctfChallengeTypes = {
    'binaryexploitation': 'BinaryExploitation',
    'cryptography': 'Cryptography',
    'forensics': 'Forensics',
    'reverseengineering': 'ReverseEngineering',
    'webexploitation': 'WebExploitation'}

class init_action(argparse.Action):
    def __init__(self, option_strings, dest, **kwargs):
        return super().__init__(option_strings, dest, nargs='?', default=argparse.SUPPRESS, **kwargs)

    def __call__(self, parser, namespace, values, option_string, **kwargs):
        # If a folder was passed with init - try to init that folder
        if(values):
            print(values)
            newDir = Path(values)
            if(not newDir.exists()):
                print("Creating new CTF Project: {}".format(values))
                newDir.mkdir()
                chdir(newDir)
                # print(Path().cwd())
                print("Copying Base Files")
                shutil.copy("../setupChallenge.py", "./setupChallenge.py")
                shutil.copy("../readme_template.md", "./reademe_template.md")

        # Ensure user is not trying to init the Base CTF Directory
        if(Path().cwd().parts[-1] == "CTF"):
            print("Invalid Directory - Please Initialize a sub-directory of CTF")
            sys.exit(-1)

        # Check to see if Directory has already been Initialized
        for DIR in ctfChallengeTypes.values():
            newFolder = Path(DIR)
            if(newFolder.exists()):
                print("Directory has already been Initialized")
                sys.exit(-1)

        print("Creating new Project Structure")
        for DIR in ctfChallengeTypes.values():
            newType = Path(DIR)
            newType.mkdir(parents=True, exist_ok=True)
            print("New Challenge Type: {}".format(DIR))

        parser.exit()

def main():
    # setup argument parser and process console args
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--init", action=init_action, help="Initialize new CTF Project Structure")
    parser.add_argument('ctfDirectory', type=str,
                        help='Challenge Type: BinaryExploitation, Cryptography, Forensics, ReverseEngineering, WebExploitation')
    parser.add_argument('ctfChallenge', type=str, help='Name of the CTF challenge')

    if not len(sys.argv[0:]) > 1:  # if program run with no arguments - print usage
        parser.print_help()
        parser.exit()

    args = parser.parse_args()  # Parse Arguments

    print(args.ctfDirectory)
    print(args.ctfChallenge)

    ctfD = str(args.ctfDirectory).lower()
    challenge = str(args.ctfChallenge)

    # lets check to see if the ctfDirectory is one of the correct Categories
    if ctfD not in ctfChallengeTypes.keys():
        print(str(args.ctfDirectory) + " is not a Challenge Category")
        sys.exit(-1)

    # use pathlib.Path to determine if a directory exists, and if not create the new challenge directory

    p = Path(ctfChallengeTypes[ctfD], challenge)
    template = Path("readme_template.md")
    if not p.exists():
        p.mkdir(parents=True)
        new_readme = Path(p, 'README.md')  # Create new readme
        flag = Path(p, 'flag')  # Create new flag file
        flag.write_text('')
        x = template.read_text()  # Read in template File
        x = x.replace('CName', challenge)  # Replace CName with Challenge Name
        x = x.replace('CatName', ctfChallengeTypes[ctfD])  # Replace CatName with Category Name
        new_readme.write_text(x)  # Write out the challenge to the new readme

    else:
        print()
        exit('Error: Challenge ' + ctfChallengeTypes[ctfD] + '/' + challenge + ' already exists')


# make sure its running as it self
if __name__ == '__main__':
    main()

    'forensics': 'Forensics',
    'reverseengineering': 'ReverseEngineering',
    'webexploitation': 'WebExploitation'}


def main():
    # setup argument parser and process console args
    parser = argparse.ArgumentParser()
    parser.add_argument('ctfDirectory', type=str,
                        help='Challenge Type: BinaryExploitation, Cryptography, Forensics, ReverseEngineering, WebExploitation')
    parser.add_argument('ctfChallenge', type=str, help='Name of the CTF challenge')

    if not len(sys.argv[1:]) == 2:  # if program run with no arguments - print usage
        parser.print_help()
        parser.exit()

    args = parser.parse_args()  # Parse Arguments

    print(args.ctfDirectory)
    print(args.ctfChallenge)

    ctfD = str(args.ctfDirectory).lower()
    challenge = str(args.ctfChallenge)

    # lets check to see if the ctfDirectory is one of the correct Categories
    if ctfD not in ctfChallengeTypes.keys():
        print(str(args.ctfDirectory) + " is not a Challenge Category")
        sys.exit(-1)

    # use pathlib.Path to determine if a directory exists, and if not create the new challenge directory

    p = Path(ctfChallengeTypes[ctfD], challenge)
    template = Path("readme_template.md")
    if not p.exists():
        p.mkdir(parents=True)
        new_readme = Path(p, 'README.md')  # Create new readme
        flag = Path(p, 'flag')  # Create new flag file
        flag.write_text('')
        x = template.read_text()  # Read in template File
        x = x.replace('CName', challenge)  # Replace CName with Challenge Name
        x = x.replace('CatName', ctfChallengeTypes[ctfD])  # Replace CatName with Category Name
        new_readme.write_text(x)  # Write out the challenge to the new readme

    else:
        print()
        exit('Error: Challenge ' + ctfChallengeTypes[ctfD] + '/' + challenge + ' already exists')


# make sure its running as it self
if __name__ == '__main__':
    main()
