import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

archivo = open("datos.txt")
caracteres = archivo.read()
archivo.close()

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
expression = parser.parse(caracteres, lexer)
print (expression)
"""
result = expression.evaluate()
print result
"""
