#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : MiJiu
# @FileName: py_yacc.py
# @Software: PyCharm


import ply.yacc as yacc
from py_lex import *
from node import node, num_node


# YACC for parsing Python

def simple_node(t, name):
    t[0] = node(name)
    for i in range(1, len(t)):
        t[0].add(node(t[i]))
    return t[0]


def p_program(t):
    '''program : statements'''
    if len(t) == 2:
        t[0] = node('[PROGRAM]')
        t[0].add(t[1])


def p_statements(t):
    '''statements : statements statement
                  | statement'''
    if len(t) == 3:
        t[0] = node('[STATEMENTS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t) == 2:
        t[0] = node('[STATEMENTS]')
        t[0].add(t[1])


def p_statement(t):
    ''' statement : assignment
                  | print
                  | if
                  | while
                  | for
                  | BREAK'''
    if t[1] == 'break':
        t[0] = simple_node(t, '[STATEMENT]')
    else:
        t[0] = node('[STATEMENT]')
        t[0].add(t[1])


def p_assignment(t):
    '''assignment : VARIABLE '=' expr
                  | VARIABLE '[' expr ']' '=' expr
                  | VARIABLE PP '''
    if len(t) == 4:
        t[0] = node('[ASSIGNMENT]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
    if len(t) == 7:
        t[0] = node('[ASSIGNMENT]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
        t[0].add(node(t[5]))
        t[0].add(t[6])
    if len(t) == 3:
        t[0] = simple_node(t, '[ASSIGNMENT]')


def p_expr(t):
    '''expr : term
            | '[' list ']'
            | expr '+' term
            | expr '-' term
            | LEN '(' VARIABLE ')' '''
    if len(t) == 2:
        t[0] = node('[EXPR]')
        t[0].add(t[1])
    if len(t) == 5:
        t[0] = simple_node(t, '[EXPR]')
    if len(t) == 4:
        t[0] = node('[EXPR]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])
    if len(t) == 4 and t[1] == '[':
        t[0] = node('[EXPR]')
        t[0].add(node(t[1]))
        t[0].add(t[2])
        t[0].add(node(t[3]))


def p_list(t):
    '''list : list ',' expr
            | expr'''
    if len(t) == 2:
        t[0] = node('[LIST]')
        t[0].add(t[1])
    if len(t) == 4:
        t[0] = node('[LIST]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])


def p_term(t):
    '''term : term '*' factor
            | term '/' factor
            | term MOD factor
            | factor'''
    if len(t) == 2:
        t[0] = node('[TERM]')
        t[0].add(t[1])
    if len(t) == 4:
        t[0] = node('[TERM]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])


def p_factor(t):
    '''factor : NUMBER
              | VARIABLE
              | VARIABLE '[' VARIABLE ']'
              | VARIABLE '[' NUMBER ']'
              | '(' expr ')' '''
    if len(t) == 2:
        t[0] = simple_node(t, '[FACTOR]')
    if len(t) == 5:
        t[0] = simple_node(t, '[FACTOR]')
    if len(t) == 4:
        t[0] = node('[FACTOR]')
        t[0].add(node(t[1]))
        t[0].add(t[2])
        t[0].add(node(t[3]))


def p_elses(t):
    '''elses : ELIF '(' condition ')' '{' statements '}'
             | ELIF '(' condition ')' '{' statements '}' elses
             | ELSE '{' statements '}' '''
    if len(t) == 5:
        t[0] = node('[ELSES]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
    if len(t) == 8:
        t[0] = node('[ELSES]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
        t[0].add(node(t[5]))
        t[0].add(t[6])
        t[0].add(node(t[7]))
    if len(t) == 9:
        t[0] = node('[ELSES]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
        t[0].add(node(t[5]))
        t[0].add(t[6])
        t[0].add(node(t[7]))
        t[0].add(t[8])


def p_for(t):
    '''for : FOR '(' assignment ';' condition ';' assignment ')' '{' statements '}' '''
    t[0] = node('[FOR]')
    t[0].add(node(t[1]))
    t[0].add(node(t[2]))
    t[0].add(t[3])
    t[0].add(node(t[4]))
    t[0].add(t[5])
    t[0].add(node(t[6]))
    t[0].add(t[7])
    t[0].add(node(t[8]))
    t[0].add(node(t[9]))
    t[0].add(t[10])
    t[0].add(node(t[11]))


def p_content(t):
    '''content : content ',' VARIABLE
               | VARIABLE'''
    if len(t) == 2:
        t[0] = simple_node(t, '[CONTENT]')
    if len(t) == 4:
        t[0] = node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(node(t[3]))


def p_print(t):
    '''print : PRINT '(' content ')' '''
    t[0] = node('[PRINT]')
    t[0].add(node(t[1]))
    t[0].add(node(t[2]))
    t[0].add(t[3])
    t[0].add(node(t[4]))


def p_if(t):
    '''if : IF '(' condition ')' '{' statements '}'
          | IF '(' condition ')' '{' statements '}' elses '''
    if len(t) == 8:
        t[0] = node('[IF]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
        t[0].add(node(t[5]))
        t[0].add(t[6])
        t[0].add(node(t[7]))
    if len(t) == 9:
        t[0] = node('[IF]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
        t[0].add(node(t[5]))
        t[0].add(t[6])
        t[0].add(node(t[7]))
        t[0].add(t[8])


def p_condition(t):
    '''condition : expr '>' expr
                 | expr '<' expr
                 | expr LE expr
                 | expr GE expr'''
    t[0] = node('[CONDITION]')
    t[0].add(t[1])
    t[0].add(node(t[2]))
    t[0].add(t[3])


def p_while(t):
    r'''while : WHILE '(' condition ')' '{' statements '}' '''
    t[0] = node('[WHILE]')
    t[0].add(node(t[1]))
    t[0].add(node(t[2]))
    t[0].add(t[3])
    t[0].add(node(t[4]))
    t[0].add(node(t[5]))
    t[0].add(t[6])
    t[0].add(node(t[7]))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


yacc.yacc()
