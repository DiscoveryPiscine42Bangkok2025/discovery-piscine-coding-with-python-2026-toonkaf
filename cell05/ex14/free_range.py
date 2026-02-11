#!/usr/bin/env python
import sys
if len(sys.argv) != 3:
    print("none")
else:
    f = int(sys.argv[1])
    e = int(sys.argv[2])
    lst = []
    for i in range(f, e + 1):
        lst.append(i)
    print(lst)    
