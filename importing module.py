# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:09:28 2020

@author: DS7_RVepuri
"""


#1. Write a Python program to read an entire text le

def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('smaple.txt')



#2. Write a Python program to read rst n lines of a le.

def file_read(fname,nline):
    from itertools import islice;
    with open(fname) as f:
            for line  in islice(f,nline):
                print((line))

file_read('smaple.txt',2)     


#3.Write a Python program to append text to a le and display the text


def file_read(fname):
    from itertools import islice;
    with open(fname,'w') as fw:
            fw.write("This is new line")
    txt = open(fname)
    print(txt.read())

file_read('smaple.txt')     


#4.Write a Python program to read last n lines of a le.

def file_read(fname):
    from itertools import islice;
    with open(fname) as f:
            last_line = f.readlines()[-1]
            print(last_line)

file_read('smaple.txt')