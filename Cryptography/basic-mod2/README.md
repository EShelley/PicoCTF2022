# **Challenge:** basic-mod2


### **Category:** Cryptography
### **Point Value:** 100
### **Author:** Will Hong
<br>

## **Description:**
A new modular challenge! Download the message [here](https://artifacts.picoctf.net/c/504/message.txt).[^1] [local](./message.txt) Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

# **Write-Up:**
Let's start by getting our message.txt file:
```bash
wget https://artifacts.picoctf.net/c/504/message.txt
```
Opening the file we can see a string of numbers:
```
186 249 356 395 303 337 190 393 146 174 446 127 385 400 420 226 76 294 144 90 291 445 137 
```
Looking back at the challenge description, we are given some instructions on how to possibly decode this message  just like in [basic-mod1](../basic-mod1/):
> Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.   


Now before we continue on lets figure out how to find the modular inverse of mod 41.  After some google search I found [this](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python/9758173#9758173) page on StackOverflow that details how to do this in python.
```python
pow(int(x),-1,41)
```
Which has been tailored to our case. The variable 'x' being the returned vaule from our split message. 
So lets user our python script from [basic-mod1](../basic-mod1/) and modify it to decode this message: [solve.py](./solve.py)

```python

orig_str = "186 249 356 395 303 337 190 393 146 174 446 127 385 400 420 226 76 294 144 90 291 445 137"
alphabet_map = []
split_message = orig_str.split()



def buildAlphabetMap():
  # since our mapping starts at 1 lets add a dummy to the beginning
  alphabet_map.append('=') # using = as its not a character in our map to detect errors
  # first add the letters
  for x in range(65,91):
    alphabet_map.append(chr(x))
  
  for x in range(48,58):
    alphabet_map.append(chr(x))
  
  alphabet_map.append('_')

buildAlphabetMap()

#print(alphabet_map)
#print(split_message)
flag = 'picoCTF{'
for x in split_message:
  a = pow(int(x),-1,41)
  flag += alphabet_map[a]
flag += '}'
print(flag)
```
Now just like in [basic-mod1](../basic-mod1/), this creates our alphabet map, and performs the calculations to get our flag.
```bash
└─$ python3 ./solve.py    
picoCTF{1NV3R53LY_H4RD_B7FB947C}
```
# **FLAG:** 
picoCTF{1NV3R53LY_H4RD_B7FB947C}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.