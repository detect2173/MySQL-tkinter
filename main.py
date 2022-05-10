from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
from turtle import color

root = Tk()
root.title('My SHRO Inventory Database')
root.configure(background='#000000')
root.geometry('1050x500')
root.resizable(width=False, height=False)

####--------------------------GUI BUILD-------------------------------------####
inv_label = ttk.Label(root, text='Inventory#: ',background='#000000',foreground='white', font=('TkDefaultFont', 16))
inv_label.grid(row=0, column=0, sticky=W, padx=(20,5), pady=10)
inv_text = StringVar()
inv_entry = ttk.Entry(root,width=18, textvariable=inv_text)
inv_entry.grid(row=0, column=1, sticky=W,padx=10, pady=10)
desc_label = ttk.Label(root, text='Description: ',background='#000000',foreground='white', font=('TkDefaultFont', 16))
desc_label.grid(row=0, column=2, sticky=W, padx=10, pady=10)
desc_text = StringVar()
desc_entry = ttk.Entry(root,width=36, textvariable=desc_text)
desc_entry.grid(row=0, column=3, sticky=W,padx=10, pady=10)
qty_label = ttk.Label(root, text='Quantity: ',background='#000000',foreground='white', font=('TkDefaultFont', 16))
qty_label.grid(row=0, column=4, sticky=W, padx=10, pady=10)
qty_text = StringVar()
qty_entry = ttk.Entry(root,width=18, textvariable=qty_text)
qty_entry.grid(row=0, column=5, sticky=W,padx=10, pady=10)
add_btn = Button(root, text='Add Item', bg='orange', fg='#000000', font='helvetica 10 bold', command='')
add_btn.grid(row=0, column=6, sticky=W,padx=20)

list_bx = Listbox(root,height=16, width=40, font='helvetica 13')
list_bx.grid(row=3, column=0, columnspan=14, sticky=W+E,pady=40, padx=25 )
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)
list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)


root.mainloop()