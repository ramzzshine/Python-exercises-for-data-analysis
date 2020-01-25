# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:11:48 2020

@author: DS7_RVepuri
"""

# 1. A Regular Expression (RegEx) is a sequence of characters that defines a 
#search pattern. For example
^a...s$  ## any five letter string starting with a and ending with s

"""
^a...s$ in	abs	    No match
        in  alias	Match
        in  abyss	Match
        in  Alias	No match
        in  An abacus	No match
"""

import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
        
""" For the specify lenght we use ^ and $ """ 

""" List of char
[ ] . ^ $ * + ? {} () \ | 
"""

"""
[] - Square brackets
Square brackets specifies a set of characters you wish to match.          
"""
[123] = 1,2,3
[azx] = a,z,x
[1-5] = 1,2,3,4,5
[a-g]
[A-T]

[^123] = not in 1,2,3
[^1-5] = not in 1,2,3,4,5
[^a-z] = not in any alphabte 


\A - Matches if the specified characters are at the start of a string
\b - Matches if the specified characters are at the beginning or end of a word.
\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.
\d - Matches any decimal digit. Equivalent to [0-9]
\D - Matches any non-decimal digit. Equivalent to [^0-9]
\s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].
\S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].
\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.
\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
\Z - Matches if the specified characters are at the end of a string.



"""a python program for matching a pattern."""

def text_match(text):
        patterns = 'ab'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a1b1bc"))

"""a python program for matching a string."""

def text_match1(text):
        patterns = 'ac' or 'b1'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')


print(text_match1("ac"))
print(text_match1("abc"))
print(text_match1("a1b1bc"))

""" a python program for matching flags."""

xx = """It felt so good to be home. 
She is such a good seamstress. 
It was a good thing they were going home tomorrow. 
You have a good family.
"""
k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
print(k1)
print(k2)



"""
write a python program for searching a string.
"""

patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


"""
write a python program for searching a pattern.
"""

patts = ['who','you']
text = """Be who you are and say what you feel, because those who mind don't 
        matter and those who matter don't mind."""

for patt in patts:
    if re.search(patt, text):
        print("Partterns found ",patt)  
    else:
        print("Patterns not found")

"""
write a python program for searching flags
"""

search = re.search(patt, text, re.M|re.I)
if search:
    print("search.group()", search.group())
   # print("Search.group(1)", search.group(1))
    print("Search.group(2)", search.group(2))
else:
    print("No results")


"""write a python program for searching and replacing a string."""


if text:
    line = re.sub('you', 'U', text)
    print(line)
print(text)

