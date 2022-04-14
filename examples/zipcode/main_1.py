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
#WIDGETS
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
        master.geometry('850x500')
        master.minsize(850,500)
        #FINDORDERADDRESS
        
        #FINDZIPCODE
        self.labelframezipcode = tk.LabelFrame(self, text= 'Find zipcode')
        self.labelframezipcode.grid(row=2,column=0,padx=25)
        
        self.findziplbl = tk.Label(self.labelframezipcode,text = 'Find zipcode',font = 'Helvetica 8 bold')
        self.findziplbl.grid(column=0,row=1)

        self.findzipbtn = tk.Button(self.labelframezipcode, text ='Find',command = self.findzipcode,height=1,width=10)
        self.findzipbtn.grid(column=2,row=1,padx=5,pady=5)

        self.entfindzip = tk.StringVar()
        self.findzipent = tk.Entry(self.labelframezipcode,textvariable=self.entfindzip)
        self.findzipent.grid(row=1, column=1)

        self.textfindzipcode = tk.Text(self.labelframezipcode,height=1,width=20)
        self.textfindzipcode.grid(row=2, column=1,padx=2,pady=2)
        
        #SCAN SHIPMENT
        self.labelframe = tk.LabelFrame(self,text='Shipment TU')
        self.labelframe.grid(row=1,column=0,padx=25)

        self.entTUvar = tk.StringVar()
        self.entTU = tk.Entry(self.labelframe,width=20,textvariable=self.entTUvar)
        self.entTU.grid(column=1,row=1)
        self.lbl = tk.Label(self.labelframe,text = 'Scanned shipment TU',font = 'Helvetica 8 bold')
        self.lbl.grid(column=0,row=1)

        self.btn = tk.Button(self.labelframe, text ='Add',command = self.writefile,height=1,width=10)
        self.btn.grid(column=2,row=1,padx=5,pady=5)

        #VALUES OF ORDER
        self.labelframeorder = tk.LabelFrame(self,text='Order configuration')
        self.labelframeorder.grid(row=0,column=0,padx=25)

        self.entfind_address_var = tk.StringVar()
        self.entfind_address = tk.Entry(self.labelframeorder,textvariable=self.entfind_address_var)
        self.entfind_address.grid(row=3, column=2)
        
        self.btn = tk.Button(self.labelframeorder, text ='Find address',command = self.find_order_address,height=1,width=10)
        self.btn.grid(column=2,row=4,padx=5,pady=5)

        countylist = [
            "Country",
            "Sweden",
            "Romania"
            ]
        
        self.varset = tk.StringVar()
        self.varset.set(countylist[0])
        self.menuofcountry = tk.OptionMenu(self.labelframeorder, self.varset, *countylist)
        self.menuofcountry.grid(row=6,column=2)
        
        self.ent_1 = tk.Entry(self.labelframeorder)
        self.ent_1.grid(row=1, column=1,padx=5,pady=1)
        lbl = tk.Label(self.labelframeorder,text = 'ORDER',font = 'Helvetica 8 bold')
        lbl.grid(row=1, column=0,padx=40,pady=5)
        
        self.ent_2 = tk.Entry(self.labelframeorder)
        self.ent_2.grid(row=2, column=1,padx=5,pady=1)
        self.lbl = tk.Label(self.labelframeorder,text = 'NAME',font = 'Helvetica 8 bold')
        self.lbl.grid(row=2, column=0,padx=40,pady=5)
        
        self.ent_3 = tk.Entry(self.labelframeorder)
        self.ent_3.grid(row=3, column=1,padx=5,pady=1)
        self.lbl = tk.Label(self.labelframeorder,text = 'SURNAME',font = 'Helvetica 8 bold')
        self.lbl.grid(row=3, column=0,padx=40,pady=5)
        
        self.ent_4 = tk.Entry(self.labelframeorder)
        self.ent_4.grid(row=4, column=1,padx=5,pady=1)
        lbl = tk.Label(self.labelframeorder,text = 'STREET',font = 'Helvetica 8 bold')
        lbl.grid(row=4, column=0,padx=40,pady=5)
        
        self.ent_5 = tk.Entry(self.labelframeorder)
        self.ent_5.grid(row=5, column=1,padx=5,pady=1)
        self.lbl = tk.Label(self.labelframeorder,text = 'NUMBER HOUSE',font = 'Helvetica 8 bold')
        self.lbl.grid(row=5, column=0,padx=40,pady=5)
        
        self.ent_6 = tk.Entry(self.labelframeorder)
        self.ent_6.grid(row=6, column=1,padx=5,pady=1)
        self.lbl = tk.Label(self.labelframeorder,text = 'MAIL',font = 'Helvetica 8 bold')
        self.lbl.grid(row=6, column=0,padx=40,pady=5)
        
        self.ent_7 = tk.Entry(self.labelframeorder)
        self.ent_7.grid(row=7, column=1,padx=5,pady=1)
        self.lbl = tk.Label(self.labelframeorder,text = 'NUMBER PHONE',font = 'Helvetica 8 bold')
        self.lbl.grid(row=7, column=0,padx=40,pady=5)

        self.ent_8 = tk.Entry(self.labelframeorder)
        self.ent_8.grid(row=8, column=1,padx=5,pady=1)
        lbl = tk.Label(self.labelframeorder,text = 'CITY',font = 'Helvetica 8 bold')
        lbl.grid(row=8, column=0,padx=40,pady=5)

        self.ent_9 = tk.Entry(self.labelframeorder)
        self.ent_9.grid(row=9, column=1,padx=5,pady=1)
        lbl = tk.Label(self.labelframeorder,text = 'ZIPCODE',font = 'Helvetica 8 bold')
        lbl.grid(row=9, column=0,padx=40,pady=5)

        self.btn = tk.Button(self.labelframeorder, text ='Convert',command = self.ins,height=1,width=10)
        self.btn.grid(row=5, column=2,padx=40,pady=5)

        self.btn_1 = tk.Button(self.labelframeorder, text= 'Clear', command = self.clear,height=1,width=10, fg='red')
        self.btn_1.grid(row=9, column=2,padx=40,pady=5)

        self.text = tk.Text(self.labelframeorder,height=20,width=40)
        self.text.grid(row=0, column=3,rowspan=10,padx=2,pady=2)
    
    def findzipcode(self):
        url = 'https://worldpostalcode.com/'
        driver = webdriver.Chrome(executable_path="C:\\Users\\ProblemSolver\\Desktop\\zipcode\\chromedriver\\chromedriver.exe")
        try:
            driver.get(url)
            time.sleep(1)
            findzip = driver.find_element_by_id('search')
            findzip.send_keys(self.entfindzip.get())
            findzip_btn = driver.find_element_by_class_name("submit").click()
            time.sleep(1)
            getzipcode = driver.find_element_by_class_name("lookup_result").text
            self.textfindzipcode.insert(tk.END, getzipcode)
        #except Exception as ex:
            #print(ex)
        finally:
            driver.close()
            driver.quit()
            
    def find_order_address(self):
        options = webdriver.ChromeOptions()
        options.add_argument = ("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36")
        url = 'https://aws.autodoc.de/login'
        url_1 = "https://aws.autodoc.de/order/view/"+format(self.entfind_address_var.get())
        driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\ProblemSolver\\Desktop\\zipcode\\chromedriver\\chromedriver.exe")
        try:
            driver.get(url)
            time.sleep(5)
            findlogin = driver.find_element_by_id('login')
            findlogin.send_keys('c2054a2a402405d9')
            time.sleep(2)

            findzip_btn = driver.find_element_by_css_selector(".btn").click()
            time.sleep(2)
            
            driver.get(url_1)
            time.sleep(2)
            
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
            time.sleep(3)

            find_city_id = driver.find_element_by_id('form_Order[lOrt]')
            self.find_city = find_city_id.get_attribute('value')
            time.sleep(1)

            find_zip_id = driver.find_element_by_id('form_Order[lPlz]')
            self.find_zip = find_zip_id.get_attribute('value')
            time.sleep(2)
            
            self.text.insert(tk.END,'  "orderId": {},\n  "preferredCarrierId": 0,\n  "salutation": "Herr",\n  "customerName": "{}",\n  "customerSurname": "{}",\n  "companyName": "",\n  "address": "{}",\n  "addressDesc": "",\n  "houseNr": "{}",\n  "email": "{}",\n  "phoneNr": "{}",\n  "city": "{}",\n  "zip": "{}",\n  "isIsland": 0,\n  "countryId": "",\n  "declaration": 0,\n  "deliveryId": 1,\n  "carrierService": 0'.format(self.entfind_address_var.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_name,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_surname,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_street,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_hnumber,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_mail,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_pnumber,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_city,
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.find_zip))
            
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()     
        

        
    def writefile(self,*args):
        with open('package.txt', 'a+') as f:
            f.write(self.entTUvar.get())
            
    def clear(self):
        self.text.delete('1.0', tk.END)
    
    def ins(self):
        if self.varset.get()=="Country":
            self.text.insert(tk.END,'  "orderId": {},\n  "preferredCarrierId": 0,\n  "salutation": "Herr",\n  "customerName": "{}",\n  "customerSurname": "{}",\n  "companyName": "",\n  "address": "{}",\n  "addressDesc": "",\n  "houseNr": "{}",\n  "email": "{}",\n  "phoneNr": "{}",\n  "city": "{}",\n  "zip": "{}",\n  "isIsland": 0,\n  "countryId": "",\n  "declaration": 0,\n  "deliveryId": 1,\n  "carrierService": 0'.format(self.ent_1.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_2.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_3.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_4.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_5.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_6.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_7.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_8.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_9.get()))
            
        if self.varset.get()=="Sweden":
            self.text.insert(tk.END,'  "orderId": {},\n  "preferredCarrierId": 0,\n  "salutation": "Herr",\n  "customerName": "{}",\n  "customerSurname": "{}",\n  "companyName": "",\n  "address": "{}",\n  "addressDesc": "",\n  "houseNr": "{}",\n  "email": "{}",\n  "phoneNr": "{}",\n  "city": "{}",\n  "zip": "{}",\n  "isIsland": 1,\n  "countryId": "12",\n  "declaration": 0,\n  "deliveryId": 1,\n  "carrierService": 0'.format(self.ent_1.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_2.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_3.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_4.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_5.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_6.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_7.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_8.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_9.get()))
        if self.varset.get()=="Romania":
            self.text.insert(tk.END, '  "orderId": {},\n  "preferredCarrierId": 0,\n  "salutation": "Herr",\n  "customerName": "{}",\n  "customerSurname": "{}",\n  "companyName": "",\n  "address": "{}",\n  "addressDesc": "",\n  "houseNr": "{}",\n  "email": "{}",\n  "phoneNr": "{}",\n  "city": "{}",\n  "zip": "{}",\n  "isIsland": 0,\n  "countryId": "190",\n  "declaration": 0,\n  "deliveryId": 1,\n  "carrierService": 0'.format(self.ent_1.get(),                                                                                                                                                                                                                                                                                                                                                                                                                                          self.ent_2.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_3.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_4.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_5.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_6.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_7.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_8.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                self.ent_9.get()))
                                                                                                                                                                                                                                                   

if __name__  == '__main__':
    app = MainFrame()
    app.mainloop()
