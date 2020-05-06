import ply.yacc as yacc
from lexer import Lexer 

#took help from https://www.dabeaz.com/ply/ply.html#ply_nn24
class Parser:
        
    def __init__(self):
        self.parser=yacc.yacc(module=self)
     
    def parse_text(self,text):
       return self.parser.parse(text)
    def check_tokens(self,text): 
        lexer=Lexer()
        lexer.build()
        lexer.check_input(text)

    
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
        statements : statement COLON 
        '''
        p[0]=[p[1]] 
    

    def p_definingvariable_statement(self,p):
        '''
        statement : INT ID EQUALS LPAREN expr RPAREN
                  | INT ID EQUALS expr 
                  | STRING ID EQUALS LPAREN expr RPAREN
                  | STRING ID EQUALS expr 
                  | BOOL ID EQUALS LPAREN expr RPAREN
                  | BOOL ID EQUALS expr
                  | DOUBLE ID EQUALS LPAREN expr RPAREN
                  | DOUBLE ID EQUALS expr
        '''
        print(len(p))
        if len(p)==5:
            p[0]=('DEFINE',p[2],p[4]) 
        elif len(p)==7:    
            p[0]=('DEFINE',p[2],p[5]) 
    def p_assignment_statement(self,p):
        '''
        statement : ID EQUALS expr 
        '''
        p[0]=('ASSIGN',p[1],p[3]) 
    def p_print_statement(self,p):
        '''
        statement : PRINT LPAREN print_expr RPAREN 
        '''
        print("hello1")
        p[0]=('PRINT',p[3])

    def p_prints_statement(self,p):
        '''
        print_expr : expr
                   | expr COMMA print_expr
        '''
        if len(p)==4:
            p[0]=  [p[1]]  + p[3]
        else:
            p[0]=[ p[1]]
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

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
        p[0]=('binop',p[1],p[2],p[3])
    
     
    def p_expr_factor(self,p):
        '''expr : 
                | INT  
                | BOOL 
                | STRING
                | INT DOT INT 
                '''
        if len(p)==2:
            p[0]=('VAL',p[1])
        elif len(p)==4:
            print('here')
            p[0]=('DOUBLE',p[1],p[3])
        
        
    def p_expr_id(self,p):
        'expr : ID'
        p[0]=('ID',p[1])
        
    #def p_error(self,p):
        #print("Syntax error in input!")
    tokens=Lexer.tokens


'''
while True:
    try:
        s=input('GO++>>')
    except EOFError:
        break
    if not s:continue
    result=parser.parse(s)
    print(result)'''
