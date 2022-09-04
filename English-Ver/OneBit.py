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

                elif x[8:10] == "IN":

                    words = x[12:]
                    TakeStuff = input(f"{words}") # Input statement is just weird like that, can't do input(x[12:])
                    continue # No more to do with this iteration
                
        print("")
        line += 1 # Debugging purposes

                    

    return code # Happy Debugging! Au revoir! Hey, future edit here, this was supposed to be a joke towards the people using this . . . fml
                

def report(code, line):
    print("Line:",line)
    print(lineCode)
    print("Returns: Not Implemented") # I'll work on this soon
    print("Comment: Not Implemeted")
    
        


def main(code):
    while True:
        print("\n\n***\tWRITE MODE\t***\n")
        write(code)

        print("\n\nCODE:")
        print("=======================")
        for x in code:
            print(x)
            print("=======================")
        print("")
        
        print("\n\n***\tREAD?\t***")
        read = input("y/n : ")
        if 'n' in read:
            continue
        print("\n\n***\tREAD MODE\t***")
        code = readC(code)

code = []
main(code)
