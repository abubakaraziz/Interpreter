from lexer import Lexer
from parser import Parser



class Interpreter():
    def __init__(self,trees):
        self.trees=trees
        print(self.trees)
    def eval_expression(self,tree):
        nodetype=tree[0]
        if nodetype=='NUM':
            return int(tree[1])
        elif nodetype=="binop":
            left_child=tree[1]
            operator=tree[2]
            right_child=tree[3] 
            left_val=self.eval_expression(left_child)
            right_val=self.eval_expression(right_child)
            if operator=='+':
                print("here")
                return left_val +right_val
            elif operator=='-':
                return left_val-right_val
            elif operator=='*':
                return left_val*right_val
            elif operator=='/':
                return left_val/right_val

    def interpret(self):
        nodetype=self.trees[0]
        if nodetype=='binop':
            return self.eval_expression(self.trees)
        elif nodetype=='ASSIGN':
            variable=nodetype[0]
            variable=self.eval_expression(self,trees[1])
             

            
            



    

lexer=Lexer()
lexer.build()
parser=Parser()
trees=parser.parse_text('3+3')
Interpret=Interpreter(trees)
print(Interpret.interpret())
