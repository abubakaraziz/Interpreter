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
        elif nodetype=="ID":
            var_val=self.env[tree[1]] 
            return var_val
    def print_variables(self):
        print(self.env)
    def interpret(self):
        print(self.trees)
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



    
def testing_variables():

    lexer=Lexer()
    lexer.build()
    parser=Parser()
    string_assign=parser.parse_text('STRING a=("start");' ) 
    double_assign=parser.parse_text('INT z=2;' )
    bool_assign=parser.parse_text('BOOL d= FALSE;')
    print_assign=parser.parse_text('PRINT(a,d);')
    Interpret=Interpreter() 
    Interpret.assign_tree(string_assign[0])
    (Interpret.interpret())

    Interpret.assign_tree(double_assign[0])
    (Interpret.interpret())
    Interpret.assign_tree(bool_assign[0])
    (Interpret.interpret()) 
    Interpret.assign_tree(print_assign[0])
    (Interpret.interpret())
testing_variables()
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
