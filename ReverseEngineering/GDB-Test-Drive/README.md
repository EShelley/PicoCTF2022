# **Challenge:** GDB Test Drive


### **Category:** [Reverse Engineering](../)
### **Point Value:** 100
### **Author:** LT 'SYREAL' JONES
<br>

## **Description:**
Can you get the flag?<br> Download this [binary](https://artifacts.picoctf.net/c/120/gdbme)[^1].[local](./gdbme)<br> Here's the test drive instructions:
```bash
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```
# **Write-Up:**
Following the prompt's instructions and after installing GDB I ran the above commands:
```bash
$ chmod +x gdbme
$ gdb gdbme
(gdb) break *(main+99)
Breakpoint 1 at 0x132a
(gdb) run
Starting program: /home/hireth/Desktop/picoCTF/picoCTF2022/GDBtestdrive/gdbme

Breakpoint 1, 0x000055555555532a in main ()
(gdb) jump *(main+104)
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_3eab6731}
(gdb) ior 1 (process 130736) exited normally]
```
Looking at the output, we first set a breakpoint at (main+99) and run the program.  This causes it to stop at the point in memory 'main+99'  Then we issue the 'jump *(main+104)' command which moves us in memory to the location (main+104) and continues executing.  At which point we are presented with our flag.
```
picoCTF{d3bugg3r_dr1v3_3eab6731}
```
# **FLAG:** 
```
picoCTF{d3bugg3r_dr1v3_3eab6731}
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.