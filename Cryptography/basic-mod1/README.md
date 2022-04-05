# **Challenge:** basic mod 1


### **Category:** [Cryptography](../)
### **Point Value:** 100
### **Author:** Will Hong
<br>

## **Description:**
We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message [here](https://artifacts.picoctf.net/c/398/message.txt).[^1] [local](./message.txt) Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

# **Write-Up:**
Let's start by getting our message.txt file:
```bash
wget https://artifacts.picoctf.net/c/398/message.txt
```
Opening the file we can see a string of numbers:
```
128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137 
```
Looking back at the challenge description, we are given some instructions on how to possibly decode this message:
> Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore


So lets create a python script to do that for us: [solve.py](./solve.py)
```python

orig_str = "128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137"
alphabet_map = []
split_message = orig_str.split()



def buildAlphabetMap():
  # first add the letters
  for x in range(65,91):
    alphabet_map.append(chr(x))
  # now the numbers
  for x in range(48,58):
    alphabet_map.append(chr(x))
  # finally the underscore character
  alphabet_map.append('_')
  

buildAlphabetMap()
#print(split_message)
flag = 'picoCTF{'
for x in split_message:
  flag += alphabet_map[int(x)%37]

flag+="}"  
print(flag)
```  
What this python script does is first build a list that contains the letters a-z, numbers 0-9 and the underscore '_', per the challenge description.  It then uses that list to map the input values to the character and finally outputs our flag value.

```bash
└─$ python3 solve.py
picoCTF{R0UND_N_R0UND_CE58A3A0}
```  


# **FLAG:**  
picoCTF{R0UND_N_R0UND_CE58A3A0}
#
[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.