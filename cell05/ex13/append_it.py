#!/usr/bin/env python
import sys
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if i[-3:] != "ism":
            print(f"{i}ism")
else:
    print("none")