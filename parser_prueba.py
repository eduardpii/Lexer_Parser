import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

archivo = open("datos.txt")
text = archivo.read()
archivo.close()

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
ast = parser.parse(text, lexer)

print (ast)
