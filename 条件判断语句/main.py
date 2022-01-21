from py_yacc import yacc
from util import clear_text
from translation import trans,v_table

text=clear_text(open('binary_search.py','r').read())
text1=clear_text(open('select_sort.py', 'r').read())

# syntax parse
root=yacc.parse(text)
root.print_node(0)

# translation
trans(root)
print(v_table)

# syntax parse
root=yacc.parse(text1)
root.print_node(0)

# translation
trans(root)
print(v_table)