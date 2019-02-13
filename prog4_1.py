def isInt(s):
    try:
        int(s)
        return True
    except:
        return False

def Tokenize(str):
    validwords = ["push" , "pop" , "add" , "sub" , "mul" , "div","mod", "skip" , "save" , "get"]

    thislist = str.split()

    for x in thislist:
        if (x not in validwords) and (isInt(x) is False):
            raise ValueError("Unexpected Token: " + x)


    return thislist

#------------------------------------------------------------------------------------------------------------------------

def Parse(tokens):

    valid1 = ["pop","add","sub","mul","div","mod","skip"]
    valid2 = ["push","save","get"]

    if len(tokens) == 1:
        if not tokens[0] in valid1:
            return False

    if len(tokens) == 2:
        if not tokens[0] in valid2:
            return False
        if tokens[1].isdigit() is False:
            return False

    return True

#------------------------------------------------------------------------------------
