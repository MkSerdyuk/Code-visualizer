name = 'example.txt'
f = open(name,'r')
code = f.read().split('\n').reverse()
pointers = []
edited_code
for i = 1 to len(code):
    if (code[i].lower()== "end" or "end."):
        edited_code[i] += " ")
        pointers += i
    elif (code[i].lower() == "begin")
        edited_code[i] += "p_"+pointers(len(pointers))
        del pointers[len(pointers)-1]
    else
        edited_code[i] += code[i]
        
        
    
        
