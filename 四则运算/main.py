#! /usr/bin/env python
#coding=utf-8
from py_yacc import yacc
from translation import trans,v_table

def clear_text(text):
    lines=[]
    for line in text.split('\n'):
        line=line.strip()
        if len(line)>0:
            lines.append(line)
    return ' '.join(lines)
text=clear_text(open('example.py','r').read())

# syntax parse
root=yacc.parse(text)
root.print_node(0)

# translation
trans(root)
print(v_table)