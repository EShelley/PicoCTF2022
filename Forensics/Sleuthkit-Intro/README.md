# **Challenge:** Sleuthkit Intro


### **Category:** [Forensics](../)
### **Point Value:** 100
### **Author:** LT 'syreal' Jones
<br>

## **Description:**
Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

Download disk [image](https://artifacts.picoctf.net/c/114/disk.img.gz)[^1].[local](./disk.img.gz)<br>
Access checker program: nc saturn.picoctf.net 52279[^1]

# **Write-Up:**
First get the image file using wget:
```bash
└─$ wget https://artifacts.picoctf.net/c/114/disk.img.gz
```
Now gunzip the file:
```bash
└─$ gzip -dk disk.img.gz         
```
Then use 'mmls' to check the disk image:
```bash
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
Looking back to the description we see we need the length of the 'linux' partition which in this case is 202752.<br>
Using that we check our work by connecting to the remote service using 'netcat':
```bash
└─$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}  
```
Which as you can see is correct, and we get our flag!
```
picoCTF{mm15_f7w!}
```
# **FLAG:** 
```
picoCTF{mm15_f7w!}
```

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.