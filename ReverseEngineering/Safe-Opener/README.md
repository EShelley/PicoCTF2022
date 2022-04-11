# **Challenge:** Safe Opener


### **Category:** [Reverse Engineering](../)
### **Point Value:** 100
### **Author:** Mubarak Mikail
<br>

## **Description:**
Can you open this safe?<br> I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java)[^1] [local](./SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: picoCTF{password}

# **Write-Up:**
Looking at the source code we have this line that appears to have an encoded version of hte password:
```java
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
```        
and given we use a base64 encoder to encode the pw before checking it against this string:
```java
Base64.Encoder encoder = Base64.getEncoder();
...
encodedkey = encoder.encodeToString(key.getBytes());
```
... we should be able to just base64 decode that string to get our password:
```bash
└─$ echo cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz | base64 -d
pl3as3_l3t_m3_1nt0_th3_saf3  
```
Now lets wrap it in the picoCTF format:
```
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```
# **FLAG:** 
```
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.