import ply.lex as lex
import re


#match='<a href:"www.google.com">'
#string_match=re.search(r'"[^"]*"',match)
#print(string_match.group(0))

class Lexer:

    tokens=('NAME','PLUS','MINUS','MULT','DIV','NUMBER','EQUALS')
     
    t_PLUS=r'\+'
    t_NAME=r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_EQUALS=r'='
        
    def t_STRING(self,t):
        r'"[^"]*"'
        return token


    def t_NUMBER(self,t):
        r'\d+'
        t.value=int(t.value)
        return t
    def __init__(self):
        self.lexer= lex.lex(module=self)

lexer=Lexer()
