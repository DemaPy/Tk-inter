import tkinter as tk

from tkinter import filedialog as fd

import json
import os

app = tk.Tk()
app.title('Problem Solver | Outbound')
app.geometry('650x220')
app.resizable(False, False)



def open_file():
        
    path='C:/Users/ProblemSolver/Desktop/Json/shipment.txt'
        
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

def getshimpent():
        f=open('responses.json')
        data = json.load(f)
        f.close()

        if os.path.exists('shipment.txt'):
                with open ('shipment.txt', "w") as f:
                        for i in data["data"]:
                                f.write(str(i['transportUnitId'])+"\n")
        else:
                with open ('shipment.txt', "a") as f:
                        for i in data["data"]:
                                f.write(str(i['transportUnitId'])+"\n")

def getorder():
        f=open('responseo.json')
        data = json.load(f)
        f.close()

        if os.path.exists('order.txt'):
            with open ('order.txt', "w") as f:
                for i in data["data"]:
                    f.write(str(i['orderId'])+"\n")
        else:
            with open ('order.txt', "a") as f:
                for i in data["data"]:
                    f.write(str(i['orderId'])+"\n")

def getitem():
    path='C:/Users/ProblemSolver/Desktop/Storage/storage.txt'
        
    f=open('response.json')
    data = json.load(f)
    f.close()
    
    if os.path.exists('storage.txt'):
        with open ('storage.txt', "w") as f:
            for i in data["data"]:
                f.write(str(i['storageItemIds'])+ "\n")
    else:
        with open ('storage.txt', "a") as f:
            for i in data["data"]:
                f.write(str(i['storageItemIds'])+ "\n")

def delcopyshipment():
        f=open('shipment.txt')
        data = f.readlines()
        newdata = list(dict.fromkeys(data))
        f.close()
        with open('shipment.txt', "w") as file:
                for i in newdata:
                        file.write(str(i))

def delcopyorder():
    f=open('order.txt')
    data = f.readlines()
    newdata = list(dict.fromkeys(data))
    f.close()
    with open('order.txt', "w") as file:
            for i in newdata:
                    file.write(str(i))

def delbrackets():
    pass


def close_app():
    app.destroy()

menubar = tk.Menu(app, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
file = tk.Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')  
#file.add_command(label="New")  
#file.add_command(label="Open")  
#file.add_command(label="Save")  
file.add_command(label="Item Servise")    
file.add_separator()  
file.add_command(label="Exit", command=close_app)  
menubar.add_cascade(label="Options", menu=file)  

#edit = tk.Menu(menubar, tearoff=0)  
#edit.add_command(label="Undo")  
#edit.add_separator()     
#edit.add_command(label="Cut")  
#edit.add_command(label="Copy")  
#edit.add_command(label="Paste")  
#menubar.add_cascade(label="Edit", menu=edit)  

#help = tk.Menu(menubar, tearoff=0)  
#help.add_command(label="About")  
#menubar.add_cascade(label="Help", menu=help)  
    
app.config(menu=menubar)


textlf = tk.LabelFrame(app, text="Text field Servise")
textlf.grid(row=0, column=3)

text = tk.Text(textlf, height = 10, width = 30)
text.grid(pady=5)

storageitemlf = tk.LabelFrame(app, text="StorageItem Servise")
storageitemlf.grid(row=0, column=0,padx=30)

btn_delbrackets= tk.Button(storageitemlf, text='Delete brackets',fg='red', command=delbrackets)
btn_delbrackets.grid(row=1, column=0, padx=5, pady=5)

btn_getitem= tk.Button(storageitemlf, text='Get item', command=getitem)
btn_getitem.grid(row=0, column=0, padx=5, pady=5)


shipmentlf = tk.LabelFrame(app, text="Order Servise")
shipmentlf.grid(row=0, column=1,padx=30)

btn_delcopy = tk.Button(shipmentlf, text='Delete copy order',fg='red', command=delcopyorder)
btn_delcopy.grid(row=1, column=0, padx=5, pady=5)
btn_getorder = tk.Button(shipmentlf, text='Get order', command=getorder)
btn_getorder.grid(row=0, column=0, padx=5, pady=5)


orderlf = tk.LabelFrame(app, text="Shipment Servise")
orderlf.grid(row=0, column=0,padx=30,columnspan=1)

btn_delcopyshipment = tk.Button(orderlf, text='Delete copy shipment', fg='red', command=delcopyshipment)
btn_delcopyshipment.grid(row=3, column=0, padx=5, pady=5)
btn_get = tk.Button(orderlf, text='Get shipment', command=getshimpent)
btn_get.grid(row=2, column=0, padx=5, pady=5)
btn_save = tk.Button(orderlf, text='Save', command=save_file)
btn_save.grid(row=1, column=0, padx=5, pady=5)
btn_open = tk.Button(orderlf, text='Open file', command=open_file)
btn_open.grid(row=0, column=0, padx=5, pady=5)


app.mainloop()
    
