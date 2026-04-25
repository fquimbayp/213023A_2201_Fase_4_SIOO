
import logging
import tkinter as tk
from ui.app import SoftwareFJApp

logging.basicConfig(filename='system.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

root = tk.Tk()
SoftwareFJApp(root)
root.mainloop()
