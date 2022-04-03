
orig_str = "128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137"
alphabet_map = []
split_message = orig_str.split()



def buildAlphabetMap():
  # first add the letters
  for x in range(65,91):
    alphabet_map.append(chr(x))
  # now the numbers
  for x in range(48,58):
    alphabet_map.append(chr(x))
  # finally the underscore character
  alphabet_map.append('_')
  

buildAlphabetMap()
#print(split_message)
flag = 'picoCTF{'
for x in split_message:
  flag += alphabet_map[int(x)%37]

flag+="}"  
print(flag)