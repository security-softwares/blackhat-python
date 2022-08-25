import lzma

i=input('input file')
o=open(i,'r')

k=lzma.LZMACompressor()
k=k.compress(o.read())+k.flush()
o=open(input('enter output file name'),'w')

o.write(k)
o.write('import lzma')
o.write('k=lzma.LZMAdecompressor()
o.write('j=k.decompress(k).lstrip("b")')
o.write('exec(j)')
