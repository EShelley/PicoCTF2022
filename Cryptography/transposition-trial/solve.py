# heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B
# 
#
# encryped via tranposition cipher, in 3 letter blocks
# so the first block is: heT
# should be The
# To do that we take each block of three and move the last to beginning

encflag = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B"
outFlag = ''
for x in range(0,len(encflag),3):
  t = encflag[x:x+3]
  o = t[-1] +t[:2]
  outFlag += o

print(outFlag)