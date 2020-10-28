
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left=PLUSASSIGNMINASSIGNMULTASSIGNDIVASSIGNleft+-MPLUSMMINUSleft*/MMLTPMDIVright-left'BREAK CONTINUE DIVASSIGN ELSE EQ EYE FLOATNUM GTEQ ID IF INTNUM LTEQ MDIV MINASSIGN MMINUS MMLTP MPLUS MULTASSIGN NEQ ONES PLUSASSIGN PRINT RETURN STRING THEN WHILE ZEROSstart : expr ';'\n             | block \n             | start expr ';'\n             | start blockexpr : INTNUM\n            | FLOATNUMexpr : IDexpr : '(' expr ')'expr : '-' exprexpr : expr '\\''array_interior : expr ',' array_interior\n                      | exprexpr : '[' array_interior ']'expr : ID '=' expr\n            | ID PLUSASSIGN expr\n            | ID MINASSIGN expr\n            | ID MULTASSIGN expr\n            | ID DIVASSIGN exprexpr : ID '[' INTNUM ']' '=' expr\n            | ID '[' INTNUM ']' PLUSASSIGN expr\n            | ID '[' INTNUM ']' MINASSIGN expr\n            | ID '[' INTNUM ']' MULTASSIGN expr    \n            | ID '[' INTNUM ']' DIVASSIGN exprexpr : ID '[' INTNUM ',' INTNUM ']' '=' expr\n            | ID '[' INTNUM ',' INTNUM ']' PLUSASSIGN expr\n            | ID '[' INTNUM ',' INTNUM ']' MINASSIGN expr\n            | ID '[' INTNUM ',' INTNUM ']' MULTASSIGN expr    \n            | ID '[' INTNUM ',' INTNUM ']' DIVASSIGN exprexpr : ID '=' ZEROS '(' INTNUM ')'\n            | ID '=' ONES '(' INTNUM ')'\n            | ID '=' EYE '(' INTNUM ')'expr : expr '+' expr\n            | expr '-' expr\n            | expr '*' expr\n            | expr '/' exprexpr : expr MPLUS expr\n            | expr MMINUS expr\n            | expr MMLTP expr\n            | expr MDIV exprexpr : expr EQ expr\n            | expr NEQ expr\n            | expr GTEQ expr\n            | expr LTEQ expr\n            | expr '>' expr\n            | expr '<' exprblock : expr ';'\n             | '{' '}'\n             | '{' start '}'\n             | while_block\n             | if_blockwhile_block : WHILE '(' expr ')' blockif_block : IF '(' expr ')' blockelse_block : ELSE block"
    
