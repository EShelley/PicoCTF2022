#! /bin/bash

if ! [ -d "./$1"]; then
	echo "Setting up new CTF challenge Folder for: " $1
	echo "======================================================================"
	echo "Create Directory"
	mkdir $1
	echo "-Done-"
	echo "Create Dummy readme.md and flag files"
	cat ./readme_template.md >  $1/README.md
	sed -i 's/<CName>/'$1'/' $1/README.md
	touch $1/flag
	
	echo "Exiting"
else
	echo $1 " is already a directory - try again"
fi
