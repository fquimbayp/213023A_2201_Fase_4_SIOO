"""
Graphical user interface layer.

SEPARATION OF CONCERNS:
This module handles only user interaction and presentation.
Business logic is delegated to the domain layer.
"""

import tkinter as tk
from services.room import RoomService
from services.equipment import EquipmentRentalService
from services.consulting import ConsultingService

class ServicesWindow:
    def __init__(self, parent, services):
        self.services = services
        self.win = tk.Toplevel(parent)
        self.win.title('Service Management')
        tk.Label(self.win, text='Service Management', font=('Arial',12)).pack()
        self.lb = tk.Listbox(self.win)
        self.lb.pack(fill=tk.BOTH, expand=True)

        if not services:
            services.extend([
                RoomService(1,'Room Reservation',50),
                EquipmentRentalService(2,'Equipment Rental',30),
                ConsultingService(3,'Specialized Consulting',100)
            ])
        self.refresh()

    def refresh(self):
        self.lb.delete(0, tk.END)
        for s in self.services:
            self.lb.insert(tk.END, s)