_lr_action_items = {'INTNUM':([0,1,3,7,8,9,10,11,12,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,44,45,46,47,73,74,77,78,79,81,83,84,88,89,90,91,92,95,96,106,107,108,109,110,111,],[4,4,-2,4,4,4,4,-49,-50,-4,-1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,70,-47,4,4,4,-3,4,-48,85,86,87,93,4,4,4,4,4,4,4,-51,-52,-46,4,4,4,4,4,]),'FLOATNUM':([0,1,3,7,8,9,10,11,12,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,44,45,46,47,73,74,83,84,88,89,90,91,92,95,96,106,107,108,109,110,111,],[5,5,-2,5,5,5,5,-49,-50,-4,-1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-47,5,5,5,-3,5,-48,5,5,5,5,5,5,5,-51,-52,-46,5,5,5,5,5,]),'ID':([0,1,3,7,8,9,10,11,12,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,44,45,46,47,73,74,83,84,88,89,90,91,92,95,96,106,107,108,109,110,111,],[6,6,-2,6,6,6,6,-49,-50,-4,-1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-47,6,6,6,-3,6,-48,6,6,6,6,6,6,6,-51,-52,-46,6,6,6,6,6,]),'(':([0,1,3,7,8,9,10,11,12,13,14,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,44,45,46,47,63,64,65,73,74,83,84,88,89,90,91,92,95,96,106,107,108,109,110,111,],[7,7,-2,7,7,7,7,-49,-50,45,46,-4,-1,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-47,7,7,7,-3,77,78,79,7,-48,7,7,7,7,7,7,7,-51,-52,-46,7,7,7,7,7,]),'-':([0,1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,73,74,75,76,83,84,88,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,111,112,113,114,115,116,],[8,8,20,-2,-5,-6,-7,8,8,8,8,-49,-50,20,-4,-1,-10,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,20,-9,20,-47,8,8,8,-3,-32,-33,-34,-35,-36,-37,-38,-39,20,20,20,20,20,20,20,20,20,20,20,-8,-13,8,-48,20,20,8,8,8,8,8,8,8,20,-51,-52,-29,-30,-31,20,20,20,20,20,-46,8,8,8,8,8,20,20,20,20,20,]),'[':([0,1,3,6,7,8,9,10,11,12,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,44,45,46,47,73,74,83,84,88,89,90,91,92,95,96,106,107,108,109,110,111,],[9,9,-2,38,9,9,9,9,-49,-50,-4,-1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-47,9,9,9,-3,9,-48,9,9,9,9,9,9,9,-51,-52,-46,9,9,9,9,9,]),'{':([0,1,3,10,11,12,16,17,43,44,47,74,83,84,95,96,106,],[10,10,-2,10,-49,-50,-4,-1,-47,10,-3,-48,10,10,-51,-52,-46,]),'WHILE':([0,1,3,10,11,12,16,17,43,44,47,74,83,84,95,96,106,],[13,13,-2,13,-49,-50,-4,-1,-47,13,-3,-48,13,13,-51,-52,-46,]),'IF':([0,1,3,10,11,12,16,17,43,44,47,74,83,84,95,96,106,],[14,14,-2,14,-49,-50,-4,-1,-47,14,-3,-48,14,14,-51,-52,-46,]),'$end':([1,3,11,12,16,17,43,47,74,95,96,106,],[0,-2,-49,-50,-4,-1,-47,-3,-48,-51,-52,-46,]),';':([2,4,5,6,15,18,40,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[17,-5,-6,-7,47,-10,-9,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-14,-15,-16,-17,-18,-8,-13,106,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),"'":([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[18,-5,-6,-7,18,-10,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-8,-13,18,18,18,-29,-30,-31,18,18,18,18,18,18,18,18,18,18,]),'+':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[19,-5,-6,-7,19,-10,19,-9,19,-32,-33,-34,-35,-36,-37,-38,-39,19,19,19,19,19,19,19,19,19,19,19,-8,-13,19,19,19,-29,-30,-31,19,19,19,19,19,19,19,19,19,19,]),'*':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[21,-5,-6,-7,21,-10,21,21,21,21,21,-34,-35,21,21,-38,-39,21,21,21,21,21,21,21,21,21,21,21,-8,-13,21,21,21,-29,-30,-31,21,21,21,21,21,21,21,21,21,21,]),'/':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[22,-5,-6,-7,22,-10,22,22,22,22,22,-34,-35,22,22,-38,-39,22,22,22,22,22,22,22,22,22,22,22,-8,-13,22,22,22,-29,-30,-31,22,22,22,22,22,22,22,22,22,22,]),'MPLUS':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[23,-5,-6,-7,23,-10,23,-9,23,-32,-33,-34,-35,-36,-37,-38,-39,23,23,23,23,23,23,23,23,23,23,23,-8,-13,23,23,23,-29,-30,-31,23,23,23,23,23,23,23,23,23,23,]),'MMINUS':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[24,-5,-6,-7,24,-10,24,-9,24,-32,-33,-34,-35,-36,-37,-38,-39,24,24,24,24,24,24,24,24,24,24,24,-8,-13,24,24,24,-29,-30,-31,24,24,24,24,24,24,24,24,24,24,]),'MMLTP':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[25,-5,-6,-7,25,-10,25,25,25,25,25,-34,-35,25,25,-38,-39,25,25,25,25,25,25,25,25,25,25,25,-8,-13,25,25,25,-29,-30,-31,25,25,25,25,25,25,25,25,25,25,]),'MDIV':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[26,-5,-6,-7,26,-10,26,26,26,26,26,-34,-35,26,26,-38,-39,26,26,26,26,26,26,26,26,26,26,26,-8,-13,26,26,26,-29,-30,-31,26,26,26,26,26,26,26,26,26,26,]),'EQ':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[27,-5,-6,-7,27,-10,27,-9,27,-32,-33,-34,-35,-36,-37,-38,-39,27,27,27,27,27,27,-14,-15,-16,-17,-18,-8,-13,27,27,27,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'NEQ':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[28,-5,-6,-7,28,-10,28,-9,28,-32,-33,-34,-35,-36,-37,-38,-39,28,28,28,28,28,28,-14,-15,-16,-17,-18,-8,-13,28,28,28,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'GTEQ':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[29,-5,-6,-7,29,-10,29,-9,29,-32,-33,-34,-35,-36,-37,-38,-39,29,29,29,29,29,29,-14,-15,-16,-17,-18,-8,-13,29,29,29,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'LTEQ':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[30,-5,-6,-7,30,-10,30,-9,30,-32,-33,-34,-35,-36,-37,-38,-39,30,30,30,30,30,30,-14,-15,-16,-17,-18,-8,-13,30,30,30,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'>':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[31,-5,-6,-7,31,-10,31,-9,31,-32,-33,-34,-35,-36,-37,-38,-39,31,31,31,31,31,31,-14,-15,-16,-17,-18,-8,-13,31,31,31,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'<':([2,4,5,6,15,18,39,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,94,97,98,99,100,101,102,103,104,112,113,114,115,116,],[32,-5,-6,-7,32,-10,32,-9,32,-32,-33,-34,-35,-36,-37,-38,-39,32,32,32,32,32,32,-14,-15,-16,-17,-18,-8,-13,32,32,32,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'}':([3,10,11,12,16,17,43,44,47,74,95,96,106,],[-2,43,-49,-50,-4,-1,-47,74,-3,-48,-51,-52,-46,]),')':([4,5,6,18,39,40,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,71,72,75,76,85,86,87,97,98,99,100,101,102,103,104,112,113,114,115,116,],[-5,-6,-7,-10,71,-9,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-14,-15,-16,-17,-18,-8,-13,83,84,97,98,99,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),',':([4,5,6,18,40,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,97,98,99,100,101,102,103,104,112,113,114,115,116,],[-5,-6,-7,-10,-9,73,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-14,-15,-16,-17,-18,81,-8,-13,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),']':([4,5,6,18,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,82,93,97,98,99,100,101,102,103,104,112,113,114,115,116,],[-5,-6,-7,-10,-9,72,-12,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-14,-15,-16,-17,-18,80,-8,-13,-11,105,-29,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'=':([6,80,105,],[33,88,107,]),'PLUSASSIGN':([6,80,105,],[34,89,108,]),'MINASSIGN':([6,80,105,],[35,90,109,]),'MULTASSIGN':([6,80,105,],[36,91,110,]),'DIVASSIGN':([6,80,105,],[37,92,111,]),'ZEROS':([33,],[63,]),'ONES':([33,],[64,]),'EYE':([33,],[65,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,10,],[1,44,]),'expr':([0,1,7,8,9,10,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,44,45,46,73,83,84,88,89,90,91,92,107,108,109,110,111,],[2,15,39,40,42,2,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,15,75,76,42,94,94,100,101,102,103,104,112,113,114,115,116,]),'block':([0,1,10,44,83,84,],[3,16,3,16,95,96,]),'while_block':([0,1,10,44,83,84,],[11,11,11,11,11,11,]),'if_block':([0,1,10,44,83,84,],[12,12,12,12,12,12,]),'array_interior':([9,73,],[41,82,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> expr ;','start',2,'p_start','Mparser.py',19),
  ('start -> block','start',1,'p_start','Mparser.py',20),
  ('start -> start expr ;','start',3,'p_start','Mparser.py',21),
  ('start -> start block','start',2,'p_start','Mparser.py',22),
  ('expr -> INTNUM','expr',1,'p_expr_num','Mparser.py',28),
  ('expr -> FLOATNUM','expr',1,'p_expr_num','Mparser.py',29),
  ('expr -> ID','expr',1,'p_expr_id','Mparser.py',32),
  ('expr -> ( expr )','expr',3,'p_expr_group','Mparser.py',35),
  ('expr -> - expr','expr',2,'p_expr_unmin','Mparser.py',40),
  ("expr -> expr '",'expr',2,'p_expr_transpose','Mparser.py',43),
  ('array_interior -> expr , array_interior','array_interior',3,'p_array_interior','Mparser.py',48),
  ('array_interior -> expr','array_interior',1,'p_array_interior','Mparser.py',49),
  ('expr -> [ array_interior ]','expr',3,'p_expr_array','Mparser.py',52),
  ('expr -> ID = expr','expr',3,'p_expr_assign','Mparser.py',57),
  ('expr -> ID PLUSASSIGN expr','expr',3,'p_expr_assign','Mparser.py',58),
  ('expr -> ID MINASSIGN expr','expr',3,'p_expr_assign','Mparser.py',59),
  ('expr -> ID MULTASSIGN expr','expr',3,'p_expr_assign','Mparser.py',60),
  ('expr -> ID DIVASSIGN expr','expr',3,'p_expr_assign','Mparser.py',61),
  ('expr -> ID [ INTNUM ] = expr','expr',6,'p_expr_arrassign','Mparser.py',64),
  ('expr -> ID [ INTNUM ] PLUSASSIGN expr','expr',6,'p_expr_arrassign','Mparser.py',65),
  ('expr -> ID [ INTNUM ] MINASSIGN expr','expr',6,'p_expr_arrassign','Mparser.py',66),
  ('expr -> ID [ INTNUM ] MULTASSIGN expr','expr',6,'p_expr_arrassign','Mparser.py',67),
  ('expr -> ID [ INTNUM ] DIVASSIGN expr','expr',6,'p_expr_arrassign','Mparser.py',68),
  ('expr -> ID [ INTNUM , INTNUM ] = expr','expr',8,'p_expr_matassign','Mparser.py',71),
  ('expr -> ID [ INTNUM , INTNUM ] PLUSASSIGN expr','expr',8,'p_expr_matassign','Mparser.py',72),
  ('expr -> ID [ INTNUM , INTNUM ] MINASSIGN expr','expr',8,'p_expr_matassign','Mparser.py',73),
  ('expr -> ID [ INTNUM , INTNUM ] MULTASSIGN expr','expr',8,'p_expr_matassign','Mparser.py',74),
  ('expr -> ID [ INTNUM , INTNUM ] DIVASSIGN expr','expr',8,'p_expr_matassign','Mparser.py',75),
  ('expr -> ID = ZEROS ( INTNUM )','expr',6,'p_expr_matinit_special','Mparser.py',78),
  ('expr -> ID = ONES ( INTNUM )','expr',6,'p_expr_matinit_special','Mparser.py',79),
  ('expr -> ID = EYE ( INTNUM )','expr',6,'p_expr_matinit_special','Mparser.py',80),
  ('expr -> expr + expr','expr',3,'p_expr_binop','Mparser.py',85),
  ('expr -> expr - expr','expr',3,'p_expr_binop','Mparser.py',86),
  ('expr -> expr * expr','expr',3,'p_expr_binop','Mparser.py',87),
  ('expr -> expr / expr','expr',3,'p_expr_binop','Mparser.py',88),
  ('expr -> expr MPLUS expr','expr',3,'p_expr_matop','Mparser.py',91),
  ('expr -> expr MMINUS expr','expr',3,'p_expr_matop','Mparser.py',92),
  ('expr -> expr MMLTP expr','expr',3,'p_expr_matop','Mparser.py',93),
  ('expr -> expr MDIV expr','expr',3,'p_expr_matop','Mparser.py',94),
  ('expr -> expr EQ expr','expr',3,'p_expr_logic','Mparser.py',99),
  ('expr -> expr NEQ expr','expr',3,'p_expr_logic','Mparser.py',100),
  ('expr -> expr GTEQ expr','expr',3,'p_expr_logic','Mparser.py',101),
  ('expr -> expr LTEQ expr','expr',3,'p_expr_logic','Mparser.py',102),
  ('expr -> expr > expr','expr',3,'p_expr_logic','Mparser.py',103),
  ('expr -> expr < expr','expr',3,'p_expr_logic','Mparser.py',104),
  ('block -> expr ;','block',2,'p_block','Mparser.py',109),
  ('block -> { }','block',2,'p_block','Mparser.py',110),
  ('block -> { start }','block',3,'p_block','Mparser.py',111),
  ('block -> while_block','block',1,'p_block','Mparser.py',112),
  ('block -> if_block','block',1,'p_block','Mparser.py',113),
  ('while_block -> WHILE ( expr ) block','while_block',5,'p_while_block','Mparser.py',117),
  ('if_block -> IF ( expr ) block','if_block',5,'p_if_block','Mparser.py',121),
  ('else_block -> ELSE block','else_block',2,'p_else_block','Mparser.py',124),
]