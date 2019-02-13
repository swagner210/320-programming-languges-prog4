import sys
from prog4_1 import *
from prog4_2 import *


def main():
    print("Assignment #4-3, Samantha Wagner, swagner210@yahoo.com")

    thisbetokens = []
    linesinfile = 0

    with open(sys.argv[1]) as f:                        #tokenize all lines in file and push onto list of tokens
        lines = f.readlines()    
        linesinfile = len(lines)
        thisbetokens =[ Tokenize(l) for l in lines ]

    
    for i in range(0,len(thisbetokens)):
        Parse(thisbetokens[i])
        

    mystack = StackMachine()

    try:
        while mystack.CurrentLine < linesinfile:

            if (mystack.CurrentLine<0):
                print( "Trying to execute invalid line: " + mystack.CurrentLine)


            val = mystack.Execute(thisbetokens[mystack.CurrentLine])


            if val is not None:
                print(val)

        print("Program terminated correctly")
    
    except IndexError as e:
        print ("line" + str(mystack.CurrentLine) + ": " + thisbetokens[mystack.CurrentLine] + "caused Invalid Memory Access")


if __name__ == "__main__":          #run main
    main()
