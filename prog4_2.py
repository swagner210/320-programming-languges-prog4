class StackMachine:

    def __init__(self):
        self.stack = []
        self.CurrentLine = 0
        self.savedict = {}

    def Execute(self,tokens):
        self.CurrentLine +=1
        try:

            if len(tokens) == 2:
                if (tokens[0] == "push"):
                    self.stack.append(int(tokens[1]))
                    return None

                elif (tokens[0] == "save"):             #********              
                    self.savedict[tokens[1]]=self.stack.pop();
                    return None

                else:
                                        #---(x[1] == "get")
                    if (tokens[1] in self.savedict):
                        self.stack.append(self.savedict[tokens[1]])
                        return None
                    else:
                        raise IndexError("Invalid Memory Access")
            
            elif (tokens[0] == "pop"):
                temp =self.stack.pop()
                return temp

            elif (tokens[0] == "add"): 
                temp = self.stack.pop()
                self.stack.append(temp + self.stack.pop())
                return None
                    

            elif (tokens[0] == "sub"):
                temp = self.stack.pop()
                self.stack.append(temp - self.stack.pop())
                return None
            
                
            elif (tokens[0] == "mul"):
                temp = self.stack.pop()
                self.stack.append(temp * self.stack.pop())
                return None

            elif (tokens[0] == "div"):
                temp = self.stack.pop()
                self.stack.append(temp / self.stack.pop())
                return None

            elif (tokens[0] == "mod"):
                temp = self.stack.pop()
                self.stack.append(temp % self.stack.pop())
                return None

            #else                        #---x==skip
            else: #(tokens[0] == "skip"):             #*************
                temp = self.stack.pop()
                temp1 = self.stack.pop()

                if temp == 0:
                    self.CurrentLine = self.CurrentLine + temp1
                return None
        except IndexError:
            print("Invalid Memory Access")

