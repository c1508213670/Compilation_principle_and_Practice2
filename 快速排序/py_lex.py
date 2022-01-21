#! /usr/bin/env python
#coding=utf-8
import ply.lex as lex

# LEX for parsing Python

# Tokens
reserved = {'if':'IF','elif':'ELIF','else':'ELSE','break':'BREAK','and':'AND','while':'WHILE','for':'FOR','print':'PRINT',
            'def':'DEF','return':'RETURN','len':'LEN'}
tokens=('VARIABLE','NUMBER','MOD','LE','GE','PLUSPLUS','MINUSEQUAL','PLUSEQUAL')+tuple(reserved.values())

literals=['=','+','-','*','/','(',')','{','}','<','>','[',']',',',';']

#Define of tokens

def t_VARIABLE(t):
    r'[a-zA-Z_]+'
    t.type = reserved.get(t.value, 'VARIABLE')  # 检查保留字
    return t

def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_MOD(t):
    r'//'
    return t

def t_LE(t):
    r'>='
    return t

def t_GE(t):
    r'<='
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MINUSEQUAL(t):
    r'-='
    return t

def t_PLUSEQUAL(t):
    r'\+='
    return t


# Ignored
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lex.lex()
