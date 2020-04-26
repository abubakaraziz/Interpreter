import ply.yacc as yacc
from lexer import Lexer 

#took help from https://www.dabeaz.com/ply/ply.html#ply_nn24
class Parser:
    def p_assign(self,p):
        'assign : NAME EQUALS expr'
        p[0]=('ASSIGN',p[1],p[3])
    def parse_text(self,text):
       return self.parser.parse(text)

    def p_expr_plus(self,p):
        '''expr : expr PLUS factor
                | factor PLUS factor'''
        p[0]=('+',p[1],p[3])

    def p_factor(self,p):
        'factor : NUMBER'
        p[0]=('NUM',p[1]) 
    tokens=Lexer.tokens
    def __init__(self):
        self.parser=yacc.yacc(module=self)
parser=Parser()
print(parser.parse_text('x=2+2'))
'''
while True:
    try:
        s=input('GO++>>')
    except EOFError:
        break
    if not s:continue
    result=parser.parse(s)
    print(result)'''
