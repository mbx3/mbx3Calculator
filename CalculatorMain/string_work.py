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
    m=re.search(r'((?:^-[0-9]*(?:\.[0-9]*)?|[0-9]*(?:\.[0-9]*)?))(\^|\√)(-?[0-9]*(?:\.[0-9]*)?)',txt)
    if m != None: return (m.start(),m.end()-1), m.groups()
    m=re.search(r'((?:^-[0-9]*(?:\.[0-9]*)?|[0-9]*(?:\.[0-9]*)?))((?:mod)|\×|\÷)(-?[0-9]*(?:\.[0-9]*)?)',txt)
    if m != None: return (m.start(),m.end()-1), m.groups()
    m=re.search(r'((?:^-[0-9]*(?:\.[0-9]*)?|[0-9]*(?:\.[0-9]*)?))(\+|\-)(-?[0-9]*(?:\.[0-9]*)?)',txt)
    if m != None: return (m.start(),m.end()-1), m.groups()
    return (0,len(txt)-1), txt

def remove_unnecessary_parentheses(txt:str):
    out = re.sub(r'\((-?[0-9]+(?:\.[0-9]*)?)\)',r'\1',txt)
    return out

def is_calculation_end(txt:str):
    if re.match(r'^-?[0-9]+(?:\.[0-9]*)?$',txt): return True
    return False

def correction(txt : str, newtxt : str = ""):
    starttxt = txt + newtxt
    txt = starttxt
    # (2)) --> (2)
    if txt.count('(') < txt.count(')'): txt = txt[::-1].replace(')','',1)[::-1]
    # * --> ×
    txt = re.sub(r'\*','×',txt)
    # / --> ÷
    txt = re.sub(r'\/','÷',txt)
    # $ --> √
    txt = re.sub(r'\$','√',txt)
    # m --> mod
    txt = re.sub(r'm[^(?:od)]','mod',txt)
    # () --> (0)
    txt = re.sub(r"\(\)","(0)",txt)
    # 1.12. --> 1.12
    txt = re.sub(r"\.(\d*)\.",r".\g<1>",txt)
    # .+ --> .0+
    txt = re.sub(r"\.(\D)",r".0\g<1>",txt)
    # -. --> -0.
    txt = re.sub(r"(\D|^)\.",r"\g<1>0.",txt)
    # 5( --> 5×(
    txt = re.sub(r"(\d|\))\(",r"\g<1>×(",txt)
    # )4 --> )×4
    txt = re.sub(r"\)(\d|\()",r")×\g<1>",txt)
    # Error!5 --> 5
    txt = re.sub(r"^(?:(?:Error!)|\+|\÷|\×|\^|\√|(?:mod))(.)",r"\g<1>",txt)
    # +- --> -
    txt = re.sub(r"(?:\+|\-)\-",r"-",txt)
    # (+ --> (
    txt = re.sub(r"(^|\()(?:\+|\÷|\×|\^|\√|(?:mod))",r"\g<1>",txt)###########
    # ×+ --> +
    txt = re.sub(r"(\+|\-|\÷|\×|\^|\√|(?:mod))(\+|\÷|\×|\^|\√|(?:mod))",r"\g<2>",txt)
    # 05 --> 5
    txt = re.sub(r"(^|[^\.\d])0(\d)",r"\g<1>\g<2>",txt)
    #    --> 0
    txt = re.sub(r"^\s*$","0",txt)
    if starttxt != txt : return correction(txt)
    return txt