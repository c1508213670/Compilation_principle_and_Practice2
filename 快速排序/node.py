#! /usr/bin/env python
#coding=utf-8
from ply.lex import LexToken
from ply.yacc import YaccSymbol


class node(list):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._value = None

    def getdata(self):
        return self._data

    def setvalue(self, value):
        self._value = value

    def getvalue(self):
        return self._value

    def append(self, n):
        if isinstance(n, LexToken):
            assert isinstance(n.value, str)
            super().append(node(n.type))
            self[-1].setvalue(n.value)
        elif isinstance(n, YaccSymbol):
            assert isinstance(n.value, node)
            super().append(n.value)
        else:
            assert False

    def clearvalue(self):
        if len(self) == 0:
            return
        else:
            self._value = None
            for child in self:
                child.clearvalue()

    def print_node(self, prefix):
        print('  ' * prefix, '+', self._data if self._value is None else self._value)
        for child in self:
            child.print_node(prefix + 1)