from lexer import Lexer
from parser import Parser



class Interpreter():
    def __init__(self):
        self.env={} 
        self.trees=[]
    def assign_tree(self,tree):
        self.trees=tree
    def get_value(self,value):
        #print(value)
        #print(type(value))
        if type(value)==bool:
            if value==True:
                return "TRUE"
            elif value==False:
                return "FALSE"
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
            if operator=='+':
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
            
        elif nodetype=="ID":
            var_val=self.env[tree[1]]
            return var_val
    def print_variables(self):
        print(self.env)
    def interpret(self):
        if self.trees[0]=='binop':
            return self.eval_expression(self.trees)
        elif self.trees[0]=='DEFINE':
            variable_name=self.trees[1]
            expr=self.trees[2]
            value=self.eval_expression(self.trees[2])
            if variable_name not in self.env:
                self.env[variable_name]=value
            else:
                print("Redeclaration Error")
        elif self.trees[0]=='PRINT':
            nodes_to_print=self.trees[1]
            for node in nodes_to_print:
                value=self.eval_expression(node)
                print(value,end='')
                print(" ",end='')
            print("")
        elif self.trees[0]=='ASSIGN':            
            variable_name=self.trees[1] 
            value=self.eval_expression(self.trees[2]) 
            if variable_name in self.env:
                self.env[variable_name]=value
            else:
                print("Variable not Initialised")
    
def testing_variables():

    lexer=Lexer()
    lexer.build()
    parser=Parser()
     
    Interpret=Interpreter() 
    a_assign=parser.parse_text('INT a =1;')
    Interpret.assign_tree(a_assign[0])
    (Interpret.interpret())

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

def check_while_loop():
    
    lexer=Lexer()
    lexer.build()
    parser=Parser()
     
    Interpret=Interpreter() 

    a_assign=parser.parse_text('3+3;') 
    print(a_assign)
    Interpret.assign_tree(a_assign[0]) 
    Interpret.interpret()
    Interpret.print_variables()
check_while_loop()
def testing_expressions(): 
    lexer=Lexer()
    lexer.build()
      
    Interpret=Interpreter() 
    parser=Parser()
    double_assign=parser.parse_text('DOUBLE z=1;' )
    bool_assign=parser.parse_text('DOUBLE d= 2^2;')
    print_assign=parser.parse_text('PRINT(d)')
    
    Interpret.assign_tree(double_assign[0])
    Interpret.interpret()
    Interpret.print_variables() 
    Interpret.assign_tree(bool_assign[0]) 
    Interpret.interpret() 
    #Interpret.assign_tree(print_assign[0]) 
    #(Interpret.interpret())

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
