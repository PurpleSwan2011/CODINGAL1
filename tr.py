import tkinter as tk
from tkinter import ttk, messagebox
class RestuarantOrderManagement:
    def __init__(self, root):
        self.root=root
        self.root.title("Restuarant Management App")
        self.menu_items={
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":3,
            "PIZZA MEAL":4,
            "CHEESE BURGER":2.5,
            "DRINKS":1
        }
        self.exchange_rate=82
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Restuarant Order Management",font=("Arial",20,"bold")).grid(row=0,columnpan=3,padx=10,pady=10)
        self.menu_labels={}
        self.menu_quantities={}
        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{items} (${price}):",font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_labels[item]=label
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item]=quantity_entry
        self.currency_var=ttk.StringVar()
        ttk.Label(frame,text="Currency:",font=("Arial",12)).grid(row=len(self.menu_items))