"""
Graphical user interface layer.

SEPARATION OF CONCERNS:
This module handles only user interaction and presentation.
Business logic is delegated to the domain layer.
"""

import tkinter as tk
from tkinter import messagebox
from core.client import Client

class ClientsWindow:
    def __init__(self, parent, clients):
        self.clients = clients
        self.win = tk.Toplevel(parent)
        self.win.title('Client Management')
        tk.Label(self.win, text='Client Management', font=('Arial',12)).pack()

        tk.Label(self.win, text='Name').pack()
        self.name = tk.Entry(self.win)
        self.name.pack()
        tk.Label(self.win, text='Email').pack()
        self.email = tk.Entry(self.win)
        self.email.pack()

        tk.Button(self.win, text='Create', command=self.create).pack()
        tk.Button(self.win, text='Update', command=self.update).pack()
        tk.Button(self.win, text='Delete', command=self.delete).pack()

        self.lb = tk.Listbox(self.win, exportselection=False)
        self.lb.pack(fill=tk.BOTH, expand=True)
        self.lb.bind('<<ListboxSelect>>', self.load)
        self.refresh()

    def load(self, event):
        try:
            c = self.clients[self.lb.curselection()[0]]
            self.name.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.name.insert(0, c.name)
            self.email.insert(0, c.email)
        except: pass

    def create(self):
        try:
            c = Client(len(self.clients)+1, self.name.get(), self.email.get())
            self.clients.append(c)
            self.refresh()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def update(self):
        try:
            idx = self.lb.curselection()[0]
            self.clients[idx].name = self.name.get()
            self.clients[idx].email = self.email.get()
            self.clients[idx].validate()
            self.refresh()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def delete(self):
        try:
            self.clients.pop(self.lb.curselection()[0])
            self.refresh()
        except:
            messagebox.showerror('Error', 'Select a client')

    def refresh(self):
        self.lb.delete(0, tk.END)
        for c in self.clients:
            self.lb.insert(tk.END, c)
