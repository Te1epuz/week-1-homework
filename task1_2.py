def inp_chk(inp1,inp2):
    if type(inp1) == str and type(inp2) == str:
        if inp1 == inp2:
            return 1
        if len(inp1) > len(inp2):
            return 2
        if len(inp1) != len(inp2) and inp2 == 'learn':
            return 3
    else:
        return 0

print(inp_chk(1,2))
print(inp_chk('a','a'))
print(inp_chk('aa','b'))
print(inp_chk('a','bb'))
print(inp_chk('a','learn'))