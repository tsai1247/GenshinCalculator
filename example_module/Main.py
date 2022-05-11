# import Weapsons.py

from Weapons import *

# init a new weapon
weapon = Weapons( { 'damage': 12, 'level': 2 } )

print( weapon.attack( ) )
print( weapon.attributes( ) )