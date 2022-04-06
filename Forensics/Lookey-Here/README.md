# **Challenge:** Lookey Here


### **Category:** [Forensics](../)
### **Point Value:** 100
### **Author:** LT 'SYREAL' JONES/ MUBARAK MIKAIL
<br>

## **Description:**
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data [here](https://artifacts.picoctf.net/c/299/anthem.flag.txt)[^1].[local]()

# **Write-Up:**
I went down the rabbit hole of different setgo techniques thinking it was something difficult -

without running a simple grep for the picoCTF prefix.... Sometimes its the easy things that get in our way >.>

```bash
└─$ cat flag anthem.flag.txt | grep picoCTF
picoCTF{gr3p_15_@w3s0m3_0abe82b2}      ANTHEM
      we think that the men of picoCTF{gr3p_15_@w3s0m3_0abe82b2}
```
# **FLAG:** 
picoCTF{gr3p_15_@w3s0m3_0abe82b2}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.