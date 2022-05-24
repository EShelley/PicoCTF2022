# **Challenge:** transposition-trial


### **Category:** Cryptography
### **Point Value:** 100
### **Author:** Will Hong
<br>

## **Description:**
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message [here](https://artifacts.picoctf.net/c/461/message.txt)[^1] [local](./message.txt).
# **Write-Up:**
Created [solve.py](./solve.py) to decryp the ciphered text:

```python
# heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B
# 
#
# encryped via tranposition cipher, in 3 letter blocks
# so the first block is: heT
# should be The
# To do that we take each block of three and move the last to beginning

encflag = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B"
outFlag = ''
for x in range(0,len(encflag),3):
  t = encflag[x:x+3]
  o = t[-1] +t[:2]
  outFlag += o

print(outFlag)
```
Running the script we get our flag:
```bash
└─$ python3 ./solve.py
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_AE131DBD}
```
# **FLAG:** 
```
picoCTF{7R4N5P051N6_15_3XP3N51V3_AE131DBD}
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.