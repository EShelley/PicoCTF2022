
orig_str = "186 249 356 395 303 337 190 393 146 174 446 127 385 400 420 226 76 294 144 90 291 445 137"
alphabet_map = []
split_message = orig_str.split()



def buildAlphabetMap():
  # since our mapping starts at 1 lets add a dummy to the beginning
  alphabet_map.append('=') # using = as its not a character in our map to detect errors
  # first add the letters
  for x in range(65,91):
    alphabet_map.append(chr(x))
  
  for x in range(48,58):
    alphabet_map.append(chr(x))
  
  alphabet_map.append('_')

buildAlphabetMap()

#print(alphabet_map)
#print(split_message)
flag = 'picoCTF{'
for x in split_message:
  a = pow(int(x),-1,41)
  flag += alphabet_map[a]
flag += '}'
print(flag)