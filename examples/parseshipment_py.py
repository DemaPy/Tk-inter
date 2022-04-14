import tkinter as tk
from tkinter import filedialog as fd
import json
import os

app = tk.Tk()
app.title('Parse shipment')
app.geometry('270x50')
app.resizable(False, False)

path='C:/Users/ProblemSolver/Desktop/Json/shipment.txt'

text = tk.Text(app)
text.place(x = 0, y = 0, relwidth = 1, relheight = 1, width = - 18)

def function():
    f=open('responses.json')
    data = json.load(f)
    f.close()

    if os.path.exists('shipment.txt'):
        with open ('shipment.txt', "w") as f:
            for i in data["data"]:
                f.write(str(i['transportUnitId'])+ "\n")
    else:
        with open ('shipment.txt', "a") as f:
            for i in data["data"]:
                f.write(str(i['transportUnitId'])+ "\n")

def open_file():
    filename = fd.askopenfilename(filetypes=[('json files', '*.json')])
    if filename:
            with open(filename, "r", -1, "utf-8") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())
                
def save_file():
        filename = fd.asksaveasfilename(filetypes=[("json","*.json")], defaultextension = "*.json")
        
        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(text.get(1.0, tk.END))

def close_app():
    app.destroy()



btn_open = tk.Button(text='Open file', command=open_file)
btn_open.grid(row=0, column=0, padx=5, pady=5)

btn_exit= tk.Button(text='Exit', fg='red', command=close_app)
btn_exit.grid(row=0, column=3, padx=5, pady=5)

btn_get = tk.Button(text='Get shipment', command=function)
btn_get.grid(row=0, column=2, padx=5, pady=5)

btn_save = tk.Button(text='Save', command=save_file)
btn_save.grid(row=0, column=1, padx=5, pady=5)

app.mainloop()
    
