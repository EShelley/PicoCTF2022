#! /bin/bash

if ! [ -d "./$1"]; then
	echo "Setting up new CTF challenge Folder for: " $1
	echo "======================================================================"
	echo "Create Directory"
	mkdir $1
	echo "-Done-"
	echo "Create Dummy readme.md and flag files"
	echo $1 " Challenge:" >  $1/readme.md
	touch $1/flag
	echo "Entering new Challenge Folder"
	cd ./$1
	echo "Exiting"
else
	echo $1 " is already a directory - try again"
fi
