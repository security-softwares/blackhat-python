#
import binascii
en=input("\033[38;5;22;48;5;227m python payload or virus file name enter ->>\033[0m ")


with open(en,'r') as f:
    t=eval(f'binascii.hexlify(b"{f.read()}")')
    o=open('main.txt','w')
    o.write(str(t))
