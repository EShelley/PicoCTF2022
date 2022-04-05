# **Challenge:** credstuff


### **Category:** Cryptography
### **Point Value:** 100
### **Author:** WILL HONG / LT 'SYREAL' JONES
<br>

## **Description:**
We found a leak of a blackmarket website's login credentials. Can you find the password of the user 'cultiris' and successfully decrypt it? Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar)[^1]. [local](./leak.tar) The first user in [usernames.txt](./leak/usernames.txt) corresponds to the first password in [passwords.txt](./leak/passwords.txt). The second user corresponds to the second password, and so on.

# **Write-Up:**
Let's start by getting the leak and extracting it:
```bash
wget https://artifacts.picoctf.net/c/534/leak.tar
tar -xf leak.tar
```  
Now we have a new folder in our working directory, with two files in it.
```bash
leak/passwords.txt
leak/usernames.txt
```

Opening them up we see single entries per line in both, with the passwords.txt looking like hashes.

usernames.txt
```text
engineerrissoles
icebunt
fruitfultry
celebritypentathlon
galoshesopinion
favorboeing
...
```
passwords.txt
```text
CMPTmLrgfYCexGzJu6TbdGwZa
GK73YKE2XD2TEnvJeHRBdfpt2
UukmEk5NCPGUSfs5tGWPK26gG
kaL36YJtvZMdbTdLuQRx84t85
K9gzHFpwF2azPayAUSrcL8fJ9
rYrtRbkHvJzPmDwzD6gSDbAE3
...
```

Knowing this I created a [solve.py](./solve.py) script to iterate through the files and search for our username:password hash combo.
```python

usernameFile = './leak/usernames.txt'
passwordFile = './leak/passwords.txt'

userToFind = 'cultiris'

# open the files
un = open(usernameFile, 'r')
pw = open(passwordFile, 'r')

unList = un.readlines()
pwList = pw.readlines()

for x in range(len(unList)):
  if(userToFind in unList[x]):
    print(unList[x] + ' : ' + pwList[x])



un.close()
pw.close()
```
Running the script we get this Output:
```bash
└─$ python3 ./solve.py
cultiris
 : cvpbPGS{P7e1S_54I35_71Z3}
 ```

 Now that doesnt looks like a password hash, and appeared to be in the format of our picoCTF{} flag.  Because of previous challenges I've done I know that 'cvpbPGS' is 'picoCTF' put throught a ROT13 cypher.  So using [rot13.com](rot13.com), I plugged in the cyphered flag and got this result:  
 ```
 picoCTF{C7r1F_54V35_71M3}
 ```
# **FLAG:** 
picoCTF{C7r1F_54V35_71M3}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.