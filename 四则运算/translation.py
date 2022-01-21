#! /usr/bin/env python
#coding=utf-8
from __future__ import division

v_table={} # variable table

def getExpr(node):
    '''expr  : expr '+' term
             | expr '-' term
             | term'''
    leftNode = node.getchild(0)
    if(leftNode.getdata()=="[OPERATION_TERM]"):
        return getTerm(leftNode)

    op = node.getchild(1).getdata()
    rightNode=node.getchild(2)

    if(leftNode.getdata()=="[OPERATION_EXPR]" and rightNode.getdata()=="[OPERATION_TERM]"):
        if(op=='+'):
            return getExpr(leftNode) + getTerm(rightNode)
        else:
            return getExpr(leftNode) - getTerm(rightNode)

def getTerm(node):
    '''term  : term '*' factor
             | term '/' factor
             | factor'''
    leftNode=node.getchild(0)
    if(leftNode.getdata()=="[FACTOR]"):return getFactor(leftNode)

    op = node.getchild(1).getdata()
    rightNode=node.getchild(2)

    if(leftNode.getdata()=="[OPERATION_TERM]" and rightNode.getdata()=="[FACTOR]"):
        if(op=='*'):
            return getTerm(leftNode) * getFactor(rightNode)
        else:
            return getTerm(leftNode) / getFactor(rightNode)


def getFactor(node):
    '''factor  : VARIABLE
               | NUMBER'''
    nodeId = node.getchild(0)
    ValueId = node.getchild(1)
    if (nodeId.getdata() == "[NUMBER]"):
        return eval(ValueId.getdata())
    else:
        return v_table[ValueId.getdata()]

def getPrint(node):
    '''elements : VARIABLE ',' elements
                | VARIABLE'''
    nodeEle = node.getchild(0)
    print(nodeEle.getdata(),v_table[nodeEle.getdata()])
    if(node.getSize()==2):
        nodeNext=node.getchild(1)
        getPrint(nodeNext)

def update_v_table(name,value):
    v_table[name]=value

def getRecursion(node):
    if(node.getdata()=='[OPERATION]'):return 0;
    elif(node.getdata() == '[PRINT]'):return 0;
    else: return 1;

def trans(node):
    for c in node.getchildren():
        if(getRecursion(node)):
            trans(c)

    # Translation

    # Assignment
    if node.getdata()=='[ASSIGNMENT]':
        ''' statement : VARIABLE '=' NUMBER'''
        value=node.getchild(2).getvalue()
        node.getchild(0).setvalue(value)
        # update v_table
        update_v_table(node.getchild(0).getdata(),value)


    # Operation
    elif node.getdata() == '[OPERATION]':
        '''operation : VARIABLE '=' expr'''
        varNode=node.getchild(0)
        exprNode=node.getchild(2)

        # update v_table
        update_v_table(varNode.getdata(), getExpr(exprNode))
        
    # Print
    elif node.getdata()=='[PRINT]':
        getPrint(node.getchild(0))
   
        
        
            
            
        
        

