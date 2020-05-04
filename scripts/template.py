from pwn import *

import struct
import sys

binary = './myfile'

context.clear(arch='amd64')  #i386 for 32 bit

p = process(binary)  # can have env={'VARNAME':'val'}

p.sendline(cyclic(128))  # crash string
p.wait()

assert pack(p.corefile.{{my_reg}}) in cyclic(128)

offset = cyclic_find(pack(p.corefile.{{my_reg}}))


