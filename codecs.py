import codecs
print("""encodings :
# hex
# quopri
# uu 
# uu_codec 
# zip 
# zlib 
# bz2 
# bz2_codec
base64""")
en=input('enter encoding -: ')
i=open(input("enter file to be encoded"),'r')
k=i.read()
main=eval(f"codecs.encode(b{k},'{en}')")
n=open(input('enter output file name -: '),'w')
n.write(f'a=codecs.decode(b"{main}","{en}")')
n.write('exec(a)')
