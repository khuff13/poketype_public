# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:09:26 2019

@author: krystinsteelman
"""

import json

with open('PokemonOffDef.json','r') as f:
    poke_dict = json.load(f)
    
with open('PokemonStrWeak.json','r') as f:
    str_weak = json.load(f)

def TypeList():
    
    type1 = 'normal'
    type2 = 'fighting'
    type3 = 'flying'
    type4 = 'poison'
    type5 = 'ground'
    type6 = 'rock'
    type7 = 'bug'
    type8 = 'ghost'
    type9 = 'steel'
    type10 = 'fire'
    type11 = 'water'
    type12 = 'grass'
    type13 = 'electric'
    type14 = 'psychic'
    type15 = 'ice'
    type16 = 'dragon'
    type17 = 'dark'
    type18 = 'fairy'
    
    list_of_types = []
    list_of_types += [typ for name, typ in locals().items() if name.startswith('type')]
    
    return list_of_types

type_list = TypeList()

#checks if lenghts matches the length of dictionary, 1 means extra, -1 means not litte,
#and 0 means they are the same length
def length_check(x, y = len(type_list)):
    if x > y:
        return 1
    elif x < y:
        return -1
    else: return 0

#checks for mispellings, will output the number of spelling errors
def type_in_list(x, y = type_list):
    unknown = []
    for i in x:
        if i not in y:
            unknown.append(i)
    return len(unknown)

class PokeType:
    
    '''def __init__(self,poke_type):
        self.poke_type  = poke_type
        self.off = []
        self.deff = []'''
    
    def __init__(self):
        self.poke_type = []
        self.off = []
        self.deff = []
        
        
    def check_type(self,type_inputs):
        if len(self.poke_type) != 0:
            self.poke_type = []
        for i in type_inputs:
            if i in type_list and i not in self.poke_type:
                self.poke_type.append(i)
            else: return False
        return True
    
    def complete_off_list(self):
        for i in type_list:
            if i not in self.off_list.keys():
                self.off_list[i] = 1
                
    def complete_def_list(self):
        for i in type_list:
            if i not in self.def_list.keys():
                self.def_list[i] = 1
    
    def get_off(self):
        self.off = []
        for i in self.poke_type:
            off_dict = {}
            subTypeList = poke_dict.get(i).get('off')
            off_list = list(subTypeList.keys())
            len_check = 0
            spell_check = 0
            len_check = length_check(len(off_list))
            if len_check != 0:
                return('LEN_ERROR: '+str(len_check)) 
            spell_check = type_in_list(off_list)
            if spell_check != 0:
                return('SPELL_ERROR: '+str(spell_check))
            for poke_type, value in subTypeList.items():
                if value != 1:
                    off_dict[poke_type] = value
            self.off.append(off_dict)
        
    def get_def(self):
        self.deff = []
        for i in self.poke_type:
            def_dict = {}
            subTypeList = poke_dict.get(i).get('def')
            def_list = list(subTypeList.keys())
            len_check = 0
            spell_check = 0
            len_check = length_check(len(def_list))
            if len_check != 0:
                return('LEN_ERROR: '+str(len_check)) 
            spell_check = type_in_list(def_list)
            if spell_check != 0:
                return('SPELL_ERROR: '+str(spell_check))
            for poke_type, value in subTypeList.items():
                if value != 1:
                    def_dict[poke_type] = value
            self.deff.append(def_dict)
            
    def off_list(self):
        #self.off_list = {}
        if len(self.off) == 1:
            self.off_list = self.off[0]
        else:
            common_off = {}
            for key,value in self.off[0].items():
                if key in self.off[1]:
                    common_off[key] = value*self.off[1].get(key)
                else:
                    common_off[key] = value
            for key,value in self.off[1].items():
                if key not in common_off.keys():
                    common_off[key] = value
            self.off_list = common_off
            
    def def_list(self):
        #self.def_list = {}
        if len(self.deff) == 1:
            self.def_list = self.deff[0]
        else:
            common_def = {}
            for key,value in self.deff[0].items():
                if key in self.deff[1]:
                    common_def[key] = value*self.deff[1].get(key)
                else:
                    common_def[key] = value
            for key,value in self.deff[1].items():
                if key not in common_def.keys():
                    common_def[key] = value
            self.def_list = common_def
            
