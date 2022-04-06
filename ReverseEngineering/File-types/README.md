# **Challenge:** File types


### **Category:** [Reverse Engineering](../)
### **Point Value:** 100
### **Author:** Geoffrey Njogu
<br>

## **Description:**
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from [here](https://artifacts.picoctf.net/c/328/Flag.pdf).[^1] [local](./Flag.pdf)

# **Write-Up:**
  
Let's start by obtaining the file using wget:
```bash
wget https://artifacts.picoctf.net/c/328/Flag.pdf
```
Now lets see what we get if we run the 'file' command on the pdf:
```bash
└─$ file Flag.pdf                                                                                                                                        1 ⚙
Flag.pdf: shell archive text
```
Let's 'cat' the file and see what we get:
catted out the file and found this at the beginning
```bash
└─$ cat ./Flag.pdf

#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.

===================
```
Following those instructions I removed everything in the file before '#!/bin/sh' which left us with:
```bash
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00046
# Made on 2022-03-15 06:50 UTC by <root@3104350fe95a>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
#   1092 -rw-r--r-- flag
#
MD5SUM=${MD5SUM-md5sum}
f=`${MD5SUM} --version | egrep '^md5sum .*(core|text)utils'`
test -n "${f}" && md5check=true || md5check=false
${md5check} || \
  echo 'Note: not verifying md5sums.  Consider installing GNU coreutils.'
if test "X$1" = "X-c"
then keep_file=''
else keep_file=true
fi
echo=echo
save_IFS="${IFS}"
IFS="${IFS}:"
gettext_dir=
locale_dir=
set_echo=false

for dir in $PATH
do
  if test -f $dir/gettext \
     && ($dir/gettext --version >/dev/null 2>&1)
  then
    case `$dir/gettext --version 2>&1 | sed 1q` in
      *GNU*) gettext_dir=$dir
      set_echo=true
      break ;;
    esac
  fi
done

if ${set_echo}
then
  set_echo=false
  for dir in $PATH
  do
    if test -f $dir/shar \
       && ($dir/shar --print-text-domain-dir >/dev/null 2>&1)
    then
      locale_dir=`$dir/shar --print-text-domain-dir`
      set_echo=true
      break
    fi
  done

  if ${set_echo}
  then
    TEXTDOMAINDIR=$locale_dir
    export TEXTDOMAINDIR
    TEXTDOMAIN=sharutils
    export TEXTDOMAIN
    echo="$gettext_dir/gettext -s"
  fi
fi
IFS="$save_IFS"
if (echo "testing\c"; echo 1,2,3) | grep c >/dev/null
then if (echo -n test; echo 1,2,3) | grep n >/dev/null
     then shar_n= shar_c='
'
     else shar_n=-n shar_c= ; fi
else shar_n= shar_c='\c' ; fi
f=shar-touch.$$
st1=200112312359.59
st2=123123592001.59
st2tr=123123592001.5 # old SysV 14-char limit
st3=1231235901

if   touch -am -t ${st1} ${f} >/dev/null 2>&1 && \
     test ! -f ${st1} && test -f ${f}; then
  shar_touch='touch -am -t $1$2$3$4$5$6.$7 "$8"'

elif touch -am ${st2} ${f} >/dev/null 2>&1 && \
     test ! -f ${st2} && test ! -f ${st2tr} && test -f ${f}; then
  shar_touch='touch -am $3$4$5$6$1$2.$7 "$8"'

elif touch -am ${st3} ${f} >/dev/null 2>&1 && \
     test ! -f ${st3} && test -f ${f}; then
  shar_touch='touch -am $3$4$5$6$2 "$8"'

else
  shar_touch=:
  echo
  ${echo} 'WARNING: not restoring timestamps.  Consider getting and
installing GNU '\''touch'\'', distributed in GNU coreutils...'
  echo
fi
rm -f ${st1} ${st2} ${st2tr} ${st3} ${f}
#
if test ! -d ${lock_dir} ; then :
else ${echo} "lock directory ${lock_dir} exists"
     exit 1
fi
if mkdir ${lock_dir}
then ${echo} "x - created lock directory ${lock_dir}."
else ${echo} "x - failed to create lock directory ${lock_dir}."
     exit 1
fi
# ============= flag ==============
if test -n "${keep_file}" && test -f 'flag'
then
${echo} "x - SKIPPING flag (file already exists)"

else
${echo} "x - extracting flag (text)"
  sed 's/^X//' << 'SHAR_EOF' | uudecode &&
begin 600 flag
M(3QA<F-H/@IF;&%G+R`@("`@("`@("`@,"`@("`@("`@("`@,"`@("`@,"`@
M("`@-C0T("`@("`Q,#(T("`@("`@8`K'<6D`,+RD@0`````!````,&))-P4`
M``#[`69L86<``$)::#DQ05DF4UEEWLZM```A____]MO3^_?;N]W_]_][[X8B
MQ;O>H?-?W[Y[_Z]X5]]S<;`!&Q@@-```9`'HC0`#0`T``'J```:-`:`-`]0>
MIH&@`>H'J-`/),:@]3RC-JAR:&@``#0`!Y3U`>D`TTTT-`&AHT'ZH&1Z@``#
MU!H`:`-`-#U/:HTT!H#U,054]"!H-`&@T9`TT`-`-`9--`,"9`:`&@#"&0&C
M1DT:``#1DR8F$#3)I@0`@`"NX4.`T$?IQ=6"R?SX<,"L_`P!T4SW4LQG;TCU
M1\Z+GAW+<]UO_8W99B#'S"(<NR;>^FF=%.2"*4!V>5,`=-/R=CCKM]'QX2=1
MB"W8;0IYJ5[?+UI#UC*Q+#4+%#V\Y8+])UAG4D=0ZW,I7'LU+X*D42Z:[,4I
M!2VQ$8W,EY.&$@P9H$R,5:"^F*/.@#^V8>2[6YGK>#\*''8K,L:!6`?R6&@P
MY%>8Q_4'S"(_/I1*1HT;P$J$"H\B-+5C\QJQ<9/-WN_=(U4MHL@O']NX12?0
MCJ$G:+EOZ$).2P%V:!="[ROU,?-#SD'+@;5_9W\XZV/Y"`]%[-2;:BGFYU,0
MD*^`K,-3UWK*L3L-TX,%R4`__$MB9'#$_6KKF9OR`\@5#%XW4B,"%6+S@>A5
M2RE?TAC<,3@(Q`?XNY(IPH2#+O9U:`#'<0`````````````!``````````L`
M`````%1204E,15(A(2$`````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
,````````````````
`
end
SHAR_EOF
  (set 20 22 03 15 06 50 49 'flag'
   eval "${shar_touch}") && \
  chmod 0644 'flag'
if test $? -ne 0
then ${echo} "restore of flag failed"
fi
  if ${md5check}
  then (
       ${MD5SUM} -c >/dev/null 2>&1 || ${echo} 'flag': 'MD5 check failed'
       ) << \SHAR_EOF
fd175c151e78c2bce9da32d9c7a18487  flag
SHAR_EOF

else
test `LC_ALL=C wc -c < 'flag'` -ne 1092 && \
  ${echo} "restoration warning:  size of 'flag' is not 1092"
  fi
fi
if rm -fr ${lock_dir}
then ${echo} "x - removed lock directory ${lock_dir}."
else ${echo} "x - failed to remove lock directory ${lock_dir}."
     exit 1
fi
exit 0

```
Now running the shell script we get this output:
```bash
└─$ sh ./Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```
Lets run the file command on flag and see what we get:
```bash
└─$ file flag
flag: current ar archive
```
Looks like its now an 'ar archive' so I used mv to give it the proper extention and then the ar -x to un archive it:
```bash
└─$ mv flag flag.a
└─$ ar -x flag.a
```
That then created a cpio archive which we can see using the file command on the new file:
```bash
└─$ file flag
flag: cpio archive
└─$ mv flag flag.cpio
└─$ cpio -iv < flag.cpio
flag
2 blocks
```
This process then continues as we unravel the multiple layers until we eventually get a ASCII Text file.  Throughout this process I ended up using google, man <command> and <command> -h, etc to find out how to unravel the file formats I was unfamiliar with.  Some of those commands are left out for brevity:
```bash
└─$ file flag
flag: bzip2 compressed data, block size = 900k
└─$ ls
flag  flag.a  flag.cpio  Flag.pdf  readme.md
└─$ mv flag flag.bz2
└─$ bunzip2 flag.bz2
└─$ ls
flag  flag.a  flag.cpio  Flag.pdf  readme.md
└─$ file flag
flag: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:49 2022, from Unix, original size modulo 2^32 326
└─$ mv flag flag.gz
└─$ gzip -dk flag.gz
└─$ file flag
flag: lzip compressed data, version: 1
└─$ lzip -d flag -o flag-1.lz
└─$ file flag-1.lz
flag-1.lz: LZ4 compressed data (v1.4+)
└─$ unlz4 -d flag-1.lz flag-lz41
flag-1.lz            : decoded 263 bytes
└─$ file flag-lz41
flag-lz41: LZMA compressed data, non-streamed, size 252
└─$ unlzma flag-lz41
unlzma: flag-lz41: Filename has an unknown suffix, skipping
└─$ mv flag-lz41 flag-lz.lzma        
└─$ unlzma flag-lz.lzma        
└─$ file flag-lz
flag-lz: lzop compressed data - version 1.040, LZO1X-1, os: Unix
└─$ lzop -d flag-lz
lzop: flag-lz: unknown suffix -- ignored
skipping flag-lz [flag-lz.raw]
└─$ mv flag-lz flag-lz.lzo
└─$ lzop -d flag-lz.lzo
└─$ file flag-lz
flag-lz: lzip compressed data, version: 1
└─$ lzip -d flag-lz -o flag2
└─$ file flag2
flag2: XZ compressed data
└─$ unxz flag2
unxz: flag2: Filename has an unknown suffix, skipping
└─$ mv flag2 flag2.xz        
└─$ unxz flag2.xz          
└─$ file flag2
flag2: ASCII text
└─$ cat flag2
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37353137353362307d0a
└─$ base64 -d flag2
�N��~��~x�����ι��4�������N��^��N��]���_���n_�N��n����]���_߽��]�ߝ��m���� 
└─$ base64 flag2
NzA2OTYzNmY0MzU0NDY3YjY2MzE2YzY1NmU0MDZkMzM1ZjZkNDA2ZTMxNzA3NTZjNDA3NDMxMzA2
ZTVmCjY2MzA3MjVmMzA2MjMyNjM3NTcyMzEzNzc5NWYzNzM1MzEzNzM1MzM2MjMwN2QwYQo=
```
The ASCII file we get at the end you can see I first thought it may be base64 encoded, but that didnt appear to be the case.
```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37353137353362307d0a
```
I then realized it may be a string of ascii hex values. So to make it easy I just used this [site](https://www.rapidtables.com/convert/number/hex-to-ascii.html) to do the conversion and we get our flag:

```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_751753b0}
```
# **FLAG:** 
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_751753b0}

[^1]: Included links to the source code may be out of date as they were what I recorded during the competition, and may be different now.