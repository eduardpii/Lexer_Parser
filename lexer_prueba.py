import lexer_rules
from ply.lex import lex
archivo = open("datos.txt")
text = archivo.read()
archivo.close()
lexer = lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
while token is not None:
    print (token.type, token.value)
    token = lexer.token()
