# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:26:30 2019

@author: krystinsteelman
"""

import PokeType as PT
import importlib
from pprint import pprint

importlib.reload(PT)

count = 0
realPoke = False
while realPoke == False and count < 4:
    if count == 0:
        print('Enter the Pokemon type(s):')
        type_input = input().split()
        poketype = PT.PokeType()
        realPoke = poketype.check_type(type_input)
    else:
        print('ERROR: Reenter the Pokemon type(s):')
        type_input = input().split()
        poketype = PT.PokeType()
        realPoke = poketype.check_type(type_input)
    count += 1
    
print(poketype.poke_type)
poketype.get_off()
poketype.get_def()
print(poketype.off)
print(poketype.deff)
poketype.off_list()
poketype.def_list()
print(poketype.off_list)
print(poketype.def_list)