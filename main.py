import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageDraw, ImageFont
from PIL import ImageTk

font = ImageFont.truetype("arial.ttf", 10, encoding='UTF-8')
i=0
def start_main():
    global i
    i=0
    edited_code=[]
    code=[]
    pointers=[]
    def module(text_print,interv,weidth,code,n,tab):
        global i
        text_print.text((10+tab*5,n*interv),code[n][1:],(0,0,0),font=font)
        if (code[n][len(code[n])-1]!=';')or ("procedure" in code[n].lower()) or ("function" in code[n].lower()):
            if code[n+1][0]=='%':
                a=(module(text_print,interv,weidth,code,n+1,tab+1))

                text_print.rectangle((2+tab*5,n*interv,weidth-2-tab*5,(a+1)*interv-3),width=2,outline=(256,0,0))
                return(a)
            elif code[n+1][0]=='@':
                pointer=0
                for j in range(1,len(code[n+1])):
                    pointer=pointer*10+int(code[n+1][j])
                i+=1
                text_print.rectangle((2+tab*5,n*interv,weidth-2-tab*5,(pointer+1)*interv-3),width=2,outline=(256,0,0))
                while i<=pointer:
                    if len(code[i])>0:
                        if(code[i][0]=='%'):
                            i=(module(text_print,interv,weidth,code,i,tab+1))
                        else:
                            if code[i][0]!='@':
                                text_print.text((10,i*interv),code[i],(0,0,0),font=font)
                            elif edited_code[i][1]=="|":
                                text_print.text((10,i*interv),'END',(0,0,0),font=font)
                            else:
                                text_print.text((10,i*interv),'BEGIN',(0,0,0),font=font)
                    i+=1
                return(pointer)
            else:
                text_print.rectangle((2+tab*5,n*interv,weidth-2-tab*5,(n+2)*interv-3),width=2,outline=(256,0,0))
                text_print.text((10+tab*5,(n+1)*interv),code[n+1],(0,0,0),font=font)
                return(n+1)
        else:
            text_print.rectangle((2+tab*5,n*interv,weidth-2-tab*5,(n+1)*interv-3),width=2,outline=(256,0,0))
            return(n)
#_______________________________________________________-            
      
#_________________________________________________            
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
    pointers = []
    for l in range(0,len(edited_code)):
        if ("end" in edited_code[l].lower()):
            edited_code[l]=("@|")
            pointers.append(str(len(edited_code)-int(l)-1))      
        elif ("begin" in edited_code[l].lower()):
            edited_code[l] = ("@"+pointers[len(pointers)-1])
            del pointers[len(pointers)-1]       
    edited_code.reverse()
    #____________________________
    interv = 15
    weidth = 620
    height = interv*len(edited_code)
    space = Image.new("RGB", (weidth,height),(256,256,256))
    text_print = ImageDraw.Draw(space)
    k=0
    tabneed=0
    i = 0
    while i+1 <= len(edited_code):
        if len(edited_code[i])>0:
            if(edited_code[i][0]=='%'):
                i=(module(text_print,interv,weidth,edited_code,i,0))
            else:
                if edited_code[i][0]!='@':
                    text_print.text((10,i*interv),edited_code[i],(0,0,0),font=font)
                elif edited_code[i][1]=="|":
                    text_print.text((10,i*interv),'END',(0,0,0),font=font)
                else:
                    text_print.text((10,i*interv),'BEGIN',(0,0,0),font=font)
        i+=1 
#__________________________________________
    img = space
    save_button = tk.Button(tab2, text = "Сохранить", width = 25, height = 2, bg ='grey',fg = 'black')
    save_button.place(relx=.5,rely=.9,anchor="c")
    save_button.config(command=lambda:save_image(img))
    img_1=ImageTk.PhotoImage(img)
    canvas = tk.Canvas(tab2,width=weidth,height = 600)
    canvas.place(relx=0.5,rely=0.4,anchor='c')
    scroll_y = tk.Scrollbar(tab2,orient="vertical", command=canvas.yview)
    scroll_y.place(x=(772+weidth/2), rely=0.5, anchor='c')
    canvas.create_image(0,0,anchor='nw',image=img_1)
    canvas.configure(scrollregion=canvas.bbox("all"))
    window.mainloop()

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
open_button.place(relx=.5, rely=.5, anchor="c")
open_button.config(command=lambda:start_main())
