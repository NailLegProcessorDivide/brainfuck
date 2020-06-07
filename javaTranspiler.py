bfChars = [',','.','<','>','[',']','+','-'," "]

javaStart = "#include <stdio.h>\nchar mem[] = char[0xffff];\nshort memPtr=0;\nvoid main(){\n"
javaEnd = "}"

fileName = input("which file should be compiled: ")
with open(fileName, 'r') as file:
    bf = file.read()
    bfLines = bf.split("\n")
    codeSegs = {}
    sector = "main"
    codeSegs[sector] = javaStart
    
    for line in bfLines:
        if len(line)==0:
            pass
        elif line[0] in bfChars:
            for c in line:
                if c == ',':
                    pass
                elif c == '.':
                    codeSegs[sector]+="print(mem[memPtr]);\n"
                elif c == '<':
                    codeSegs[sector]+="memPtr--;\n"
                elif c == '>':
                    codeSegs[sector]+="memPtr++;\n"
                elif c == '[':
                    codeSegs[sector]+="while(mem[0xffff & memPtr]!=0){\n"
                elif c == ']':
                    codeSegs[sector]+="}\n"
                elif c == '-':
                    codeSegs[sector]+="mem[0xffff & memPtr]--;\n"
                elif c == '+':
                    codeSegs[sector]+="mem[0xffff & memPtr]++;\n"
                elif c == '/':
                    break
    codeSegs["main"]+=javaEnd
    with open(fileName+".c", 'w') as saveFile:
        saveFile.write(codeSegs["main"])
        print("written")
