
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BREAK CLASS COMMA DEF DIVIDE DMINUS DOT DPLUS EDIVIDE ELIF ELSE EQ FOR GE GT ID IF LBRACE LBRACKET LE LEN LPAREN LT MINEQUAL MINUS NE NUMBER OR PLUS PLUSEQUAL PRINT RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES WHILEprogram : statementsstatements : statements statement\n                  | statement statement : assignment\n                  | expr\n                  | print\n                  | if\n                  | while\n                  | for\n                  | break\n                  | function\n                  | class\n                  | returnassignment : variable ASSIGN expr\n                  | variable MINEQUAL expr\n                  | variable PLUSEQUAL expr\n                  | variable DPLUS\n                  | variable DMINUSvariable : variable LBRACKET expr RBRACKET\n                | ID DOT ID\n                | IDexpr : expr PLUS term\n            | expr MINUS term\n            | term\n            | string\n            | arrayterm : term TIMES factor\n            | term DIVIDE factor\n            | term EDIVIDE factor\n            | factorfactor : variable\n              | NUMBER\n              | len\n              | call\n              | LPAREN expr RPAREN exprs : exprs COMMA expr\n             | exprlen : LEN LPAREN variable RPARENprint : PRINT LPAREN exprs RPAREN\n             | PRINT LPAREN RPARENarray : LBRACKET exprs RBRACKET\n             | LBRACKET RBRACKETcondition : condition OR join\n                 | joinjoin : join AND equality\n            | equalityequality : equality EQ rel\n                | equality NE rel\n                | relrel : expr LT expr\n           | expr LE expr\n           | expr GT expr\n           | expr GE expr\n           | exprif : IF LPAREN condition RPAREN LBRACE statements RBRACE\n          | IF LPAREN condition RPAREN LBRACE statements RBRACE elseelse : ELIF LPAREN condition RPAREN LBRACE statements RBRACE\n            | ELIF LPAREN condition RPAREN LBRACE statements RBRACE else\n            | ELSE LBRACE statements RBRACEwhile : WHILE LPAREN condition RPAREN LBRACE statements RBRACEfor : FOR LPAREN assignment SEMICOLON condition SEMICOLON assignment RPAREN LBRACE statements RBRACEbreak : BREAKfunction : DEF ID LPAREN args RPAREN LBRACE statements RBRACE\n                | DEF ID LPAREN RPAREN LBRACE statements RBRACEargs : args COMMA ID\n            | IDcall : ID LPAREN exprs RPAREN\n            | ID LPAREN RPAREN\n            | ID DOT ID LPAREN exprs RPAREN\n            | ID DOT ID LPAREN RPARENreturn : RETURN\n              | RETURN exprsclass : CLASS ID LBRACE functions RBRACEfunctions : functions function\n                 | functionstring : STRING'
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,18,18,18,-70,-73,18,18,18,18,-69,-55,-60,18,-64,-56,-63,18,18,18,18,-59,-61,18,18,-57,-58,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,20,20,20,-70,-73,20,20,20,20,-69,-55,-60,20,-64,-56,-63,20,20,20,20,-59,-61,20,20,-57,-58,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,21,21,21,-70,-73,21,21,21,21,-69,-55,-60,21,-64,-56,-63,21,21,21,21,-59,-61,21,21,-57,-58,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,22,22,22,-70,-73,22,22,22,22,-69,-55,-60,22,-64,-56,-63,22,22,22,22,-59,-61,22,22,-57,-58,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,23,23,23,-70,-73,23,23,23,23,-69,-55,-60,23,-64,-56,-63,23,23,23,23,-59,-61,23,23,-57,-58,]),'DEF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,87,89,91,92,109,110,111,112,113,114,123,128,130,131,132,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,24,-41,-19,-39,-67,24,-75,-36,-38,24,24,24,-70,-73,-74,24,24,24,24,-69,-55,-60,24,-64,-56,-63,24,24,24,24,-59,-61,24,24,-57,-58,]),'CLASS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,26,26,26,-70,-73,26,26,26,26,-69,-55,-60,26,-64,-56,-63,26,26,26,26,-59,-61,26,26,-57,-58,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,151,152,154,155,157,158,159,160,161,162,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,27,27,27,-70,-73,27,27,27,27,-69,-55,-60,27,-64,-56,-63,27,27,27,27,-59,-61,27,27,-57,-58,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,54,55,57,58,60,61,62,63,64,65,66,68,69,70,72,73,83,84,86,88,89,91,92,94,95,96,97,98,99,100,101,103,104,108,109,112,113,114,123,127,128,130,131,133,134,135,136,138,139,140,141,143,144,145,149,150,151,152,154,155,157,158,159,160,161,162,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,25,-62,53,-21,56,25,25,-30,-76,-32,-33,-34,-2,25,25,25,25,25,-17,-18,25,25,25,25,25,-31,25,25,82,84,25,-72,-37,-42,82,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,105,-20,-68,25,-41,-19,-39,25,25,25,25,25,25,25,25,25,125,25,-67,-36,-38,25,25,137,25,-70,-73,25,25,82,25,25,-69,-55,-60,25,-64,-56,-63,25,25,25,25,25,-59,-61,25,25,-57,-58,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,23,25,27,28,29,30,31,32,33,35,38,39,40,41,42,43,47,49,50,51,55,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,88,89,91,92,94,95,96,97,98,99,100,101,103,108,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,150,151,152,154,155,157,158,159,160,161,162,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,30,-62,-21,30,30,-30,-76,-32,-33,-34,-2,30,30,30,-17,-18,30,30,-31,30,30,30,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,30,-41,-19,-39,30,30,30,30,30,30,30,30,30,30,-67,-36,-38,30,30,30,-70,-73,30,30,30,30,-69,-55,-60,30,-64,-56,-63,30,30,30,30,30,-59,-61,30,30,-57,-58,]),'LBRACKET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,23,25,27,28,29,30,31,32,33,35,38,39,40,41,42,43,47,49,50,51,55,57,58,60,62,63,64,65,66,68,69,70,72,73,81,82,84,86,88,89,90,91,92,94,95,96,97,98,99,100,101,103,108,109,112,113,114,123,125,128,130,131,133,134,136,138,139,140,141,143,144,145,149,150,151,152,154,155,157,158,159,160,161,162,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,43,-24,-25,-26,28,-62,-21,28,28,-30,-76,-32,-33,-34,-2,28,28,28,-17,-18,28,28,43,28,28,28,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,43,-21,-20,-68,28,-41,43,-19,-39,28,28,28,28,28,28,28,28,28,28,-67,-36,-38,28,28,-20,28,-70,-73,28,28,28,28,-69,-55,-60,28,-64,-56,-63,28,28,28,28,28,-59,-61,28,28,-57,-58,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,23,25,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,55,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,88,89,91,92,94,95,96,97,98,99,100,101,103,108,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,150,151,152,154,155,157,158,159,160,161,162,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,31,-62,-21,31,31,-30,-76,-32,-33,-34,-2,31,31,31,31,31,-17,-18,31,31,31,31,31,-31,31,31,31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,31,-41,-19,-39,31,31,31,31,31,31,31,31,31,31,-67,-36,-38,31,31,31,-70,-73,31,31,31,31,-69,-55,-60,31,-64,-56,-63,31,31,31,31,31,-59,-61,31,31,-57,-58,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,53,55,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,88,89,91,92,94,95,96,97,98,99,100,101,103,108,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,146,149,150,151,152,154,155,157,158,159,160,161,162,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,47,19,50,51,52,-62,55,19,19,-30,-76,-32,-33,-34,61,-2,19,19,19,19,19,-17,-18,19,19,19,19,19,-31,19,19,83,19,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,108,-68,19,-41,-19,-39,19,19,19,19,19,19,19,19,19,19,-67,-36,-38,19,19,19,-70,-73,19,19,19,19,-69,-55,-60,19,-64,-56,150,-63,19,19,19,19,19,-59,-61,19,19,-57,-58,]),'LEN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,23,25,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,55,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,88,89,91,92,94,95,96,97,98,99,100,101,103,108,109,112,113,114,123,128,130,131,133,134,136,138,139,140,141,143,144,145,149,150,151,152,154,155,157,158,159,160,161,162,],[34,34,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,34,-62,-21,34,34,-30,-76,-32,-33,-34,-2,34,34,34,34,34,-17,-18,34,34,34,34,34,-31,34,34,34,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,34,-41,-19,-39,34,34,34,34,34,34,34,34,34,34,-67,-36,-38,34,34,34,-70,-73,34,34,34,34,-69,-55,-60,34,-64,-56,-63,34,34,34,34,34,-59,-61,34,34,-57,-58,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,112,113,130,131,139,140,141,144,145,149,157,158,161,162,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,-36,-38,-70,-73,-69,-55,-60,-64,-56,-63,-59,-61,-57,-58,]),'RBRACE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23,25,27,29,30,31,32,33,35,41,42,49,57,58,60,62,63,64,65,66,68,69,70,72,73,84,86,89,91,92,109,110,111,112,113,130,131,132,133,134,138,139,140,141,143,144,145,149,154,155,157,158,160,161,162,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-31,-24,-25,-26,-62,-21,-71,-30,-76,-32,-33,-34,-2,-17,-18,-31,-72,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,-40,-35,-20,-68,-41,-19,-39,-67,131,-75,-36,-38,-70,-73,-74,140,141,144,-69,-55,-60,149,-64,-56,-63,157,158,-59,-61,161,-57,-58,]),'PLUS':([5,14,15,16,17,25,29,30,31,32,33,48,49,58,60,62,63,64,65,66,67,68,69,70,73,78,84,86,89,91,109,112,113,119,120,121,122,130,139,],[36,-31,-24,-25,-26,-21,-30,-76,-32,-33,-34,36,-31,36,-42,-22,-23,36,36,36,36,-27,-28,-29,-35,36,-20,-68,-41,-19,-67,36,-38,36,36,36,36,-70,-69,]),'MINUS':([5,14,15,16,17,25,29,30,31,32,33,48,49,58,60,62,63,64,65,66,67,68,69,70,73,78,84,86,89,91,109,112,113,119,120,121,122,130,139,],[37,-31,-24,-25,-26,-21,-30,-76,-32,-33,-34,37,-31,37,-42,-22,-23,37,37,37,37,-27,-28,-29,-35,37,-20,-68,-41,-19,-67,37,-38,37,37,37,37,-70,-69,]),'ASSIGN':([14,25,81,82,84,91,125,],[38,-21,38,-21,-20,-19,-20,]),'MINEQUAL':([14,25,81,82,84,91,125,],[39,-21,39,-21,-20,-19,-20,]),'PLUSEQUAL':([14,25,81,82,84,91,125,],[40,-21,40,-21,-20,-19,-20,]),'DPLUS':([14,25,81,82,84,91,125,],[41,-21,41,-21,-20,-19,-20,]),'DMINUS':([14,25,81,82,84,91,125,],[42,-21,42,-21,-20,-19,-20,]),'TIMES':([14,15,25,29,31,32,33,49,62,63,68,69,70,73,84,86,91,109,113,130,139,],[-31,44,-21,-30,-32,-33,-34,-31,44,44,-27,-28,-29,-35,-20,-68,-19,-67,-38,-70,-69,]),'DIVIDE':([14,15,25,29,31,32,33,49,62,63,68,69,70,73,84,86,91,109,113,130,139,],[-31,45,-21,-30,-32,-33,-34,-31,45,45,-27,-28,-29,-35,-20,-68,-19,-67,-38,-70,-69,]),'EDIVIDE':([14,15,25,29,31,32,33,49,62,63,68,69,70,73,84,86,91,109,113,130,139,],[-31,46,-21,-30,-32,-33,-34,-31,46,46,-27,-28,-29,-35,-20,-68,-19,-67,-38,-70,-69,]),'RPAREN':([15,16,17,25,29,30,31,32,33,41,42,47,48,49,55,58,60,62,63,64,65,66,68,69,70,71,73,74,75,76,77,78,79,82,83,84,85,86,89,90,91,105,106,108,109,112,113,115,116,117,118,119,120,121,122,125,129,130,137,139,142,153,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-17,-18,72,73,-31,86,-37,-42,-22,-23,-14,-15,-16,-27,-28,-29,92,-35,93,-44,-46,-49,-54,102,-21,107,-20,109,-68,-41,113,-19,-66,126,130,-67,-36,-38,-43,-45,-47,-48,-50,-51,-52,-53,-20,139,-70,-65,-69,148,156,]),'COMMA':([15,16,17,25,29,30,31,32,33,49,57,58,59,60,62,63,68,69,70,71,73,84,85,86,89,91,105,106,109,112,113,129,130,137,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,88,-37,88,-42,-22,-23,-27,-28,-29,88,-35,-20,88,-68,-41,-19,-66,127,-67,-36,-38,88,-70,-65,-69,]),'RBRACKET':([15,16,17,25,28,29,30,31,32,33,49,58,59,60,62,63,67,68,69,70,73,84,86,89,91,109,112,113,130,139,],[-24,-25,-26,-21,60,-30,-76,-32,-33,-34,-31,-37,89,-42,-22,-23,91,-27,-28,-29,-35,-20,-68,-41,-19,-67,-36,-38,-70,-69,]),'SEMICOLON':([15,16,17,25,29,30,31,32,33,41,42,49,60,62,63,64,65,66,68,69,70,73,75,76,77,78,80,84,86,89,91,109,113,115,116,117,118,119,120,121,122,124,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-17,-18,-31,-42,-22,-23,-14,-15,-16,-27,-28,-29,-35,-44,-46,-49,-54,103,-20,-68,-41,-19,-67,-38,-43,-45,-47,-48,-50,-51,-52,-53,135,-70,-69,]),'LT':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,78,84,86,89,91,109,113,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,98,-20,-68,-41,-19,-67,-38,-70,-69,]),'LE':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,78,84,86,89,91,109,113,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,99,-20,-68,-41,-19,-67,-38,-70,-69,]),'GT':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,78,84,86,89,91,109,113,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,100,-20,-68,-41,-19,-67,-38,-70,-69,]),'GE':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,78,84,86,89,91,109,113,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,101,-20,-68,-41,-19,-67,-38,-70,-69,]),'EQ':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,76,77,78,84,86,89,91,109,113,116,117,118,119,120,121,122,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,96,-49,-54,-20,-68,-41,-19,-67,-38,96,-47,-48,-50,-51,-52,-53,-70,-69,]),'NE':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,76,77,78,84,86,89,91,109,113,116,117,118,119,120,121,122,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,97,-49,-54,-20,-68,-41,-19,-67,-38,97,-47,-48,-50,-51,-52,-53,-70,-69,]),'AND':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,75,76,77,78,84,86,89,91,109,113,115,116,117,118,119,120,121,122,130,139,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,95,-46,-49,-54,-20,-68,-41,-19,-67,-38,95,-45,-47,-48,-50,-51,-52,-53,-70,-69,]),'OR':([15,16,17,25,29,30,31,32,33,49,60,62,63,68,69,70,73,74,75,76,77,78,79,84,86,89,91,109,113,115,116,117,118,119,120,121,122,124,130,139,153,],[-24,-25,-26,-21,-30,-76,-32,-33,-34,-31,-42,-22,-23,-27,-28,-29,-35,94,-44,-46,-49,-54,94,-20,-68,-41,-19,-67,-38,-43,-45,-47,-48,-50,-51,-52,-53,94,-70,-69,94,]),'DOT':([25,82,],[54,104,]),'LBRACE':([56,93,102,107,126,147,148,156,],[87,114,123,128,136,151,152,159,]),'ELIF':([140,161,],[146,146,]),'ELSE':([140,161,],[147,147,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,114,123,128,136,151,152,159,],[2,133,134,138,143,154,155,160,]),'statement':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[3,35,3,3,3,35,35,3,35,35,3,3,35,35,3,35,]),'assignment':([0,2,52,114,123,128,133,134,135,136,138,143,151,152,154,155,159,160,],[4,4,80,4,4,4,4,4,142,4,4,4,4,4,4,4,4,4,]),'expr':([0,2,19,27,28,38,39,40,43,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[5,5,48,58,58,64,65,66,67,58,78,78,58,112,78,78,78,78,119,120,121,122,78,58,5,5,5,5,5,5,5,5,78,5,5,5,5,5,5,]),'print':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'if':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'while':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'for':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'break':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'function':([0,2,87,110,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[11,11,111,132,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'class':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'return':([0,2,114,123,128,133,134,136,138,143,151,152,154,155,159,160,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'variable':([0,2,19,27,28,36,37,38,39,40,43,44,45,46,47,50,51,52,55,61,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,135,136,138,143,150,151,152,154,155,159,160,],[14,14,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,81,49,90,49,49,49,49,49,49,49,49,49,49,49,14,14,14,14,14,81,14,14,14,49,14,14,14,14,14,14,]),'term':([0,2,19,27,28,36,37,38,39,40,43,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[15,15,15,15,15,62,63,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'string':([0,2,19,27,28,38,39,40,43,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'array':([0,2,19,27,28,38,39,40,43,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'factor':([0,2,19,27,28,36,37,38,39,40,43,44,45,46,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[29,29,29,29,29,29,29,29,29,29,29,68,69,70,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'len':([0,2,19,27,28,36,37,38,39,40,43,44,45,46,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'call':([0,2,19,27,28,36,37,38,39,40,43,44,45,46,47,50,51,55,88,94,95,96,97,98,99,100,101,103,108,114,123,128,133,134,136,138,143,150,151,152,154,155,159,160,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'exprs':([27,28,47,55,108,],[57,59,71,85,129,]),'condition':([50,51,103,150,],[74,79,124,153,]),'join':([50,51,94,103,150,],[75,75,115,75,75,]),'equality':([50,51,94,95,103,150,],[76,76,76,116,76,76,]),'rel':([50,51,94,95,96,97,103,150,],[77,77,77,77,117,118,77,77,]),'args':([83,],[106,]),'functions':([87,],[110,]),'else':([140,161,],[145,162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','py_yacc.py',48),
  ('statements -> statements statement','statements',2,'p_statements','py_yacc.py',55),
  ('statements -> statement','statements',1,'p_statements','py_yacc.py',56),
  ('statement -> assignment','statement',1,'p_statement','py_yacc.py',67),
  ('statement -> expr','statement',1,'p_statement','py_yacc.py',68),
  ('statement -> print','statement',1,'p_statement','py_yacc.py',69),
  ('statement -> if','statement',1,'p_statement','py_yacc.py',70),
  ('statement -> while','statement',1,'p_statement','py_yacc.py',71),
  ('statement -> for','statement',1,'p_statement','py_yacc.py',72),
  ('statement -> break','statement',1,'p_statement','py_yacc.py',73),
  ('statement -> function','statement',1,'p_statement','py_yacc.py',74),
  ('statement -> class','statement',1,'p_statement','py_yacc.py',75),
  ('statement -> return','statement',1,'p_statement','py_yacc.py',76),
  ('assignment -> variable ASSIGN expr','assignment',3,'p_assignment','py_yacc.py',83),
  ('assignment -> variable MINEQUAL expr','assignment',3,'p_assignment','py_yacc.py',84),
  ('assignment -> variable PLUSEQUAL expr','assignment',3,'p_assignment','py_yacc.py',85),
  ('assignment -> variable DPLUS','assignment',2,'p_assignment','py_yacc.py',86),
  ('assignment -> variable DMINUS','assignment',2,'p_assignment','py_yacc.py',87),
  ('variable -> variable LBRACKET expr RBRACKET','variable',4,'p_variable','py_yacc.py',100),
  ('variable -> ID DOT ID','variable',3,'p_variable','py_yacc.py',101),
  ('variable -> ID','variable',1,'p_variable','py_yacc.py',102),
  ('expr -> expr PLUS term','expr',3,'p_expr','py_yacc.py',120),
  ('expr -> expr MINUS term','expr',3,'p_expr','py_yacc.py',121),
  ('expr -> term','expr',1,'p_expr','py_yacc.py',122),
  ('expr -> string','expr',1,'p_expr','py_yacc.py',123),
  ('expr -> array','expr',1,'p_expr','py_yacc.py',124),
  ('term -> term TIMES factor','term',3,'p_term','py_yacc.py',136),
  ('term -> term DIVIDE factor','term',3,'p_term','py_yacc.py',137),
  ('term -> term EDIVIDE factor','term',3,'p_term','py_yacc.py',138),
  ('term -> factor','term',1,'p_term','py_yacc.py',139),
  ('factor -> variable','factor',1,'p_factor','py_yacc.py',151),
  ('factor -> NUMBER','factor',1,'p_factor','py_yacc.py',152),
  ('factor -> len','factor',1,'p_factor','py_yacc.py',153),
  ('factor -> call','factor',1,'p_factor','py_yacc.py',154),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','py_yacc.py',155),
  ('exprs -> exprs COMMA expr','exprs',3,'p_exprs','py_yacc.py',170),
  ('exprs -> expr','exprs',1,'p_exprs','py_yacc.py',171),
  ('len -> LEN LPAREN variable RPAREN','len',4,'p_len','py_yacc.py',183),
  ('print -> PRINT LPAREN exprs RPAREN','print',4,'p_print','py_yacc.py',193),
  ('print -> PRINT LPAREN RPAREN','print',3,'p_print','py_yacc.py',194),
  ('array -> LBRACKET exprs RBRACKET','array',3,'p_array','py_yacc.py',209),
  ('array -> LBRACKET RBRACKET','array',2,'p_array','py_yacc.py',210),
  ('condition -> condition OR join','condition',3,'p_condition','py_yacc.py',223),
  ('condition -> join','condition',1,'p_condition','py_yacc.py',224),
  ('join -> join AND equality','join',3,'p_join','py_yacc.py',236),
  ('join -> equality','join',1,'p_join','py_yacc.py',237),
  ('equality -> equality EQ rel','equality',3,'p_equality','py_yacc.py',249),
  ('equality -> equality NE rel','equality',3,'p_equality','py_yacc.py',250),
  ('equality -> rel','equality',1,'p_equality','py_yacc.py',251),
  ('rel -> expr LT expr','rel',3,'p_rel','py_yacc.py',263),
  ('rel -> expr LE expr','rel',3,'p_rel','py_yacc.py',264),
  ('rel -> expr GT expr','rel',3,'p_rel','py_yacc.py',265),
  ('rel -> expr GE expr','rel',3,'p_rel','py_yacc.py',266),
  ('rel -> expr','rel',1,'p_rel','py_yacc.py',267),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE','if',7,'p_if','py_yacc.py',279),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE else','if',8,'p_if','py_yacc.py',280),
  ('else -> ELIF LPAREN condition RPAREN LBRACE statements RBRACE','else',7,'p_else','py_yacc.py',295),
  ('else -> ELIF LPAREN condition RPAREN LBRACE statements RBRACE else','else',8,'p_else','py_yacc.py',296),
  ('else -> ELSE LBRACE statements RBRACE','else',4,'p_else','py_yacc.py',297),
  ('while -> WHILE LPAREN condition RPAREN LBRACE statements RBRACE','while',7,'p_while','py_yacc.py',318),
  ('for -> FOR LPAREN assignment SEMICOLON condition SEMICOLON assignment RPAREN LBRACE statements RBRACE','for',11,'p_for','py_yacc.py',331),
  ('break -> BREAK','break',1,'p_break','py_yacc.py',348),
  ('function -> DEF ID LPAREN args RPAREN LBRACE statements RBRACE','function',8,'p_function','py_yacc.py',355),
  ('function -> DEF ID LPAREN RPAREN LBRACE statements RBRACE','function',7,'p_function','py_yacc.py',356),
  ('args -> args COMMA ID','args',3,'p_args','py_yacc.py',379),
  ('args -> ID','args',1,'p_args','py_yacc.py',380),
  ('call -> ID LPAREN exprs RPAREN','call',4,'p_call','py_yacc.py',392),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','py_yacc.py',393),
  ('call -> ID DOT ID LPAREN exprs RPAREN','call',6,'p_call','py_yacc.py',394),
  ('call -> ID DOT ID LPAREN RPAREN','call',5,'p_call','py_yacc.py',395),
  ('return -> RETURN','return',1,'p_return','py_yacc.py',425),
  ('return -> RETURN exprs','return',2,'p_return','py_yacc.py',426),
  ('class -> CLASS ID LBRACE functions RBRACE','class',5,'p_class','py_yacc.py',437),
  ('functions -> functions function','functions',2,'p_functions','py_yacc.py',448),
  ('functions -> function','functions',1,'p_functions','py_yacc.py',449),
  ('string -> STRING','string',1,'p_string','py_yacc.py',460),
]
