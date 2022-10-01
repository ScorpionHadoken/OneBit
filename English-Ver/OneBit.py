"""
**********************    Code Language Concept in Python    ***********************************

Was Writing this in C but I'm going to write in Python to fully understand what I want to do
Going to Make This the Human-Readable version because why not

************************************************************************************************
"""

import sys # Was wanting to make something with no dependencies, but sys is built-in :/

codeType = input("Case lower? (y/n): ")

def write(code):
    used = 0 # To append to different blocks
    x = 0
    for _ in range(0,256):
        
        LnWrite = input(f"{x} ")
        if LnWrite == "EXIT":
            return code
        elif LnWrite == "CLEAR":
            code = [[]]
            used = 0
            x = 0
            continue
        elif LnWrite == "BLOCK":
            code.append([])
            used += 1 # += if multiple blocks
            x = 0
            continue

        else:
            code[used].append(LnWrite)
        x += 1

    return code

match codeType:

    case 'n':

        def readC(code): # Oh yeah, the fun part. Wrote this last, am excited.
            line = 0
            for x in code:

                if x[0:4] == "VOID": # Pain in the darn arse, you can't see it, but this is the second time I wrote this.

                    if x[5:8] == "SET": # Used to do INT and STR but that jacked up OP CHAR PRT, just use the right things!
                        code[line] = x[9:]
                        line += 1
                        continue # No need to check for anything if the code is now overwritten

                    elif x[5:7] == "EX": # EX for export
                        
                        if x[8:13] == "WRITE":
                            f = open( code[ int( x[14] ) ], "w") # Get void set line, which should be a file name, difference here is that it can be any file
                            f.write(x[15:])
                            f.close()

                        else:
                            f = open( x[8:] + ".1bit","w") # Save to a file ext I made up
                            f.close()

                    elif x[5:7] == "IM": # IM for import
                        readC( code[ int( x[8:] ) ] ) # Run block code defined after IM

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
                            line += 1
                            continue

                        elif x[8:10] == "IN":
                            words = x[11:]
                            TakeStuff = input(f"{words}") # Input statement is just weird like that, can't do input(x[12:])
                            code[line] = TakeStuff
                
                line += 1 # Debugging purposes

    case 'y':
        
        def readC(code): # Yes I copied readC, and only changed this comment and the if statements. WHATCHA GONNA DO BOUT IT!?
            line = 0
            for x in code:

                if x[0:4] == "void": # Pain in the darn arse, you can't see it, but this is the second time I wrote this.

                    if x[5:8] == "set": # Used to do INT and STR but that jacked up OP CHAR PRT, just use the right things!
                        code[line] = x[9:]
                        line += 1
                        continue # No need to check for anything if the code is now overwritten

                    elif x[5:7] == "ex": # EX for export

                        if x[8:13] == "write":
                            f = open( code[ int( x[14] ) ], "w") # Get void set line, which should be a file name, difference here is that it can be any file
                            f.write(x[15:])
                            f.close()

                        else:
                            f = open( x[8:] + ".1bit","w") # Save to a file ext I made up
                            f.close()

                    elif x[5:7] == "im": # IM for import
                        print(x[8:])
                        readC( code[ int( x[ 8: ] ) ] ) # Run block code defined after IM
                        continue

                elif x[0:2] == "op":

                    if x[3:7] == "math":

                        if x[8:11] == "add":
                            code[ int( x[12:] ) ] = int( code[ int( x[12:] ) ] ) # Convert string to int
                            code[ int( x[12:] ) ] += 1 # add converted string
                            code[ int( x[12:] ) ] = str( code[ int( x[12:] ) ] ) # convert back, for printing and such
                            continue

                        elif x[8:11] == "sub":
                            code[ int( x[12:] ) ] = int( code[ int( x[12:] ) ] ) # same thing here, but subtracting 
                            code[ int( x[12:] ) ] -= 1
                            code[ int( x[12:] ) ] = str( code[ int( x[12:] ) ] )

                    elif x[3:7] == "char":

                        if x[8:11] == "prt":
                            print(code[ int(x[12:]) ]) # Index line number to print out by slicing string after 14th char
                            line += 1
                            continue

                        elif x[8:10] == "in":
                            words = x[11:]
                            TakeStuff = input(f"{words}") # Input statement is just weird like that, can't do input(x[12:])
                            code[line] = TakeStuff
                line += 1 # Debugging purposes
    
        


def main(code):
    
    while True:
        print("\n\n***\tWRITE MODE\t***\n")
        code = write(code)
            
        print("\033c")
        
        print("\n\n***\tREAD?\t***")
        print(f"REPORT:\nBLOCKS: {len(code)}\nSIZE: {sys.getsizeof(code)}\n")
        read = input("y/n : ")
        print("\033c")
        if 'n' in read:
            continue

        
        print("\n\n***\tREAD MODE\t***")
        readC(code[0])
        print("\033c")

if __name__ == '__main__':
    code = [[]] # added sublist in list so BLOCK statements in the editor can be used without an IndexError
    main(code)
