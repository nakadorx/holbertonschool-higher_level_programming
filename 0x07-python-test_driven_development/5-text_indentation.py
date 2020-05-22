#!/usr/bin/python3
"""
text indentation
"""


def text_indentation(text):
    """
    text indentation
    """
    newText = ""

    if type(text) is not str:
        raise TypeError('text must be a string')
        return

    for i in text:
        newText += i
        if i in [".", "?", ":"]:
                print(newText.lstrip(), end='\n\n')
                newText = ""
    if i in [".", "?", ":"]:
        print(newText.lstrip(), end="")
    else:
        print(newText.lstrip(), end="\n")
