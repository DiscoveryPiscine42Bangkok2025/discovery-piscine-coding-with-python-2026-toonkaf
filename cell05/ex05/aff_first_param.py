#!/usr/bin/env python
import sys

if (len(sys.argv) > 1):
    print(sys.argv[1])
else:
    print("none")

# print(sys.argv[1] if len(sys.argv) > 1 else "none")