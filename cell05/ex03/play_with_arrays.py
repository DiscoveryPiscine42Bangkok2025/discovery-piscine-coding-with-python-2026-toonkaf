#!/usr/bin/env python
lst = [2,8,9,48,8,22,-12,2]
st = {num + 2 for num in lst if num+2 >= 10}
print(lst)
print(st)