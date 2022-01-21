#! /usr/bin/env python
#coding=utf-8
import ply.yacc as yacc
from py_lex import *
from node import node

# YACC for parsing Python
# 添加node方法
def generateNode(t, nodeName):
    resultNode = node(nodeName)
    for i in t.slice[1:]:
        resultNode.append(i)
    return resultNode


def p_program(t):
    '''program : statements'''
    t[0] = generateNode(t, '[PROGRAM]')


def p_statements(t):
    '''statements : statements statement
                  | statement'''
    t[0] = generateNode(t, '[STATEMENTS]')


def p_statement(t):
    ''' statement : assignment
                  | print
                  | if
                  | while
                  | for
                  | returnsomething
                  | function
                  | runfunction
                  | BREAK'''
    t[0] = generateNode(t, '[STATEMENT]')


def p_returnsomething(t):
    '''returnsomething : RETURN
                       | RETURN list'''
    t[0] = generateNode(t, '[RETURNSOMETHING]')


def p_assignment(t):
    '''assignment : VARIABLE '=' expr
                  | VARIABLE MINUSEQUAL expr
                  | VARIABLE PLUSEQUAL expr
                  | VARIABLE '[' expr ']' '=' expr
                  | VARIABLE PLUSPLUS'''
    t[0] = generateNode(t, '[ASSIGNMENT]')


def p_expr(t):
    '''expr : expr '+' term
            | expr '-' term
            | term
            | '[' list ']' '''
    t[0] = generateNode(t, '[EXPR]')


def p_list(t):
    '''list : list ',' expr
            | expr'''
    t[0] = generateNode(t, '[LIST]')


def p_term(t):
    '''term : term '*' factor
            | term '/' factor
            | term MOD factor
            | factor'''
    t[0] = generateNode(t, '[TERM]')


def p_factor(t):
    '''factor : NUMBER
              | VARIABLE
              | VARIABLE '[' VARIABLE ']'
              | VARIABLE '[' NUMBER ']'
              | LEN '(' VARIABLE ')'
              | '(' expr ')' '''
    t[0] = generateNode(t, '[FACTOR]')


def p_print(t):
    '''print : PRINT '(' VARIABLE ')' '''
    t[0] = generateNode(t, '[PRINT]')


def p_if(t):
    r'''if : IF '(' conditions ')' '{' statements '}'
           | IF '(' conditions ')' '{' statements '}' elses '''
    t[0] = generateNode(t, '[IF]')


def p_elses(t):
    '''elses : ELIF '(' conditions ')' '{' statements '}'
             | ELIF '(' conditions ')' '{' statements '}' elses
             | ELSE '{' statements '}' '''
    t[0] = generateNode(t, '[ELSES]')


def p_while(t):
    r'''while : WHILE '(' conditions ')' '{' statements '}' '''
    t[0] = generateNode(t, '[WHILE]')


def p_for(t):
    '''for : FOR '(' assignment ';' conditions ';' assignment ')' '{' statements '}' '''
    t[0] = generateNode(t, '[FOR]')

def p_conditions(t):
    '''conditions : condition AND condition
                  | condition'''
    t[0] = generateNode(t, '[CONDITIONS]')

def p_condition(t):
    '''condition : expr '>' expr
                 | expr LE expr
                 | expr '<' expr
                 | expr GE expr'''
    t[0] = generateNode(t, '[CONDITION]')


def p_function(t):
    r'''function : DEF VARIABLE '(' args ')' '{' statements '}' '''
    t[0] = generateNode(t, '[FUNCTION]')

def p_args(t):
    '''args : args ',' VARIABLE
            | VARIABLE'''
    t[0] = generateNode(t, '[ARGS]')

def p_runfunction(t):
    r'''runfunction : VARIABLE '(' list ')' '''
    t[0] = generateNode(t, '[RUNFUNCTION]')
    
                
def p_error(t):
    print("Syntax error at '%s'" % t.value)

yacc.yacc()
