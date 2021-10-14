from PIL import Image,ImageDraw
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk

start = False
def start_main():
    file_name = filedialog.askopenfilename()
    #if start == True:
     #   result_img.destroy()
    #else:
     #   start = True
#_______        
    name = file_name
    f = open(name,'r')
    code = f.read().split('\n')
    edited_code = ['']
    for i in range (0, len(code)):
        if (("else" in code[i].lower() or "if" in code[i].lower() or "for" in code[i].lower() or "while" in code[i].lower()) and not("begin" in code[i+1].lower())):
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
                        text_print.line((2+tabneed*5,i,2+tabneed*5,i+(pointer-k-1)*interv),fill='red',width=2)
                        text_print.text((10+tabneed*5,i),"BEGIN",(0,0,0))
                        tabneed+=1
                    elif cur_str[1]=="|":
                        text_print.text((10+tabneed*5,i),"END",(0,0,0))
                elif cur_str[0]=="%":
                    cur_str_1 = ''
                    for j in range(1,len(cur_str)):
                        cur_str_1+=cur_str[j]
                    print(cur_str_1)
                    print(cur_str)
                    text_print.text((10+tabneed*5,i),cur_str_1,(0,0,0))
                    text_print.line((2+tabneed*5,i,2+tabneed*5,i+2*interv),fill='red',width=2)
        k+=1  
#____
    img = space
    result_img = tk.Label(tab2, image = ImageTk.PhotoImage(img))
    result_img.place(relx=.5, rely=.5, anchor="c")
    save_button = tk.Button(tab2, text = "Сохранить", width = 25, height = 2, bg ='grey',fg = 'black')
    save_button.place(relx=.5,rely=0.9,anchor="n")
    save_button.config(command=lambda:save_image(img))
def save_image(img):
    file_name = filedialog.asksaveasfilename(filetypes=(("Image File (PNG)", "*.png"),("Image File (JPEG)", "*.jpeg")))
    img.save(file_name)
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
