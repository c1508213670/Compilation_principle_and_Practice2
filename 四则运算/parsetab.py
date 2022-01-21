
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "NUMBER PRINT VARIABLEprogram : statementsstatements : statements statement\n                  | statement statement : assignment\n                  | operation\n                  | printassignment : VARIABLE '=' NUMBERoperation : VARIABLE '=' exprexpr  : expr '+' term\n             | expr '-' term\n             | termterm  : term '*' factor\n             | term '/' factor\n             | factorfactor  : VARIABLE\n               | NUMBERprint : PRINT '(' elements ')' elements : VARIABLE ',' elements\n                | VARIABLE"
    
_lr_action_items = {')':([12,13,25,],[19,-19,-18,]),'(':([3,],[10,]),'+':([14,15,16,17,18,26,27,28,29,30,],[-11,23,-16,-14,-15,-16,-12,-13,-9,-10,]),'*':([14,16,17,18,26,27,28,29,30,],[21,-16,-14,-15,-16,-12,-13,21,21,]),'-':([14,15,16,17,18,26,27,28,29,30,],[-11,24,-16,-14,-15,-16,-12,-13,-9,-10,]),'NUMBER':([11,21,22,23,24,],[16,26,26,26,26,]),'/':([14,16,17,18,26,27,28,29,30,],[22,-16,-14,-15,-16,-12,-13,22,22,]),',':([13,],[20,]),'PRINT':([0,1,2,6,7,8,9,14,15,16,17,18,19,26,27,28,29,30,],[3,3,-4,-3,-6,-5,-2,-11,-8,-7,-14,-15,-17,-16,-12,-13,-9,-10,]),'VARIABLE':([0,1,2,6,7,8,9,10,11,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,],[4,4,-4,-3,-6,-5,-2,13,18,-11,-8,-7,-14,-15,-17,13,18,18,18,18,-16,-12,-13,-9,-10,]),'=':([4,],[11,]),'$end':([1,2,5,6,7,8,9,14,15,16,17,18,19,26,27,28,29,30,],[-1,-4,0,-3,-6,-5,-2,-11,-8,-7,-14,-15,-17,-16,-12,-13,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([11,23,24,],[14,29,30,]),'elements':([10,20,],[12,25,]),'statements':([0,],[1,]),'assignment':([0,1,],[2,2,]),'factor':([11,21,22,23,24,],[17,27,28,17,17,]),'program':([0,],[5,]),'statement':([0,1,],[6,9,]),'expr':([11,],[15,]),'print':([0,1,],[7,7,]),'operation':([0,1,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','py_yacc.py',16),
  ('statements -> statements statement','statements',2,'p_statements','py_yacc.py',22),
  ('statements -> statement','statements',1,'p_statements','py_yacc.py',23),
  ('statement -> assignment','statement',1,'p_statement','py_yacc.py',33),
  ('statement -> operation','statement',1,'p_statement','py_yacc.py',34),
  ('statement -> print','statement',1,'p_statement','py_yacc.py',35),
  ('assignment -> VARIABLE = NUMBER','assignment',3,'p_assignment','py_yacc.py',41),
  ('operation -> VARIABLE = expr','operation',3,'p_operation','py_yacc.py',50),
  ('expr -> expr + term','expr',3,'p_expr','py_yacc.py',57),
  ('expr -> expr - term','expr',3,'p_expr','py_yacc.py',58),
  ('expr -> term','expr',1,'p_expr','py_yacc.py',59),
  ('term -> term * factor','term',3,'p_term','py_yacc.py',70),
  ('term -> term / factor','term',3,'p_term','py_yacc.py',71),
  ('term -> factor','term',1,'p_term','py_yacc.py',72),
  ('factor -> VARIABLE','factor',1,'p_factor','py_yacc.py',83),
  ('factor -> NUMBER','factor',1,'p_factor','py_yacc.py',84),
  ('print -> PRINT ( elements )','print',4,'p_print','py_yacc.py',93),
  ('elements -> VARIABLE , elements','elements',3,'p_elements','py_yacc.py',98),
  ('elements -> VARIABLE','elements',1,'p_elements','py_yacc.py',99),
]
