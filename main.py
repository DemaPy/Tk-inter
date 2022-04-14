import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from selenium import webdriver
import webbrowser
import time

import PIL.Image
import PIL.ImageTk

import json
import os

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        self.options = webdriver.ChromeOptions()
        self.options.add_argument = ("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
        self.driver = webdriver.Chrome(options=self.options, executable_path="C:\\Users\\bende\\Desktop\\ProblemSolverM13\\chromedriver\\chromedriver.exe")
        
        self.textlf = ttk.LabelFrame(root, text="Text field Servise", padding=(10, 15, 10, 15))
        self.textlf.grid(row=0, column=3,pady=15,padx=(15,15))

        self.text = tk.Text(self.textlf, height = 10, width = 30)
        self.text.grid(pady=5,padx=5)

        self.shipmentlf = ttk.LabelFrame(root,padding=(5, 15, 5, 15), text="Order Servise")
        self.shipmentlf.grid(row=0, column=1,pady=15 ,padx=15)

        #self.btn_delcopy = ttk.Button(self.shipmentlf, text='Delete copy order', style="Accent.TButton", command=self.delcopyorder)
        #self.btn_delcopy.grid(row=1, column=0, padx=5, pady=5)
        self.btn_getorder = ttk.Button(self.shipmentlf, text='Get order', style="Accent.TButton", command=self.getorder)
        self.btn_getorder.grid(row=0, column=0, padx=5, pady=5)

        self.btn_loadAPI = ttk.Button(self.shipmentlf, text='Load API', style="Accent.TButton", command=self.load_API)
        self.btn_loadAPI.grid(row=2, column=0, padx=5, pady=5)

        self.btn_getjson = ttk.Button(self.shipmentlf, text='Get Json', style="Accent.TButton", command=self.load_packages)
        self.btn_getjson.grid(row=3, column=0, padx=5, pady=5)


        self.orderlf = ttk.LabelFrame(root, padding=(5, 15, 5, 15), text="Shipment Servise")
        self.orderlf.grid(row=0, column=0, pady=15, padx=(30,15) ,columnspan=1)

        #self.btn_delcopyshipment = ttk.Button(self.orderlf, text='Delete copy shipment', style="Accent.TButton", command=self.delcopyshipment)
        #self.btn_delcopyshipment.grid(row=3, column=0, padx=5, pady=5)
        self.btn_get = ttk.Button(self.orderlf, text='Get shipment', style="Accent.TButton", command=self.getshimpent)
        self.btn_get.grid(row=2, column=0, padx=5, pady=5)
        self.btn_save = ttk.Button(self.orderlf, text='Save', style="Accent.TButton", command=self.save_file)
        self.btn_save.grid(row=1, column=0, padx=5, pady=5)
        self.btn_open = ttk.Button(self.orderlf, text="Open file", style="Accent.TButton",command=self.open_file)
        self.btn_open.grid(row=0, column=0, padx=5, pady=5)
        
        self.exitbtn = ttk.Checkbutton(text="Exit", style="Toggle.TButton", command=self.close_app)
        self.exitbtn.grid(row=1, column=3, padx=5, pady=5)

    def load_API(self):
        try:
            url = ("https://openapi.m13.autodoc.de/?urls.primaryName=Api%20Admin%20Gateway%20Service")
            self.driver.get(url)
        except Exception as e:
            print(e)
            self.driver.quit()

    def login_WMS(self):
        find_field = self.driver.find_element_by_id("barcode-18")
        find_field.send_keys("5f2572bec088d")
        
        time.sleep(2)
        
        find_btn = self.driver.find_element_by_xpath("//button[@title='Submit']")
        find_btn.click()


    def load_packages(self):
            reprint_sTU = self.driver.find_element_by_css_selector("button.btn.execute.opblock-control__btn")
            reprint_sTU.click()

            time.sleep(15)

            get_json = self.driver.find_element_by_xpath("//div[@class='download-contents']")
            get_json.click()
            
    
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
        f=open('Json/responses.json')
        data = json.load(f)
        f.close()

        if os.path.exists('Txt/shipment.txt'):
            with open ('Txt/shipment.txt', "w") as f:
                for i in data["data"]:
                    f.write(str(i['transportUnitId'])+"\n")
        else:
            with open ('Txt/shipment.txt', "a") as f:
                for i in data["data"]:
                    f.write(str(i['transportUnitId'])+"\n")

        f=open('Txt/shipment.txt')
        data = f.readlines()
        newdata = list(dict.fromkeys(data))
        f.close()
        with open('Txt/shipment.txt', "w") as file:
            for i in newdata:
                file.write(str(i))

    def getorder(self):
        f=open('Json/responseo.json')
        data = json.load(f)
        f.close()

        if os.path.exists('order.txt'):
            with open ('Txt/order.txt', "w") as f:
                for i in data["data"]:
                    f.write(str(i['orderId'])+"\n")
        else:
            with open ('Txt/order.txt', "a") as f:
                for i in data["data"]:
                    f.write(str(i['orderId'])+"\n")

        f=open('Txt/order.txt')
        data = f.readlines()
        newdata = list(dict.fromkeys(data))
        f.close()
        with open('Txt/order.txt', "w") as file:
            for i in newdata:
                file.write(str(i))

    #def delcopyshipment(self):
        #f=open('Txt/shipment.txt')
        #data = f.readlines()
        #newdata = list(dict.fromkeys(data))
        #f.close()
        #with open('Txt/shipment.txt', "w") as file:
            #for i in newdata:
                #file.write(str(i))

    #def delcopyorder(self):
        #f=open('Txt/order.txt')
        #data = f.readlines()
        #newdata = list(dict.fromkeys(data))
        #f.close()
        #with open('Txt/order.txt', "w") as file:
            #for i in newdata:
                #file.write(str(i))

    def openNewWindow(self):
        pass

    def close_app(self):
        root.destroy()
        self.driver.quit()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Problem Solver M13 | Outbound")
    
    im = PIL.Image.open("img/autodoc.png")
    photo = PIL.ImageTk.PhotoImage(im)
    root.iconphoto(False, photo)
    
    #set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.grid()

    # Set a minsize for the window, and place it in the middle
    #root.update()
    #root.minsize(root.winfo_width(), root.winfo_height())
    #x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    #y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    #root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
    root.geometry('660x310')
    root.resizable(False, False)
    root.mainloop()
