import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox


import json
import os

#INITIALIZE
class MainFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = FirstFrame(self)
        self.frame.grid()

    def change(self, frame):
        self.frame.grid_forget()
        self.frame = frame(self)
        self.frame.grid()
#LOGIN
class FirstFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        ttk.Frame.__init__(self, master, **kwargs)
        master.title('Problem Solver')
        master.geometry('400x200')
        master.resizable(False,False)

        lbl= ttk.Label(self, text = 'Enter password',font='Helvetica 18 bold')
        lbl.grid(row=0,padx=110,pady=5)

        self.pwd = ttk.Entry(self, show = '*')
        self.pwd.grid(row=1,padx=5,pady=5)
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)

        btn = ttk.Button(self, text ='Login', style="Accent.TButton", command = self.check)
        btn.grid(row=2,padx=5,pady=5)
#PASSWORD
    def check(self, event=None):
        if self.pwd.get() == 'solver':
            self.master.change(SecondFrame)
        else:
            messagebox.showwarning("Access denied", "Username or Password incorrect!")
#WORKZONE
class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title('Problem Solver | Outbound')
        master.geometry('650x220')
        master.resizable(False, False)

        self.textlf = ttk.LabelFrame(master, text="Text field Servise")
        self.textlf.grid(row=0, column=3)

        self.text = tk.Text(self.textlf, height = 10, width = 30)
        self.text.grid(pady=5, padx=5)

        self.shipmentlf = ttk.LabelFrame(master, text="Order Servise")
        self.shipmentlf.grid(row=0, column=1,padx=30)

        self.btn_delcopy = ttk.Button(self.shipmentlf, text='Delete copy order', style="Accent.TButton", command=self.delcopyorder)
        self.btn_delcopy.grid(row=1, column=0, padx=5, pady=5)
        self.btn_getorder = ttk.Button(self.shipmentlf, text='Get order', style="Accent.TButton", command=self.getorder)
        self.btn_getorder.grid(row=0, column=0, padx=5, pady=5)


        self.orderlf = ttk.LabelFrame(master, text="Shipment Servise")
        self.orderlf.grid(row=0, column=0,padx=30,columnspan=1)

        self.btn_delcopyshipment = ttk.Button(self.orderlf, text='Delete copy shipment', style="Accent.TButton", command=self.delcopyshipment)
        self.btn_delcopyshipment.grid(row=3, column=0, padx=5, pady=5)
        self.btn_get = ttk.Button(self.orderlf, text='Get shipment', style="Accent.TButton", command=self.getshimpent)
        self.btn_get.grid(row=2, column=0, padx=5, pady=5)
        self.btn_save = ttk.Button(self.orderlf, text='Save', style="Accent.TButton", command=self.save_file)
        self.btn_save.grid(row=1, column=0, padx=5, pady=5)
        self.btn_open = ttk.Button(self.orderlf, text="Open file", style="Accent.TButton",command=self.open_file)
        self.btn_open.grid(row=0, column=0, padx=5, pady=5)
        
        self.menubar = tk.Menu(master, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
        
        self.file = tk.Menu(self.menubar, tearoff=0, background='#ffcc99', foreground='black')  
        #file.add_command(label="New")  
        #file.add_command(label="Open")  
        #file.add_command(label="Save")  
        self.file.add_command(label="Item Servise", command=self.openNewWindow)    
        self.file.add_separator()  
        self.file.add_command(label="Exit", command=self.close_app)  
        self.menubar.add_cascade(label="Options", menu=self.file)  

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

        self.master.config(menu=self.menubar)
        
    def open_file(self):               
        filename = fd.askopenfilename(filetypes=[('json files', '*.json')])
        if filename:
            with open(filename, "r", -1, "utf-8") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())
                
    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("json","*.json")], defaultextension = "*.json")
                
        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))

    def getshimpent(self):
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

    def getorder(self):
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

    def delcopyshipment(self):
        f=open('shipment.txt')
        data = f.readlines()
        newdata = list(dict.fromkeys(data))
        f.close()
        with open('shipment.txt', "w") as file:
            for i in newdata:
                file.write(str(i))

    def delcopyorder(self):
        f=open('order.txt')
        data = f.readlines()
        newdata = list(dict.fromkeys(data))
        f.close()
        with open('order.txt', "w") as file:
            for i in newdata:
                file.write(str(i))

    def check(self, event=None):
        if self.pwd.get() == 'solver':
            self.master.change(SecondFrame)
        else:
            messagebox.showwarning("Access denied", "Username or Password incorrect!")

    def close_app(self):
        master.destroy()

    def openNewWindow(self):
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Problem Solve | Outbound\Get items")
        newWindow.geometry("200x200")
        newWindow.resizable(False, False)

        self.storageitemlf = tk.LabelFrame(newWindow, text="StorageItem Servise")
        self.storageitemlf.grid(row=0, column=0,padx=40, pady=30)

        self.btn_delbrackets= tk.Button(self.storageitemlf, text='Delete brackets',fg='red', command=self.delbrackets)
        self.btn_delbrackets.grid(row=1, column=0, padx=5, pady=5)
        self.btn_getitem= tk.Button(self.storageitemlf, text='Get item', command=self.getitem)
        self.btn_getitem.grid(row=0, column=0, padx=5, pady=5)
        
    def getitem(self):         
        f=open('responsestorage.json')
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

    def delbrackets(self):
        pass

    

if __name__  == '__main__':
    master = MainFrame()
    master.mainloop()
    
