import re

def first_priority_parenthes(txt:str):
    parentheses=0
    layer=[]
    for i in txt:
        if i == ')': parentheses -= 1
        layer.append(parentheses)
        if i == '(': parentheses += 1
    firstIndex = layer.index(max(layer))
    lastIndex = -1
    for i in range(firstIndex,len(layer)):
        if layer[i] != max(layer):
            lastIndex = i-1
            break
    else: lastIndex = len(layer)-1
    return (firstIndex,lastIndex), txt[firstIndex:lastIndex+1]

def first_priority_expression(txt:str):
    m=re.search(r'((?:^-[0-9]+(?:\.[0-9]*)?|[0-9]+(?:\.[0-9]*)?))(\^|\$)(-?[0-9]+(?:\.[0-9]*)?)',txt)
    if m != None: return m.groups()
    m=re.search(r'((?:^-[0-9]+(?:\.[0-9]*)?|[0-9]+(?:\.[0-9]*)?))(\*|\/)(-?[0-9]+(?:\.[0-9]*)?)',txt)
    if m != None: return m.groups()
    m=re.search(r'((?:^-[0-9]+(?:\.[0-9]*)?|[0-9]+(?:\.[0-9]*)?))(\+|\-)(-?[0-9]+(?:\.[0-9]*)?)',txt)
    if m != None: return m.groups()

def remove_unnecessary_parentheses(txt:str):
    out = re.sub(r'\((-?[0-9]+(?:\.[0-9]*)?)\)',r'\1',txt)
    return out
