#! /usr/bin/env python
#coding=utf-8
from __future__ import division
from __future__ import print_function

var_class_table={}
class_table={}
class_member={}
f_table={}
list_table={}

def getRecursion(node):
    if(node.getdata() == '[CLASS]'):return 1;
    else:return 1;

def classinit(node,name):
    para1=node.getchild(0).getdata()
    para2=node.getchild(1).getdata()
    para3=node.getchild(2).getdata()
    class_member[name]=[para1,para2,para3]

class Tran:

    
    def __init__(self):
        self.v_table={} # variable table
        self.value=0

    def update_v_table(self,name,value):
        self.v_table[name]=value

    def trans(self,node):

        
        # Translation
        r'''def_init : DEF init '(' SELF ',' VARIABLE ',' VARIABLE ',' VARIABLE ')' '{' class_assign class_assign class_assign '}' '''
        if node.getdata() == '[CLASS]':
            CLASS_NAME=node.getchild(0).getdata()
            CLASS_INIT=node.getchild(1)
            CLASS_ADD=node.getchild(2)
            CLASS_PRINT=node.getchild(3)
            classinit(CLASS_INIT,CLASS_NAME)

        if node.getdata() == '[CLASS_CONSTRUCT]':
            VAR_NAME=node.getchild(0).getdata()
            CLASS_NAME=node.getchild(2).getdata()
            PARA1=node.getchild(4).getdata()
            PARA2=node.getchild(5).getdata()
            PARA3=node.getchild(6).getdata()

            membervar_table = {}
            membervar_table[class_member[CLASS_NAME][0]]=PARA1
            membervar_table[class_member[CLASS_NAME][1]]=PARA2
            membervar_table[class_member[CLASS_NAME][2]]=PARA3


            var_class_table[VAR_NAME]=membervar_table

        if node.getdata() == '[MEMBERVAR_ADD]':
            VAR_NAME=node.getchild(0).getdata()
            MEMBERNAME=node.getchild(2).getdata()
            PARA=node.getchild(4).getdata()
            var_class_table[VAR_NAME][MEMBERNAME]=int(var_class_table[VAR_NAME][MEMBERNAME])+int(PARA)

        if node.getdata()=='[MEMBERVAR_PRINT]':
            VAR_NAME=node.getchild(0).getdata()
            print(var_class_table[VAR_NAME])



        # Assignment
        if node.getdata() == '[ASSIGNMENT]':
            ''' statement : VARIABLE '=' NUMBER'''
            if (node.getchild(0).getdata() == '[VARIABLE]'):
                targetVar = node.getchild(1).getdata()
            else:
                VarSlice = node.getchild(1).getdata().rstrip(']').split("[")
                ListName = VarSlice[0]
                if (VarSlice[1].isdigit()):
                    index = VarSlice[1]
                else:
                    index = self.v_table[VarSlice[1]]
                targetVar = ListName + "[" + str(index) + "]"

            if (node.getchild(3).getdata() == '[LIST]'):
                ListLen = node.getchild(4).getdata().count(',') + 1
                ListSlice = node.getchild(4).getdata().strip('[]').split(',')
                list_table[targetVar] = ListLen
                count = 0
                for i in ListSlice:
                    self.update_v_table(targetVar + "[" + str(count) + "]", eval(i))
                    count += 1
            if (node.getchild(3).getdata() == '[LIST VAR]'):
                TargetSlice = node.getchild(4).getdata().rstrip(']').split("[")
                TargetName = TargetSlice[0]
                Targetindex = self.v_table[TargetSlice[1]]
                value = self.v_table[TargetName + "[" + str(Targetindex) + "]"]
                self.update_v_table(targetVar, value)
            if (node.getchild(3).getdata() == '[LIST MEMBER]'):
                value = self.v_table[node.getchild(4).getdata()]
                self.update_v_table(targetVar, value)
            if (node.getchild(3).getdata() == '[Len Function]'):
                LenTarget = node.getchild(4).getdata()
                self.update_v_table(targetVar, list_table[LenTarget])
            if (node.getchild(3).getdata() == '[INTERGER]'):
                value = eval(node.getchild(4).getdata())
                self.update_v_table(targetVar, value)
            if (node.getchild(3).getdata() == '[VARIABLE]'):
                value = self.v_table[node.getchild(4).getdata()]
                self.update_v_table(targetVar, value)
            

            
        
        # Operation
        elif node.getdata()=='[OPERATION]':
            '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                         | VARIABLE '=' VARIABLE '-' VARIABLE'''
            arg0=self.v_table[node.getchild(2).getdata()]
            arg1=self.v_table[node.getchild(4).getdata()]
            op=node.getchild(3).getdata()
            
            if op=='+':
                value=arg0+arg1
            else:
                value=arg0-arg1
            
            node.getchild(0).setvalue(value)
            # update v_table
            self.update_v_table(node.getchild(0).getdata(),value)
            
          
            
        # Print
        elif node.getdata() == '[PWQRINT]':
            '''print : PRINT '(' VARIABLE ')' '''
            if (node.getchild(2).getdata() in list_table):
                ListName = node.getchild(2).getdata()
                Lenlist = list_table[ListName]
                count = 0
                print(ListName + "=" + "[", end='')
                while (count < Lenlist):
                    print(self.v_table[ListName + "[" + str(count) + ']'], end=',')
                    count += 1
                print(']')
            else:
                arg0 = self.v_table[node.getchild(2).getdata()]
                print(arg0)
        
        # If
        elif node.getdata()=='[IF]':
            r'''if : IF '(' condition ')' '{' statements '}' '''
            children=node.getchildren()
            self.trans(children[0])
            condition=children[0].getvalue()
            if condition:
                self.value=1

                    
        # While
        elif node.getdata() == '[CONDITION]':
            '''condition : VARIABLE '>' VARIABLE
                         | VARIABLE '<' VARIABLE'''

            if (node.getchild(0).getdata()[-1] == "]"):
                TargetSlice = node.getchild(0).getdata().rstrip(']').split("[")
                TargetName = TargetSlice[0]
                Targetindex = self.v_table[TargetSlice[1]]
                value = self.v_table[TargetName + "[" + str(Targetindex) + "]"]
                arg0 = value
            else:
                arg0 = self.v_table[node.getchild(0).getdata()]
            arg1 = self.v_table[node.getchild(2).getdata()]
            op = node.getchild(1).getdata()
            if op == '>':
                node.setvalue(arg0 > arg1)
            elif op == '<':
                node.setvalue(arg0 < arg1)
                
                    
        # Condition
        elif node.getdata()=='[SIMPLE_CONDITION]':
            '''condition : VARIABLE '>' VARIABLE
                         | VARIABLE '<' VARIABLE'''
            
            arg0=self.v_table[node.getchild(0).getdata()]
            arg1=self.v_table[node.getchild(2).getdata()]
            op=node.getchild(1).getdata()
            if op=='>':
                node.setvalue(arg0>arg1)
            elif op=='<':
                node.setvalue(arg0<arg1)
                
        elif node.getdata()=='[FUNCTION]':
            r'''function : DEF VARIABLE '(' VARIABLE ',' VARIABLE ',' VARIABLE ')' '{' statements '}' '''

            fname=node.getchild(1).getdata()
            vname=[node.getchild(3).getdata(),node.getchild(4).getdata(),node.getchild(5).getdata()]
            f_table[fname]=(vname,node.getchild(6)) # function_name : (variable_names, function)
        
        elif node.getdata()=='[RUNFUNCTION]':
            r'''runfunction : VARIABLE '(' VARIABLE ',' VARIABLE ',' VARIABLE ')' '''
        
            fname=node.getchild(1).getdata()
            vname1=[node.getchild(3).getdata(),node.getchild(4).getdata(),node.getchild(5).getdata()]
            
            vname0,fnode=f_table[fname]
            
            t=Tran()
            for i in range(0,len(vname1)):
                t.v_table[vname0[i]]=self.v_table[vname1[i]]

            t.trans(fnode.getchildren()[0])
            ##t.trans(ifNode)
            if(t.value!=1):
                for c in fnode.getchildren()[1:]:
                    t.trans(c)
            print(t.v_table)

        elif node.getdata()=='[RETURN]':
            print(self.v_table)
            print(f_table)

        else:
            for c in node.getchildren():
                    if(getRecursion(c)):
                        self.trans(c)
        
        return node.getvalue()
            
                
                
            
            

