This was used just to copy some code for another assignment


import random
globalVariable = "thisisaglobalvariable"

def main():
    print("this is the main function")
    #call the local function
    localFunction()
    #call the global function
    globalFunction()

def globalFunction():
    #change the global variable
    globalVariable = "thisisachangedglobalvariable"
    print(globalVariable)

def localFunction():
    localVariable = "thisisalocalvariable"
    #Both statements will print wihtout error as the function is able to see the global variable and its local variable
    print(globalVariable)
    print(localVariable)

if __name__ == "__main__":
    main()


const = 10
changableVariable = 0
changableVariable = changeVariable(changableVariable)

    def changeVariable(variable, const):
        variable = 20 + const
        return variable