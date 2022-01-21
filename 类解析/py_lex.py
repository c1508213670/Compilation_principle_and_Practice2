#! /usr/bin/env python
#coding=utf-8
import ply.lex as lex

# LEX for parsing Python

# Tokens
tokens=('SELF','SELFVAR','defprint','VARIABLE','NUMBER','IF','WHILE','PRINT','DEF','RETURN','LIST','LIST_VAR','LEN','AND','CLASS','init','add')

literals=['=','+','-','*','(',')','{','}','<','>',';','[',']',',',':','.']

#Define of tokens

def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_defprint(t):
    r'print_info'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_SELFVAR(t):
    r'self\.[a-zA-Z_]+'
    return t

def t_SELF(t):
    r'self'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_init(t):
    r'__init__'
    return t

def t_add(t):
    r'add_'
    return t




def t_AND(t):
    r'and'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DEF(t):
    r'def'
    return t

def t_RETURN(t):
    r'return'
    return t


def t_LEN(t):
    r'len'
    return t

def t_LIST(t):
    r'\[[0-9,]+\]'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]+(\[[a-zA-z0-9]+\])?'
    return t


# Ignored
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lex.lex()
