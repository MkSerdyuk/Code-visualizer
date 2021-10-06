from PIL import Image,ImageDraw
name = 'example.txt'
f = open(name,'r')
code = f.read().split('\n')
code.reverse()
pointers = []
edited_code = ['']
for i in range(0,len(code)):
    if (code[i].lower()== "end" or code[i].lower()=="end."):
        edited_code.append("@|")
        pointers.append(str(i))
    elif (code[i].lower() == "begin"):
        edited_code.append("@"+pointers[len(pointers)-1])
        del pointers[len(pointers)-1]
    else:
        edited_code.append(code[i])
edited_code.reverse()
#____________________________
weidth = 620
height = 877
interv = 15
space = Image.new("RGB", (weidth,height),(256,256,256))
text_print = ImageDraw.Draw(space)
k=0
for i in range(1,height,interv): 
    if k<len(edited_code):
        cur_str=str(edited_code[k])
        if len(cur_str)>0:
            if cur_str[0]!="@":
                text_print.text((10,i),edited_code[k],(0,0,0))
            elif cur_str[1]!="|":
                pointer=0
                for j in range(len(cur_str)-1):
                    pointer=pointer*10+int(cur_str[j+1])
                text_print.line((2,i,2,i+pointer*interv),fill='red',width=2)
    k+=1
space.show()

        
    
        
