# **Challenge:** bloat.py


### **Category:** Reverse Engineering
### **Point Value:** 200
### **Author:**  LT 'syreal' Jones
<br>

## **Description:**
Can you get the flag? Run this Python program(https://artifacts.picoctf.net/c/433/bloat.flag.py)[^1] [local](./bloat.flag.py) in the same directory as this encrypted flag(https://artifacts.picoctf.net/c/433/flag.txt.enc)[^1] [local](./flag.txt.enc).


# **Write-Up:**
Looking at the source it looks like arg133() is what checks for our password:
I determined this as this function appears to be the only one doing a comparison.  
Plus:  
  arg444 is the file handle to the encrypted flag file.  
  arg432 is the input returned from the password prompt
  arg112() prints out this message "Welcome back... your flag, user:"
```python
def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
  else:
    print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
    sys.exit(0)
    return False
    
def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])
```  
 We could just bypass it by making it return true, effectively "de-bloating" the program: 
```python
def arg133(arg432):
  return True  
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
  else:
    print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
    sys.exit(0)
    return False
    
def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])
```
Running the program and just hitting enter for the password:
```bash
└─$ python3 ./bloat.flag.py
Please enter correct password for flag: 
Welcome back... your flag, user:
picoCTF{d30bfu5c4710n_f7w_1763a697}  
```
# **FLAG:** 
```
picoCTF{d30bfu5c4710n_f7w_1763a697}  
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.