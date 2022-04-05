# **Challenge:** file-run2


### **Category:** Reverse Engineering
### **Point Value:** 100
### **Author:** Will Hong
<br>

## **Description:**
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program [here](https://artifacts.picoctf.net/c/356/run).[^1]  

# **Write-Up:**
Downloaded with wget, added execute bit, and ran the program:
```bash
└─$ wget https://artifacts.picoctf.net/c/356/run
└─$ chmod +x ./run
```
Tried a direct copy first then iterated through until i got the input right:
```
└─$ ./run "Hello!"?
dquote>                                                 
dquote> exit               
dquote> " 
Won't you say 'Hello!' to me first?
                                                                                                                                                             

└─$ ./run "Hello!"
dquote> "
Won't you say 'Hello!' to me first?
                                                                                                                                                             

└─$ ./run 'Hello!'
The flag is: picoCTF{F1r57_4rgum3n7_0097836e} 
```
# **FLAG:** 
picoCTF{U51N6_Y0Ur_F1r57_F113_2a4dec6a}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.