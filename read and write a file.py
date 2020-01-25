# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:45:47 2020

@author: DS7_RVepuri
"""
# Write a Python program to read an entire text file.


def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('PY SAMPLE.txt')

#Write a Python program to read rst n lines of a FILE.

def read_entire_file(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice (f,nlines):
            print(line)
read_entire_file('PY SAMPLE.txt',2)

#Write a Python program to append text to a file and display the text

def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('PY SAMPLE.txt')

#Python Program to Append the Contents of One File to Another File
name1 = input("Enter file to be read from: ")
name2 = input("Enter file to be appended to: ")
fin = open("PY SAMPLE.txt", "r")
data2 = fin.read()
fin.close()
fout = open("PY Sample2", "a")
fout.write(data2)
fout.close()

# read last n lines

def LastNLines (f,n):
    with open(f) as file:
        print('Last',n,'lines from file:',f)
        for line in (file.readlines() [-n:]):
            print(line,end = ' ')
            
name = input ('Enter the filename:')
n = input ('No of lines to read:')
try:
    LastNLines(name,n)
except:
    print('file error:')