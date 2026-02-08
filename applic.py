# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 03:10:45 2026

@author: admin
"""

import math 

bigW = int(input("Give me a width for the container: "))
bigH = int(input("Give me a height for the container: "))
smolw = int(input("Give width for small one: "))
smolh = int(input("Give height for small one: "))

sol = max(bigW/smolw * bigH/smolh, bigH/smolw, bigW/smolh)
if (bigW < min(smolh, smolw) or bigH < min(smolh, smolw)):
    sol = 0
print(math.trunc(sol))