# **Challenge:** patchme.py


### **Category:** [Reverse Engineering](../)
### **Point Value:** 100
### **Author:** LT 'syreal' Jones
<br>

## **Description:**
Can you get the flag?<br> Run this Python [program](https://artifacts.picoctf.net/c/391/patchme.flag.py)[^1] [local](./patchme.flag.py) in the same directory as this encrypted [flag](https://artifacts.picoctf.net/c/391/flag.txt.enc)[^1].[local](./flag.txt.enc)

# **Write-Up:**
After getting the two files we run the program and are prompted for a password:
```bash
└─$ python3 ./patchme.flag.py                                                                                                                            1 ⚙
Please enter correct password for flag: 
That password is incorrect
```

lets examine the code

We find the password in a plain text form in this conditional:
```python
if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000")
```                   
Compressing it down we get:

ak98-=90adfjhgj321sleuth9000 

Lets Try it!

```bash
└─$ python3 ./patchme.flag.py                                                                                                                            1 ⚙
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_68aa6913}
```  
# **FLAG:** 
picoCTF{p47ch1ng_l1f3_h4ck_68aa6913}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.