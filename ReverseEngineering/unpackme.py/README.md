# **Challenge:** unpackme.py


### **Category:** Reveerse Engineering
### **Point Value:** 100
### **Author:** LT 'syreal' Jones
<br>

## **Description:**
Can you get the flag? Reverse engineer this Python [program](https://artifacts.picoctf.net/c/469/unpackme.flag.py) [^1] [local](./unpackme.flag.py).

# **Write-Up:**

Looking at the source it has a base64 string thats encoded using another string 'correctstaplecorrectstaplecorrec'
and at the end it uses exec to run the code contained in that string.   

Running the script we get:  
```
└─$ python3 ./unpackme.flag.py
What's the password? password
That password is incorrect.
```
I changed exec() to print()  

Before:
```python
plain = f.decrypt(payload)
exec(plain.decode())
```
After:
```python
plain = f.decrypt(payload)
print(plain.decode())
```  
to see if it would print the code to the console and it did; giving us:
```bash
└─$ python3 ./unpackme.flag.py

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_45a1a353}')
else:
  print('That password is incorrect.')
```
Looking at the code we can see that the correct password is "batteryhorse".  We can also see our flag there as well:

```
picoCTF{175_chr157m45_45a1a353}
```
We can also run the original python script to get the flag as well:

```bash
└─$ python3 ./unpackme.flag.py
What's the password? batteryhorse
picoCTF{175_chr157m45_45a1a353}
```

# **FLAG:** 
```
picoCTF{175_chr157m45_45a1a353}
```


[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.