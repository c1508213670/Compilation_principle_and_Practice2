#! /usr/bin/env python
#coding=utf-8
from __future__ import division
from node import node

BREAK = 'BREAK'
RETURN = 'RETURN'

f_table={} # function table
class Translator():
    
    def __init__(self):
        self.v_table={} # variable table
        self.value = None # needed if RETURN was translated

    def translate(self,n: node):
        # Translation
        data = n.getdata()
        if data == '[PROGRAM]':
            self.translate(n[0])

        elif data == '[STATEMENTS]':
            for node in n:
                n.setvalue(self.translate(node))
                if n.getvalue() == BREAK or n.getvalue() == RETURN:
                    break

        elif data == '[STATEMENT]':
            if n[0].getdata() == 'BREAK':
                n.setvalue(BREAK)
            elif n[0].getdata() == '[RETURNSOMETHING]':
                n.setvalue(RETURN)
            else:
                n.setvalue(self.translate(n[0]))

        elif data == '[RETURNSOMETHING]':
            if len(n) == 1:
                n.setvalue(RETURN)
            elif len(n) == 2:
                self.value = self.translate(n[1])
                n.setvalue(RETURN)

        elif data == '[ASSIGNMENT]':
            if n[1].getdata() == '=':
                self.v_table[n[0].getvalue()] = self.translate(n[2])
            elif n[1].getdata() == 'MINUSEQUAL':
                self.v_table[n[0].getvalue()] -= self.translate(n[2])
            elif n[1].getdata() == 'PLUSEQUAL':
                self.v_table[n[0].getvalue()] += self.translate(n[2])
            elif n[1].getdata() == 'PLUSPLUS':
                self.v_table[n[0].getvalue()] += 1
            elif n[4].getdata() == '=':
                self.v_table[n[0].getvalue()][self.translate(n[2])] = self.translate(n[5])
            n.setvalue(self.v_table[n[0].getvalue()])

        elif data == '[EXPR]':
            if n[0].getdata() == '[TERM]':
                n.setvalue(self.translate(n[0]))
            elif n[1].getdata() == '+':
                n.setvalue(self.translate(n[0]) + self.translate(n[2]))
            elif n[1].getdata() == '-':
                n.setvalue(self.translate(n[0]) - self.translate(n[2]))
            elif n[1].getdata() == '[LIST]':
                n.setvalue(list(self.translate(n[1])))

        elif data == '[LIST]':
            if n[0].getdata() == '[EXPR]':
                n.setvalue([self.translate(n[0]), ])
            elif n[0].getdata() == '[LIST]':
                self.translate(n[0]).append(self.translate(n[2]))
                n.setvalue(n[0].getvalue())

        elif data == '[TERM]':
            if n[0].getdata() == '[FACTOR]':
                n.setvalue(self.translate(n[0]))
            elif n[1].getdata() == '*':
                n.setvalue(self.translate(n[0]) * self.translate(n[2]))
            elif n[1].getdata() == '/':
                n.setvalue(self.translate(n[0]) / self.translate(n[2]))
            elif n[1].getdata() == 'MOD':
                n.setvalue(self.translate(n[0]) // self.translate(n[2]))

        elif data == '[FACTOR]':
            if n[0].getdata() == 'NUMBER':
                n.setvalue(int(n[0].getvalue()))
            elif len(n) == 1:
                n.setvalue(self.v_table[n[0].getvalue()])
            elif n[0].getdata() == 'LEN':
                n.setvalue(len(self.v_table[n[2].getvalue()]))
            elif n[1].getdata() == '[EXPR]':
                n.setvalue(self.translate(n[1]))
            elif n[2].getdata() == 'NUMBER':
                n.setvalue(self.v_table[n[0].n[0].getvalue()][n[2].getvalue()])
            elif n[2].getdata() == 'VARIABLE':
                n.setvalue(self.v_table[n[0].getvalue()][self.v_table[n[2].getvalue()]])

        elif data == '[PRINT]':
            print(self.v_table[n[2].getvalue()])

        elif data == '[IF]':
            if self.translate(n[2]):
                n.setvalue(self.translate(n[5]))  # trace BREAK
            elif len(n) == 8:
                n.setvalue(self.translate(n[7]))
            else:
                n.setvalue(None)

        elif data == '[ELSES]':
            if n[0].getdata() == 'ELSE':
                n.setvalue(self.translate(n[2]))
            elif self.translate(n[2]):
                n.setvalue(self.translate(n[5]))
            elif len(n) == 8:
                n.setvalue(self.translate(n[7]))
            else:
                n.setvalue(None)

        elif data == '[WHILE]':
            n.setvalue(None)
            while self.translate(n[2]):
                status = self.translate(n[5])
                if status == BREAK:
                    break
                elif status == RETURN:
                    n.setvalue(status)
                    break

        elif data == '[FOR]':
            n.setvalue(None)
            self.translate(n[2])
            while self.translate(n[4]):
                status = self.translate(n[5])
                if status == BREAK:
                    break
                elif status == RETURN:
                    n.setvalue(status)
                    break
                else:
                    self.translate(n[6])

        elif data == '[CONDITIONS]':
            if len(n) == 1:
                n.setvalue(self.translate(n[0]))
            elif len(n) == 3:
                if self.translate(n[0]) and self.translate(n[2]):
                    n.setvalue(True)
                else:
                    n.setvalue(False)

        elif n.getdata() == '[CONDITION]':
            operator = n[1].getdata()
            if operator == '>':
                n.setvalue(self.translate(n[0]) > self.translate(n[2]))
            elif operator == 'LE':
                n.setvalue(self.translate(n[0]) >= self.translate(n[2]))
            elif operator == '<':
                n.setvalue(self.translate(n[0]) < self.translate(n[2]))
            elif operator == 'GE':
                n.setvalue(self.translate(n[0]) <= self.translate(n[2]))
                
        elif data=='[FUNCTION]':
            fname=n[1].getvalue()
            varList=self.translate(n[3])
            f_table[fname]=(varList,n[6]) # function_name : (variable_names, function)

        elif data=='[ARGS]':
            if n[0].getdata() == 'VARIABLE':
                n.setvalue([n[0].getvalue(),])
            elif n[0].getdata() == '[ARGS]':
                self.translate(n[0]).append(n[2].getvalue())
                n.setvalue(n[0].getvalue())
        
        elif data=='[RUNFUNCTION]':
            args,function = f_table[n[0].getvalue()]
            values = self.translate(n[2])
            
            t=Translator()
            t.v_table=dict(zip(args,values))
            t.translate(function)
            # function.clearvalue()
            # result = t.value
            print(t.v_table)
        
        return n.getvalue()
            
                
                
            
            

