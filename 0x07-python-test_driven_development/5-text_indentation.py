#!/usr/bin/python3
"""
This is the 5-text_indentation module.

The 5-text_indentation module supplies one function, text_indentation(text).
For example,
>>> text_indentation("Common burger ingredients: buns, beef and ketchup.")
Common burger ingredients:
<BLANKLINE>
buns, beef and ketchup.
<BLANKLINE>
"""


def text_indentation(text):
    """Prints a text with 2 new lines after given characters(.),(?)and(:)"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for chr in text:
        if flag == 0:
            if chr == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if chr == '?' or chr == '.' or chr == ':':
                print(chr)
                print()
                flag = 0
            else:
                print(chr, end="")
