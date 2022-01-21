#! /usr/bin/env python
#coding=utf-8
import ply.yacc as yacc
from py_lex import *
from node import node,num_node

# YACC for parsing Python

def simple_node(t,name):
    t[0]=node(name)
    for i in range(1,len(t)):
        t[0].add(node(t[i]))
    return t[0]

def p_program(t):
    '''program : statements'''
    if len(t)==2:
        t[0]=node('[PROGRAM]')
        t[0].add(t[1])
        
def p_statements(t):
    '''statements : statements statement
                  | statement'''
    if len(t)==3:
        t[0]=node('[STATEMENTS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t)==2:
        t[0]=node('[STATEMENTS]')
        t[0].add(t[1])

def p_statement(t):
    ''' statement : assignment
                  | operation
                  | print
                  | if
                  | while
                  | function
                  | runfunction
                  | return
                  | class
                  | classfunc0
                  | classfunc1
                  | classfunc2'''
    if len(t)==2:
        t[0]=node(['STATEMENT'])
        t[0].add(t[1])

def p_return(t):
    '''return : RETURN'''
    t[0]=node('[RETURN]')

def p_assignment(t):
    '''assignment : VARIABLE '=' NUMBER
                  | VARIABLE '=' VARIABLE
                  | VARIABLE '=' LIST
                  | VARIABLE '=' LEN '(' VARIABLE ')' '''
    t[0] = node('[ASSIGNMENT]')
    if(t[1][-1]=="]"):
        t[0].add(node('[LIST MEMBER]'))
    else:
        t[0].add(node('[VARIABLE]'))
    t[0].add(node(t[1]))
    if len(t)==4:
        t[0].add(node(t[2]))
        if(t[3][0]=="["):
            t[0].add(node('[LIST]'))
        else:
            if(t[3][-1]=="]"):
                if(t[3][-2].isdigit()):
                    t[0].add(node('[LIST MEMBER]'))
                else:
                    t[0].add(node('[LIST VAR]'))
            else:
                if(t[3].isdigit()):
                    t[0].add(node('[INTERGER]'))
                else:
                    t[0].add(node('[VARIABLE]'))

        t[0].add(node(t[3]))
    if len(t)==7:
        t[0].add(node(t[2]))
        t[0].add(node('[Len Function]'))
        t[0].add(node(t[5]))
        
def p_class_assign(t):
    '''class_assign : SELFVAR '=' VARIABLE  '''
    t[0]=node('[CLASS_ASSIGN]')
    t[0].add(node(t[1]))
    t[0].add(node(t[3]))

def p_class_operation(t):
    ''' class_operation : SELFVAR '=' SELFVAR '+' VARIABLE '''
    t[0]=node('[CLASS_OPERATION]')
    t[0].add(node(t[1]))
    t[0].add(node('[EQUAL]'))
    t[0].add(node(t[3]))
    t[0].add(node('[PLUS]'))
    t[0].add(node(t[5]))

def p_operation(t):
    '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                 | VARIABLE '=' VARIABLE '-' VARIABLE'''
    if len(t)==6:
        t[0]=simple_node(t,'[OPERATION]')

def p_print(t):
    '''print : PRINT '(' VARIABLE ',' VARIABLE ')' '''
    t[0]=node('[PRINT]')
    t[0].add(node(t[3]))
    t[0].add(node(t[5]))
                
def p_if(t):
    r'''if : IF '(' condition ')' '{' statements '}' '''
    if len(t)==8:
        t[0]=node('[IF]')
        t[0].add(t[3])
        t[0].add(t[6])

def p_class(t):
    r'''class : CLASS VARIABLE '{' def_init def_add def_print '}' '''
    t[0]=node('[CLASS]')
    t[0].add(node(t[2]))
    t[0].add(t[4])
    t[0].add(t[5])
    t[0].add(t[6])

def p_def_init(t):
    r'''def_init : DEF init '(' SELF ',' VARIABLE ',' VARIABLE ',' VARIABLE ')' '{' class_assign class_assign class_assign '}' '''
    t[0]=node('[CLASS_INIT]')
    t[0].add(node(t[6]))
    t[0].add(node(t[8]))
    t[0].add(node(t[10]))
    t[0].add(t[13])
    t[0].add(t[14])
    t[0].add(t[15])


def p_def_add(t):
    r'''def_add : DEF add VARIABLE '(' SELF ',' VARIABLE ')' '{' class_operation '}' '''
    t[0]=node('[CLASS_ADD]')
    t[0].add(node(t[3]))
    t[0].add(t[10])

def p_def_print(t):
    r'''def_print : DEF defprint '(' SELF ')' '{' print '}' '''
    t[0]=node('[CLASS_PRINT]')
    t[0].add(t[7])

def p_classfunc0(t):
    r'''classfunc0 : VARIABLE '=' VARIABLE  '(' VARIABLE ',' NUMBER ',' NUMBER ')'  '''
    t[0]=node('[CLASS_CONSTRUCT]')
    t[0].add(node(t[1]))
    t[0].add(node('[CLASS_NAME]'))
    t[0].add(node(t[3]))
    t[0].add(node('[INPUT_PARA]'))
    t[0].add(node(t[5]))
    t[0].add(node(t[7]))
    t[0].add(node(t[9]))

def p_classfunc1(t):
    r'''classfunc1 : VARIABLE '.' add VARIABLE '(' NUMBER ')' '''
    t[0]=node('[MEMBERVAR_ADD]')
    t[0].add(node(t[1]))
    t[0].add(node('[MEMBERVAR_NAME]'))
    t[0].add(node(t[4]))
    t[0].add(node('[INPUT_PARA]'))
    t[0].add(node(t[6]))

def p_classfunc2(t):
    r''' classfunc2 : VARIABLE '.' defprint '(' ')' '''
    t[0]=node('[MEMBERVAR_PRINT]')
    t[0].add(node(t[1]))


def p_function(t):
    r'''function : DEF VARIABLE '(' VARIABLE ',' VARIABLE ',' VARIABLE ')' '{' statements '}' '''
    if len(t)==13:
        t[0]=node('[FUNCTION]')
        t[0].add(node('[FUNC_NAME]'))
        t[0].add(node(t[2]))
        t[0].add(node('[INPUT_VAR]'))
        t[0].add(node(t[4]))
        t[0].add(node(t[6]))
        t[0].add(node(t[8]))
        t[0].add(t[11])

def p_runfunction(t):
    r'''runfunction : VARIABLE '(' VARIABLE ',' VARIABLE ',' VARIABLE ')' '''
    if len(t)==9:
        t[0]=node('[RUNFUNCTION]')
        t[0].add(node('[FUNC_NAME]'))
        t[0].add(node(t[1]))
        t[0].add(node('[INPUT_VAR]'))
        t[0].add(node(t[3]))
        t[0].add(node(t[5]))
        t[0].add(node(t[7]))
        
    

def p_condition(t):
    '''condition : VARIABLE '<' VARIABLE AND VARIABLE '>' VARIABLE
                 | VARIABLE '<' VARIABLE AND VARIABLE '<' '=' VARIABLE
                 | VARIABLE '<' '=' VARIABLE
                 | VARIABLE '>' '=' VARIABLE
                 | VARIABLE '<' VARIABLE
                 | VARIABLE '>' VARIABLE'''

    if len(t)==4:
        t[0]=simple_node(t,'[SIMPLE_CONDITION]')
    if len(t)==5:
        t[0]=simple_node(t,'[ANOTHER_CONDITION]')
    if len(t)>=8:
        t[0]=simple_node(t,'[AND_CONDITION]')


def p_while(t):
    r'''while : WHILE '(' condition ')' '{' statements '}' '''
    if len(t)==8:
        t[0]=node('[WHILE]')
        t[0].add(t[3])
        t[0].add(t[6])
    
                
def p_error(t):
    print("Syntax error at '%s'" % t.value)

yacc.yacc()
