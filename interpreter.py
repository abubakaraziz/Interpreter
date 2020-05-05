from lexer import Lexer
from parser import Parser



class Interpreter():
    def __init__(self,trees):
        self.trees=trees
        self.env={} 
        print("Main Tree is: ")
        print(self.trees)
         
    def eval_expression(self,tree):
        nodetype=tree[0]
        if nodetype=='NUM':
            return int(tree[1])
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

    def interpret(self):
        if self.trees[0]=='binop':
            return self.eval_expression(self.trees)
        elif self.trees[0]=='DEFINE':
            variable_name=self.trees[1]
            expr=self.trees[2]
            value=self.eval_expression(self.trees[2])
            self.env[variable_name]=value
            print(self.env)
        elif self.trees[0]=='PRINT':
            nodes_to_print=self.trees[1]
            for node in nodes_to_print:
                value=self.eval_expression(node)
                print(value)

            



    

lexer=Lexer()
lexer.build()
parser=Parser()
trees=parser.parse_text('PRINT(2,3+3)')
print(trees)
Interpret=Interpreter(trees[0])
(Interpret.interpret())
