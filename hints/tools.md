# tools, and stages of exploitation

## what tools to use, how and when to use them

### 1. Recon

Figure out whatever you can about the file. Use commands, utils, and tools 
such as:

- run the program, and look at the source (if you can) to see what it does

- `file`

### 2. Static analysis

- `objdump -M intel -D myfile | grep -A35 main.:`

- diassemble with ghidra

### 3. Dynamic analysis

- use `gdb` (with pwndbg!)
- radare2

### to be organized...

xxd, gdb backtrace, sys proc map (in gdb) gdb list ltrace, strace, strings 
objdump -x, and pwntools python library

- 
