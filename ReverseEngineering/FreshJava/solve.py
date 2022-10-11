# import the regex stuff
import re

# open the KeygenMe.Java file and read it in
with open('./KeygenMe.java') as f:
    lines = f.readlines()

# now we run out regex Magic and get all of the flag string/position pairs    
x = re.findall(r"[(](\d+)[)]( != )['](\S)[']",str(lines))

# I knew there had to be a way to sort that list and found [this](https://docs.python.org/3/library/functions.html#sorted) in the python docs
# Some more googling led to using an inline lambda function to define a custon key for sorted()
x = sorted(x, key=lambda pos: int(pos[0]))

outText = '' # string to hold the flag
for l in x:
 outText += l[2] # extract out the flag characters
print(outText) # display the flag to the console