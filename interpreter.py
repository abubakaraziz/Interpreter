from lexer import Lexer
from parser import Parser
import sys
import copy

class Interpreter():
    def __init__(self):
        self.env={} 
        self.trees=[]
        self.structs={}
    def get_value(self,value):
        if type(value)==bool:
            if value==True:
                return True 
            elif value==False:
                return False 
        elif type(value)==str:
            return str(value)
        elif type(value)==int:
            return int(value)
    def eval_expression(self,tree):
        nodetype=tree[0] 
        if nodetype=='VAL':
            return  self.get_value(tree[1])
        elif nodetype=='DOUBLE':
            double=str(tree[1])+"."+str(tree[2])
            double=float(double)
            return double
        elif nodetype=='NEGVAL':
            return -tree[1]
        elif nodetype=="binop":
            operator=tree[2]
            left_val=self.eval_expression(tree[1])
            right_val=self.eval_expression(tree[3])
            if operator=='+' and right_val=='+':
                self.env[tree[1][1]]=self.env[tree[1][1]]+1; 
            elif operator=='+':
                return left_val +right_val
            elif operator=='-':
                return left_val-right_val
            elif operator=='*':
                return left_val*right_val
            elif operator=='/':
                return left_val/right_val
            elif operator=='^':
                return left_val**right_val
            elif operator=='<=':
                return left_val<=right_val 
            elif operator=='>=':
                return left_val>=right_val
            elif operator=='<':
                return left_val<right_val
            elif operator=='>':
                return left_val>right_val 
            elif operator=='==':
                return left_val==right_val
            elif operator=='&':
                return (left_val and right_val)
            elif operator=='|':
                return (left_val or right_val) 
            elif operator=='!=':
                return (left_val != right_val)

        elif nodetype=='NOT':
            value=not tree[1]
            return value 
        elif nodetype=="ID":
            var_val=self.env[tree[1]]
            return var_val
        elif nodetype=="+":
            return "+"
    def print_variables(self):
        print(self.env)
    def execute_statements(self,statements): 
        for tree in statements:
            if tree[0]=='binop':
                val=self.eval_expression(tree)
                return val 
            elif tree[0]=='NOT':
                value=not tree[1]
                return value 
            elif tree[0]=='DEFINE':
                variable_name=tree[1]
                expr=tree[2]
                value=self.eval_expression(tree[2])
                if variable_name not in self.env:
                    self.env[variable_name]=value
                else:
                    print("Redeclaration Error")
                    sys.exit()
            elif tree[0]=='PRINT':
                nodes_to_print=tree[1]
                for node in nodes_to_print:
                    value=self.eval_expression(node)
                    print(value,end='')
                    print(" ",end='')
                print("")
            elif tree[0]=='ASSIGN':            
                variable_name=tree[1] 
                value=self.eval_expression(tree[2]) 
                if variable_name in self.env:
                    self.env[variable_name]=value
                else:
                    print("Variable not Initialised")
            elif tree[0]=="STRUCT":
                struct_name=tree[1]
                print(struct_name)
                struct_variables=tree[2]
                self.structs[struct_name]=struct_variables
                print(self.structs) 
    def interpret(self,trees):
        if trees[0]=="statements":
            statements=trees[1]
            if statements != None:
                self.execute_statements(statements)
        
        elif trees[0]=="loop":
            first_statements=trees[1]
            loop_statements=trees[2]
            loop_condition=trees[3]
            last_statements=trees[4]      
            self.interpret(first_statements)   
            outside_var=copy.deepcopy(self.env)
            #print("outside_var", outside_var)
            while((self.eval_expression(loop_condition[1]))):
                self.env={}
                self.env=copy.deepcopy(outside_var)
                self.interpret(loop_statements)

                #print("ENV:",self.env)
                for key in self.env:
                    if key in outside_var:
                        outside_var[key]=self.env[key]
                
                #print("outside_var", outside_var)
                self.env=outside_var
                
                #print("ENV:",self.env)
            self.interpret(last_statements)


