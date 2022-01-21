#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : MiJiu
# @FileName: py_lex.py
# @Software: PyCharm


import ply.lex as lex

# LEX for parsing Python

# Tokens
tokens = ('VARIABLE', 'NUMBER', 'IF', 'WHILE', 'PRINT', 'LEN', 'ELIF', 'ELSE', 'BREAK', 'FOR', 'MOD', 'LE', 'GE', 'PP')

literals = ['=', '+', '-', '*', '(', ')', '{', '}', '<', '>', '[', ']', ',', '/', ';']


# Define of tokens

def t_NUMBER(t):
    r'[0-9]+'
    return t


def t_PRINT(t):
    r'print'
    return t


def t_IF(t):
    r'if'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_MOD(t):
    r'//'
    return t


def t_LE(t):
    r'<='
    return t


def t_GE(t):
    r'>='
    return t


def t_PP(t):
    r'\+\+'
    return t


def t_LEN(t):
    r'len'
    return t


def t_FOR(t):
    r'for'
    return t


def t_ELIF(t):
    r'elif'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_BREAK(t):
    r'break'
    return t


def t_VARIABLE(t):
    r'[a-zA-Z_]+'
    return t


# Ignored
t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()
