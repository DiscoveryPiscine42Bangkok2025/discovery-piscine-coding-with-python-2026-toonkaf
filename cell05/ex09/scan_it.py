#!/usr/bin/env python
import sys
import re
count = len(re.findall(sys.argv[1],sys.argv[2]))
print(count if len(sys.argv) == 3 and count > 0 else "none")