def check_structs():
    
    lexer=Lexer()
    lexer.build()
    parser=Parser()
     
    Interpret=Interpreter() 

    
    a_assign=parser.parse_text('STRUCT BookStruct {INT a; STRING name; INT b;};')
    print(a_assign)
    (Interpret.interpret(a_assign))
    Interpret.print_variables()

check_structs()

def testing_variables():
    lexer=Lexer()
    lexer.build()
    parser=Parser()
     
    Interpret=Interpreter() 
    a_assign=parser.parse_text('PRINT(NOT TRUE==(NOT (NOT TRUE)) & (TRUE !=0));')
    print(a_assign)
    (Interpret.interpret(a_assign))
    Interpret.print_variables()
    '''
    b_assign=parser.parse_text('INT b=4;')
    
    Interpret.assign_tree(b_assign[0])
    (Interpret.interpret())
 
    b_increment=parser.parse_text('b=b+1;')
       
    Interpret.assign_tree(b_increment[0])
    (Interpret.interpret())


    c_assign=parser.parse_text('DOUBLE c=(1.5+0.5+2);') 
    
    Interpret.assign_tree(c_assign[0])
    (Interpret.interpret())

    determinant_assign=parser.parse_text('DOUBLE determinant=b^2-4*a*c;' )
        
    Interpret.assign_tree(determinant_assign[0])
    (Interpret.interpret())
        
    quadratic_assign=parser.parse_text('DOUBLE root1=(determinant^1/2);' )
        
    Interpret.assign_tree(quadratic_assign[0])
    (Interpret.interpret())

    number_assign=parser.parse_text('PRINT(root1);PRINT(root1);PRINT(determinant);DOUBLE x=3.5;') 
    print(number_assign)
    Interpret.assign_tree(number_assign[0])
    (Interpret.interpret())
    Interpret.print_variables()
    '''

def check_expr():
    
    lexer=Lexer()
    lexer.build()
    parser=Parser()
     
    Interpret=Interpreter() 

    bool_assign=parser.parse_text('BOOL d=False;') 
    Interpret.assign_tree(bool_assign[0]) 
    (Interpret.interpret())
    print_assign=parser.parse_text('(2 & 2 ) | (3 & (2 &2));')  
    print(print_assign)
    Interpret.assign_tree(print_assign[0]) 
    print(Interpret.interpret())
    Interpret.print_variables()

def check_while_loop():

    lexer=Lexer()
    lexer.build()
    parser=Parser()
     
    Interpret=Interpreter() 
    while_loop_tree=parser.parse_text(""" 
                                      INT i=0;
                                      DO {
                                      INT b=0;
                                      DO {
                                      INT c=0;
                                        DO 
                                      {   
                                        PRINT("(",i,",",b,",",c,")"); 
                                        c=c+1;   
                                        }WHILE(c<2)
                                       b=b+1;
                                     }WHILE(b<2)
                                      
                                      i=i+1;

                                     } WHILE (i<2)
                                     """) 
    Interpret.interpret(while_loop_tree)
    Interpret.print_variables()
#check_while_loop()
def testing_expressions(): 
    lexer=Lexer()
    lexer.build()
      
    Interpret=Interpreter() 
    parser=Parser()
    a_assign=parser.parse_text('INT a=1;INT b=4;b=b+1;DOUBLE c=(1.5+0.5+2);DOUBLE determinant= b^2-4*a*c;DOUBLE quadratic_root1=(determinant^0.5-b)/(2.0*a);PRINT (quadratic_root1);PRINT("hello");')
    print(a_assign)  
    Interpret.assign_tree(a_assign)
    Interpret.interpret()
    Interpret.print_variables() 
    #Interpret.assign_tree(print_assign[0]) 
    #(Interpret.interpret())
#testing_expressions()
def testing():

    lexer=Lexer()
    lexer.build()
    parser=Parser()

    line1=parser.parse_text('INT x=2')
    line2=parser.parse_text('STRING a="start"')

    Interpret=Interpreter(line1[0])
    (Interpret.interpret())
    Interpret.assign_tree(line2[0])
    (Interpret.interpret())
