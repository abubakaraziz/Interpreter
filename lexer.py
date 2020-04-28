import ply.lex as lex
import re

#citation:https://www.dabeaz.com/ply/, https://stackoverflow.com,
#match='<a href:"www.google.com">'
#https://my.eng.utah.edu/~cs3100/lectures/l14/ply-3.4/doc/ply.html
#string_match=re.search(r'"[^"]*"',match)
#print(string_match.group(0))



class Lexer:

    #keywords
    keywords={
    'print':'PRINT',
    'int': 'INT',
    'string':'STRING',
    'bool' : 'BOOL'
    }
    NUMERICAL_OPERATORS=['PLUS','MINUS','DIV','MULT','SQUARE','PERCENT','EQUALS']
    LOGICAL_OPERATORS=['LESS', 'GREATER','LESSEQUAL','GREATEREQUAL','NOTEQUAL','EQUAL','NOT','AND','OR','AND_LOGICAL','OR_LOGICAL']
    PARENTHESIS=['LPAREN','RPAREN','COLON','COMMA']
    OTHERS=['ID','NUMBER']
    tokens=[]
    tokens.extend(NUMERICAL_OPERATORS)
    tokens.extend(LOGICAL_OPERATORS)
    tokens.extend(PARENTHESIS)
    tokens.extend(OTHERS)
    tokens+=keywords.values()
   #NUMERICAL OPERATOR  
    t_PLUS=r'\+'
    t_MINUS=r'-'
    t_DIV=r'/'
    t_MULT=r'\*'
     
   #LOGICAL OPERATOR
    t_EQUALS=r'='
    t_LESS=r'<'
    t_GREATER=r'>'
    t_AND=r'&'
    t_OR=r'\|'
    t_AND_LOGICAL=r'&&'
    t_OR_LOGICAL=r'\|\|'
    t_NOT=r'\!'

    #PARENTHESIS
    t_LPAREN=r'\('
    t_RPAREN=r'\)'
    t_COLON=r'\;'
    t_COMMA=r'\,'
    #OTHERS
    t_ignore=' \t' 

    def t_ID(self,t):   
        r'[a-zA-Z_][a-zA-Z0-9_]*'

        if t.value in self.keywords:
            t.type=self.keywords[t.value]
        return t

    def t_STRING(self,t):
        r'"[^"]*"'
        t.value=t.value[1:-1]
        return t


    def t_NUMBER(self,t):
        r'\d+'
        t.value=int(t.value)
        return t
     # Error handling rule
    def t_error(self,t):
         print("Illegal character '%s'" % t.value[0])
         t.lexer.skip(1)
    def check_input(self,input_text):
        self.lexer.input(input_text)
        for tok in self.lexer:
            print(tok)

    def build(self,**kwargs): 
        self.lexer= lex.lex(module=self,**kwargs)
#lexer=Lexer()
#lexer.build()
#lexer.check_input("print(100);")
