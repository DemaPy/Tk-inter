import tkinter as tk

window = tk.Tk()
window.geometry('400x200')
window.resizable(False,False)

def write():
    with open('shipment.txt', 'a+') as f:
        data = ent_tu.get()
        convert = int(str(data)[5:])
        f.write(str(convert) +'\n')

        #file = open('shipment.txt', 'r')
        #list_of_lists = []
        #for line in file:
            #stripped_line = line.strip()
            #line_list = stripped_line.split()
            #list_of_lists.append(line_list)


ent_tu = tk.StringVar()
ent = tk.Entry(textvariable=ent_tu)
ent.grid(row=0, column=1,padx=5,pady=5)
ent.focus()

lbl = tk.Label(text='Scann sTU bitch')
lbl.grid(row=0, column=0,padx=5,pady=5)

btn = tk.Button(text='Add', command=write)
btn.grid(row=0, column=2,padx=5,pady=5)

if __name__ == '__main__':
    write()
