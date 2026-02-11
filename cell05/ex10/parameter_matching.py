#!/usr/bin/env python
import sys
if len(sys.argv) != 2:
    print("none")
    sys.exit()
key = input("What was the parameter? ")
if sys.argv[1] == key:
    print("Good job!")
else:
    print("Nope, Sorry...")