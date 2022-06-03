#! /bin/bash

if   [ $# -eq 2 ]; then
if ! [ -d "./$1/$2"]; then
	echo "Setting up new CTF challenge Folder for: " $2
	echo "======================================================================"
	echo "Create Directory"
	mkdir ./$1/$2 -p
	echo "-Done-"
	echo "Create Dummy readme.md and flag files"
	cat ./readme_template.md >  ./$1/$2/README.md
	sed -i 's/CName/'$2'/' ./$1/$2/README.md
	sed -i 's/CatName/'$1'/' ./$1/$2/README.md
	touch ./$1/$2/flag
	
	echo "Exiting"
else
	echo $1/$2 " is already a directory - try again"
fi
else
	echo "./setupChallenge.sh <Challenge Name> <Category>"
fi