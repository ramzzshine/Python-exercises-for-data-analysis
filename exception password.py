# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:30:22 2020

@author: DS7_RVepuri
"""

import warnings
password = 'Ramy_123'
def check_number(s):
    ''' Check whether the input string is a digit. '''
    try: 
        input(s)
        return True
    except:
        # do not catch error
        return False
def check_validity(pw):
    ''' Return True if input pw is valid, and return False if invalid.'''
    special_chars = ['_']
    if isinstance(pw,str): pw=list(pw) # I could have appointed to a diff var name
    else: warnings.warn('Password has to be a string object.')
    res = False
    valid_dict={'small_let':False, 'num':False, 'special_chars':False, 
                'cap_let':False, 'len':False } 
    if len(pw)>= 6: valid_dict['len']=True
    for i in pw:
        if i.islower(): valid_dict['small_let'] = True
        if i in special_chars: valid_dict['special_chars'] = True
        if i.isupper(): valid_dict['cap_let'] = True
        if not valid_dict['num']:  valid_dict['num'] = check_number(i)
    if all(valid_dict.values()): res = True
    return res

print (check_validity(password))

from itertools import groupby
Input =[4,6,2,8,2,2,5,7,8]
Input.sort()
Input
print([list(j)for i,j in groupby(Input)])