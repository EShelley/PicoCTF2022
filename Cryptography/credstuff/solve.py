
usernameFile = './leak/usernames.txt'
passwordFile = './leak/passwords.txt'

userToFind = 'cultiris'

# open the files
un = open(usernameFile, 'r')
pw = open(passwordFile, 'r')

unList = un.readlines()
pwList = pw.readlines()

for x in range(len(unList)):
  if(userToFind in unList[x]):
    print(unList[x] + ' : ' + pwList[x])



un.close()
pw.close()