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