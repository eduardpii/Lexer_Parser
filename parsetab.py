
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS termexpression : termterm : term TIMES factorterm : factorfactor : NUMBERfactor : LPAREN expression RPARENexpression : expression MINUS termterm : term DIVIDE factor'
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,9,],[4,4,4,4,4,4,]),'LPAREN':([0,5,6,7,8,9,],[5,5,5,5,5,5,]),'$end':([1,2,3,4,11,12,13,14,15,],[0,-2,-4,-5,-1,-7,-3,-8,-6,]),'PLUS':([1,2,3,4,10,11,12,13,14,15,],[6,-2,-4,-5,6,-1,-7,-3,-8,-6,]),'MINUS':([1,2,3,4,10,11,12,13,14,15,],[7,-2,-4,-5,7,-1,-7,-3,-8,-6,]),'RPAREN':([2,3,4,10,11,12,13,14,15,],[-2,-4,-5,15,-1,-7,-3,-8,-6,]),'TIMES':([2,3,4,11,12,13,14,15,],[8,-4,-5,8,8,-3,-8,-6,]),'DIVIDE':([2,3,4,11,12,13,14,15,],[9,-4,-5,9,9,-3,-8,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,],[1,10,]),'term':([0,5,6,7,],[2,2,11,12,]),'factor':([0,5,6,7,8,9,],[3,3,3,3,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parser_rules.py',5),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',9),
  ('term -> term TIMES factor','term',3,'p_term_times','parser_rules.py',13),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',17),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_rules.py',21),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser_rules.py',25),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parser_rules.py',32),
  ('term -> term DIVIDE factor','term',3,'p_term_divide','parser_rules.py',36),
]
