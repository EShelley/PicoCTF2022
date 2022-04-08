# **Challenge:** rail-fence


### **Category:** [Cryptography](../)
### **Point Value:** 100
### **Author:** WILL HONG
<br>

## **Description:**
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher)[^1]. Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? Download the message here(https://artifacts.picoctf.net/c/277/message.txt)[^1].[local](./message.txt) Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.

# **Write-Up:**
Found this python script to encode and decode rail fence 
[https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/](https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/)

I changed the driver code in the program to decode our flag:
```python
# Driver code
if __name__ == "__main__":
	
	# Now decryption of the
	# same cipher-text
	print(decryptRailFence("Ta _7N6DDEhlg:W3D_H3C31N__883ef sHR053F38N43D1B i33___ND", 4))
```
running it with our message.txt we get:

```bash
└─$ python3 ./railfenceCipher.py 
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D81DB8E3
```
Putting it in picoCTF{} format:
```
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D81DB8E3}
```
# **FLAG:** 
```
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D81DB8E3}
```
[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.