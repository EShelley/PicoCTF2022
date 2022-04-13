# **Challenge:** substitution1


### **Category:** [Cryptography](../)
### **Point Value:** 100
### **Author:** WILL HONG
<br>

## **Description:**
A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. Download the message [here](https://artifacts.picoctf.net/c/419/message.txt).[^1] [local](./message.txt)

# **Write-Up:**
Looking at [message.txt](./message.txt) we can see that we're not given a key to work with. So we will need to build our own. To accomplish this we can to try and make some assumptions based on the cyphered text, run the decryption, and see if our assumptions lead to readable text.  If so we can then continue the process until we have the full key and deciphered text.<br><br> I can see a few substitutions based on known decrypted text ie.
```
qxc euzi ly: plgrGQE{EJ3SF3OGB_4774GN5_4J3_G001_C5M0GGTM}
```
the end part looks like a picoCTF{} flag format so
```
p = p
l = i
g = c (lowercase = lowercase)
r = o
G = C (Uppercase = Uppercase)
Q = T
E = F
```
Then along with the assumption:
```
qxc = the
euzi = flag
ly = is
```
So we can start builing out our sustitution alphabet using these vaules using '?' as our unknowns and placing our know/assumed values in the same place as the deciphered alphabet:
```python
subKey =  "z?g?ceixl??u??rp??yq??????"
alphabet ="abcdefghijklmnopqrstuvwxyz"
```

Using this in a new solve.py:
```python
subKey =  "z?g?ceixl??u??rp??yq??????"
alphabet ="abcdefghijklmnopqrstuvwxyz"

txt="GQEy (yxrjq erj gzpqfjc qxc euzi) zjc z qbpc re grwpfqcj ycgfjlqb grwpcqlqlro. Groqcyqzoqy zjc pjcycoqct vlqx z ycq re gxzuucoicy vxlgx qcyq qxclj gjczqlalqb, qcgxolgzu (zot irriuloi) ynluuy, zot pjrmucw-yrualoi zmlulqb. Gxzuucoicy fyfzuub gracj z ofwmcj re gzqcirjlcy, zot vxco yruact, czgx blcuty z yqjloi (gzuuct z euzi) vxlgx ly yfmwlqqct qr zo rouloc ygrjloi ycjalgc. GQEy zjc z ijczq vzb qr uczjo z vltc zjjzb re grwpfqcj ycgfjlqb ynluuy lo z yzec, ucizu coaljrowcoq, zot zjc xryqct zot puzbct mb wzob ycgfjlqb ijrfpy zjrfot qxc vrjut erj efo zot pjzgqlgc. Erj qxly pjrmucw, qxc euzi ly: plgrGQE{EJ3SF3OGB_4774GN5_4J3_G001_C5M0GGTM}".lower()

outText = ''
for x in txt:
 if(x in subKey):
  outText += alphabet[subKey.index(x)]
 else:
  outText += x
  
print(outText)
```
we get this output:
```bash
python3 ./solve.py                                                                                                                                   2 ⚙
ctfs (shojt foj captfje the flag) aje a tbpe of cowpftej secfjitb cowpetitioo. cootestaots aje pjeseotet vith a set of challeoges vhich test theij cjeatiaitb, techoical (aot googliog) snills, aot pjomlew-solaiog amilitb. challeoges fsfallb coaej a ofwmej of categojies, aot vheo solaet, each bielts a stjiog (callet a flag) vhich is sfmwittet to ao oolioe scojiog sejaice. ctfs aje a gjeat vab to leajo a vite ajjab of cowpftej secfjitb snills io a safe, legal eoaijooweot, aot aje hostet aot plabet mb waob secfjitb gjofps ajofot the vojlt foj ffo aot pjactice. foj this pjomlew, the flag is: picoctf{fj3sf3ocb_4774cn5_4j3_c001_e5m0cctm}
```

So we can now make the assumption that "(shojt foj captfje the flag)": should be "(short for capture the flag)"

meaing we now know that:
```
j = r
f = u
```
lets put those in our matrix and run it again:
```bash
└─$ python3 ./solve.py
ctfs (short for capture the flag) are a tbpe of cowputer securitb cowpetitioo. cootestaots are preseotet vith a set of challeoges vhich test their creatiaitb, techoical (aot googliog) snills, aot promlew-solaiog amilitb. challeoges usuallb coaer a ouwmer of categories, aot vheo solaet, each bielts a striog (callet a flag) vhich is sumwittet to ao oolioe scoriog seraice. ctfs are a great vab to learo a vite arrab of cowputer securitb snills io a safe, legal eoairooweot, aot are hostet aot plabet mb waob securitb groups arouot the vorlt for fuo aot practice. for this promlew, the flag is: picoctf{fr3su3ocb_4774cn5_4r3_c001_e5m0cctm}
```
Taking this part 'tbpe of cowputer securitb cowpetitioo' we can infer that:
```
b=y
w=m
o=n
```

And again: 
```
python3 ./solve.py
ctfs (short for capture the flag) are a type of computer security competition. contestants are presentet vith a set of challenges vhich test their creatiaity, technical (ant googling) snills, ant promlem-solaing amility. challenges usually coaer a nummer of categories, ant vhen solaet, each yielts a string (callet a flag) vhich is summittet to an online scoring seraice. ctfs are a great vay to learn a vite array of computer security snills in a safe, legal enaironment, ant are hostet ant playet my many security groups arount the vorlt for fun ant practice. for this promlem, the flag is: picoctf{fr3su3ncy_4774cn5_4r3_c001_e5m0cctm}
```
'presentet vith' should be 'presented with'
```
t = d
v = w
```
'creatiaity, technical (ant googling) snills' should be 'creativity, technical (and googling)'
```
a = v
t = d
n = k
```
and another round:
```bash
ctfs (short for capture the flag) are a type of computer security competition. contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and promlem-solving amility. challenges usually cover a nummer of categories, and when solved, each yields a string (called a flag) which is summitted to an online scoring service. ctfs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played my many security groups around the world for fun and practice. for this promlem, the flag is: picoctf{fr3su3ncy_4774ck5_4r3_c001_e5m0ccdm}
```
'nd promlem-solving amility' = 'nd problem-solving ability'
```
m = b
```
Now we're down to 4 letters remaining:

subKey =  "zmgtceixl?nuworp?jyqfav?b?"

'picoctf{fr3su3ncy' = 'picoctf{fr3qu3ncy' or frequency in 1447speak
```
s = q
```
Now our substitution key is:
```python
subKey =  "zmgtceixl?nuworpsjyqfav?b?"
```
Let's run it again:
```bash
└─$ python3 ./solve.py
ctfs (short for capture the flag) are a type of computer security competition. contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. ctfs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. for this problem, the flag is: picoctf{fr3qu3ncy_4774ck5_4r3_c001_e5b0ccdb}
```

That left us with 3 unknowns but it appears we have enough of the subsitiution to get the flag:
```
picoctf{fr3qu3ncy_4774ck5_4r3_c001_e5b0ccdb}
```
Submitted and we are correct!

Note: Hint 1 says to use a frequency attack(didnt use this directly - did it manually): In the future I want to implement a frequency attack solution to improve my skill base.

https://stackoverflow.com/questions/40985203/counting-letter-frequency-in-a-string-python
# **FLAG:** 
```
picoctf{fr3qu3ncy_4774ck5_4r3_c001_e5b0ccdb}
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.