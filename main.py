from PIL import Image,ImageDraw
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk

i=0
def start_main():
    global i
    def module(text_print,interv,weidth,code,n,tab):
        global i
        text_print.text((10+tab*5,n*interv),code[n][1:],(0,0,0))
        if code[n][len(code[n])-1]!=';':
            if code[n+1][0]=='%':
                module(text_print,interv,weidth,code,n+1,tab+1)
            elif code[n+1][0]=='@':
                pointer=0
                for j in range(1,len(code[n+1])):
                    pointer=pointer*10+int(code[n+1][j])
                '''    
                for k in range(n+1,pointer):
                    text_print.text((10+tab*5,(k)*interv),code[k],(0,0,0))
                '''
                i+=1
                while i!=pointer:
                    if len(edited_code[i])>0:
                        if(edited_code[i][0]=='%'):
                            module(text_print,interv,weidth,edited_code,i,1)
                        else:
                            if edited_code[i][0]!='@':
                                text_print.text((10,i*interv),edited_code[i],(0,0,0))
                            elif edited_code[i][1]=="|":
                                text_print.text((10,i*interv),'END',(0,0,0))
                            else:
                                text_print.text((10,i*interv),'BEGIN',(0,0,0))
                    i+=1 
                text_print.rectangle((2+tab*5,n*interv,weidth-2-tab*5,(pointer-1)*interv),width=2,outline=(256,0,0))
        else:
            text_print.rectangle((2+tab*5,n*interv,weidth-2-tab*5,n+1*interv),width=2,outline=(256,0,0))
            text_print.text((10+tab*5,n*interv),code[n],(0,0,0))
    file_name = filedialog.askopenfilename()      
    name = file_name
    f = open(name,'r')
    code = f.read().split('\n')
    edited_code = ['']
    for i in range (0, len(code)):
        if (("procedure" in code[i].lower() or "function" in code[i].lower() or "else" in code[i].lower() or "if" in code[i].lower() or "for" in code[i].lower() or "while" in code[i].lower())):
            edited_code.append("%"+code[i])
        else:
            edited_code.append(code[i])
    edited_code.reverse()
    code.reverse()
    pointers = ['']
    for i in range(0,len(edited_code)):
        if ("end" in edited_code[i].lower()):
            edited_code[i]=("@|")
            pointers.append(str(len(edited_code)-int(i)+1))
        elif ("begin" in edited_code[i].lower()):
            edited_code[i] = ("@"+pointers[len(pointers)-1])
            del pointers[len(pointers)-1]
    edited_code.reverse()
    #____________________________
    weidth = 620
    height = 877
    interv = 15
    space = Image.new("RGB", (weidth,height),(256,256,256))
    text_print = ImageDraw.Draw(space)
    k=0
    tabneed=0
    i = 0
    while i+1 <= len(edited_code):
        if len(edited_code[i])>0:
            if(edited_code[i][0]=='%'):
                module(text_print,interv,weidth,edited_code,i,1)
            else:
                if edited_code[i][0]!='@':
                    text_print.text((10,i*interv),edited_code[i],(0,0,0))
                elif edited_code[i][1]=="|":
                    text_print.text((10,i*interv),'END',(0,0,0))
                else:
                    text_print.text((10,i*interv),'BEGIN',(0,0,0))
        i+=1 
    '''
    for i in range(1,height,interv): 
        if k<len(edited_code):
            cur_str=str(edited_code[k])
            if len(cur_str)>0:
                if cur_str[0]!=("@") and cur_str[0]!=("%"):
                    text_print.text((10+tabneed*5,i),edited_code[k],(0,0,0))
                elif cur_str[0]=="@":    
                    if (cur_str[1]!="|"):
                        pointer=0
                        for j in range(len(cur_str)-1):
                            pointer=pointer*10+int(cur_str[j+1])
                        text_print.line((2+tabneed*5,i,2+tabneed*5,i+(pointer-k-1)*interv-interv//3),fill='red',width=2)
                        text_print.text((10+tabneed*5,i),"BEGIN",(0,0,0))
                        tabneed+=1
                    elif cur_str[1]=="|":
                        text_print.text((10+tabneed*5,i),"END",(0,0,0))
                        tabneed -=1
                elif cur_str[0]=="%":
                    cur_str_1 = ''
                    tabneed+=1
                    for j in range(1,len(cur_str)):
                        cur_str_1+=cur_str[j]
                    text_print.text((10+tabneed*5,i),cur_str_1,(0,0,0))
                    text_print.line((2+tabneed*5,i,2+tabneed*5,i+2*interv),fill='red',width=2)
        k+=1
        '''
#____
    img = space
#    result_img = tk.Label(tab2, image = ImageTk.PhotoImage(img))
#    result_img.place(relx=.5, rely=.5, anchor="c")
    canvas = tk.Canvas(tab2, width=weidth, height=height)
    canvas.place(relx=.45,rely=.3, anchor="c")
    img=ImageTk.PhotoImage(img)
    def createImg(x, y):
        canvas.create_image(x, y, image=img)
    createImg(500,700)     
    save_button = tk.Button(tab2, text = "Сохранить", width = 25, height = 2, bg ='grey',fg = 'black')
    save_button.place(relx=.5,rely=0.9,anchor="n")
    save_button.config(command=lambda:save_image(img))

def save_image(img):
    file_name = filedialog.asksaveasfilename(filetypes=[("Image File (PNG)", "*.png"),("Image File (JPEG)", "*.jpeg")],title=("Сохранить как..."))
    try:
        img.save(file_name)
    except ValueError:
        img.save(file_name+'.png')

window = tk.Tk()
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Меню")
tab_control.add(tab2, text = "Результат")
tab_control.pack(expand=1, fill="both")
window.title("Визуализатор кода")
open_button = tk.Button(tab1, text = "Открыть", width =25, height = 2, bg = 'grey',fg = 'black') 
open_button.place(relx=.5, rely=.5, anchor="s")
open_button.config(command=lambda:start_main())
