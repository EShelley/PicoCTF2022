# **Challenge:** substitution0


### **Category:** [Cryptography](../)
### **Point Value:** 100
### **Author:** WILL HONG
<br>

## **Description:**
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?<br> Download the message [here](https://artifacts.picoctf.net/c/384/message.txt)[^1].[local](./message.txt)

# **Write-Up:**
using this info I wrote [solve.py](./solve.py):
```python
subKey = "IADNMLPFYEJSWBZVXUHKGROCQT".lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

bodyTxt = "Fmumgvzb Smpuibn iuzhm, oykf i puirm ibn hkikmsq iyu, ibn auzgpfk wm kfm ammksm\
luzw i psihh dihm yb ofydf yk oih mbdszhmn. Yk oih i amigkylgs hdiuiaimgh, ibn, ik\
kfik kywm, gbjbzob kz bikguisyhkh—zl dzguhm i pumik vuytm yb i hdymbkylyd vzybk\
zl rymo. Kfmum omum koz uzgbn asidj hvzkh bmiu zbm mckumwykq zl kfm aidj, ibn i\
szbp zbm bmiu kfm zkfmu. Kfm hdismh omum mcdmmnybpsq fiun ibn pszhhq, oykf iss kfm\
ivvmiuibdm zl agubyhfmn pzsn. Kfm omypfk zl kfm ybhmdk oih rmuq umwiujiasm, ibn,\
kijybp iss kfybph ybkz dzbhynmuikyzb, Y dzgsn fiunsq asiwm Egvykmu lzu fyh zvybyzb\
umhvmdkybp yk.".lower()

flagTxt = "Kfm lsip yh: vydzDKL{5GA5717G710B_3R0SG710B_A1N36772}".lower()

print("Sub key: " + subKey)
print("Alphabet: " + alphabet)
print("Body Text(cyphered):\n" + bodyTxt +'\n')
print("Flag Text(cyphered): " + flagTxt +'\n')

bodyOutText = ''
flagOutText = ''

for y in bodyTxt:
  if(y in subKey):
    bodyOutText += alphabet[subKey.index(y)]
  else:
    bodyOutText += y

print("Body Text(Uncyphered):\n" + bodyOutText+'\n')


for x in flagTxt:
  if(x in subKey):
    flagOutText += alphabet[subKey.index(x)]
  else:
    flagOutText += x
    
print("Decrypted Flag: " + flagOutText)
```
The inputs are the provided key and cypher text. Then the program performs the substitution cipher on the text:
```
└─$ python3 ./solve.py
Sub key: iadnmlpfyejswbzvxuhkgrocqt
Alphabet: abcdefghijklmnopqrstuvwxyz
Body Text(cyphered):
fmumgvzb smpuibn iuzhm, oykf i puirm ibn hkikmsq iyu, ibn auzgpfk wm kfm ammksmluzw i psihh dihm yb ofydf yk oih mbdszhmn. yk oih i amigkylgs hdiuiaimgh, ibn, ikkfik kywm, gbjbzob kz bikguisyhkh—zl dzguhm i pumik vuytm yb i hdymbkylyd vzybkzl rymo. kfmum omum koz uzgbn asidj hvzkh bmiu zbm mckumwykq zl kfm aidj, ibn iszbp zbm bmiu kfm zkfmu. kfm hdismh omum mcdmmnybpsq fiun ibn pszhhq, oykf iss kfmivvmiuibdm zl agubyhfmn pzsn. kfm omypfk zl kfm ybhmdk oih rmuq umwiujiasm, ibn,kijybp iss kfybph ybkz dzbhynmuikyzb, y dzgsn fiunsq asiwm egvykmu lzu fyh zvybyzbumhvmdkybp yk.

Flag Text(cyphered): kfm lsip yh: vydzdkl{5ga5717g710b_3r0sg710b_a1n36772}

Body Text(Uncyphered):
hereupon legrand arose, with a grave and stately air, and brought me the beetlefrom a glass case in which it was enclosed. it was a beautiful scarabaeus, and, atthat time, unknown to naturalists—of course a great prize in a scientific pointof view. there were two round black spots near one extremity of the back, and along one near the other. the scales were exceedingly hard and glossy, with all theappearance of burnished gold. the weight of the insect was very remarkable, and,taking all things into consideration, i could hardly blame jupiter for his opinionrespecting it.

Decrypted Flag: the flag is: picoctf{5ub5717u710n_3v0lu710n_b1d36772}
```
Resulting in our flag:
picoctf{5ub5717u710n_3v0lu710n_b1d36772}
  
# **FLAG:** 
```
picoctf{5ub5717u710n_3v0lu710n_b1d36772}
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.