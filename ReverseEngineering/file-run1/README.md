# **Challenge:** file-run1


### **Category:** Reverse Engineering
### **Point Value:** 100
### **Author:** Will Hong
<br>

## **Description:**
A program has been provided to you, what happens if you try to run it on the command line? Download the program [here](https://artifacts.picoctf.net/c/313/run).[^1]  

# **Write-Up:**

Downloaded with wget, added execute bit, and ran the program:
```bash
└─$ wget https://artifacts.picoctf.net/c/313/run
└─$ chmod +x ./run
└─$ ./run
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_2a4dec6a}    
```
And as you  can see it the 'run' program simply echos the flag to the console.
# **FLAG:** 
picoCTF{U51N6_Y0Ur_F1r57_F113_2a4dec6a}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.