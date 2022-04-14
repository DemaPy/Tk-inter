import tkinter as tk
from tkinter import messagebox
import webbrowser
from selenium import webdriver
import time

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
class FirstFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title('Problem Solver')
        master.geometry('400x200')
        master.resizable(False,False)

        lbl= tk.Label(self, text = 'Enter password',font='Helvetica 18 bold',pady = 40)
        lbl.grid(row=0,padx=110,pady=5)

        self.pwd = tk.Entry(self, show = '*')
        self.pwd.grid(row=1,padx=5,pady=5)
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)

        btn = tk.Button(self, text ='Login',command = self.check)
        btn.grid(row=2,padx=5,pady=5)
#PASSWORD
    def check(self, event=None):
        if self.pwd.get() == 'solver':
            self.master.change(SecondFrame)
        else:
            messagebox.showwarning("Access denied", "Username or Password incorrect!")
#WORZONE
class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title('Problem Solver M13')
        master.geometry('500x350')
        master.minsize(500,350)

        self.btn = tk.Button(self, text ='Find address',command = self.find_order_address,height=1,width=10)
        self.btn.grid(column=2,row=4,padx=5,pady=5)
        
        self.entfind_address_var = tk.StringVar()
        self.entfind_address = tk.Entry(self,textvariable=self.entfind_address_var)
        self.entfind_address.grid(row=3, column=2)
        
        self.btn_1 = tk.Button(self, text= 'Clear', command = self.clear,height=1,width=10, fg='red')
        self.btn_1.grid(row=9, column=2,padx=40,pady=5)
        self.text = tk.Text(self,height=20,width=40)
        self.text.grid(row=0, column=3,rowspan=10,padx=2,pady=2)
            
    def find_order_address(self):
        options = webdriver.ChromeOptions()
        options.add_argument = ("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
        url = 'https://aws.autodoc.de/login'
        url_1 = "https://aws.autodoc.de/order/view/"+format(self.entfind_address_var.get())
        driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\ProblemSolver\\Desktop\\zipcode\\chromedriver\\chromedriver.exe")
        try:
            driver.get(url)
            time.sleep(3)
            findlogin = driver.find_element_by_id('login')
            findlogin.send_keys('c2054a2a402405d9')
            time.sleep(2)

            findzip_btn =driver.find_element_by_css_selector(".btn").click()
            time.sleep(2)
            
            driver.get(url_1)
            time.sleep(1)
            
            find_name_id = driver.find_element_by_id('form_Order[lVorname]')
            self.find_name = find_name_id.get_attribute('value')
            time.sleep(2)

            find_surname_id = driver.find_element_by_id('form_Order[lName]')
            self.find_surname = find_surname_id.get_attribute('value')
            time.sleep(1)

            find_street_id = driver.find_element_by_id('form_Order[lStrasse]')
            self.find_street = find_street_id.get_attribute('value')
            time.sleep(2)

            find_hnumber_id = driver.find_element_by_id('form_Order[delivery_house]')
            self.find_hnumber = find_hnumber_id.get_attribute('value')
            time.sleep(1)

            find_mail_id = driver.find_element_by_id('form_Order[Email]')
            self.find_mail = find_mail_id.get_attribute('value')
            time.sleep(2)

            find_pnumber_id = driver.find_element_by_id('form_Order[rTelefon]')
            self.find_pnumber = find_pnumber_id.get_attribute('value')
            time.sleep(1)

            find_city_id = driver.find_element_by_id('form_Order[lOrt]')
            self.find_city = find_city_id.get_attribute('value')
            time.sleep(1)

            find_zip_id = driver.find_element_by_id('form_Order[lPlz]')
            self.find_zip = find_zip_id.get_attribute('value')
            time.sleep(2)

            find_country_id = driver.find_element_by_id('form_Order[delivery_country_id]')
            self.find_country = find_country_id.get_attribute('value')
            time.sleep(1)
            
            self.text.insert(tk.END,'  "orderId": {},\n  "preferredCarrierId": 0,\n  "salutation": "Herr",\n  "customerName": "{}",\n  "customerSurname": "{}",\n  "companyName": "",\n  "address": "{}",\n  "addressDesc": "",\n  "houseNr": "{}",\n  "email": "{}",\n  "phoneNr": "{}",\n  "city": "{}",\n  "zip": "{}",\n  "isIsland": 0,\n  "countryId": "{}",\n  "declaration": 0,\n  "deliveryId": 1,\n  "carrierService": 0'.format(self.entfind_address_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_name,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_surname,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_street,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_hnumber,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_mail,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_pnumber,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_city,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_zip,self.find_country))
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()     
        

        
            
    def clear(self):
        self.text.delete('1.0', tk.END)
        
if __name__  == '__main__':
    app = MainFrame()
    app.mainloop()
