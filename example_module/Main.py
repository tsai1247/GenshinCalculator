#!/usr/bin/env python
# python version: 3.8.10
# import Weapsons.py
from Weapons import *

# init a new weapon
weapon = Weapons( { 'damage': 12, 'level': 2 } )

print( weapon.attack( ) )
print( weapon.attributes( ) )