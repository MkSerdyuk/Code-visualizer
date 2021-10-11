import tkinter as tk
from tkinter import filedialog
from PIL import Image
import subprocess
from shutil import copyfile

def start_main():
    file_name = filedialog.askopenfilename()
    copyfule(file_name,'example.txt')
    process = subprocess.run([sys.executable,'main.py'])
def save_image(img):
    file_name = filedialog.asksaveasfilename(filetypes=(("Image File", "*.png")))
    img.save(file_name)

window = tk.Tk()
open_button = tk.Button( text = "Открыть", width = 220, height = 55, bg = 'grey',fg = 'black') 
open_button.grid(row = 1,column = 1)
open_button.config(command=lambda:start_main())
