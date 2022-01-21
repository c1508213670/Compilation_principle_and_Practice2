#! /usr/bin/env python
#coding=utf-8
from py_yacc import yacc
from translation import Translator

def clear_text(text):
    lines=[]
    for line in text.split('\n'):
        line=line.strip()
        if len(line)>0:
            lines.append(line)
    return ' '.join(lines)

text=clear_text(open('quick_sort.py','r').read())

# syntax parse
root=yacc.parse(text)
root.print_node(0)

# translation

t=Translator()
t.translate(root)
print(t.v_table)