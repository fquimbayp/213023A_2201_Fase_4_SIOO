"""
Graphical user interface layer.

SEPARATION OF CONCERNS:
This module handles only user interaction and presentation.
Business logic is delegated to the domain layer.
"""

import tkinter as tk
from tkinter import messagebox
from core.reservation import Reservation

class ReservationsWindow:
    def __init__(self, parent, clients, services, reservations):
        self.clients = clients
        self.services = services
        self.reservations = reservations
        self.win = tk.Toplevel(parent)
        self.win.title('Reservation Management')
        tk.Label(self.win, text='Reservation Management', font=('Arial',12)).pack()

        tk.Label(self.win, text='Clients').pack()
        self.client_box = tk.Listbox(self.win, exportselection=False)
        self.client_box.pack()

        tk.Label(self.win, text='Services').pack()
        self.service_box = tk.Listbox(self.win, exportselection=False)
        self.service_box.pack()

        tk.Label(self.win, text='Hours').pack()
        self.hours = tk.Entry(self.win)
        self.hours.pack()

        tk.Button(self.win, text='Create', command=self.create).pack()
        tk.Button(self.win, text='Update Hours', command=self.update).pack()
        tk.Button(self.win, text='Delete', command=self.delete).pack()

        tk.Label(self.win, text='Reservations').pack()
        self.lb = tk.Listbox(self.win, exportselection=False)
        self.lb.pack(fill=tk.BOTH, expand=True)
        self.lb.bind('<<ListboxSelect>>', self.load)

        self.refresh()

    def refresh(self):
        self.client_box.delete(0, tk.END)
        self.service_box.delete(0, tk.END)
        self.lb.delete(0, tk.END)
        for c in self.clients:
            self.client_box.insert(tk.END, c)
        for s in self.services:
            self.service_box.insert(tk.END, s)
        for r in self.reservations:
            self.lb.insert(tk.END, r)

    def load(self, event):
        try:
            r = self.reservations[self.lb.curselection()[0]]
            self.hours.delete(0, tk.END)
            self.hours.insert(0, str(r.hours))
        except: pass

    def create(self):
        try:
            h = self.hours.get().strip()
            if not h.isdigit(): raise ValueError('Invalid hours')
            r = Reservation(
                len(self.reservations)+1,
                self.clients[self.client_box.curselection()[0]],
                self.services[self.service_box.curselection()[0]],
                int(h)
            )
            r.confirm()
            self.reservations.append(r)
            self.refresh()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def update(self):
        try:
            idx = self.lb.curselection()[0]
            h = self.hours.get().strip()
            if not h.isdigit(): raise ValueError('Invalid hours')
            self.reservations[idx].hours = int(h)
            self.reservations[idx].confirm()
            self.refresh()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def delete(self):
        try:
            self.reservations.pop(self.lb.curselection()[0])
            self.refresh()
        except:
            messagebox.showerror('Error', 'Select a reservation')
