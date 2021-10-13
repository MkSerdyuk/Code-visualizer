import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

def start_main():
    file_name = filedialog.askopenfilename()
    if start == True:
        result_img.destroy()
    else:
        start = True
    result_img = Label(tab2, image = img)
    result_img.image = img
    result_img.pack(relx=.5, rely=.5, anchor="c")
    save_button = tk.Button(tab2, text = "Сохранить", width = 25, height = 2, bg ='grey',fg = 'black')
    save_button.place(relx=.5,rely=0.9,anchor="c")
    save_button.config(command=lambda:save_image(img))
def save_image(img):
    file_name = filedialog.asksaveasfilename(filetypes=(("Image File (PNG)", "*.png"),("Image File (JPEG)", "*.jpeg")))
    img.save(file_name)
start = False
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
