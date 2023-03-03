
def Osum(a,b):
    return a+b

def Osub(a,b):
    return a-b

def Omul(a,b):
    return a*b

def Odiv(a,b):
    return a/b

def Opow(a,b):
    return a**b

def Orad(a,b=2):
    return a**(1/b)

OPERATOR_FUNCTIONS=[Osum,Osub,Omul,Odiv,Opow,Orad]

class Node:
    def __init__(self,operator,op_left,op_right) -> None:
        self.operator=operator
        self.op_left=op_left
        self.op_right=op_right
    
    def calc_node(self):
        l = self.op_left.calc_node() if type(self.op_left) == Node else self.op_left
        r = self.op_right.calc_node() if type(self.op_right) == Node else self.op_right
        return self.operator(l,r)
        