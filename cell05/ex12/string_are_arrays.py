#!/usr/bin/env python
import sys
if len(sys.argv) != 1 and sys.argv[1].count("z"):
    print(sys.argv[1].count("z") * "z")
else:
    print("none")