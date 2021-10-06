import PIL
name = 'example.txt'
f = open(name,'r')
code = f.read().split('\n')
code.reverse()
pointers = []
edited_code = []
for i in range(len(code)):
    if (code[i].lower()== "end" or code[i].lower()=="end."):
        edited_code.append("->|")
        pointers.append(str(i))
    elif (code[i].lower() == "begin"):
        edited_code.append("->"+pointers[len(pointers)-1])
        del pointers[len(pointers)-1]
    else:
        edited_code.append(code[i])
edited_code.reverse()
for i in range(len(edited_code)):
    print(edited_code[i])
        
    
        
