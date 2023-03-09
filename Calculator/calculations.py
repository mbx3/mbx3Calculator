from Calculator.string_work import *
import re

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

def operator_to_function(operator:str):
    if operator == '+' : return Osum        
    if operator == '-' : return Osub        
    if operator == '×' : return Omul        
    if operator == '÷' : return Odiv        
    if operator == '^' : return Opow        
    if operator == '√' : return Orad        

def calculate(txt:str):
    while True:
        lastTxt = ''
        while txt != lastTxt:
            lastTxt = txt
            txt=remove_unnecessary_parentheses(txt)
        fppIndex, fpp = first_priority_parenthes(txt)
        fpeIndex, fpe = first_priority_expression(fpp)
        new_txt = Node(operator_to_function(fpe[1]),float(fpe[0]),float(fpe[2])).calc_node() if type(fpe) == tuple else fpe
        txt = txt[:fppIndex[0]+fpeIndex[0]] + str(new_txt) + txt[fppIndex[0]+1+fpeIndex[1]:]
        if is_calculation_end(txt): return str(int(float(txt))) if int(float(txt)) == float(txt) else txt

