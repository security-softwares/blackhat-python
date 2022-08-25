import os
try:
  import rsa
except:
  print('module not found try pip3 install rsa or press y',end='')
  i=input()
  if i=='y' or i=="Y":
  os.system('pip3 install rsa ')
 

publicKey, privateKey = rsa.newkeys(512)
f=open(input('enter file name to be encrypted'),'r')

# this is the string that we will be encrypting
message = f.read()

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
            publicKey)

j=input('enter output file name')
j=open(j,'w')
j.write('import rsa')
j.write(f'pv={privateKey}')
j.write("exec('decMessage = rsa.decrypt(encMessage, pv).decode()')")

print('success')
