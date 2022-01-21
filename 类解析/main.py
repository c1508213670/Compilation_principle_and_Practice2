#! /usr/bin/env python
#coding=utf-8
from py_yacc import yacc
from util import clear_text
from translation import Tran,f_table,list_table,class_table,var_class_table,class_member
text=clear_text(open('stu.py','r').read())

# syntax parse
root=yacc.parse(text)
root.print_node(0)


# translation

t=Tran()
t.trans(root)
print('the result below is class_memeber and var_class_table')
print(class_member)
print(var_class_table)
