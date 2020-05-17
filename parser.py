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
        ('left','AND_LOGICAL','OR_LOGICAL','NOTEQUAL'),  
        ('nonassoc','LESSEQUAL','GREATEREQUAL','LESS','GREATER'),
        ('left','LOGICAL_EQUAL'),

        ('right','NOT'),
        ('left','PLUS','MINUS'),
        ('left','MULT','DIV'),
        ('left','SQUARE'),
        ('left','LPAREN','RPAREN')
        ) 
    #Statements 
    
    def p_program(self,p):
        '''
        program : program DO LBRACE program RBRACE WHILE loop_conditions program 
                | statements
                | empty
        '''
        if len(p)==1:
            p[0]=p[1]
        if len(p)==2:
            p[0]=('statements',p[1])
        elif len(p)==9:
            p[0]=('loop',p[1],p[4],p[7],p[8])

    def p_empty(self,p):
        '''
        empty : 
        '''
        pass
    
    
    def p_loop_conditions(self,p):
        '''
        loop_conditions : LPAREN expr RPAREN 
        '''
        p[0]=('loop_condition',p[2])
    def p_statements_many(self,p):
        '''
        statements : statements statement COLON
                   | statement COLON
        '''
        if len(p)==4:
            p[0]=p[1] + [p[2]]
        elif len(p)==3:
            p[0]=[p[1]]
        


    def p_definingvariable_statement(self,p):
        '''
        statement : STRUCT ID LBRACE VARIABLES RBRACE
                  | INT ID EQUALS expr 
                  | STRING ID EQUALS expr 
                  | BOOL ID EQUALS expr
                  | DOUBLE ID EQUALS expr
                  | ID EQUALS expr
                  | ID ID 
                  | expr
                     
        '''
        if len(p)==6:
            p[0]=('STRUCT',p[2],p[4])
        elif len(p)==5:
            p[0]=('DEFINE',p[2],p[4]) 
        elif len(p)==4: 
            p[0]=('ASSIGN',p[1],p[3]) 
        elif len(p)==3:
            p[0]=('STRUCTINST',p[1],p[2])
        elif len(p)==2: 
            p[0]=p[1] 


    
    def p_VARIABLES(self,p):
        '''
        VARIABLES : single_intialize VARIABLES 
                  | single_intialize 
        '''
        
        if len(p)==3:
            p[0]=  [p[1]]  + p[2]
        else:
            p[0]=[ p[1]]
    def p_not_intialize(self,p):
        '''
         single_intialize : INT ID COLON
                          | STRING ID COLON
                          | DOUBLE ID COLON
                            
        '''

        if len(p)==4:
            p[0]=(p[1],p[2])
      
    def p_print_statement(self,p):
        '''
        statement : PRINT LPAREN print_expr RPAREN
        '''
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


    #| expr LESS expr
    #| expr GREATER expr'''
    def p_expr_brackets(self,p):
        ''' 
            expr :   LPAREN expr RPAREN
        
        '''
        p[0]=p[2]
    def p_expr_binop(self,p):

        '''expr : expr PLUS expr
                | expr MINUS expr
                | expr MULT expr
                | expr DIV expr 
                | expr SQUARE expr
                | expr LESSEQUAL expr
                | expr GREATEREQUAL expr
                | expr LESS expr
                | expr GREATER expr 
                | expr LOGICAL_EQUAL expr
                | expr NOTEQUAL expr
                | expr AND_LOGICAL expr
                | expr OR_LOGICAL expr
                | expr PLUS PLUS
                | NOT expr
                | MINUS expr
                        '''
        if p[2]=="+" and p[3]=="+":
            p[0]=('ASSIGNINC',p[1])
        elif len(p)==4:
            p[0]=('binop',p[1],p[2],p[3])
        elif len(p)==3 and p[1]=='NOT':
            p[0]=('NOT', p[2]) 
        elif len(p)==3 and p[1]=='-': 
            p[0]=('binop',('VAL',0),'-',p[2])
    def p_expr_factor(self,p):
        '''expr : STRUCT_NAME 
                | DOUBLE 
                | INT  
                | BOOL 
                | STRING
                '''
        
        
        if len(p)==4:
            p[0]=('DOUBLE',p[1],p[3])
        
        elif len(p)==3: 
            if p[1]=='MINUS':
                p[0]=('NEGVAL',p[2])
            elif p[1]=='NOT': 
                p[0]=('NOT',p[2]) 
        elif len(p)==2:
            p[0]=('VAL',p[1])
     
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
