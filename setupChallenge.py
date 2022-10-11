#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

ctfChallengeTypes = {
    'binaryexploitation': 'BinaryExploitation',
    'cryptography': 'Cryptography',
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
