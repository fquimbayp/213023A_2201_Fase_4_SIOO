"""
Graphical user interface layer.

SEPARATION OF CONCERNS:
This module handles only user interaction and presentation.
Business logic is delegated to the domain layer.
"""

import tkinter as tk
from ui.clients_view import ClientsWindow
from ui.services_view import ServicesWindow
from ui.reservations_view import ReservationsWindow

class SoftwareFJApp:
    def __init__(self, root):
        self.root = root
        root.title('Software FJ - Main Menu')
        self.clients = []
        self.services = []
        self.reservations = []

        tk.Label(root, text='Software FJ Management System', font=('Arial',14)).pack(pady=10)
        tk.Button(root, text='Manage Clients', command=lambda: ClientsWindow(root,self.clients)).pack(fill=tk.X)
        tk.Button(root, text='Manage Services', command=lambda: ServicesWindow(root,self.services)).pack(fill=tk.X)
        tk.Button(root, text='Manage Reservations', command=lambda: ReservationsWindow(root,self.clients,self.services,self.reservations)).pack(fill=tk.X)
