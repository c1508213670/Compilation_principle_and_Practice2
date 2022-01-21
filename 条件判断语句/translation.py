#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : MiJiu
# @FileName: translation.py
# @Software: PyCharm


from __future__ import division

v_table = {}  # variable table


def update_v_table(name, value):
    v_table[name] = value


def trans(node):
    # Translation

    # Program
    if node.getdata() == '[PROGRAM]':
        '''program : statements'''
        trans(node.getchild(0))

    # Statements
    if node.getdata() == '[STATEMENTS]':
        '''statements : statements statement
                      | statement'''
        for c in node.getchildren():
            node.setvalue(trans(c))
            if node.getvalue() == 'break':
                break

    # Statement
    elif node.getdata() == '[STATEMENT]':
        ''' statement : assignment
                      | print
                      | if
                      | while
                      | for
                      | BREAK'''
        if node.getchild(0).getdata() == 'break':
            node.setvalue('break')
        else:
            node.setvalue(trans(node.getchild(0)))

    # Assignment
    elif node.getdata() == '[ASSIGNMENT]':
        '''assignment : VARIABLE '=' expr
                      | VARIABLE '[' expr ']' '=' expr
                      | VARIABLE PP '''
        if node.getlen() == 3:
            value = trans(node.getchild(2))
            node.setvalue(value)
            # update v_table
            update_v_table(node.getchild(0).getdata(), value)
        if node.getlen() == 2:
            value = v_table[node.getchild(0).getdata()] + 1
            node.setvalue(value)
            # update v_table
            update_v_table(node.getchild(0).getdata(), value)
        if node.getlen() == 6:
            value = trans(node.getchild(5))
            value1 = trans(node.getchild(2))
            v_table[node.getchild(0).getdata()][value1] = value

    # Expr
    elif node.getdata() == '[EXPR]':
        '''expr : term
                | '[' list ']'
                | expr '+' term
                | expr '-' term
                | LEN '(' VARIABLE ')' '''
        if node.getlen() == 1:
            node.setvalue(trans(node.getchild(0)))
        elif node.getlen() == 3 and node.getchild(1).getdata() == '[LIST]':
            node.setvalue(list(trans(node.getchild(1))))
        elif node.getlen() == 3 and node.getchild(1).getdata() == '+':
            node.setvalue(trans(node.getchild(0)) + trans(node.getchild(2)))
        elif node.getlen() == 3 and node.getchild(1).getdata() == '-':
            node.setvalue(trans(node.getchild(0)) - trans(node.getchild(2)))
        elif node.getlen() == 4:
            node.setvalue(len(v_table[node.getchild(2).getdata()]))

    # List
    elif node.getdata() == '[LIST]':
        '''list : list ',' expr
                | expr'''
        if node.getlen() == 1:
            node.setvalue([trans(node.getchild(0))])
        elif node.getlen() == 3:
            trans(node.getchild(0)).append(trans(node.getchild(2)))
            node.setvalue(node.getchild(0).getvalue())

        # if node.getlen() == 1:
        #     node.setvalue(list(str(trans(node.getchild(0)),)) )
        # elif node.getlen() == 3:
        #     a=list(trans(node.getchild(0)))
        #     a.append(str(trans(node.getchild(2))))
        #     node.setvalue(a)

    # Term
    elif node.getdata() == '[TERM]':
        '''term : term '*' factor
                | term '/' factor
                | term MOD factor
                | factor'''
        if node.getlen() == 1:
            node.setvalue(trans(node.getchild(0)))
        elif node.getlen() == 3 and node.getchild(1).getdata() == '*':
            node.setvalue(trans(node.getchild(0)) * trans(node.getchild(2)))
        elif node.getlen() == 3 and node.getchild(1).getdata() == '/':
            node.setvalue(trans(node.getchild(0)) / trans(node.getchild(2)))
        else:
            node.setvalue(trans(node.getchild(0)) // trans(node.getchild(2)))

    # Factor
    elif node.getdata() == '[FACTOR]':
        '''factor : NUMBER
                  | VARIABLE
                  | VARIABLE '[' VARIABLE ']'
                  | VARIABLE '[' NUMBER ']'
                  | '(' expr ')' '''
        if node.getlen() == 1 and node.getchild(0).getdata().isdigit():
            node.setvalue(int(node.getchild(0).getdata()))
        elif node.getlen() == 1 and not node.getchild(0).getdata().isdigit():
            node.setvalue(v_table[node.getchild(0).getdata()])
        elif node.getlen() == 3:
            node.setvalue(trans(node.getchild(1)))
        elif node.getlen() == 4 and not node.getchild(2).getdata().isdigit():
            node.setvalue(v_table[node.getchild(0).getdata()][v_table[node.getchild(2).getdata()]])
        elif node.getlen() == 4 and node.getchild(2).getdata().isdigit():
            node.setvalue(v_table[node.getchild(0).getdata()][node.getchild(2).getdata()])

    # While
    elif node.getdata() == '[WHILE]':
        r'''while : WHILE '(' condition ')' '{' statements '}' '''
        while trans(node.getchild(2)):
            if trans(node.getchild(5)) == 'break':
                break
    # If
    elif node.getdata() == '[IF]':
        r'''if : IF '(' condition ')' '{' statements '}'
               | IF '(' condition ')' '{' statements '}' elses '''
        if trans(node.getchild(2)):
            node.setvalue(trans(node.getchild(5)))
        elif node.getlen() == 8:
            node.setvalue(trans(node.getchild(7)))

    # Elses
    elif node.getdata() == '[ELSES]':
        '''elses : ELIF '(' condition ')' '{' statements '}'
                 | ELIF '(' condition ')' '{' statements '}' elses
                 | ELSE '{' statements '}' '''
        if node.getlen() == 4:
            node.setvalue(trans(node.getchild(2)))
        elif trans(node.getchild(2)):
            node.setvalue(trans(node.getchild(5)))
        elif node.getlen() == 8:
            node.setvalue(trans(node.getchild(7)))

    # For
    elif node.getdata() == '[FOR]':
        '''for : FOR '(' assignment ';' condition ';' assignment ')' '{' statements '}' '''
        trans(node.getchild(2))
        while trans(node.getchild(4)):
            if trans(node.getchild(9)) == 'break':
                break
            else:
                trans(node.getchild(6))

    # Condition
    elif node.getdata() == '[CONDITION]':
        '''condition : expr '>' expr
                     | expr '<' expr
                     | expr LE expr
                     | expr GE expr'''
        op = node.getchild(1).getdata()
        if op == '>':
            node.setvalue(trans(node.getchild(0)) > trans(node.getchild(2)))
        elif op == '<':
            node.setvalue(trans(node.getchild(0)) < trans(node.getchild(2)))
        elif op == '>=':
            node.setvalue(trans(node.getchild(0)) >= trans(node.getchild(2)))
        elif op == '<=':
            node.setvalue(trans(node.getchild(0)) <= trans(node.getchild(2)))

    # CONTENT
    elif node.getdata() == '[CONTENT]':
        '''content : content ',' VARIABLE
                   | VARIABLE'''
        if node.getlen() == 1:
            node.setvalue([v_table[node.getchild(0).getdata()]])
        if node.getlen() == 3:
            trans(node.getchild(0)).append(v_table[node.getchild(2).getdata()])
            node.setvalue(node.getchild(0).getvalue())

    # Print
    elif node.getdata() == '[PRINT]':
        '''print : PRINT '(' content ')' '''
        arg0 = trans(node.getchild(2))
        if len(arg0) == 1:
            print(arg0[0])
        else:
            for i in range(len(arg0) - 1):
                print(arg0[i]),
            print(arg0[len(arg0) - 1])

    return node.getvalue()
