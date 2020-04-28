import ply.yacc as yacc
from lexer import Lexer 

#took help from https://www.dabeaz.com/ply/ply.html#ply_nn24
class Parser:
        
    def __init__(self):
        self.parser=yacc.yacc(module=self)
    
    def parse_text(self,text):
       return self.parser.parse(text)

    precedence=(
        ('left','PLUS','MINUS'),
        ('left','MULT','DIV'),
        ) 
    #Statements 
    def p_statements_many(self,p):
        '''
        statements : statements statement
        '''
        p[0]=p[1] + [p[2]]

    def p_statements_single(self,p):
        
        '''
        statements : statement 
        '''
        p[0]=[p[1]] 
    
    def p_assignment_statement(self,p):
        '''
        statement : ID EQUALS expr 
        '''
        p[0]=('ASSIGN',p[1],p[3]) 
    def p_print_statement(self,p):
        '''
        statement : ID LPAREN expr RPAREN 
        '''
        print("here")
        p[0]=('PRINTS',[p[3]])

    #| expr AND expr 
    #| expr OR expr  
    #| expr AND_LOGICAL expr
    #| expr OR_LOGICAL expr

    #| expr LESS expr
    #| expr GREATER expr'''
    def p_expr_binop(self,p):
        '''expr : expr PLUS expr
                | expr MINUS expr
                | expr MULT expr
                | expr DIV expr 
                '''
        print('hello')
        p[0]=('binop',p[1],p[2],p[3])
    def p_expr_factor(self,p):
        'expr : NUMBER'
        p[0]=('NUM',p[1])
        
        
    def p_expr_id(self,p):
        'expr : ID'
        print('hello')
        p[0]=('ID',p[1])
    def p_expr_string(self,p):
        'expr : STRING' 
        p[0]=('STRING',p[1])
    

    #def p_error(self,p):
        #print("Syntax error in input!")
    tokens=Lexer.tokens
    #print(tokens)
lexer=Lexer()

lexer.build()

lexer.check_input("PRINT(2)")
parser=Parser()
print(parser.parse_text('PRINT(2+2)'))


'''
while True:
    try:
        s=input('GO++>>')
    except EOFError:
        break
    if not s:continue
    result=parser.parse(s)
    print(result)'''
