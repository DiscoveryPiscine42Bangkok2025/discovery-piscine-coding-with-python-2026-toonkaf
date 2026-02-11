#!/usr/bin/env python
import sys
import re
print(len(re.findall(sys.argv[1],sys.argv[2])) if len(sys.argv) == 3 else "none")