"""
**********************    Code Language Concept in Python    ********************************

Was Writing this in C but I'm going to write in Python to fully understand what I want to do
Going to Make This the Human-Readable version because why not

************************************************************************************************
"""

class UnorderedError(Exception):
    pass

def write(code):
    for x in range(0,256):
        LnWrite = input(f"{x} ")
        if LnWrite == "EXIT":
            return code
        elif LnWrite == "CLEAR":
            code = []

        else:
            code.append(LnWrite)

    return code

def readC(code): # Oh yeah, the fun part. Wrote this last, am excited.
    line = 0
    for x in code:

        if x[0:4] == "VOID": # Pain in the darn arse, you can't see it, but this is the second time I wrote this.

            if x[5:8] == "SET": # Used to do INT and STR but that jacked up OP CHAR PRT, just use the right things!
                code[line] = x[9:]
                continue # No need to check for anything if the code is now overwritten

        elif x[0:2] == "OP":

            if x[3:7] == "MATH":

                if x[8:11] == "ADD":
                    code[ int( x[12:] ) ] = int( code[ int( x[12:] ) ] )
                    code[ int( x[12:] ) ] += 1
                    code[ int( x[12:] ) ] = str( code[ int( x[12:] ) ] ) # fml

                elif x[8:11] == "SUB":
                    code[ int( x[12:] ) ] = int( code[ int( x[12:] ) ] )
                    code[ int( x[12:] ) ] -= 1
                    code[ int( x[12:] ) ] = str( code[ int( x[12:] ) ] )

            elif x[3:7] == "CHAR":

                if x[8:11] == "PRT":
                    print(code[ int(x[12:]) ]) # Index line number to print out by slicing string after 14th char
                    continue

                elif x[8:10] == "IN":

                    words = x[11:]
                    TakeStuff = input(f"{words}") # Input statement is just weird like that, can't do input(x[12:])
                    code[line] = TakeStuff
                    continue # No more to do with this iteration
        
                
        print("")
        line += 1 # Debugging purposes


def readCL(code): # Yes I copied readC, and only changed this comment and the if statements. WHATCHA GONNA DO BOUT IT!?
    line = 0
    for x in code:

        if x[0:4] == "void": # Pain in the darn arse, you can't see it, but this is the second time I wrote this.

            if x[5:8] == "set": # Used to do INT and STR but that jacked up OP CHAR PRT, just use the right things!
                code[line] = x[9:]
                continue # No need to check for anything if the code is now overwritten

        elif x[0:2] == "op":

            if x[3:7] == "math":

                if x[8:11] == "add":
                    code[ int( x[12:] ) ] = int( code[ int( x[12:] ) ] )
                    code[ int( x[12:] ) ] += 1
                    code[ int( x[12:] ) ] = str( code[ int( x[12:] ) ] ) # fml

                elif x[8:11] == "sub":
                    code[ int( x[12:] ) ] = int( code[ int( x[12:] ) ] )
                    code[ int( x[12:] ) ] -= 1
                    code[ int( x[12:] ) ] = str( code[ int( x[12:] ) ] )

            elif x[3:7] == "char":

                if x[8:11] == "prt":
                    print(code[ int(x[12:]) ]) # Index line number to print out by slicing string after 14th char
                    continue

                elif x[8:10] == "in":

                    words = x[11:]
                    TakeStuff = input(f"{words}") # Input statement is just weird like that, can't do input(x[12:])
                    code[line] = TakeStuff
                    continue # No more to do with this iteration
        
                
        print("")
        line += 1 # Debugging purposes


def write(code):
    for x in range(0,256):
        LnWrite = input(f"{x} ")
        if LnWrite == "EXIT":
            return code
        elif LnWrite == "CLEAR":
            code = []

        else:
            code.append(LnWrite)

    return code

                    

    return code # Happy Debugging! Au revoir! Hey, future edit here, this was supposed to be a joke towards the people using this . . . fml
                

def report(code, line):
    print("Line:",line)
    print(lineCode)
    print("Returns: Not Implemented") # I'll work on this soon
    print("Comment: Not Implemeted")
    
        


def main(code):
    codeType = input("Case lower? (y/n): ")
    
    while True:
        print("\n\n***\tWRITE MODE\t***\n")
        write(code)
            
        print("\033c")

        print("\n\nCODE:")
        print("=======================")
        for x in code:
            print(x)
            print("=======================")
        print("\033c");
        
        print("\n\n***\tREAD?\t***")
        read = input("y/n : ")
        print("\033c");
        if 'n' in read:
            continue

        
        print("\n\n***\tREAD MODE\t***")
        if 'n' in codeType:
            code = readC(code)
        elif 'y' in codeType:
            code = readCL(code)
        print("\033c")

code = []
main(code)
